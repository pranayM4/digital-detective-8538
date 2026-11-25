# The Digital Detective — Explore Your Computer • Build a Mini System Report

**Diwali Independent Learning Assignment**  
**Course:** Introduction to Computer Systems / SnAI  
**Student Name:** Pranay Ranjan  
**USN:** 2392608538  
**Campus / Section:** B.Tech CSE (First Year)  
**GitHub Profile:** [@pranayM4](https://github.com/pranayM4)  
**Repository Name:** [digital-detective-8538](https://github.com/pranayM4/digital-detective-8538)  
**Repository URL:** https://github.com/pranayM4/digital-detective-8538  

---

## 1. Project Overview

**The Digital Detective** is an individual learning assignment designed to explore the internal workings of modern computer systems. Through hands-on investigation on macOS, practical Terminal operations, Python programming, version control workflows, and network diagnostics, this project deconstructs how hardware, operating systems, and networks interact to execute software.

Every mission was completed sequentially on my local computer, thoroughly tested, sanitized for personal data privacy, documented using the required 8-section reflection format, and pushed to GitHub with dedicated, meaningful Git commits.

---

## 2. Topics Explored

- **Computer Architecture & IPOS Cycle**: Deconstruction of input, CPU processing, memory management, display output, and persistent storage.
- **Hardware & Software Taxonomy**: Differentiating physical components from operating systems, application software, and system utilities.
- **Embedded & Everyday Systems**: Architecture of dedicated computer systems (ATMs, traffic lights, transit fare gates).
- **Command-Line Interface (CLI)**: Navigating directory hierarchies, safe file operations, Unix flags (`-l`, `-a`, `-h`), and stdout-to-stdin pipelines (`|`).
- **Operating System Internals**: Kernel metrics (`Darwin`), process lifecycle, process identifiers (PIDs), APFS storage analysis, path resolution, and Unix permission bits (`rwx`).
- **Program Execution Paradigms**: Ahead-of-time compilation versus line-by-line interpretation, and Python's hybrid bytecode/PVM execution model.
- **Number Systems & Data Representation**: Manual step-by-step conversions between decimal, binary, and hexadecimal; Python verification; and character encoding standards (ASCII vs. UTF-8).
- **Version Control & Collaboration**: Git staging index, atomic commits, branch isolation (`update-about`), remote synchronization, and GitHub Pull Requests.
- **Computer Networking & Web Architecture**: Network topologies (LAN, MAN, WAN), DNS domain resolution, ICMP reachability (`ping`), and the full 7-step HTTP/HTTPS website request lifecycle.

---

## 3. Mission Navigation Index

| Mission | Title | Key Activities & Deliverables | Status | README Link |
|:---:|:---|:---|:---:|:---:|
| **0** | **Repository & Workspace Setup** | Environment checks (Python 3.14.7, Git 2.55.0), folder scaffolding, root documentation, and GitHub remote connection. | Complete | [Mission 0 README](mission-00-setup/README.md) |
| **1** | **Computer Fundamentals & IPOS** | IPOS trace of writing and saving code, hardware vs. software taxonomy, and 3 embedded systems. | Complete | [Mission 1 README](mission-01-computer-basics/README.md) |
| **2** | **Terminal & File Management** | Safe file management in `terminal-practice/`, core CLI commands, flags, pipelines, and Homebrew inspection. | Complete | [Mission 2 README](mission-02-terminal/README.md) |
| **3** | **Operating System & Permissions** | Kernel metrics, process table and PID analysis, storage audit, absolute vs. relative paths, and file permissions. | Complete | [Mission 3 README](mission-03-operating-system/README.md) |
| **4** | **How Programs Run** | Executing `hello.py` and comprehensive comparison of compilers, interpreters, and hybrid bytecode models. | Complete | [Mission 4 README](mission-04-programs/README.md) |
| **5** | **Number Systems, Python & Data** | 7 manual step-by-step conversions, Python verification, `number_converter.py`, and ASCII/UTF-8 encoding notes. | Complete | [Mission 5 README](mission-05-numbers-data/README.md) |
| **6** | **Git, GitHub & Collaboration** | Staging vs. committing, branching (`update-about`), live Pull Request #1, and 9-command Git glossary. | Complete | [Mission 6 README](mission-06-git-github/README.md) |
| **7** | **Computer Networks** | 8 network concepts, live `ping` and `nslookup` on `example.com`, and 7-step website opening lifecycle. | Complete | [Mission 7 README](mission-07-networking/README.md) |
| **8** | **Final Review & Submission** | Comprehensive repository audit, quality verification, and final submission report. | Complete | [Mission 8 README](mission-08-final-report/README.md) |

---

## 4. Instructions for Running Programs

All Python programs were developed using Python 3 and standard library features without external dependencies.

### Running `hello.py` (Mission 4)
From the repository root folder, run:
```bash
python3 mission-04-programs/hello.py
```
**Expected Output:**
```text
Hello from Python
```

### Running `number_converter.py` (Mission 5)
From the repository root folder, run:
```bash
python3 mission-05-numbers-data/number_converter.py
```
Alternatively, navigate to the mission directory:
```bash
cd mission-05-numbers-data
python3 number_converter.py
```
**Interactive Sample Session:**
```text
=== Decimal to Binary & Hexadecimal Converter ===
Enter a positive decimal integer: 25
Decimal Value:     25
Binary Value:      0b11001
Hexadecimal Value: 0x19
```

---

## 5. My Learning

During the execution of these investigative missions, I gained practical understanding of three core concepts:
1. **The Power of the Command Line:** I learned that GUI desktop interfaces are simply visual abstractions over operating system system calls. Operating through the Terminal with commands like `pwd`, `ls -lh`, and Unix pipes (`|`) allows for precise, automated file and process management without the overhead of window management.
2. **Positional Number Systems & Binary Representation:** By working through manual successive divisions and power expansions, I realized how hardware digital circuits represent all data (numbers, text, and instructions) using binary logic states (bits), and how hexadecimal provides a clean human-readable notation for bytes.
3. **Version Control Discipline:** Git is not just for backup storage; it creates a verifiable, immutable history of project progression. Isolating changes in dedicated branches like `update-about` protects the production codebase (`main`) and enables structured code review through Pull Requests.

---

## 6. Repository Commitment & Integrity Policy

- **Sequential Execution**: Every mission was completed, documented, and verified before proceeding to the subsequent mission.
- **Genuine Commits**: Each mission has at least one distinct, meaningful commit recording actual changes.
- **Privacy Assurance**: Sensitive identifiers (hostnames, local usernames, private IP addresses, Wi-Fi network names) have been sanitized as `[redacted]` across all documentation.
- **Zero Sudo Usage**: All operations were conducted strictly inside user space within the repository directory.
