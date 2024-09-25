I developed a packet sniffer tool that captures and analyzes network packets and display relevant information such as source and destination IP addresses, protocols, and payload data while ensuring the ethical use of the tool for educational purposes.

A packet sniffer is a software or hardware tool that intercepts and logs traffic passing over a digital network. It captures data packets, which are units of data transmitted between network devices, and allows for inspection of these packets for various purposes, such as debugging, security analysis, network management, and performance monitoring.

I have used resources like Visual Studio Code as the text editor and used internet resources for debugging. This task is executed using the following steps:

<h3>Libraries:</h3>

We have used the _scapy_ library.

**Scapy** is a powerful Python library used for network packet manipulation. It allows users to craft, send, receive, and analyze network packets. With Scapy, you can perform a variety of network tasks, including sniffing network traffic, sending custom packets, and developing security tools or network applications.

![image](https://github.com/gpanushka/PRODIGY_CS_05/assets/167328539/46d64996-af18-4283-a628-767df358261c)

<h3>packet_handler function:</h3>
<h4>Extracting IP information:</h4>

![image](https://github.com/gpanushka/PRODIGY_CS_05/assets/167328539/37217ffc-e6bf-4b6e-b576-85ec32cd06f0)

Checks if the packet has an IP layer and extracts the source IP (ip_src), destination IP (ip_dst), and protocol number.

<h4>Handling TCP Packets:</h4>

![image](https://github.com/gpanushka/PRODIGY_CS_05/assets/167328539/b242fabc-2329-4a47-a7bb-ab79414019c1)

If the packet is a TCP packet, it extracts the source port (tcp_sport), destination port (tcp_dport), and payload.

<h4>Handling UDP Packets:</h4>

![image](https://github.com/gpanushka/PRODIGY_CS_05/assets/167328539/ac576760-7a65-4789-a6fa-cf4c749c86fc)

If the packet is a UDP packet, it extracts the source port (udp_sport), destination port (udp_dport), and payload.

TCP and UDP are fundamental protocols of the Internet that serve different purposes based on the requirements of reliability, speed, and efficiency. Understanding the differences between TCP and UDP is crucial for network design, troubleshooting, and application development.

<h4>Main Function:</h4>

![image](https://github.com/gpanushka/PRODIGY_CS_05/assets/167328539/998b420f-1b7b-468d-820c-dd083266f6b8)


This function starts the packet sniffer and captures packets indefinitely, using _sniff_ to apply the _packet_handler_ function to each captured packet. _store=0_ means packets are not stored in memory.

<h4>Entry Point:</h4>

![image](https://github.com/gpanushka/PRODIGY_CS_05/assets/167328539/0ebb7daf-4a54-4af4-ad2a-acb053c35477)

This condition allows the script to be run directly or imported without executing the sniffer.


<h3>OUTPUT:</h3>

On running the program, we get these IP addresses as the output.

![image](https://github.com/gpanushka/PRODIGY_CS_05/assets/167328539/264e8981-9c17-48e4-8459-36464b59b438)

![image](https://github.com/gpanushka/PRODIGY_CS_05/assets/167328539/ba74522b-77fa-45a5-a48e-68a89be370d8)


<h4>Explaination of the output:</h4>

<h5>Example for TCP:</h5>

IP Packet: 172.20.10.6 -> 13.89.179.11 | Protocol: 6
TCP Packet: 172.20.10.6:64786 -> 13.89.179.11:443
--------------------
Source IP: 172.20.10.6
Destination IP: 13.89.179.11
Protocol: TCP (protocol number 6)
Source Port: 64786
Destination Port: 443 (HTTPS)

<h5>Example for UDC</h5>

UDP Packets

IP Packet: 172.20.10.6 -> 172.20.10.15 | Protocol: 17
UDP Packet: 172.20.10.6:137 -> 172.20.10.15:137
Payload: NBNSHeader / NBNSQueryRequest who has '\\ANUSHKA'
--------------------
Source IP: 172.20.10.6
Destination IP: 172.20.10.15
Protocol: UDP (protocol number 17)
Source Port: 137 (NetBIOS Name Service)
Destination Port: 137 (NetBIOS Name Service)
Payload: Contains an NBNS query (NetBIOS Name Service query)
