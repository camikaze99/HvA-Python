#!/usr/bin/python
# (c) 2019 Camille Molenaar IC102 f.h.schippers@hva.nl
import hva_pcap as pcap
import hva_pckt as pckt

# Opens the pcap file and uses the pcap library to turn it into usable data
rdr = pcap.open_offline('xsupport.pcap')

count = 0

# This function prints the nTimestamp, source IP address,
# destination IP address, source IP address
def printNoAck(time, sAdd, dAdd, sPo, dPo):

    print("\nTimestamp: \t\t\t", time, "\nSource IP Address: \t\t" , sAdd,
    "\nDestination IP Address: \t", dAdd, "\nSource Port: \t\t\t", sPo,
    "\nDestination Port: \t\t", dPo)


for hdr, data in rdr:

    eth = pckt.Eth.decode(data)
    if eth is None: continue
    ip = pckt.Ip.decode(eth.pl)
    if eth is None: continue
    tcp = pckt.Tcp.decode(ip.pl)
    if tcp is None: continue

    if tcp.ack == 0:
        printNoAck(hdr.ts, ip.saddr, ip.daddr, tcp.sport, tcp.dport)
        count = count + 1

print("\nSuspicious packets: \t\t", count)
#    break
