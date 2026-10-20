# Learning notes — quizzes and written IR concepts

**Author:** Julio Barros

Condensed study notes from IA455 quizzes. **Instructor question text is not reproduced here**; see `archive/canvas-submissions/` for original DOCX exports.

## Attack lifecycle

- Seven phases: reconnaissance, weaponization, delivery, exploitation, installation, command and control, actions on objectives.
- Not every incident hits every phase — phishing may compress early stages; APT-style activity typically spans the full chain.

## Live response vs forensic disk image

| Approach | Strengths | Trade-offs |
|----------|-----------|------------|
| **Live response** | Captures volatile data (processes, connections, RAM-resident malware); faster; less downtime | Risk of altering evidence; easy to miss non-volatile artifacts |
| **Disk image** | Bit-for-bit storage including deleted/unallocated data; stable for court-style preservation | No RAM; imaging time and downtime |

## IR checklists (NIST-style framing)

Five practical lenses used in coursework: **identification**, **containment**, **eradication**, **recovery**, and **lessons learned**.

Examples of high-value data points:

- **Identification:** incident type and time of detection — drives severity and staffing.
- **Containment:** which systems/services are affected and how wide the blast radius is.
- **Eradication / recovery:** root cause removal and verified restore paths.
- **Lessons learned:** timeline reconstruction and control gaps.

## When live collection and memory images help

Live questions memory often answers:

- What is executing right now?
- Which sockets are open to external IPs?
- Who is logged on?
- Which files are open or changing in real time?

Memory imaging is especially useful for fileless malware, insider misuse, encryption keys in RAM, rootkits, and active C2 during intrusions.

## Evidence handling reminder

When USB or other media is attached for collection, document **chain of custody**, use **write blockers** where appropriate, and prefer **cryptographic hashes** before and after imaging.

## Network monitoring design (quiz themes)

When planning monitoring with IT stakeholders, clarify:

- Critical assets and services to watch
- Protocols and applications that matter on each segment
- Existing tools (SIEM, IDS, firewall logging) to integrate with
- Retention and compliance constraints on logs

Egress visibility ideas from class discussion: span/tap or mirror on key uplinks, firewall logging on outbound rules, IDS on north-south paths, segmentation, and periodic control testing.

## TLS and perfect forward secrecy (conceptual)

**Perfect forward secrecy (PFS)** uses ephemeral key agreement (e.g. ECDHE) so compromise of a long-term key does not decrypt past sessions. That protects users but limits **passive decryption** of captured TLS after the fact.

Course context also covered **authorized** inspection models (e.g. corporate proxies with installed trust roots) versus attacking third-party traffic — only the former is appropriate in enterprise defense.

## Original submissions

- `Quiz 1.docx`, `QUIZ 2.docx`, `Quiz 3 - Ch7.docx`, `IA455-Quiz-4.docx`
- Exam PDFs: `ia455-midterm final.pdf`, `ia455-final.pdf` (archived, not summarized online)
