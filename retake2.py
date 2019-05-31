#!/usr/bin/python
# (c) 2019 Camille Molenaar IC102 camille.molenaar@hva.nl
import hva_pcap as pcap
import hva_pckt as pckt
import pprint

# Opens the pcap file and uses the pcap library to turn it into usable data
rdr = pcap.open_offline('xsupport.pcap')

# Declaring count to count the number of suspicious packets later
# OLD: count = 0
connection_info = dict()

"""
This function prints the timestamp, source IP address,
destination IP address, source port and destination port and uses a format.
"""
def printNoAck(time, sAdd, dAdd, sPo, dPo):

    print("\nTimestamp: \t\t\t", time, "\nSource IP Address: \t\t" , sAdd,
    "\nDestination IP Address: \t", dAdd, "\nSource Port: \t\t\t", sPo,
    "\nDestination Port: \t\t", dPo)

# For loop to loop through the data dump by using the pckt library
for hdr, data in rdr:

    eth = pckt.Eth.decode(data)
    if eth is None: continue
    ip = pckt.Ip.decode(eth.pl)
    if eth is None: continue
    tcp = pckt.Tcp.decode(ip.pl)
    if tcp is None: continue

    # Key is based on the ports and ips.
    key = "{}{}{}{}".format(ip.saddr, ip.daddr, tcp.sport, tcp.dport)
    if not key in connection_info:
        connection_info[key] = dict()
        connection_info[key]['source_ip'] = str(ip.saddr)
        connection_info[key]['destination_ip'] = str(ip.daddr)
        connection_info[key]['source_port'] = str(tcp.sport)
        connection_info[key]['destination_port'] = str(tcp.dport)
        # De rest van de info kan je hier aanvullen :^)
    # Increase the number of attempted connections.
    if 'connection_attempts' not in connection_info[key]:
        connection_info[key]['connection_attempts'] = 0
    connection_info[key]['connection_attempts'] += 1

# If the TCP acknowledgement has a value of 0, it means that there was no ack.
    if tcp.ack == 0:
        printNoAck(hdr.ts, ip.saddr, ip.daddr, tcp.sport, tcp.dport)
# The count variable keeps track of the amount of suspicious packets
        # OLD: count = count + 1
        if 'no_ack' not in connection_info[key]:
            connection_info[key]['no_ack'] = 0
            # Also keep a list of timestamps for the no acks.
            connection_info[key]['no_ack_times'] = []
        # Increase the number of no acknowledgments.
        connection_info[key]['no_ack'] += 1
        connection_info[key]['no_ack_times'].append(hdr.ts)
# Displays the total amount of suspicious packets
# OLD: print("\nSuspicious packets: \t\t", count)

# Find suspicious connections: 1 or more no ack.
min_no_ack = 1
susp_info = dict()
#  Filter the connection information.
for key in connection_info:
    single_connection = connection_info[key]
    if 'no_ack' in single_connection and single_connection['no_ack'] >= min_no_ack:
        susp_info[key] = single_connection

pp = pprint.PrettyPrinter(indent=4)
pp.pprint(susp_info)
print("Total number of suspicious connections is: {}.".format(len(susp_info)))
