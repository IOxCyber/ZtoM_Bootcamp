## Nessus tool (Community Edition):
- vulnerability assessment tool for Internal IPs (16 IPs) only with CE version.

- Download from [here](tenable.com/Download/nessus?)
- On kali 
- Installation: `sudo dpkg -i package_name`
- To Start: `copy path, displayed after successfully installed the nessus tool.`
- To configure: `go to displayed link eg. https ://kali:port/` in browser, provide email ID to get the `Activation Code`
- It'll take ~45+ mins to set up (Plugin update takes more time.).

- To Scan: New Scan > all type of scans available
- Basic Network Scan > Put nessary info > Target IP > Discovery (Port to scan) > Assessment (for known vulnerability) > save > Launch.

- After scan > click on scan name > Vulnerabilities in different category (Critical, Mixed, High, Medium, Low, Info)
- Drill down by clicking on the vulnerabilities > google it > Fix them

- Next in Exploitation Section >>
