## Advance Nmap: 
### [Script Category](https://nmap.org/book/nse-usage.html)
- Scripts Location: cd /usr/share/nmap/scripts
- Syntex: nmap --script Script_Category_Name IP_Address Scan-Option eg. `nmap --script auth -sS 192.168.x.x`
- To get help menu for a script: `sudo nmap --script-help Script_Groups_Name`

### Script Groups:
- Syntex: nmap --script Script_Groups_Name IP_Address eg. `nmap --script firewall-bypass.nse 192.168.x.x`


### To login to target using different protocols:
- To make a connection to a port: `IP_Address:Port`
- To do ftp: `ftp 192.168.x.x`
- 

## Vulnerability Analysis:
- Searching about a vulnerability on google.
- using `searchsploit`: results the vulnerabilities with the version. (eg: searchsploit Software_version_name)
- 
