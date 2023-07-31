## Nessus tool (Community Edition):
- Designed to help `identify security vulnerabilities and misconfigurations in computer systems, networks, and applications.`

## Features:
1. Vulnerability Scanning: `To discover known security vulnerabilities`, missing patches, weak configurations, and other potential issues.
2. Plugin Support: `Collection of plugins to detect a wide range of vulnerabilities`
3. Policy and Compliance Auditing/Check: `Assess systems against controls based on security policies and compliance standards` eg. CIS benchmarks, HIPAA, PCI DSS, etc.
4. Reporting: `generates detailed reports that about identified vulnerabilities, severity levels, and suggested remediation steps.`
5. Integration: `Can integrate with other security tools and facilitate the automated sharing of data.`

## Policies or Custom Scan Templates: `filetype: .nessus`
- `Defines what types of Security Checks, and tests will be performed.`
- Once created, can be selected from the `Scan Templates` on `Scan Page`.
- We can `Create, Import, Modify or Delete` a policy.
- Within a policy, `users can select or exclude specific plugins`.
- Can define the frequency of scanning for target assets.
- Policies can include authentication credentials[^1]. 

## Policies Types:
1. Predefined Policies/Scan Templates:
- `Created by Tenable and are based on best practices and industry standards` eg. basic network scans, web application scans, compliance-specific scans (e.g., PCI DSS), etc.

2. Custom Policies:
- `Allow organizations to modify the scanning process` according to their unique security requirements and constraints.
- Can be found in `User Defined` tab.

## Scanner Templates/Scan Types: 
1. Discovery: 
- Host Discovery (Perform a simple scan to discover live hosts & Open Ports)
- Attack Surface Discovery (Use Bit Discovery to scan High-Level Domains & extract subdomains & DNS-related Data)

2. Vulnerabilities: 
- 

3. Compliance: 
- 
 
## Additional:
- Agent-Based Scanning (optional): A lightweight s/w installed, particularly useful for environments with restricted network access or offline systems.
- Cloud and Container Scanning (optional): supports scanning cloud-based infrastructure and container environments.
 
## IMP Notes:
- While Nessus complies with plugins, we can't create scans, view policies or plugin rules.
- Plugins are small scripts that perform individual security checks for various vulnerabilities and misconfigurations.

> Download from [here](tenable.com/Download/nessus?)
# Installation On kali: 
- `sudo dpkg -i package_name`
- To Start: `copy path, displayed after successfully installed the nessus tool.`
- To configure: `go to displayed link eg. https ://kali:port/` in browser, provide email ID to get the `Activation Code`
- It'll take ~45+ mins to set up (Plugin update takes more time.).

[^1]: Allow Nessus to login to the target or APp to perform more comprehensive scans eg. Auth Vulnerabilities check, yield more accurate & detailed results.
