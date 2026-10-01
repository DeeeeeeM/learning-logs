Perform commands 

nmap -sn 10.6.6.0/24 = Host Discovery Scan
nmap -sV 10.6.6.0/24 = 
nmap -O 10.6.6.0/24 = Operating System
nmap -A 10.6.6.0/24 = 
nmap -sV -p 80 10.6.6.23 = specific port
nmap -sV **-p-** 10.6.6.23 = ALL ports

**NMAP can be saved in a file**
*nmap -sV-o_________ scan_result.txt 10.6.6.23*
oN - text
oX - xml
oA - all file formats

Convert XML to HTML
xsltproc scan_report.xml -o report.html

1. Connect to an FTP server `ftp 10.6.6.23
2. Use a common username for servers `anonymous`
3. use `ls` to check files
4. Then use `get filename.txt` to get files

**Show docker containers**
docker ps

**Navigate to docker container**
docker exec -it (docker container id) /bin/bash 
or sh

Connect to an SMB Client
smbclient -L //10.6.6.23/ -N 
smblient //10.6.6.23/ workfiles

SMB Map
smbmap -H 10.6.6.23


enum4linux 10.6.6.23
enum4linux -a 10.6.6.23
enum4linux -u user -p pass 10.6.6.23

sudo dpkg -i filenam.deb

**Install Nessusd and Start**
sudo systemctl start nessusd.service\n
sudo systemctl status nessusd.service\n

- **nmap --script smb-enum-users.nse** _<host>_
nmap --script smb-enum-shares 10.6.6.23

**All smb commands**
cd /usr/share/nmap/scripts
ls smbx

rizaline
admin123


FLAG 1: QzBuZ3I0dHNfMG5fcjAwdCFfWTB1XzB3bjNkX3RoM19iMHg=\
FLAG 2: Voltez V png
FLAG 3: FLAG('Perseverance_Breaks_Barriers')
FLAG 4: flag4{'Strength_In_Challenge_GrowthInPain'}

lego
summer
220 Xlight FTP Server 3.9
TCP/UDP