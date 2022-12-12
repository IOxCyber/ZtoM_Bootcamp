# Information-Gathering stage of ethical hacking.

## Two Types of Recon
  1. Active - By Interacting with target eg. social engineering, active scanning etc 
  2. Passive - Indirectly (Middle source) eg. thu a websites.

for an Org: IP address, emails, phone numbers, Technologies used etc.

###

## How to get IP address of Target:
ping - To send ICMP packets to the website.
eg. ping xx.xx.xx.xx

nslookup - IP of Target by Hostname.
eg. nslookup hostname

whois: More info about target.
eg. DNS servers, physical location, Registration Data etc 

WhatWeb: Stealthy level(Http only), web scanner to to identify different web technologies used by the website.
Whatweb offers both passive scanning and aggressive testing.

eg. whatweb website -v (verbose for better readability)

## Scan a VM(Home Network) by [whatweb](https://www.whatweb.net/) tool:
1. get the IP (ifconfig)
2. scan the complete range of IP.
3. whatweb ip-range --aggression <aggression_level> -v --no-error (to not show error which comes by scanning the offline IPs)
aggression_level: 1- Stealthy, 3- Aggressive, 4- Heavy

##
***To Save the result, use > (greater than sign):***
eg: whatweb ip-range --aggression <aggression_level> -v --no-error > result.txt

###

**2. Passive**
By website: eg. ipchecker, whatweb 




