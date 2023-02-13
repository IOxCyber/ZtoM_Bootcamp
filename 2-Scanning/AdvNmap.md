## Advance Nmap: 
### [Script Scripting Engine](https://nmap.org/book/nse-usage.html)
- Use to Network Discovery, Service, backdoor, detection, Vulnerability scanning.
- run with permission

### Script Category: To run a Category containing all the related scripts.
- Scripts Location: cd /usr/share/nmap/scripts
- To update the script DB: sudo nmap --script-updatedb
- Syntex: nmap --script Script_Name IP_Address Scan-Option eg. `nmap --script auth -sS 192.168.x.x`
- To get help menu for a script: `sudo nmap --script-help Script_Groups_Name`

### Script Groups: To run a specific script
- Syntex: nmap --script Script_Groups_Name IP_Address eg. `nmap --script firewall-bypass.nse 192.168.x.x`



### Most Useful Scripting Category:
- auth: This categorized scripts related to user authentication.
- broadcast: This is a very interesting category of scripts that use broadcast petitions to gather information. 
- brute: This category is for scripts that help conduct brute-force password auditing.
- default: This category is for scripts that are executed when a script scan is executed ( -sC ).
- discovery: This category is for scripts related to host and service discovery.
- dos: This category is for scripts related to denial of service attacks.
- exploit: This category is for scripts that exploit security vulnerabilities.
- external: This category is for scripts that depend on a third-party service. 
- fuzzer: This category is for Nmap scripts that are focused on fuzzing.
- intrusive: These scripts might crash system by generate lot of network noise, sysadmins considers it intrusive.
- malware: This category is for scripts related to malware detection.
- safe: This category is for scripts that are considered safe in all situations.
- version: This category is for NSE scripts that are used for advanced versioning.
- vuln: This category is for scripts related to security vulnerabilities.


### To login to target using different protocols:
- To make a connection to a port: `IP_Address:Port`
- To do ftp: `ftp 192.168.x.x`


## Vulnerability Analysis:
- Searching about a vulnerability on google or using tools such as searchsploit.

## Searchsploit: 
- lists out vulnerabilities associated with the version. (eg: `searchsploit software_version_name`)
- provides path, `locate path` to locate the file in the system.
- 

