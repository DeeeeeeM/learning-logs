Reconnaissance & Footprinting

## 1. Reconnaissance

### Active Reconnaissance

**Definition:** Directly interacts with/probes the target to gather information.

**Examples:**

- Host enumeration
    
- Network enumeration
    
- User enumeration
    
- Group enumeration
    
- Network share enumeration
    
- Web page enumeration
    
- Application enumeration
    
- Service enumeration
    
- Packet crafting
    
- Port scanning
    

### Passive Reconnaissance

**Definition:** Gathers information without directly interacting with the target.

**Examples:**

- Third-party databases
    
- Network traffic intelligence
    
- Domain enumeration
    
- Packet inspection
    
- OSINT
    

|Type|Interaction|Example|
|---|---|---|
|Active|Direct interaction|Nmap scan|
|Passive|No direct interaction|WHOIS, search engines, public databases|

---

# 2. OSINT

**OSINT — Open-Source Intelligence**

Collecting information from publicly available sources.

### Common Sources

- Search engines
    
- Social media
    
- DNS records
    
- WHOIS
    
- Certificate Transparency
    
- Public documents
    
- GitHub/GitLab
    
- Breach information
    
- Web archives
    

### Useful OSINT Tools

**WhatsMyName (WMN)**

- Searches whether a username exists across many websites.
    
- Useful for identifying online accounts.
    

**Start.me OSINT Tools**

- Collection of OSINT resources.
    

Resource:  
[https://www.osinttechniques.com/osint-tools.html](https://www.osinttechniques.com/osint-tools.html)

---

# 3. SpiderFoot

**Purpose:** Automated reconnaissance and OSINT scanner.

- Queries 1000+ open-information sources.
    
- Provides GUI-based reconnaissance.
    
- Can target:
    
    - Domains
        
    - IP addresses
        
    - Subnets
        
    - ASNs
        
    - Emails
        
    - Phone numbers
        
    - Names
        

### Start SpiderFoot

```bash
spiderfoot -l 127.0.0.1:5001
```

### Profiles

|Profile|Purpose|
|---|---|
|Passive|Public information without direct target interaction|
|Footprint|Discover external-facing assets|
|Investigate|Investigate indicators/entities|
|All|Comprehensive scan|

### Output

- DNS records
    
- Co-hosted sites
    
- Open ports
    
- Leaked credentials
    
- Geolocation
    
- Relationship graphs
    

### Export

- CSV
    
- JSON
    
- GEXF
    

---

# 4. Recon-ng

**Purpose:** Modular framework for reconnaissance.

### Start

```bash
recon-ng
```

### Workspace

```text
workspaces create test
```

### Marketplace

```text
marketplace refresh
marketplace search bing
marketplace install recon/domains-hosts/bing_domain_web
```

### Load Module

```text
modules load recon/domains-hosts/bing_domain_web
```

### Configure Target

```text
options set source hackxor.net
```

### Run

```text
run
```

### View Results

```text
dashboard
show hosts
```

**Key concept:** Recon-ng uses modules and workspaces to organize reconnaissance.

---

# 5. Shodan

**Shodan:** Internet-wide search engine for connected devices/services.

Shodan continuously scans Internet-connected systems and stores results in a searchable database.

### Useful For

- Internet-facing hosts
    
- IoT devices
    
- Exposed services
    
- Potentially vulnerable systems
    
- Security research
    

**Website:**  
[https://www.shodan.io/](https://www.shodan.io/)

---

# 6. DNS Enumeration

**Purpose:** Discover domain/IP information and potential entry points.

### Tools

|Tool|Purpose|
|---|---|
|`nslookup`|DNS lookups|
|`host`|DNS/rDNS lookups|
|`dig`|Detailed DNS queries|
|WHOIS|Domain/IP registration information|

### Basic nslookup

```bash
nslookup <website>
```

### Find Name Servers

```text
nslookup
set type=ns
cisco.com
```

### Query Specific DNS Server

```bash
nslookup netacad.com 8.8.8.8
```

Useful for comparing results from different DNS resolvers.

### Split-Horizon DNS

A domain can resolve differently depending on where the query originates.

Example:

```text
Internal network → 10.0.0.5
Internet → Public IP
```

---

# 7. WHOIS

**Purpose:** Obtain domain/IP registration information.

### Commands

```bash
whois h4cker.org
```

```bash
whois cisco.com
```

```bash
whois 72.163.5.201
```

Can provide information such as:

- Domain registration
    
- Registrar
    
- Administrative information
    
- Technical information
    
- IP registration information
    

---

# 8. DIG

**Purpose:** Detailed DNS querying.

### Basic DNS Query

```bash
dig cisco.com
```

### IPv6 Address

```bash
dig cisco.com AAAA
```

### Query Name Servers

```bash
dig cisco.com 8.8.8.8 ns
```

### Reverse DNS

```bash
dig -x 72.163.5.201
```

**Reverse DNS (rDNS):**

```text
IP address → Hostname
```

### host

```bash
host 72.163.10.1
```

```bash
host hsrp-72-163-10-1.cisco.com
```

### FCrDNS

**Forward-Confirmed Reverse DNS**

Used particularly in email security to verify that forward and reverse DNS information correspond.

---

# 9. Cloud vs Self-Hosted

A company can own:

```text
example.com
subdomain.example.com
```

while the actual application is hosted by a cloud provider.

**Important:**  
Domain ownership ≠ application hosting location.

Recon may therefore reveal:

- Company-owned domains
    
- Cloud-hosted applications
    
- Subdomains
    
- Different infrastructure providers
    

---

# 10. Port Scanning

**Port scan:** Active reconnaissance that sends probes to determine whether services are listening.

### TCP SYN Scan Concept

```text
Scanner → SYN → Target
Scanner ← SYN/ACK → Open
Scanner ← RST → Closed
No response → Filtered
```

|Response|Meaning|
|---|---|
|SYN/ACK|Port open/listening|
|RST|Port closed|
|No response|Filtered|

---

# 11. Social Media Reconnaissance

Information can be gathered from:

- LinkedIn
    
- Facebook
    
- Instagram
    
- X/Twitter
    
- Other public profiles
    

### Information of Interest

- Employees
    
- Job roles
    
- Technologies used
    
- Company infrastructure
    
- Organizational structure
    
- Projects
    

**Job postings** can also reveal:

- Technology stacks
    
- Operating systems
    
- Cloud platforms
    
- Security tools
    
- Required skills
    

---

# 12. Company Reputation & Security Posture

Previous security incidents can reveal information about an organization.

Potential information:

- Previous breaches
    
- Exposed credentials
    
- Security weaknesses
    
- Technology information
    
- Public incident reports
    

---

# 13. SSL/TLS Certificate Reconnaissance

SSL/TLS certificates can reveal information about:

- Domains
    
- Subdomains
    
- Organization information
    
- Certificate configuration
    
- Potential cryptographic weaknesses
    

### Certificate Transparency (CT)

Publicly trusted Certificate Authorities log issued certificates in publicly available, auditable logs.

Useful for discovering certificates issued for domains.

### crt.sh

[https://crt.sh/](https://crt.sh/)

---

# 14. SSL/TLS Tools

|Tool|Purpose|
|---|---|
|`sslscan`|Identify supported SSL/TLS ciphers and certificate information|
|`ssldump`|Analyze/decode SSL traffic|
|`sslyze`|Analyze SSL/TLS server configuration|
|`sslh`|Run multiple services on port 443|
|`sslsplit`|SSL/TLS MITM-related testing|

### sslscan

```bash
sslscan netacad.com
```

### Export output to HTML

```bash
sslscan netacad.com | aha > sfa_cert.html
```

**aha:** Converts terminal output into HTML while preserving formatting.

---

# 15. Breach / Password Information

Public breach information can expose:

- Usernames
    
- Passwords
    
- Email addresses
    
- Organizational information
    

### Tools Mentioned

- WhatBreach
    
- LeakLooker
    
- Buster
    
- Scavenger
    
- PwnDB
    
- h8mail
    

**Use only with authorized/lawful investigations.**

Resources:

- [https://github.com/Ekultek/WhatBreach](https://github.com/Ekultek/WhatBreach)
    
- [https://github.com/woj-ciech/LeakLooker](https://github.com/woj-ciech/LeakLooker)
    
- [https://github.com/sham00n/buster](https://github.com/sham00n/buster)
    
- [https://github.com/rndinfosecguy/Scavenger](https://github.com/rndinfosecguy/Scavenger)
    
- [https://github.com/davidtavarez/pwndb](https://github.com/davidtavarez/pwndb)
    

---

# 16. File Metadata

Files can contain useful metadata.

### Examples

- Images
    
- Word documents
    
- Excel files
    
- PowerPoint files
    

### EXIF

**EXIF — Exchangeable Image File Format**

May contain information associated with images.

Potential information:

- Camera/device information
    
- Dates
    
- Location information
    
- Software used
    

---

# 17. Search Engine Reconnaissance

Search engines can be used to discover publicly accessible information.

### Common Operators

|Operator|Purpose|Example|
|---|---|---|
|`filetype:`|Search specific file type|`filetype:xls`|
|`inurl:`|Search within URLs|`inurl:search-text`|
|`link:`|Search links containing a term|`link:example.com`|
|`intitle:`|Search page titles|`intitle:"Index of /etc"`|

### Google Dorking

Using advanced search operators to locate specific publicly accessible information.

Example from the material:

```text
intext:JSESSIONID OR intext:PHPSESSID inurl:access.log ext:log
```

Another example:

```text
"public $user =" | "public $password =" | "public $secret =" | "public $db =" ext:txt | ext:log -git
```

**Important:** Only use against systems/data you are authorized to investigate.

### Google Hacking Database

[https://www.exploit-db.com/google-hacking-database/](https://www.exploit-db.com/google-hacking-database/)

---

# 18. Web Archives

Archives can reveal historical versions of websites.

### Resources

**Internet Archive / Wayback Machine**

[https://web.archive.org/](https://web.archive.org/)

Useful for:

- Old pages
    
- Removed content
    
- Historical subdomains
    
- Previous site structure
    
- Historical technologies
    

---

# 19. Public Source Code

Public repositories can expose useful information about an organization.

### Examples

- GitHub
    
- GitLab
    

Potentially exposed information:

- Application code
    
- Configuration
    
- Technology stack
    
- Internal URLs
    
- API information
    
- Credentials/secrets accidentally committed
    

---

# 20. Pentest Environment

Recommended environments from the material:

### Kali Linux

[https://www.kali.org/](https://www.kali.org/)

### Parrot OS

[https://www.parrotsec.org/](https://www.parrotsec.org/)

### WebSploit Labs

[https://websploit.org/](https://websploit.org/)

---

# Quick Command Reference

```bash
# SpiderFoot
spiderfoot -l 127.0.0.1:5001

# Recon-ng
recon-ng

# DNS
nslookup <website>
nslookup netacad.com 8.8.8.8

# WHOIS
whois <domain>
whois <IP>

# DIG
dig <domain>
dig <domain> AAAA
dig <domain> 8.8.8.8 ns
dig -x <IP>

# Reverse DNS
host <IP>

# SSL/TLS
sslscan <domain>

# Export SSL scan
sslscan <domain> | aha > report.html
```

---

# Key Values to Remember

|Concept|Remember|
|---|---|
|Active Recon|Directly interacts with target|
|Passive Recon|Does not directly interact with target|
|OSINT|Publicly available information|
|SpiderFoot|Automated OSINT/recon|
|Recon-ng|Modular reconnaissance framework|
|Shodan|Search engine for Internet-connected systems|
|DNS|Maps domains ↔ IP/infrastructure information|
|WHOIS|Domain/IP registration information|
|`nslookup`|Basic DNS queries|
|`dig`|Detailed DNS queries|
|rDNS|IP → hostname|
|FCrDNS|Forward + reverse DNS confirmation|
|Port Scan|Determines listening/filtered/closed ports|
|CT|Public certificate issuance logs|
|`sslscan`|SSL/TLS reconnaissance|
|EXIF|File/image metadata|
|Google Dorking|Advanced search-engine reconnaissance|
|Wayback Machine|Historical website information|
|GitHub/GitLab|Public source-code reconnaissance|

---

# Reconnaissance Flow

```text
Target
  ↓
Passive Recon
  ↓
OSINT
  ↓
DNS / WHOIS
  ↓
Subdomains / IPs
  ↓
Certificate Information
  ↓
Public Documents / Metadata
  ↓
Social Media / Job Posts
  ↓
Active Recon
  ↓
Host / Service / Port Enumeration
  ↓
Build Target Profile
```

> **Core idea:** Reconnaissance builds a picture of the target before deeper security testing.

## Resources

- OSINT Tools: [https://www.osinttechniques.com/osint-tools.html](https://www.osinttechniques.com/osint-tools.html)
- Kali Linux: [https://www.kali.org/](https://www.kali.org/)
    
- Parrot OS: [https://www.parrotsec.org/](https://www.parrotsec.org/)
    
- WebSploit Labs: [https://websploit.org/](https://websploit.org/)
    
- crt.sh: [https://crt.sh/](https://crt.sh/)
    
- Shodan: [https://www.shodan.io/](https://www.shodan.io/)
    
- Google Hacking Database: [https://www.exploit-db.com/google-hacking-database/](https://www.exploit-db.com/google-hacking-database/)
    
- Wayback Machine: [https://web.archive.org/](https://web.archive.org/)
    
- SpiderFoot video: [https://www.youtube.com/watch?v=yw_KPBdAKHo](https://www.youtube.com/watch?v=yw_KPBdAKHo)