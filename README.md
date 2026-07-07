# DecodeLabs Cybersecurity Internship Portfolio

Welcome to my cybersecurity project portfolio completed during my industrial training at **DecodeLabs (Batch 2026)**. This repository houses four distinct practical milestones progressing from fundamental security coding and cryptography to analytical threat hunting and network defense.

---

## 🛠️ Tech Stack & Skills
* **Security Core:** Threat Analysis, Incident Handling, Cryptography, Data Validation
* **Development & Logic:** Python / JavaScript, String Handling, Conditional Operations
* **Defensive Mechanisms:** Entropy Checks, Cipher Logic, Phishing Triaging, Log Analysis

---

## 📂 Project Overview

### 🔒 Project 1: Automated Password Strength Checker
* **Goal:** Create an engine to calculate password entropy and validate compliance against enterprise security policies.
* **Key Implementations:**
  * Strict evaluation of length parameters.
  * Conditional evaluation checking for upper/lowercase distribution, numeric values, and special character variety.
  * Dynamic classification mapping inputs into `Weak`, `Medium`, or `Strong` tier rankings.
* **Core Skills:** String handling, condition testing, basic identity & access management validation.

### 🔑 Project 2: Symmetric Cryptographic Engine
* **Goal:** Implement programmatic encryption and decryption processes to understand confidentiality frameworks for data in transit.
* **Key Implementations:**
  * Reversible algorithmic logic leveraging basic substitution ciphers (e.g., Caesar Cipher / Vigenère Cipher mechanics).
  * Feature mapping enabling customizable alphanumeric shift offsets.
  * Integrated rendering showcasing raw text, obfuscated ciphertext, and fully recovered plaintext side-by-side.
* **Core Skills:** Data protection principles, mathematical/programmatic logic building.

### 🛡️ Project 3: Enterprise Phishing Awareness Analysis
* **Goal:** Act as a defensive Security Operations Center (SOC) Analyst to triage communication data, detect deceptive elements, and counter malicious social engineering delivery systems.
* **Key Implementations:**
  * Deconstruct email components to flag invalid syntax headers, spoofed addresses, and mismatched domains.
  * Dissect payload Delivery Methods—specifically highlighting URL shorteners hiding active threats, lookalike/typosquatting domains, and high-urgency keywords.
  * Formulated an organizational **"Red Flag Check-sheet"** to classify threats into distinct logical categories.
* **Core Skills:** Threat hunting, URL triaging, cyber attack vector awareness, incident mitigation logic.

### 🎛️ Project 4: Network Traffic Monitoring & Threat Detection
* **Goal:** Analyze enterprise system behaviors, investigate event logging architectures, and detect anomalous activity pattern deviations across network interfaces.
* **Key Implementations:**
  * Baseline log evaluation and parsing for system events.
  * Developing alert logic parameters to signal credential stuffing, unauthorized privilege escalation, or unusual data exfiltration vectors.
  * Mapping attack vectors to recognized industry models like the MITRE ATT&CK framework.
* **Core Skills:** SIEM operations, log auditing, rule customization, network defense workflows.

---

## 🚀 How to Run the Codebases

### Prerequisites
Ensure your environment satisfies the execution binaries depending on your configuration framework:
```bash
# Verify Python runtime environment
python --version

# Verify Node.js runtime environment (if using JS implementations)
node --version

Setup
Clone the project archive:

Bash
git clone [https://github.com/harisch007/decodelabs-cybersecurity.git](https://github.com/harisch007/decodelabs-cybersecurity.git)
cd decodelabs-cybersecurity
Navigate into your desired workspace directory and execute the primary entry files:

Bash
cd project-1-password-checker
python main.py
