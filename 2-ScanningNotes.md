# Scanning - The Second Phase of Pen Testing

## Defination:
- Focused on much deeper aspect of Information Gathering
- Mainly emphasized on collecting info on Technology using by the Target. 
- Accomplised by sending packets on target with [TCP[^1]/UDP[^2]] protol , returned with some info of target.
- looking for open ports (total 65535) of target eg. ssh 22, http 80, https 443, ftp 21, dns 53, smtp 25

## [Netdiscover](https://www.kali.org/tools/netdiscover/)
Active/passive ARP reconnaissance tool, To check active Hosts on a network
leverages the Address Resolution Protocol (ARP) to discover connected clients on a network.


## [Nmap Network Mapper](https://nmap.online/en/nmap-commands) - Zenmap (Online Nmap)
By default, Nmap performs a SYN Scan, host discovery and then performs a port scan against each host it determines is online.
Host discovery(process of calculating of live hosts.) is also known as ping scan.
Can useful in Port Status, OS version, Protocal Version.

[Free site to learning nmap - scanme.nmap.org](http://scanme.nmap.org/)

Flags:
-sS (SYN Quick Scan/ default scan mode), -sT (TCP connect scan), -sU(UDP slow), -sA(ACK), -sL (List out Target IPs/ Host Discovery list), 

[Cheatsheet Common Scans](https://www.stationx.net/nmap-cheat-sheet/):
1. nmap -sp x.x.x.x/24 - Ping Scan (CIDR Notation)
2. nmap -Pn x.x.x.x/24 - No Ping (skip Host Discovery, Consider all hosts Up/Online)
3. nmap 192.168.1.1 - Scan a single IP
4. nmap 192.168.1.1 192.168.2.1 -	Scan specific IP(s)
5. nmap 192.168.1.1 -p port1,port2 or port range	- Port scan for a range
6. nmap 192.168.1.1-254 - Scan a range
7. nmap scanme.nmap.org -	Scan a domain
8. nmap -iL targets.txt - Scan targets from a file
9. nmap -iR 100	Scan 100 - random hosts
10. nmap –exclude 192.168.1.1	- Exclude listed hosts
11. nmap --traceroute x.x.x.x - To check the traceroute taken by a packet to reach the destination
12. nmap 192.168.1.1 –top-ports 2000	- Port scan the top x ports
13. nmap 192.168.1.1 -sV	- Attempts to determine the version of the service running on port
14. nmap 192.168.1.1 -A -	Enables OS detection, version detection, script scanning, and traceroute ~(Aggressive Scan)~
15. nmap 192.168.1.1 -O	- Remote OS detection using TCP/IP stack fingerprinting
16. nmap 192.168.1.1 -oN	result.txt target_IP - To save scan result in a file
17. nmap 192.168.1.1 -v - Verbose mode, to see what's happening after running nmap cmd.

Note: -Option can be given before or after the IP is provided.



## [Metasploitable VM - for scanning purpose as Vulnerable Target](https://sourceforge.net/directory/windows/?q=vulnerable+machine)





[^1]: TCP (Transmission Control Protocol) connection-oriented, 3 way handshake (SYN, SYN/ACK, ACK), No packet loss protocol, used in file transfer, chats.
[^2]: UDP (User Data Procol) connectionless, fast protocol, may loss packets, used in audio/video stream.
