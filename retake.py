#!/usr/bin/python
import hva_pcap
import hva_pckt

connections = {}
connections[0] = "Hello"
connections["test"] = "Value"
connections["test2"] = "Value2"
print(connections[0], "\n")
print(connections)


"""
connections.append()
connections.delete()

https://www.pythonforbeginners.com/dictionary/how-to-use-dictionaries-in-python/

https://www.tutorialspoint.com/python/python_dictionary.htm

Tuple values cannot be changed
mytuple = ("one", 1, 'x')
print(mytuple)

print connection[Value]

Tuple index in dict

for
    if condition:
        continue
    if condition:
        break

for condition:
    if pckt.type!= "TCP":
        continue
        if pckt.flags not in ("syn", "ack")
            continue


myReq = (pcap.sip, pcap.dport ect)
mySynData[myReq] = 1
print(mySynData)


if (flags = "ack")
    delete mySynData[(...)]
"""
