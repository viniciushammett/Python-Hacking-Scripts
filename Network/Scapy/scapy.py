import sys
try:
    from scapy.all import *
except:
    sys.exit("[!] Install library using the command: sudo pip3 install scapy")

conf.verb = 0 

port = ["Define range ports"]

IPpackege = IP(dst ="Define host IP")
TCPpackege = TCP(dport=port, flags="S")
package = IPpackege/TCPpackege

ans, unans = sr(package, inter=0.1, timeout=1)

print("Port\tState")
for PackageReceveid in ans:
    print(PackageReceveid[1][IP].sport,"\t", PackageReceveid[1][TCP].print("%flags%"))