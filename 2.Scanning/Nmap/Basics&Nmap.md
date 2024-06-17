# Scanning - The Second Phase of Pen Testing

## [Netdiscover](https://www.kali.org/tools/netdiscover/)
- Active/passive ARP reconnaissance tool.
- ```To check active Hosts on a network```
- leverages the Address Resolution Protocol (ARP) to discover connected clients on a network.


## [Nmap Network Mapper](https://nmap.online/en/nmap-commands) - Zenmap (Online Nmap)

### `By Default Nmap uses the SYN scan (-sS) if the user has the necessary privileges (root/administrator), otherwise it falls back to a TCP connect scan (-sT).`

- Host discovery(process of calculating of live hosts.) is also known as ping scan.
- Can useful in Port Status, OS version, Protocal Version.
- Between the protocols User Datagram Protocol (UDP) and Transmission Control Protocol (TCP), ```there are 65,535 ports available for communication between devices.```

[Free site to learning nmap - scanme.nmap.org](http://scanme.nmap.org/)

## Flags:
1. -sS (SYN Quick Scan/ default scan mode)
- `less likely to be logged by the target system (IDS), Faster due to sending fewer packets` 
- need root/administrator privileges to send raw packets
2. -sT (TCP full connect scan)
- Nmap uses the operating system's networking API to establish a full TCP connection with the target port, sends a SYN packet to the target port.
- If the port is open, the target responds with a SYN/ACK, completes the handshake with an ACK, establishing a full connection.
- Nmap then closes the connection with a FIN packet or by sending an RST packet.
- `Because a full connection is established, it is more likely to be logged by the target system, making it easier to detect.`

3. -sU(UDP slow) 
- `To discover open UDP ports on a target, slower`
- `Identifies services running on non-standard ports that might be missed by TCP scans.`
- Many firewalls and IDS are less configured to log UDP traffic compared to TCP.
- Scanning for services like DNS, SNMP, NTP, and others that typically run on UDP.

4. -sA(ACK)
- `Helps in understanding firewall rules and policies by identifying which ports are filtered.`
- less likely to be logged.

5. -sL (List out Target IPs/ Host Discovery list)

## [Cheatsheet Common Scans](https://www.stationx.net/nmap-cheat-sheet/):
1. ```nmap -sn x.x.x.x/24 - Ping Scan (CIDR Notation)/ Disable Port scanning. Same as NetDiscover.```
2. ```nmap -Pn x.x.x.x/24 - No Ping (skip Host Discovery, Consider all hosts Up/Online)```
3. nmap 192.168.1.1 - Scan a single IP
4. nmap 192.168.1.1 192.168.2.1 -	Scan specific IP(s)
5. nmap 192.168.1.1 -p port1,port2 or port range(1-1234)	- Port scan for a range
6. nmap 192.168.1.1-254 - Scan a range
7. nmap scanme.nmap.org -	Scan a domain
8. nmap -iL targets.txt - Scan targets from a file
9. nmap -iR 100	Scan 100 - random hosts.
10. nmap --top-ports <num> - to scan specified top ports.

11. nmap --traceroute x.x.x.x - To check the traceroute(different routers through packet passes) taken by a packet to reach the destination
12. nmap 192.168.1.1 –top-ports 2000	- Port scan the top x ports
13. ```nmap 192.168.1.1 -sV	- Attempts to determine the version of the service running on port```
14. ```nmap 192.168.1.1 -A -	Enables OS detection, version detection, script scanning, and traceroute ~(Aggressive Scan)~```
15. ```nmap 192.168.1.1 -O	- Remote OS detection using TCP/IP stack fingerprinting```
16. nmap 192.168.1.1 -oN	result.txt target_IP - To save scan result in a file
17. nmap 192.168.1.1 -v - **Verbose mode, to see what's happening after running nmap cmd.**
18. nmap –exclude 192.168.1.1	- Exclude listed hosts.
19. ```nmap -F x.x.x.x - Fast mode (scan 1000 ports), top 100 ports most useful one.```
20. ```nmap -oN output x.x.x.x - To save Output of scan or use >> fileName```

Note: 
  - Option can be given before or after the IP is provided.
  - On Windows VM, firewall can block ping scan as well as nmap scan. (Turn off Windows defender firewall before testing in VM)) 
  - To turn off Windows defender firewall: Control Panel > System & Security > Turn Windows defender firewall on or off.
  

[^1]: TCP (Transmission Control Protocol) connection-oriented, 3 way handshake (SYN, SYN/ACK, ACK), No packet loss protocol, used in file transfer, chats.
[^2]: UDP (User Data Procol) connectionless, fast protocol, may loss packets, used in audio/video stream.
