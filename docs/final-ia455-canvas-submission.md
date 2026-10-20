# FINAL IA455

**Source:** [`FINAL IA455.docx`](../archive/canvas-submissions/FINAL%20IA455.docx)  
**Course:** IA 455 - Incident Response (EMU)  
**Author:** Julio Barros

> Canvas export. For study summaries without duplicating instructor prompts, see [learning-notes.md](learning-notes.md).

0c98769e42b364711c478226ef199bfbba90db80175eb1b8cd565aa694c09852

user32.dll,KERNEL32.dll, ADVAPI32.dll, WININET.dll

CreateMutexA, OpenMutexA

http://www.malwareanalysisbook.com

No explicit user, that means can be dynamically generated.

- Get-Process | Where-Object {$_.Path -like "*temp*"} | Select-Object Name, Path

- f1c87ea43ae0de72fde56bbe41a28dd7a227d295bf00a6f07cfaeb2e297d59cc
- Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" | Remove-Item -Force.
- Get-Service | Export-Csv -Path "current_services.csv"

- Based on the analysis of the access log (q4-access.log), the most contacted external destination is http://www1-google-analytics.com/collect, which received a total of 9075 requests.
Using the access log and the packet capture file (q4.pcap), several compromised hosts within the network were identified. The first host, 172.16.42.108, established communication with suspected C2 servers (13.226.238.81 and 23.62.236.162) based on the packet capture data. Its first observed connection to the C2 server 13.226.238.81 occurred at approximately 2.077791 seconds in the packet capture timeline.

Another compromised host, 172.16.42.107, communicated with external destinations as shown in the access log. Its first recorded external communication occurred at timestamp 1584606356.584, as observed in the access log file. Similarly, 172.16.42.105 was identified as compromised, with its first connection to external IPs logged at 1584606107.926. Additionally, the access logs reveal two more compromised hosts: 172.16.42.103 and 172.16.42.109, with their first connections logged at 1584606137.585 and 1584606205.082, respectively.

The combination of access log data and packet capture analysis highlights 172.16.42.108 as a key compromised host actively communicating with the C2 server. The presence of multiple internal hosts connecting to external IPs suggests a wider compromise within the network, necessitating further investigation to mitigate the threat.

- PID               Local Address               Remote Address                      State
- 2532   192.168.1.100:12345    167.172.201.123:443     ESTABLISHED
- PID       PPID    ImageFileName   Threads       Handles
- 2532    4452    cmd.exe                             1                 10
