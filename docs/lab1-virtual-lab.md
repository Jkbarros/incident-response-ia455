# Lab 1 — Virtual incident response lab

**Author:** Julio Barros

Built a small IR practice environment in VMware for IA455 hands-on work.

## Components

### pfSense firewall

Used pfSense with a slightly different VM sizing than the default class template (more RAM and CPU) after issues in earlier courses. Firewall rules and segmentation supported later log and PCAP exercises.

### Security Onion

Followed the instructor’s recommended Security Onion image with extra CPU and RAM. During ISO install, setup failed once due to **insufficient disk**; adding **~60 GB** of storage on a dedicated school SSD resolved it.

### Kali Linux

Reused a long-running Kali VM (upgraded CPU/RAM after a hardware refresh). Standard Kali ISO install from [kali.org](https://www.kali.org/).

### Windows 10 desktop

Created a Windows 10 ISO with Microsoft’s media creation tool (licensed key), then allocated **extra CPU and RAM** to reduce crashes common in nested lab VMs.

## Outcome

A stable four-VM stack: perimeter (pfSense), monitoring (Security Onion), attacker/analysis (Kali), and victim/end-user (Windows) — enough to run course labs without constantly rebuilding images.

## Original submission

See `archive/canvas-submissions/Lab1.docx` (includes VM screenshots from Canvas).
