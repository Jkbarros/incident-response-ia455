# Quiz 1

**Source:** [`Quiz 1.docx`](../archive/canvas-submissions/Quiz%201.docx)  
**Course:** IA 455 - Incident Response (EMU)  
**Author:** Julio Barros

> Canvas export. For study summaries without duplicating instructor prompts, see [learning-notes.md](learning-notes.md).

### Name: Julio Barros

### Quiz 1:

1.(a) How many phases are in the attack lifecycle?

There are 7 phases of attack lifecycle. Reconnaissance, Weaponization, Delivery, Exploitation, Installation, Command and Control, Actions on Objective. That way ends the lifecycle of attack.

1.(b) Do all attacks encompass all phases of the attack lifecycle?

No, not all attacks encompass all phases of the attack lifecycle. Some attacks might skip certain phases or merge multiple phases depending on the nature of the attack and the attacker's goals. There are two different attacks Simple Attacks and Advanced attacks.

- Simple attacks: Such as phishing, may primarily focus on the delivery and exploitation phases without needing an extensive reconnaissance or weaponization phase.
- Advanced attacks: More sophisticated attacks, like advanced persistent threats (APTs), typically involve all phases to ensure success and maintain long-term access to the target.

2.(a) Explain the pros and cons of performing a live response evidence collection versus a forensic disk image.

Live Response Evidence Collection

- Pros:
- Captures Volatile Data: Allows for the collection of volatile information, such as running processes, network connections, open files, and active memory content, which are not captured in a static forensic disk image.
- Quick Action: Enables immediate action, which can be crucial in an active incident, helping to understand the current state of a system and prevent further damage or data loss.
- Minimal Downtime: Often requires less downtime for the affected system compared to creating a full forensic disk image, which might be essential in environments where continuous operation is critical.
- Cons:
- Potential for Contamination: There is a risk of altering or contaminating the evidence because the system is live and changes can occur during data collection.
- Limited Scope: May not capture a comprehensive picture of the system's state if not carefully planned and executed, missing out on less volatile data that could be relevant.

Forensic Disk Image:

- Pros:
- Comprehensive Snapshot: Provides a full and exact copy of a system's storage, including deleted files, unallocated space, and other areas that might contain residual data, which can be crucial for thorough investigations.
- Minimizes Evidence Alteration: Because it is a direct bit-by-bit copy of the storage device, it minimizes the risk of evidence alteration during the imaging process.
- Cons:
- No Volatile Data: Does not capture volatile data, such as RAM contents, running processes, or network connections active at the time of imaging, which could be critical in understanding an ongoing attack.
- Time-Consuming: The imaging process can be time-consuming and might require taking the system offline, causing potential downtime and loss of business continuity.

2.(b) Why is a live response the most common method of evidence preservation during an IR?

There are 4 methods of evidence preservation:

- Real-Time Insight: It provides immediate visibility into the current state of a system, allowing incident responders to quickly assess and contain an ongoing attack.
- Preservation of Volatile Data: Since live response captures volatile data (e.g., RAM contents, active network connections, and running processes) that would be lost if the system were shut down or imaged later, it is crucial for understanding the dynamics of the incident as it unfolds.
- Flexibility and Speed: Live response allows for quicker decision-making and response, which is critical in minimizing damage and preventing data exfiltration or further spread of an attack.
- Operational Continuity: In many environments, especially those requiring high availability, taking a system offline for a full forensic image may not be feasible. A live response allows investigation while maintaining system operation.

3. Discuss some of the challenges related to outsourced IT services as they pertain to conducting an investigation. How can they be dealt with?

In your first FOIA (Freedom of Information Act) case, you've encountered challenges such as communication gaps, risk of evidence tampering, and limited control over systems and data. To address these, it's crucial to establish a centralized communication hub and appoint FOIA coordinators to streamline interactions between departments and third-party providers, ensuring timely responses. Implementing clear handling protocols and leveraging forensic tools like EnCase can help maintain evidence integrity and reduce the risk of tampering. Additionally, pre-established access agreements with third parties and escalation paths for delays can ensure faster access to necessary data and mitigate bottlenecks.

To further improve FOIA processes, automated management systems can track request statuses and communications, reducing delays and errors. Specialized FOIA response teams comprising legal, IT, and cybersecurity professionals can collaborate efficiently, ensuring prompt action and adherence to protocols. Regular audits and training programs for staff involved in the FOIA process can also help ensure evidence preservation and data integrity, ultimately streamlining investigations and reducing the complications you're currently facing.
