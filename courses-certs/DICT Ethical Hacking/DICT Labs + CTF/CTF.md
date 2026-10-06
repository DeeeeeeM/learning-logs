
What is the password of socuser


What is flag1. Type only the content for the flag. AS IS. 


What is root flag. Type only the content for the flag. AS IS. 


What is flag2. Type only the content for the flag. AS IS. 


What is the password of vboxuser


How many tables use by the web app


What is flag1. Type only the content for the flag. AS IS. 


What is the root password


What is the jrizal password



**

Bonus Flag

flag{failure_is_the_first_step_to_success}

**

**

What is flag1. Type only the content for the flag. AS IS.

ZmxhZ3tldmVyeV9wcm9ibGVtX2hhc19hX3NvbHV0aW9ufQ==

flag{every_problem_has_a_solution}

**


PORT     STATE SERVICE  VERSION
21/tcp   open  ftp      ProFTPD
80/tcp   open  http     Apache httpd 2.4.58 ((Unix) OpenSSL/1.1.1w PHP/8.0.30 mod_perl/2.0.12 Perl/v5.34.1)
443/tcp  open  ssl/http Apache httpd 2.4.58 ((Unix) OpenSSL/1.1.1w PHP/8.0.30 mod_perl/2.0.12 Perl/v5.34.1)
3306/tcp open  mysql    MySQL 5.5.5-10.4.32-MariaDB


Starting Nmap 7.94 ( https://nmap.org ) at 2026-10-03 08:28 UTC
Nmap scan report for 192.168.56.110
Host is up (0.0071s latency).
Not shown: 996 closed tcp ports (conn-refused)
PORT     STATE SERVICE  VERSION
21/tcp   open  ftp      ProFTPD

80/tcp   open  http     Apache httpd 2.4.58 ((Unix) OpenSSL/1.1.1w PHP/8.0.30 mod_perl/2.0.12 Perl/v5.34.1)
|_http-title: Student Information System
|_http-server-header: Apache/2.4.58 (Unix) OpenSSL/1.1.1w PHP/8.0.30 mod_perl/2.0.12 Perl/v5.34.1
443/tcp  open  ssl/http Apache httpd 2.4.58 ((Unix) OpenSSL/1.1.1w PHP/8.0.30 mod_perl/2.0.12 Perl/v5.34.1)
| tls-alpn: 
|_  http/1.1
|_http-server-header: Apache/2.4.58 (Unix) OpenSSL/1.1.1w PHP/8.0.30 mod_perl/2.0.12 Perl/v5.34.1
|_http-title: Student Information System
| ssl-cert: Subject: commonName=localhost/organizationName=Apache Friends/stateOrProvinceName=Berlin/countryName=DE
| Not valid before: 2004-10-01T09:10:30
|_Not valid after:  2010-09-30T09:10:30
|_ssl-date: TLS randomness does not represent time
3306/tcp open  mysql    MySQL 5.5.5-10.4.32-MariaDB
| mysql-info: 
|   Protocol: 10
|   Version: 5.5.5-10.4.32-MariaDB
|   Thread ID: 39
|   Capabilities flags: 63486
|   Some Capabilities: SupportsCompression, Support41Auth, SupportsLoadDataLocal, ODBCClient, ConnectWithDatabase, Speaks41ProtocolOld, SupportsTransactions, FoundRows, InteractiveClient, LongColumnFlag, IgnoreSpaceBeforeParenthesis, IgnoreSigpipes, DontAllowDatabaseTableColumn, Speaks41ProtocolNew, SupportsMultipleResults, SupportsMultipleStatments, SupportsAuthPlugins
|   Status: Autocommit
|   Salt: Mu)hSFEdJ&}ea6*opd%,
|_  Auth Plugin Name: mysql_native_password

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 27.57 seconds
