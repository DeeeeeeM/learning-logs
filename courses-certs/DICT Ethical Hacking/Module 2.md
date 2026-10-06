# Module 2: Information Gathering and Footprinting

## 1. Types of Penetration Tests

### Network Infrastructure Testing

Focuses on the security of the **network infrastructure**.

Common targets:

- Switches
    
- Routers
    
- Firewalls
    
- AAA servers — Authentication, Authorization, Accounting
    
- IDS/IPS
    
- Other network services

**Goal:** Determine how well the network infrastructure protects against attacks.

### Application-Based Testing

Focuses on security weaknesses in **applications and web applications**.

Common issues:

- Misconfiguration
    
- Input validation problems
    
- Injection vulnerabilities
    
- Logic flaws
    
- Authentication/authorization issues

**Resource:** OWASP Web Security Testing Guide (WSTG)

### Cloud Penetration Testing

Evaluates security in cloud environments.

Common cloud service models:

- **SaaS** — Software as a Service
    
- **PaaS** — Platform as a Service
    
- **IaaS** — Infrastructure as a Service

**Shared Responsibility Model:**

- Cloud Provider → Responsible for security of the cloud infrastructure.
    
- Customer → Responsible for security of what they deploy and configure in the cloud.

> Cloud security involves technical, physical, and administrative controls.

---

## 2. Bug Bounty

**Bug Bounty:** A program where organizations allow security researchers to find and report vulnerabilities in their systems.

Researchers may receive:

- Recognition
    
- Monetary rewards
    
- Other rewards

**Important:** Bug bounty testing must follow the program's **scope and rules**.

---

## 3. Testing Perspectives

The amount of information given to the tester determines the testing perspective.

### Unknown-Environment Test

Also commonly called **Black Box** testing.

- Tester receives little or no internal information.
    
- Simulates an external attacker.
    
- Tester must discover information through reconnaissance.

**Perspective:**

> "What could an outside attacker discover?"

### Known-Environment Test

Also commonly called **White Box** testing.

- Tester receives significant information about the target.
    
- May receive network diagrams, source code, credentials, documentation, etc.
    
- Allows deeper security assessment.

**Perspective:**

> "Find as many security weaknesses as possible with detailed knowledge of the environment."

### Partially Known Environment Test

Also commonly called **Gray Box** testing.

- Tester receives some information.
    
- May receive credentials without receiving complete infrastructure documentation.
    
- Combines elements of Black Box and White Box testing.

**Perspective:**

> "Simulate an attacker who has obtained some information or credentials."

### Quick Comparison

|Test|Information Given|Perspective|
|---|---|---|
|**Unknown / Black Box**|Little or none|External attacker|
|**Partially Known / Gray Box**|Some information|Limited insider / compromised account|
|**Known / White Box**|Significant information|Deep security assessment|

---

# 4. Penetration Testing Methodologies & Standards

## MITRE ATT&CK

**MITRE ATT&CK** is a knowledge base of adversary **tactics, techniques, and sub-techniques**.

Used by:

- Penetration testers
    
- Red teams
    
- Threat hunters
    
- Incident responders
    
- Security teams

### ATT&CK Coverage

Includes matrices for areas such as:

- Enterprise
    
- Mobile
    
- Cloud
    
- ICS

### Key Concept

**Tactics** = Why an attacker performs an action.

**Techniques** = How the attacker performs it.

Example:

> **Tactic:** Credential Access  
> **Technique:** Credential Dumping

ATT&CK can help security professionals understand and map real-world attacker behavior.

---

## OWASP Web Security Testing Guide (WSTG)

Focuses on **web application security testing**.

Covers testing for vulnerabilities such as:

- XSS — Cross-Site Scripting
    
- XXE — XML External Entity
    
- CSRF — Cross-Site Request Forgery
    
- SQL Injection
    
- Authentication weaknesses
    
- Authorization issues
    
- Configuration problems

**Main use:** Guide for testing and improving web application security.

---

## NIST SP 800-115

Provides guidance for **planning and conducting information security testing**.

Useful for:

- Planning security assessments
    
- Conducting technical security tests
    
- Analyzing findings
    
- Reporting results

**Main idea:** Provides a structured approach to security testing.

---

## OSSTMM

**Open Source Security Testing Methodology Manual**

Provides a structured and repeatable approach to security testing.

Areas include:

- Operational security
    
- Trust analysis
    
- Human security
    
- Physical security
    
- Wireless security
    
- Telecommunications
    
- Data networks
    
- Compliance
    
- Reporting

### Key Concept

**Repeatable + Consistent Testing**

The goal is to make security testing measurable and systematic.

---

## PTES

**Penetration Testing Execution Standard**

Provides a standardized approach to performing penetration tests.

### 7 Phases

1. **Pre-engagement Interactions**
    
    - Define scope, objectives, rules, and authorization.
        
2. **Intelligence Gathering**
    
    - Collect information about the target.
        
3. **Threat Modeling**
    
    - Identify potential attack paths and threats.
        
4. **Vulnerability Analysis**
    
    - Identify and analyze security weaknesses.
        
5. **Exploitation**
    
    - Validate vulnerabilities through controlled exploitation.
        
6. **Post-Exploitation**
    
    - Assess the impact and extent of obtained access.
        
7. **Reporting**
    
    - Document findings, evidence, impact, and recommendations.
        

### Easy Way to Remember

> **Plan → Gather → Model → Find → Exploit → Assess → Report**

---

## ISSAF

**Information Systems Security Assessment Framework**

Provides a framework for performing security assessments.

### General Flow

1. Information Gathering
    
2. Network Mapping
    
3. Vulnerability Identification
    
4. Penetration
    
5. Gaining Access & Privilege Escalation
    
6. Further Enumeration
    
7. Compromising Remote Users/Sites
    
8. Maintaining Access
    
9. Covering Tracks

> Some activities, such as maintaining access and covering tracks, should only be performed when explicitly authorized by the engagement rules.

---

# 5. Information Gathering & Footprinting

### Information Gathering

The process of collecting information about a target before attempting deeper security testing.

Information may include:

- Domains
    
- IP addresses
    
- Subdomains
    
- DNS records
    
- Technologies
    
- Open ports
    
- Services
    
- Employees or organizational information
    
- Publicly available documents

### Footprinting

**Footprinting** is the process of creating a profile of the target by gathering information from available sources.

It is commonly part of the **reconnaissance phase**.

---

## 6. OSINT

**OSINT — Open-Source Intelligence**

Gathering information from **publicly available sources**.

Examples:

- Search engines
    
- Public websites
    
- DNS information
    
- Social media
    
- Public documents
    
- Certificate information
    
- Public code repositories

### Goal

Build an understanding of the target **without directly attacking it**.

> OSINT is useful during reconnaissance because information publicly exposed by an organization may reveal potential attack surfaces.

---

# 7. Quick Reference

|Topic|Main Purpose|
|---|---|
|**Network Infrastructure Test**|Test network devices and infrastructure|
|**Application Testing**|Test applications for security weaknesses|
|**Cloud Testing**|Assess security of cloud environments|
|**Bug Bounty**|Authorized vulnerability research with possible rewards|
|**Black Box**|Test with little/no information|
|**Gray Box**|Test with limited information|
|**White Box**|Test with extensive information|
|**MITRE ATT&CK**|Understand/map adversary behavior|
|**OWASP WSTG**|Web application security testing|
|**NIST SP 800-115**|Security testing guidance|
|**OSSTMM**|Repeatable security testing methodology|
|**PTES**|Structured penetration testing process|
|**ISSAF**|Security assessment framework|
|**OSINT**|Gather publicly available information|
|**Footprinting**|Build a profile of the target|

---

# Key Takeaways

- **Footprinting = Build a profile of the target.**
    
- **OSINT = Gather publicly available information.**
    
- **Black Box = Little information.**
    
- **Gray Box = Some information.**
    
- **White Box = Extensive information.**
    
- **MITRE ATT&CK = Adversary tactics and techniques.**
    
- **OWASP WSTG = Web application testing.**
    
- **NIST SP 800-115 = Security testing guidance.**
    
- **OSSTMM = Repeatable security testing.**
    
- **PTES = 7-phase penetration testing methodology.**
    
- **ISSAF = Security assessment framework.**
    
- Always perform testing within the **authorized scope**.

## References

- [MITRE ATT&CK](https://attack.mitre.org/)
    
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
    
- [NIST SP 800-115](https://csrc.nist.gov/pubs/sp/800/115/final)
    
- [OSSTMM](https://www.isecom.org/)
    
- [PTES](http://www.pentest-standard.org/)