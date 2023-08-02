## Compliance:
- Use to figure out the `non-compliant` system.
- We can include 1 or more compliance check or `Audits` when configure a scan or policy.
- It `supports custom audits with .audit file format` & can be used to audit the configuration of Unix, Windows, DBs, SCADA, IBM & Cisco systems.
- Each Compliance Check requires Credentials to login to different type of Systems.
- List can be find [here](https://docs.tenable.com/nessus/10_5/Content/Compliance.htm)


> If scan is based on User defined policy, you can't configure `Compliance settings in scan`.

### Supported Custom Audit Files:
1. Tenable-created audit file.
2. Security Content Automation Protocol(SCAP) Data Stream file.
3. Custom Audit file created or Customized for a specific environment.


### Steps to upload:
1. Login to Nessus.
2. Scan > My Scan > New Scan > Scan Templates
3. `Compliance tab` > Filter Compliance for `custom`
4. `Select the Audit type` from the List that can be uploaded.
5. `Add File` & select custom file to upload from the machine.
6. Save the Scan or Launch immediately.








