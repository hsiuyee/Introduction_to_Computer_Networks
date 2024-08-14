from scapy.config import conf
conf.ipv6_enabled = False
from scapy.all import *
import sys

# Get the path of the pcap file
INPUTPATH = '/home/cn2023-lab1/Desktop/out/TCP_h3.pcap'

# Read the pcap file
packets = rdpcap(INPUTPATH)

# Initialize the variable to store total transmit bits for port 7777
total_transmit_bits = 0

# Iterate through all TCP packets
for packet in packets[TCP]:
    # Get the source and destination ports
    src_port = packet[2].sport
    dst_port = packet[2].dport

    # Check if the source port is 7777
    if dst_port == 7777:
        # Calculate the transmit bits for the current packet
        transmit_bits = len(packet)

        # Accumulate the transmit bits to the total
        total_transmit_bits += transmit_bits
        
print("--- TCP ---")
# Output the total transmit bits for port 7777
print(f"Flow1(h1->h3): {total_transmit_bits * 8 / 5000000} Mbps")

# Get the path of the pcap file
INPUTPATH = '/home/cn2023-lab1/Desktop/out/TCP_h3.pcap'

# Read the pcap file
packets = rdpcap(INPUTPATH)

# Initialize the variable to store total transmit bits for port 7777
total_transmit_bits = 0
# Iterate through all TCP packets
for packet in packets[TCP]:
    # Get the source and destination ports
    src_port = packet[2].sport
    dst_port = packet[2].dport

    # Check if the source port is 7777
    if dst_port == 7778:
        # Calculate the transmit bits for the current packet
        transmit_bits = len(packet)

        # Accumulate the transmit bits to the total
        total_transmit_bits += transmit_bits
        
        
# Output the total transmit bits for port 7777
print(f"Flow2(h1->h3): {total_transmit_bits * 8 / 5000000} Mbps")

# Get the path of the pcap file
INPUTPATH = '/home/cn2023-lab1/Desktop/out/TCP_h4.pcap'

# Read the pcap file
packets = rdpcap(INPUTPATH)

# Initialize the variable to store total transmit bits for port 7777
total_transmit_bits = 0
count = 0
# Iterate through all TCP packets
for packet in packets[TCP]:
    # Get the source and destination ports
    src_port = packet[2].sport
    dst_port = packet[2].dport

    # Check if the source port is 7777
    if dst_port == 7779:
        # Calculate the transmit bits for the current packet
        transmit_bits = len(packet)

        # Accumulate the transmit bits to the total
        total_transmit_bits += transmit_bits
        
        
# Output the total transmit bits for port 7777
print(f"Flow3(h2->h4): {total_transmit_bits * 8 / 5000000} Mbps")

print()
print("--- UDP ---")

# Get the path of the pcap file
INPUTPATH = '/home/cn2023-lab1/Desktop/out/UDP_h3.pcap'

# Read the pcap file
packets = rdpcap(INPUTPATH)

# Initialize the variable to store total transmit bits for port 7777
total_transmit_bits = 0
# Iterate through all UDP packets
for packet in packets[UDP]:
    # Get the source and destination ports
    src_port = packet[2].sport
    dst_port = packet[2].dport

    # Check if the source port is 7777
    if dst_port == 7787:
        # Calculate the transmit bits for the current packet
        transmit_bits = len(packet)

        # Accumulate the transmit bits to the total
        total_transmit_bits += transmit_bits
        
# Output the total transmit bits for port 7777
print(f"Flow1(h1->h3): {total_transmit_bits * 8 / 5000000} Mbps")

# Get the path of the pcap file
INPUTPATH = '/home/cn2023-lab1/Desktop/out/UDP_h3.pcap'

# Read the pcap file
packets = rdpcap(INPUTPATH)

# Initialize the variable to store total transmit bits for port 7777
total_transmit_bits = 0

for packet in packets[UDP]:
    # Get the source and destination ports
    src_port = packet[2].sport
    dst_port = packet[2].dport

    # Check if the source port is 7777
    if dst_port == 7788:
        # Calculate the transmit bits for the current packet
        transmit_bits = len(packet)

        # Accumulate the transmit bits to the total
        total_transmit_bits += transmit_bits
        
# Output the total transmit bits for port 7777
print(f"Flow2(h1->h3): {total_transmit_bits * 8 / 5000000} Mbps")

# Get the path of the pcap file
INPUTPATH = '/home/cn2023-lab1/Desktop/out/UDP_h4.pcap'

# Read the pcap file
packets = rdpcap(INPUTPATH)

# Initialize the variable to store total transmit bits for port 7777
total_transmit_bits = 0

# Iterate through all UDP packets
for packet in packets[UDP]:
    # Get the source and destination ports
    src_port = packet[2].sport
    dst_port = packet[2].dport

    # Check if the source port is 7777
    if dst_port == 7789:
        # Calculate the transmit bits for the current packet
        transmit_bits = len(packet)

        # Accumulate the transmit bits to the total
        total_transmit_bits += transmit_bits
        
# Output the total transmit bits for port 7777
print(f"Flow3(h2->h4): {total_transmit_bits * 8 / 5000000} Mbps")


