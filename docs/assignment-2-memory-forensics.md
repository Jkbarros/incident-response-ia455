# Assignment 2 — Memory forensics (Volatility 2)

**Author:** Julio Barros  
**Dump:** `MemoryDump_Lab1.raw` (Win7 SP1 x64 profile)  
**Tooling:** Volatility 2 (`vol.py`)

Practical walkthrough of identifying a memory image profile and answering investigation questions with standard plugins.

## 1. Identify the system profile

```bash
python2 vol.py -f ~/Desktop/MemoryDump_Lab1.raw imageinfo
```

`imageinfo` suggests the correct `--profile=` value (here **Win7SP1x64**) before running other plugins.

## 2. Running processes

```bash
python2 vol.py -f ~/Desktop/MemoryDump_Lab1.raw --profile=Win7SP1x64 pslist
```

`pslist` walks the EPROCESS list — useful for spotting unexpected parent/child relationships and processes without on-disk images.

## 3. Network connections

```bash
python2 vol.py -f ~/Desktop/MemoryDump_Lab1.raw --profile=Win7SP1x64 netscan
```

`netscan` surfaces TCP/UDP endpoints and states from memory — helpful when disk artifacts are missing or adversaries use fileless techniques.

## 4. Loaded DLLs per process

```bash
python2 vol.py -f ~/Desktop/MemoryDump_Lab1.raw --profile=Win7SP1x64 dlllist
```

`dlllist` shows modules loaded into each process context for DLL injection and sideloading review.

## 5. Open files

```bash
python2 vol.py -f ~/Desktop/MemoryDump_Lab1.raw --profile=Win7SP1x64 filescan
```

`filescan` locates `FILE_OBJECT` structures still present in RAM.

## 6. User sessions

```bash
python2 vol.py -f ~/Desktop/MemoryDump_Lab1.raw --profile=Win7SP1x64 sessions
```

`sessions` lists logon sessions — supports correlating activity to accounts during live-compromise scenarios.

## Takeaways

- **Profile first** — wrong profile produces misleading plugin output.
- Memory complements disk: connections, injected code, and ephemeral handles often exist only in RAM.
- Plugin choice maps directly to investigative questions (who is connected, what is running, what modules are loaded).

## Original submission

`archive/canvas-submissions/Assignment 2 - Memory Forensics Pratical.docx`
