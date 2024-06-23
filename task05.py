from scapy.all import *

def packet_handler(packet):
    if IP in packet:
        ip_src = packet[IP].src
        ip_dst = packet[IP].dst
        protocol = packet[IP].proto
        print(f"IP Packet: {ip_src} -> {ip_dst} | Protocol: {protocol}")

        if TCP in packet:
            tcp_sport = packet[TCP].sport
            tcp_dport = packet[TCP].dport
            payload = packet[TCP].payload
            print(f"TCP Packet: {ip_src}:{tcp_sport} -> {ip_dst}:{tcp_dport}")
            if payload:
                print(f"Payload: {payload}")
        
        elif UDP in packet:
            udp_sport = packet[UDP].sport
            udp_dport = packet[UDP].dport
            payload = packet[UDP].payload
            print(f"UDP Packet: {ip_src}:{udp_sport} -> {ip_dst}:{udp_dport}")
            if payload:
                print(f"Payload: {payload}")
        
        print("--------------------")

def main():
    print("Packet Sniffer started...")

    # Capture packets indefinitely
    sniff(prn=packet_handler, store=0)

if __name__ == "__main__":
    main()
