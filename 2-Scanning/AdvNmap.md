## Advance Nmap: 
### [Script Scripting Engine](https://nmap.org/book/nse-usage.html)
- Use to Network Discovery, Service, backdoor, detection, Vulnerability scanning.

### Script Category: To run a Category containing all the related scripts.
- Scripts Location: cd /usr/share/nmap/scripts
- Syntex: nmap --script Script_Name IP_Address Scan-Option eg. `nmap --script auth -sS 192.168.x.x`
- To get help menu for a script: `sudo nmap --script-help Script_Groups_Name`

### Script Groups: To run a specific script
- Syntex: nmap --script Script_Groups_Name IP_Address eg. `nmap --script firewall-bypass.nse 192.168.x.x`


### To login to target using different protocols:
- To make a connection to a port: `IP_Address:Port`
- To do ftp: `ftp 192.168.x.x`


## Vulnerability Analysis:
- Searching about a vulnerability on google or using tools such as searchsploit.

## Searchsploit: 
- lists out vulnerabilities associated with the version. (eg: `searchsploit software_version_name`)
- provides path, `locate path` to locate the file in the system.
- 

