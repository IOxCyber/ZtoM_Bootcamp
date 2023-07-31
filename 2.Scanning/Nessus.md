## Nessus tool (Community Edition):
- Designed to help `identify security vulnerabilities and misconfigurations in computer systems, networks, and applications.`

## Features:
1. Vulnerability Scanning: `To discover known security vulnerabilities`, missing patches, weak configurations, and other potential issues.
2. Plugin Support: `Collection of plugins to detect a wide range of vulnerabilities`
3. Policy and Compliance Auditing: `Assess systems against controls based on security policies and compliance standards` eg. CIS benchmarks, HIPAA, PCI DSS, etc.
4. Reporting: `generates detailed reports that about identified vulnerabilities, severity levels, and suggested remediation steps.`
5. Integration: `Can integrate with other security tools and facilitate the automated sharing of data.`

## Policies: `filetype: .nessus`
- `Predefined configuration or allow Custom Templates creation to perform a scan`.
- Once created, can be selected from the `Scan Templates` on `Scan Page`.
- We can `Create, Import, Modify or Delete` a policy.

## Scans Templates:
- Here, you can `create, view, and manage scans and resources.`
 
## Notes:
- While Nessus complies with plugins, we can't create scans, view policies or plugin rules.
- 


> Download from [here](tenable.com/Download/nessus?)
# Installation On kali: 
- `sudo dpkg -i package_name`
- To Start: `copy path, displayed after successfully installed the nessus tool.`
- To configure: `go to displayed link eg. https ://kali:port/` in browser, provide email ID to get the `Activation Code`
- It'll take ~45+ mins to set up (Plugin update takes more time.).
