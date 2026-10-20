# IA455-Quiz-4

**Source:** [`IA455-Quiz-4.docx`](../archive/canvas-submissions/IA455-Quiz-4.docx)  
**Course:** IA 455 - Incident Response (EMU)  
**Author:** Julio Barros

> Canvas export. For study summaries without duplicating instructor prompts, see [learning-notes.md](learning-notes.md).

IA-455 Incident Response 	Yunguo Guan

Quiz 4 	Revision: 06/04/2024

50pts

Quiz 4:

When architecting a new network monitoring system, what types of questions should be asked of the IT or network staff? How can you help ensure complete visibility into traffic egressing your networks?

When architecting a new network monitoring system, it’s essential to ask IT or network staff questions that reveal the scope, requirements, and challenges of their network environment. Examples include:

What are the key assets or services that require monitoring? Understanding which assets are critical will help prioritize resources and focus on high-risk areas.

What types of network traffic need to be monitored? This clarifies which protocols, services, and applications are used within the network, aiding in developing filters or alerts tailored to relevant traffic.

What current security and monitoring tools are already in place? This helps avoid redundancy and ensures new systems integrate smoothly with existing ones.

Are there specific compliance or regulatory requirements? These could affect data storage, access controls, or monitoring capabilities and inform which logs need retention and monitoring.

To ensure complete visibility into traffic leaving the network (egress traffic), consider implementing tools such as network taps or port mirroring to capture traffic across various network segments. Configuring intrusion detection/prevention systems (IDS/IPS) and setting up firewall rules to log and monitor egress traffic also aids visibility. Regular auditing, network segmentation, and threat intelligence integration further enhance monitoring effectiveness.

What is perfect forward secrecy and how does it affect your ability to decrypt SSL traffic? How might you decrypt SSL traffic that is encrypted using a forward secrecy algorithm?

Perfect Forward Secrecy (PFS) is a property of cryptographic systems that ensures session keys are unique for each session and not derived from a single master key. In SSL/TLS protocols, PFS is implemented through ephemeral key exchanges (e.g., using Diffie-Hellman Ephemeral [DHE] or Elliptic Curve Diffie-Hellman Ephemeral [ECDHE]). This feature protects past sessions even if a private key is compromised, increasing security but complicating decryption efforts.

To decrypt SSL traffic with PFS, a man-in-the-middle (MITM) approach can be used. This typically involves installing a trusted certificate on endpoints to intercept traffic before it’s encrypted with a forward secrecy algorithm. Organizations may deploy SSL decryption appliances that function as proxies to capture and inspect traffic. However, this method requires that the organization has control over the devices, and it raises privacy concerns, so it should be implemented in compliance with legal standards and only in environments where privacy expectations are clearly defined.

## Quiz: Questions formatting

Quizzes consist of several two part questions. Students are required to answer both parts of the questions, in one or more paragraphs. The answer should be supported by knowledge gained by the book, lecture, or student research. It is acceptable to include APA style citations as part of a Quiz answer. All quizzes in the class are open book / open notes / open internet. Students are encouraged to research their answers.

The questions in the quiz will be on the top of the quiz Canvas page, so students are able to see the questions, and prepare their answers before starting the quiz. It is advised that the answers be proofread and have spelling and grammar checks ran before submission.

Late submissions will follow the class policy of a 10% penalty for less than a week late, and 20% for a week or more late.

## Quiz: Formatting and Requirements

Answer should be formatted as one or more paragraphs consisting of a minimum of four sentences. Giving shorter answers will result in deductions. There are no upper limits on the word count or length of answers.

Students should write their answers using professional or academic English and use professional looking fonts and formatting. Any citations included should be in APA style, or some similar type of formatting.
