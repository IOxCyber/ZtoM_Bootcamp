## Nessus tool: `CVE: Common Vulnerability `
- Designed to help `identify security vulnerabilities and misconfigurations in computer systems, networks, and applications.`
- It's a Automated vulnerability scanner.
- can scan for a specific CVE (Common Vulnerabilities and Exposures)
- Nessus has the ability to login to remote Linux (with SSH) & Windows (MS auth technologies).
- Performs following scanning eg. 
- - Port Scanning, Banner Grabbing, OS & Service Detection, Vulnerability Detection (Signature based detection)

## Vulnerability Management Lifecycle:
1. `Discover/Identify` all the critical assets, systems, container etc.
2. `Prioritise Assets` Based on risk/vulnerability.
3. Assess
4. Report, with the Identified Vulnerabilities, severity level & remediation steps.
5. Remediate, Deploy the patch to vulnerable systems.
6. Verify, Again run the scan to check if the vulnerabilities are mitigated.

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
- Provides separate templates for scanners & agents i.e Scanner Templates & Agent Templates.

## Components:

> # 1. Policies:
## Policies Types:
1. Predefined Policies/Scan Templates:
- `Created by Tenable and are based on best practices and industry standards` eg. basic network scans, web application scans, compliance-specific scans (e.g., PCI DSS), etc.

2. Custom Policies:
- `Allow organizations to modify the scanning process` according to their unique security requirements and constraints.
- Can be found in `User Defined` tab.

###

> # 2. Templates:
## A. Scanner Templates/Scan Types: `Discovery<>Vulnerabilities<>Compliance<>`
### 1. Discovery:
- Host Discovery `(Perform a simple scan to discover live hosts & Open Ports)`
- Attack Surface Discovery `(Use Bit Discovery to scan High-Level Domains & extract subdomains & DNS-related Data)`

### 2. Vulnerabilities:
- Basic Network Scan: `identify security vulnerabilities and misconfigurations in common services and systems.`
- Advanced Network Scan: `Same settings as Basic but with additional Configuration option`
- Advanced Dynamic Scan: `Here, you can configure dynamic plugin filters instead of manually selecting plugin` & any plugins that match your filters are automatically added to the scan or policy.
- Malware Scan: `Scans for malware on Windows and Unix systems`
- Mobile Device Scan `Nessus Manager Only`: 'Use this template to scan what is installed on the targeted mobile devices and report on the installed applications or application versions' vulnerabilities.'
- Web Application Tests: `Scan for published and unknown web vulnerabilities.`
- Credentialed Patch Audit: `Authenticates hosts and enumerates missing updates.`
- More: <img width="572" alt="image" src="https://github.com/IOxCyber/ZtoM_Bootcamp/assets/40174034/fe057977-b920-4b88-ac9b-64814b4ef313">

### 3. Compliance: 
- Audit Cloud Infrastructure: `Audits the configuration of third-party cloud services. eg. Amazon Web Service (AWS), Google Cloud Platform, Microsoft Azure, Rackspace, Salesforce.com, and Zoom`
- Internal PCI Network Scan: `To ensure compliance with the Payment Card Industry Data Security Standard (PCI DSS)`
- MDM Config Audit: `targets Mobile Device Management (MDM) configurations.`
- Offline Config Audit: Assesses the security of configuration files and settings on a target system or device, `even when the system is offline or not actively running.`
- Policy Compliance Auditing: `Audits system configurations against a known baseline.` eg. password complexity, system settings, or registry values on Windows & running processes, user security policy, and content of files in Linux.
- SCAP and OVAL Auditing: The National Institute of Standards and Technology (NIST) Security Content Automation Protocol (SCAP) is `a set of policies for managing vulnerabilities and policy compliance in government agencies`
- Unofficial PCI Quarterly External Scan.

## B. Agent Templates (Tenable Nessus Manager Only):
- 2 types of Agent Template Categories:
    1. Vulnerabilities
      - <img width="568" alt="image" src="https://github.com/IOxCyber/ZtoM_Bootcamp/assets/40174034/6cc2aa70-a2f6-4f89-b8fa-ea90013d31df">

    2. Compliance:
      - <img width="573" alt="image" src="https://github.com/IOxCyber/ZtoM_Bootcamp/assets/40174034/acc601db-9038-462d-83fd-fd445ebb54d6">

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
