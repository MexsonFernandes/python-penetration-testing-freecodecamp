#! /usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("Welcome to nmap tool")

ip = input(
    "Enter ip to scan: "
)

print("Scanning...", ip)

res = input("""
    Enter scan type:
    1 - SYN ACK
    2 - UDP
    3 - COMPREHENSIVE
""")

print("You selected: ", res)

def scan(s_methods, s_type):
    print("Nmap Version", scanner.nmap_version())
    scanner.scan(ip, '1-1024', s_methods)
    print(scanner.scaninfo())
    print("IP Status: ", scanner[ip].state())
    print("Protocols: ", scanner[ip].all_protocols())
    print("Open Ports: ", scanner[ip][s_type].keys())

def scan(s_type, ):


if res == '1':
    scan('-v sS','tcp')
elif res == '2':
    scan('-v sU', 'udp')
elif res == '3':
    comprehensive('-v -sS -sV -sC -A -O', 'tcp')
else:
    print('Wrong selection!')


