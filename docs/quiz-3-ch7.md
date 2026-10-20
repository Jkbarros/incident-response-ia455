# Quiz 3 - Ch7

**Source:** [`Quiz 3 - Ch7.docx`](../archive/canvas-submissions/Quiz%203%20-%20Ch7.docx)  
**Course:** IA 455 - Incident Response (EMU)  
**Author:** Julio Barros

> Canvas export. For study summaries without duplicating instructor prompts, see [learning-notes.md](learning-notes.md).

1. a) What investigative questions is a live data collection likely to help answer?

What processes are currently running on the system? Live data collection can identify malicious software that might be running in memory, which could otherwise disappear if the system is turned off or rebooted.

What network connections are active? Investigators can use live data to identify ongoing communications between the system and external servers, which may reveal command-and-control (C2) channels used by attackers.

What users are logged into the system? This information can help ascertain whether unauthorized users are accessing the system at the time of investigation.

What files are currently open or in use? Live data collection can show which files are being accessed, helping to identify potential data exfiltration or malicious file activity.

What changes are occurring in real-time? By analyzing live data, investigators can monitor system activities like file modifications, new process creation, or registry changes, providing insights into potential ongoing attacks.

1.(b) In what situations would collecting an image of memory be most useful to the investigation?

Detecting Malware Infections: Advanced malware often resides only in memory to avoid detection by traditional antivirus software. Capturing a memory image can reveal hidden or encrypted malware that is not stored on disk, allowing investigators to analyze it for indicators of compromise.

Investigating Insider Threats: When dealing with potential insider threats, memory images can reveal the usage of sensitive applications, data manipulation activities, or the execution of scripts and commands that do not leave traces on disk.

Recovering Encryption Keys and Passwords: Memory captures can sometimes reveal encryption keys, passwords, or other sensitive information that could be used to access encrypted files or systems. This is particularly useful in cases where the suspect refuses to provide access credentials.

Analyzing Rootkits: Rootkits often operate at the kernel level and manipulate system processes, making them difficult to detect using standard disk-based forensics. Memory analysis allows investigators to detect and understand the behavior of rootkits.

Investigating Network Intrusions: During a network intrusion, memory forensics can uncover malicious network activity, such as the existence of backdoors, unauthorized remote access tools (RATs), or evidence of data exfiltration.

2.) If you have connected evidence hard drives to a system for imaging, do you need to use a write blocker if you are going to boot to a Linux-based forensic CD? Explain why or why not.

A write blocker is a hardware or software tool that ensures data on a storage device cannot be altered during the imaging process. It is designed to prevent any unintentional writings that could compromise the integrity of the evidence. Linux-based forensic CDs, such as the ones running tools like dd or dcfldd, often include built-in mechanisms to mount drives in a read-only state. However, there are still risks involved:

Potential Mistakes: During the mounting process, it is possible to make mistakes in command execution that could inadvertently cause the drive to be mounted in a read-write state. The use of a write blocker removes this risk by enforcing a physical barrier against writing.

System Processes: In some cases, the operating system might interact with the connected drives even if they are not explicitly mounted. Some Linux distributions may still attempt to write logs or other system files to connected storage devices. A write blocker eliminates this possibility.

Standard Forensic Procedure: Using a write blocker is a widely accepted standard in forensic procedures to ensure that evidence integrity is maintained. Even if the forensic CD is designed to avoid writes, using a write blocker provides an additional layer of security and credibility to the imaging process.
