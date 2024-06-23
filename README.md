This is my fifth task as a Cyber Security Intern at Prodigy InfoTech where I was supposed to develop a packet sniffer tool that captures and analyzes network packets and display relevant information such as source and destination IP addresses, protocols, and payload data while ensuring the ethical use of the tool for educational purposes.

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
