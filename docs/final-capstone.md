# Final capstone — Malware, logs, and host artifacts

**Author:** Julio Barros

Summary of my IA455 final practical: static/dynamic malware indicators, PowerShell triage, web access-log analysis, PCAP correlation, and live-connection style host data.

## Malware static indicators (sample)

| Indicator | Value / note |
|-----------|----------------|
| SHA-256 | `0c98769e42b364711c478226ef199bfbba90db80175eb1b8cd565aa694c09852` |
| Imported DLLs (examples) | `user32.dll`, `KERNEL32.dll`, `ADVAPI32.dll`, `WININET.dll` |
| API hints | `CreateMutexA`, `OpenMutexA` |
| Network string | `http://www.malwareanalysisbook.com` |
| Mutex / naming | No fixed user-visible name — may be generated at runtime |

## Host triage (PowerShell examples)

Processes running from suspicious locations:

```powershell
Get-Process | Where-Object {$_.Path -like "*temp*"} | Select-Object Name, Path
```

Persistence cleanup example (lab context):

```powershell
Get-ItemProperty -Path "HKLM:\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" | Remove-Item -Force
```

Service baseline export:

```powershell
Get-Service | Export-Csv -Path "current_services.csv"
```

Additional sample hash from the exercise: `f1c87ea43ae0de72fde56bbe41a28dd7a227d295bf00a6f07cfaeb2e297d59cc`.

## Access log analysis (`q4-access.log`)

- Most contacted external destination in the dataset: **`http://www1-google-analytics.com/collect`** (9,075 requests) — useful for baselining “noisy” egress before hunting C2.
- Multiple internal hosts showed outbound activity consistent with compromise during the lab window.

## PCAP correlation (`q4.pcap`)

| Host | Observation |
|------|-------------|
| **172.16.42.108** | Communicated with suspected C2 addresses **13.226.238.81** and **23.62.236.162**; first C2 connection to 13.226.238.81 at ~**2.08 s** in the capture timeline |
| **172.16.42.107** | External comms in access log; first external timestamp **1584606356.584** |
| **172.16.42.105** | First external connection logged at **1584606107.926** |
| **172.16.42.103** | First external connection at **1584606137.585** |
| **172.16.42.109** | First external connection at **1584606205.082** |

Combining **HTTP logs** and **PCAP** showed **172.16.42.108** as a primary C2 talker while several peers exhibited outbound hits — consistent with lateral or staged compromise in the scenario.

## Network / process snapshot (lab table)

| PID | Local | Remote | State |
|-----|-------|--------|-------|
| 2532 | 192.168.1.100:12345 | 167.172.201.123:443 | ESTABLISHED |

| PID | PPID | Image | Threads | Handles |
|-----|------|-------|---------|---------|
| 2532 | 4452 | `cmd.exe` | 1 | 10 |

## Original submission

`archive/canvas-submissions/FINAL IA455.docx`
