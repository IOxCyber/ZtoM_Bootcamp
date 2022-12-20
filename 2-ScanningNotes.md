# Scanning - The Second Phase of Pen Testing

## Defination:
- Focused on much deeper aspect of Information Gathering
- Mainly emphasized on collecting info on Technology using by the Target. 
- Accomplised by sending packets on target with [TCP[^1]/UDP[^2]] protol , returned with some info of target.
- looking for open ports (total 65535) of target eg. ssh 22, http 80, https 443, ftp 21, dns 53, smtp 25

## To check active Hosts on a network by [Netdiscover](https://www.kali.org/tools/netdiscover/)
Active/passive ARP reconnaissance tool
leverages the Address Resolution Protocol (ARP) to discover connected clients on a network.


## Nmap Network Mapper()

## [Metasploitable VM - for scanning purpose as Vulnerable Target](https://sourceforge.net/directory/windows/?q=vulnerable+machine)





[^1]: TCP (Transmission Control Protocol) is a connection-oriented, 3 way handshake (SYN, SYN/ACK, ACK), No packet loss protocol, used in file transfer, chats.
[^2]: UDP (User Data Procol) is a connectionless, fast protocol, may loss packets, used in audio/video stream.
