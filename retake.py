#!/usr/bin/python
# (c) 2019 Camille Molenaar IC102 camille.molenaar@hva.nl
import hva_pcap as pcap
import hva_pckt as pckt

# Opens the pcap file and uses the pcap library to turn it into usable data
rdr = pcap.open_offline('xsupport.pcap')

# Declaring count to count the number of suspicious packets later
count = 0

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

# If the TCP acknowledgement has a value of 0, it means that there was no ack.
    if tcp.ack == 0:
        printNoAck(hdr.ts, ip.saddr, ip.daddr, tcp.sport, tcp.dport)
# The count variable keeps track of the amount of suspicious packets
        count = count + 1
# Displays the total amount of suspicious packets
print("\nSuspicious packets: \t\t", count)
