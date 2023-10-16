# Information GatheringRedHawk

## Two Types of Recon
  1. Active - By Interacting with target eg. social engineering(Interviewing), automated scanning or manual scanning etc 
  2. Passive - Indirectly (Middle source) eg. thu a websites eg. ipchecker, whatweb to gather OSINT.

###

## To get IP address of a Target:
ping - To send ICMP packets to the website (Uses no ports)
eg. ping xx.xx.xx.xx

### 1. nslookup 
To get IP of Target by Hostname.
eg. nslookup hostname

### 2. whois:
- To fetch DNS servers, physical location, Registration Data etc about target. 

### 3. WhatWeb: 
- *Web scanner to identify different web technologies used by the website.*
- Stealthy level(Http only) Whatweb offers both passive scanning and aggressive testing.

eg. whatweb website -v (verbose for better readability)

## Scan a VM(Home Network) by [whatweb - Kali tool](https://www.whatweb.net/) tool:
1. get the IP (ifconfig)
2. scan the complete range of IP.
3. whatweb ip-range --aggression <aggression_level> -v --no-error (to not show error which comes by scanning the offline IPs)
aggression_level: 1- Stealthy, 3- Aggressive, 4- Heavy

***To Save the result, use > (greater than sign):***
*Syntex*
> whatweb ip-range --aggression <aggression_level> -v --no-error > result.txt

###
###

### 4. [Harvester - Email Records/Tool](https://www.kali.org/tools/theharvester/)
: To find email accounts, subdomain names, virtual hosts, open ports / banners, and employee names related to a specific domain or all domains.

*Syntex*
> theHarvester -d <Target_Domain> -l <Int_Result_Limit> -b <Specific_source> or all

- By default gives 500 results.
- Not always provides required results.

### 5. [Hunter.io - Email Records/Site](https://hunter.io/?via=ion)
Paid or free account. same as theHarvester.
Only 5 mails without sign in

### 6. [Namecheckr - Web Site](https://www.namecheckr.com/) & [Namechk](https://namechk.com/)
To check username availability on different social media.


###

## Other Information Gathering tools can be download on VM from GitHub.
eg. , [Sherlock - to find usernames across social networks](https://www.kali.org/tools/sherlock/), [Other Tools](https://securitytrails.com/blog/osint-tools)


- How to Download tools from GitHub: 
*Syntex*
> git clone "GitHub_link_of_tool"


## How to enable Copy/Paste in VM: Devices > Drag and Drop > set Bidirectional. 













