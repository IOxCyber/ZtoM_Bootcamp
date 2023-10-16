## 1. [Recon-ng - Kali tool](https://hackertarget.com/recon-ng-tutorial/)
- Full featured passive recon framework for web-based OSINT.
- Similar to Metasploit framework but It's ```used only to gather OSINT not for exploit the target.```
- can used other tools features by adding API keys.

Usage:

    Recon-ng is a complete package of Information gathering tools.
    Recon-ng can be used to find IP Addresses of target.
    Recon-ng can be used to look for error based SQL injections.
    Recon-ng can be used to find sensitive files such as robots.txt.
    Recon-ng can be used to find information about Geo-IP lookup, Banner grabbing, DNS lookup, port scanning, sub-domain information, reverse IP using WHOIS lookup .
    Recon-ng can be used to detects Content Management Systems (CMS) in use of a target web application,
    InfoSploit can be used for  WHOIS data collection, Geo-IP lookup, Banner grabbing, DNS lookup, port scanning, sub-domain information, reverse IP, and MX records lookup
    Recon-ng is a complete package (TOOL)  for information gathering. This tool is free and Open Source.
    Recon-ng subdomain finder modules is used to find subdomains of a singer domain.
    Recon-ng can be used to find robots.txt file of a website.
    Recon-ng port scanner modules find closes and open ports which can be used to maintain access to the server.
    Recon-ng has various modules that can be used to get the information about target.

## Syntex
> recon-ng --help (use help command wherever seemed stucked)
> 
> module-path > `info` (to get info on a module)
>
> Create a Workspace: `workspaces create <workspace-name>`
> 
> Search for the Modules in marketplaces `marketplace serach <keyword>`
>
> Install the Modules: `marketplace install <module-path>`
>
> set an option in modules: `option set or unset <Option-Name>`
> 
> Load modules:  `workspace load <module_path>`
>
> set the options: `option set <Option-Value>` > `run`
>
> To show any result from Dashboard: `eg. show hosts/contacts`

## Adding API Keys:
- keys add <API-Name> <API-Keys>

## Database: To interact/modify with the Data stored in the Tool itself.
- db <delete|insert|notes|query|schema>


*[Get Started](https://www.geeksforgeeks.org/recon-ng-installation-on-kali-linux/)*

Defination:
> [recon-ng][default] default is workspaces (like a folder), can create workspaces
> [recon-ng][default] > marketplace search <keywork> 
 


