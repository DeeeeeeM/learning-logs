# Module 1: Legal Frameworks, Ethics & Safe Lab Setup

## 1. Understanding Security

**Why do we need security?**

- Protect sensitive data and information.
    
- Prevent unauthorized access to systems and networks.
    
- Maintain confidentiality, integrity, and availability (CIA Triad).
    
- Protect organizations and individuals from cyber threats.

**CIA Triad**

- **Confidentiality** — Only authorized users can access information.
    
- **Integrity** — Data remains accurate and unaltered.
    
- **Availability** — Systems and data remain accessible when needed.

## 2. Ethical Hacking

**Ethical Hacker:** A security professional who simulates cyberattacks with proper authorization to identify vulnerabilities and improve an organization's security.

**Main objectives:**

- Identify security weaknesses.
    
- Test system defenses.
    
- Determine the impact of vulnerabilities.
    
- Recommend security improvements.

**Ethical vs. Malicious Hacking**

- **Ethical:** Authorized, within scope, intended to improve security.
    
- **Malicious:** Unauthorized, intended for personal gain, disruption, theft, or other harmful purposes.

## 3. Penetration Testing

**Penetration Testing (Pentesting):** An authorized security assessment that simulates real-world attacks to identify and validate vulnerabilities.

**Goal:**

- Find exploitable vulnerabilities.
    
- Assess their potential impact.
    
- Evaluate security defenses.
    
- Recommend remediation.

**Pentesting Stages:**

1. **Planning & Reconnaissance** — Define scope, obtain authorization, and gather information.
    
2. **Scanning & Enumeration** — Discover hosts, open ports, services, and potential vulnerabilities.
    
3. **Exploitation** — Validate whether vulnerabilities can be exploited.
    
4. **Post-Exploitation** — Assess the extent and impact of access obtained.
    
5. **Analysis & Reporting** — Document findings, evidence, risks, and recommendations.
    
6. **Remediation & Retesting** — Verify that security weaknesses have been fixed.

> Note: Maintaining persistent access is not required in every penetration test.

## 4. Common Threat Actors

|Threat Actor|Description|Common Motivation|
|---|---|---|
|**Organized Cybercrime**|Coordinated criminal groups conducting cyberattacks.|Financial gain, extortion, data theft|
|**Hacktivists**|Individuals or groups using cyberattacks to promote causes or beliefs.|Political, social, or ideological goals|
|**State-Sponsored Attackers**|Attackers supported or directed by governments.|Espionage, intelligence, strategic advantage|
|**Insider Threats**|People with legitimate access who create security risks.|Malicious intent, negligence, or compromised accounts|

**Types of Insider Threats:**

- **Malicious:** Intentionally abuses authorized access.
    
- **Negligent:** Accidentally creates security risks.
    
- **Compromised:** Has an account or device taken over by an attacker.

## 5. Legal Frameworks & Ethics

**Key Principles:**

- **Authorization** — Obtain permission before testing.
    
- **Scope** — Test only approved systems and activities.
    
- **Confidentiality** — Protect sensitive information.
    
- **Data Protection** — Handle personal and confidential data responsibly.
    
- **Responsible Disclosure** — Report vulnerabilities through appropriate channels.

**Relevant Philippine Laws:**

- **RA 10175 — Cybercrime Prevention Act of 2012:** Addresses cybercrime offenses.
    
- **RA 10173 — Data Privacy Act of 2012:** Protects personal information and regulates its processing.

## 6. Safe Lab Setup

**Purpose:** Practice cybersecurity techniques in a controlled environment without affecting real-world systems.

**Common Lab Tools:**

- **VirtualBox / VMware** — Run virtual machines.
    
- **Kali Linux** — Security testing operating system.
    
- **Metasploitable** — Intentionally vulnerable practice machine.
    
- **Nmap** — Network discovery and scanning.
    
- **Nessus** — Vulnerability assessment.
    
- **Docker** — Run isolated applications and services.

**Virtual Network Modes:**

|Mode|Purpose|
|---|---|
|**NAT**|Provides internet access through the host.|
|**Bridged**|Connects the VM to the physical network.|
|**Host-only**|Creates a private network between the host and VMs.|
|**Internal Network**|Connects VMs through an isolated virtual network.|

**Lab Safety:**

- Isolate vulnerable machines from public networks.
    
- Use test accounts and non-sensitive data.
    
- Take VM snapshots before major changes.
    
- Test only authorized targets.
    
- Document configurations and findings.

## Key Takeaways

- **Cybersecurity:** Protects systems and information through the CIA Triad.
    
- **Ethical Hacking:** Authorized security testing to identify weaknesses.
    
- **Penetration Testing:** Simulates attacks to validate vulnerabilities and assess their impact.
    
- **Threat Actors:** Have different motivations, capabilities, and attack methods.
    
- **Legal & Ethical Practice:** Requires authorization, defined scope, and responsible handling of data.
    
- **Safe Lab:** Provides a controlled environment for hands-on cybersecurity learning.

## References

- [NIST SP 800-115 — Security Testing Guide](https://csrc.nist.gov/pubs/sp/800/115/final)
    
- [OWASP Web Security Testing Guide](https://owasp.org/www-project-web-security-testing-guide/)
    
- [RA 10175 — Cybercrime Prevention Act](https://lawphil.net/statutes/repacts/ra2012/ra_10175_2012.html)
    
- [RA 10173 — Data Privacy Act](https://lawphil.net/statutes/repacts/ra2012/ra_10173_2012.html)


# Module 2: Information Gathering and Footprinting

## 1. Penetration Testing Assessment

A penetration test is a **point-in-time assessment** of an organization's security.

It can:

- Identify vulnerabilities
    
- Demonstrate potential impact
    
- Help prioritize remediation
    
- Provide evidence of security weaknesses
    

**Important:** A penetration test **does not guarantee overall security**. Vulnerabilities can appear after the test, so remediation and retesting are important.

---

## 2. Pre-Engagement

Before testing begins, the tester and customer must agree on:

- **Scope** — What will and will not be tested
    
- **Targets** — Systems, networks, applications, APIs, etc.
    
- **Timeline** — When testing will happen
    
- **Testing methods** — What techniques are allowed
    
- **Restrictions** — What cannot be tested
    
- **Communication** — Who to contact and how
    
- **Reporting** — Who receives the results
    
- **Legal authorization** — Written permission to test

### Scope

The scope should clearly identify:

- IP ranges
    
- Applications
    
- Networks
    
- Wireless networks/SSIDs
    
- Domains and subdomains
    
- Cloud/third-party systems
    
- In-scope and out-of-scope assets

### Allow List vs. Deny List

**Allow list**  
→ Assets that **can be tested**

**Deny list**  
→ Assets that **must not be tested**

Always follow the agreed scope.

---

## 3. Rules of Engagement (RoE)

The **Rules of Engagement** define the conditions under which the penetration test will be performed.

May include:

- Testing timeline
    
- Testing location
    
- Testing hours
    
- Communication methods
    
- Source IP addresses
    
- Security controls that may detect/block testing
    
- Allowed/disallowed attacks
    
- Emergency contacts


Example:

> SQL injection may be allowed in development but prohibited in production.

The tester and appropriate stakeholders must agree on these rules before testing.

---

## 4. Governance, Risk, and Compliance (GRC)

## Governance

How an organization **directs and manages security**.

Includes:

- Policies
    
- Responsibilities
    
- Decision-making
    
- Security requirements
    

### Risk

The possibility that a threat will cause harm to an organization.

Penetration testing helps identify and understand security risks so they can be prioritized and reduced.

### Compliance

Following applicable:

- Laws
    
- Regulations
    
- Industry requirements
    
- Organizational policies


Examples from the module include:

- **PCI DSS** — Payment card industry
    
- **GLBA** — Financial sector
    
- **HIPAA** — Healthcare
    
- **NY DFS Cybersecurity Regulation**


Some regulations may require periodic penetration testing or vulnerability assessments.

### Key idea

> **GRC ensures that security testing supports the organization's business, legal, and regulatory requirements — not just technical security.**

---

## 5. Legal & Contract Concepts

### SLA — Service-Level Agreement

Defines expected service levels such as:

- Quality
    
- Timeline
    
- Cost
    
- Performance


### SOW — Statement of Work

Defines the actual work to be performed.

Usually includes:

- Scope
    
- Timeline
    
- Location
    
- Requirements
    
- Payment schedule
    
- Other project conditions


### MSA — Master Service Agreement

A reusable agreement that establishes general terms for recurring work.

### NDA — Non-Disclosure Agreement

Protects confidential information.

Types:

- **Unilateral** — One party shares information
    
- **Bilateral** — Both parties share information
    
- **Multilateral** — Three or more parties are involved


### Contract

Should clearly define:

- Services
    
- Terms
    
- Payment
    
- Responsibilities
    
- Authorization


Written authorization from the proper signing authority is essential. Third parties may also need to provide authorization.

---

## 6. Local Restrictions

A penetration test may have technical or organizational restrictions.

Examples:

- Certain tools cannot be used
    
- Production systems cannot be attacked
    
- Some systems are out of scope
    
- Certain exploits are prohibited
    
- Testing may be limited by system performance
    
- Privacy laws may restrict handling of data


These restrictions must be communicated with the appropriate stakeholders.

---

## 7. Scope Creep

**Scope creep** = Uncontrolled expansion of the penetration testing project.

Causes:

- Poor change management
    
- Poor communication
    
- Incomplete identification of requirements
    
- Client requesting additional work


### Solution

If additional work is outside the original agreement:

> **Document it and obtain a new/agreed SOW.**

Do not simply perform additional testing outside the original scope.

---

## 8. Organizational & Customer Considerations

A penetration tester must understand the **organization and customer**, not just the technology.

Important questions:

- What does the customer want to achieve?
    
- Why is the penetration test being performed?
    
- Who will make decisions based on the findings?
    
- Who will receive the report?
    
- Who needs access to sensitive results?
    
- Who are the important stakeholders?
    
- How should communication happen?
    
- Who should be contacted during an emergency?


Possible report recipients:

- ISM
    
- CISO
    
- CIO
    
- CTO
    
- Technical teams


The report should be appropriate for its intended audience.

---

## 9. Customer Perspective

Customers may ask:

- Why do we need penetration testing?
    
- How much will it cost?
    
- What is the ROI?
    
- Can we perform it ourselves?
    
- How does testing improve security?


The tester should be able to explain:

- What is being tested
    
- Why it matters
    
- What risks were identified
    
- Potential impact
    
- Recommended remediation
    
- How testing provides value


### Important

Penetration testing should **not be performed only to satisfy compliance**.

The goal should be to improve the organization's security posture.

---

## 10. Ethical Hacking Mindset

A penetration tester must demonstrate **professionalism and integrity**.

### Important principles

**Background checks**

- Clients may verify the tester's identity, credentials, and skills.


**Follow the scope**

- Never test systems simply because they are accessible.
    
- Follow the allow/deny lists.
    

**Protect sensitive information**

- Keep findings, credentials, PII, and other sensitive data confidential.
    

**Report real criminal activity**

- If evidence shows that a real attacker has compromised the organization, report it immediately.
    

**Respect tool restrictions**

- Do not use prohibited tools.
    

**Limit invasiveness**

- Testing should match the agreed scope and risk.
    

**Maintain professionalism**

- Act as a trusted security professional, not as an uncontrolled attacker.


---

## 11. Unknown vs. Known Environment

### Unknown Environment

**Black Box**

Tester has very limited information.

Goal:

> Simulate an external attacker.

### Known Environment

**White Box**

Tester receives significant information such as:

- Network diagrams
    
- IP addresses
    
- Configurations
    
- Credentials
    
- Source code


Goal:

> Identify as many security weaknesses as possible.

### Partially Known Environment

**Gray Box**

Tester receives some information but not everything.

---

## 12. Information Gathering & Footprinting

### Information Gathering

Collect information about the target before deeper testing.

Examples:

- Domains
    
- IP addresses
    
- DNS
    
- Technologies
    
- Services
    
- Applications
    
- Organizational information


### Footprinting

Building a **profile of the target** using available information.

### OSINT

**Open-Source Intelligence**

Information collected from publicly available sources.

Examples:

- Search engines
    
- Websites
    
- Social media
    
- Public documents
    
- DNS
    
- Public repositories


---

## 13. Penetration Testing Methodologies

|Methodology|Main Focus|
|---|---|
|**MITRE ATT&CK**|Adversary tactics and techniques|
|**OWASP WSTG**|Web application testing|
|**NIST SP 800-115**|Security testing guidance|
|**OSSTMM**|Repeatable security testing|
|**PTES**|Penetration testing process|
|**ISSAF**|Security assessment|

### PTES — 7 Phases

> **Pre-engagement → Intelligence Gathering → Threat Modeling → Vulnerability Analysis → Exploitation → Post-exploitation → Reporting**

---

## Quick Exam Review

### Assessment

**Pen Test = Point-in-time security assessment**

### GRC

**Governance → How security is managed**  
**Risk → What could go wrong and its impact**  
**Compliance → What requirements must be followed**

### Pre-engagement

**Scope → Rules → Authorization → Communication → Testing → Reporting**

### Legal documents

**SLA → Service expectations**  
**SOW → Specific work**  
**MSA → General/reusable agreement**  
**NDA → Confidentiality**  
**Contract → Legal agreement and authorization**

### Scope

**Allow list → Test it**  
**Deny list → Don't test it**

### Mindset

**Authorized + Professional + Ethical + Within Scope**

### Testing perspective

**Black Box → Little information**  
**Gray Box → Some information**  
**White Box → Extensive information**

### Main lesson

> **A good penetration tester is not simply someone who can find vulnerabilities. They must understand the customer's goals, business risks, legal requirements, scope, organizational constraints, and ethical responsibilities.**

