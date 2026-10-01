
## Module 1: Legal Frameworks, Ethics & Safe Lab Setup 
- Understanding Ethical Hacking and Penetration Testing
- Exploring Penetration Testing Methodologies
- Building Your Own Lab

Why we need Security?
- Protect authentication and access control for sensitive assets, data, informations that can be damaging to a company or an individual.

![[Pasted image 20260919124017.png]]

**Ethical hacker:** a person who acts as an attacker and evaluates the security posture of a network's or system's infrastructure to identify and possibly exploit any security weaknesses found and then determine if a compromise is possible. Basically a legal way to breach the system's infrastructure of an organization to look for vulnerabilities in products, apps, or web services.

### Pentesting Stages
Planning & Recon > Scanning > Gaining Access or Exploitation > Maintaning Access > Analysis and Reporting

Penetration Testing
Goal:  Actively exploit vulnerabilities to determine their real-world impact and assess the effectiveness of an organization's security defenses.

Scope: Attempting to gain unauthorized access to systems, extract sensitive data, or disrupt services to evaluate the system's resilience against cyberattacks.

Methodology: Penetration testers follow a systematic approach to assess the security of a specific system, network, or application. They actively attempt to exploit identified
vulnerabilities and provide detailed information on the impact of successful attacks.

Reporting: Penetration testers deliver reports that not only highlight vulnerabilities but also describe how an attacker could exploit them. These reports may include recommendations for remediation and improving security measures.

****Organized Crime****

Organized crime is an illegal group not much different in a terrorist group that is funded to attack a certain company, individual, group etc. and they are motivated by either revenge or money

****Hacktivists****

They hack certain governments services or individual to make a point or to further their beliefs, using cybercrime as their method of attack. 

****State-Sponsored Attackers****

A government sponsored Hacker / Attacker that are tasked to steal any intel or information to other governments, individuals that are a threat to a country, or important information from a certain person.

****Insider Threats****
An insider threat is a threat that comes from inside an organization. 


## Module 2: Information Gathering and Footprinting


 **Common environmental considerations for the types of penetration tests:**

****Network Infrastructure Tests****

It is focused on evaluating the security posture of the actual network infrastructure and how it is able to help defend against attacks. This often includes the switches, routers, firewalls, and supporting resources, such as authentication, authorization, and accounting (AAA) servers and IPSs.

****Application-Based Tests****

Focuses on testing for security weaknesses in enterprise applications. Misconfigurations, input validation issues, injection issues, and logic flaws. Open Web Application Security Project (OWASP) is a great resource for this test.

****Penetration Testing in the Cloud****

Cloud security is the responsibility of both the client and the cloud provider. You want to ensure that the CSP has the same layers of security (logical, physical, and administrative) in place that you would have for services you control such as (software as a service [SaaS], platform as a service [PaaS], or infrastructure as a service [IaaS]).


Other info:
**Bug bounty** programs enable security researchers and penetration testers to get recognition (and often monetary compensation) for finding vulnerabilities in websites, applications, or any other types of systems.

**Perspective from which the testing is performed:**

****Unknown-Environment Test****
The tester is typically provided only a very limited amount of information to have the tester start 
out with the perspective that an external attacker might have.

****Known-Environment Test****
The tester starts out with a significant amount of information about the organization and its infrastructure to identify as many security holes as possible.

****Partially Known Environment Test****
Hybrid approach between unknown- and known. The testers may be provided credentials but not full documentation of the network infrastructure to allow the testers to still provide results of their testing from the perspective of an external attacker’s point of view.

**Penetration testing methodologies and other standards:**

MITRE ATT&CK https://attack.mitre.org/
A collection of different matrices of tactics, techniques, and subtechniques. These includes 

- Enterprise ATT&CK Matrix
- Network
- Cloud
- ICS

Mobile. Tactics and techniques that adversaries use while preparing for an attack, including:

- Gathering of information (open-source intelligence [OSINT].
- Technical and people weakness identification, and more.
- Different exploitation and post-exploitation techniques. 

Both offensive security professionals (penetration testers, red teamers, bug hunters, and so on) and incident responders and threat hunting teams use it.

OWASP Web Security Testing Guide (WSTG) [_https://owasp.org/www-project-web-security-testing-guide/_](https://owasp.org/www-project-web-security-testing-guide/).
covers the high-level phases of web application security providing attack vectors for testing cross-site scripting (XSS), XML external entity (XXE) attacks, cross-site request forgery (CSRF), and SQL injection attacks; as well as how to prevent and mitigate these attacks.

NIST SP 800-115 [_https://csrc.nist.gov/publications/detail/sp/800-115/final_](https://csrc.nist.gov/publications/detail/sp/800-115/final).
provides organizations with guidelines on planning and conducting information security testing.

Open Source Security Testing Methodology Manual (OSSTMM) [_https://www.isecom.org_](https://www.isecom.org/)
a document that lays out repeatable and consistent security testing:

- Operational Security Metrics
- Trust Analysis
- Work Flow
- Human Security Testing
- Physical Security Testing
- Wireless Security Testing
- Telecommunications Security Testing
- Data Networks Security Testing
- Compliance Regulations
- Reporting with the Security Test Audit Report (STAR)

Penetration Testing Execution Standard (PTES) [_http://www.pentest-standard.org_](http://www.pentest-standard.org/)
Provides information about types of attacks and methods, and it provides information on the latest tools available to accomplish the testing methods outlined.

1. Pre-engagement interactions
2. Intelligence gathering
3. Threat modeling
4. Vulnerability analysis
5. Exploitation
6. Post-exploitation
7. Reporting

Information Systems Security Assessment Framework (ISSAF)

- Information gathering
- Network mapping
- Vulnerability identification
- Penetration
- Gaining access and privilege escalation
- Enumerating further
- Compromising remote users/sites
- Maintaining access
- Covering the tracks

Kali Linux
user: kali
pass: kali


Module 3: Scanning, Enumeration & Vulnerability Identification


Module 4: Basic Exploitation in a Controlled Environment
Module 5: Capstone Project & Responsible Disclosure