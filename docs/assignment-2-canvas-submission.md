# Assignment 2 - Memory Forensics Pratical

**Source:** [`Assignment 2 - Memory Forensics Pratical.docx`](../archive/canvas-submissions/Assignment%202%20-%20Memory%20Forensics%20Pratical.docx)  
**Course:** IA 455 - Incident Response (EMU)  
**Author:** Julio Barros

> Canvas export. For study summaries without duplicating instructor prompts, see [learning-notes.md](learning-notes.md).

Name: Julio Barros EID:E01963387

To Identify the System Profile

python2 vol.py -f ~/Desktop/MemoryDump_Lab1.raw imageinfo

List Running Processes

python2 vol.py -f ~/Desktop/MemoryDump_Lab1.raw --profile=Win7SP1x64 pslist

List Open Network Connections

python2 vol.py -f ~/Desktop/MemoryDump_Lab1.raw --profile=Win7SP1x64 netscan

List Loaded DLLs for Each Process

python2 vol.py -f ~/Desktop/MemoryDump_Lab1.raw --profile=Win7SP1x64 dlllist

Scan for Open Files

python2 vol.py -f ~/Desktop/MemoryDump_Lab1.raw --profile=Win7SP1x64 filescan

List User Sessions

python2 vol.py -f ~/Desktop/MemoryDump_Lab1.raw --profile=Win7SP1x64 sessions
