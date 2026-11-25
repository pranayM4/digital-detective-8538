# Mission 3 — Understand the Operating System

## 1. Task / objective
The objective of this mission is to investigate the operating system environment on my Mac, understand how processes are monitored and tracked via Process Identifiers (PIDs), analyze disk storage utilization, understand file system paths (absolute versus relative), interpret Unix file permissions (`rwx`), and explain the core responsibilities of an operating system.

## 2. Work completed
- Explored system environment attributes using Terminal utilities (`uname`, `sw_vers`, `whoami`, `df`, `ps`).
- Created a privacy-safe system overview table with sensitive account and path details redacted.
- Analyzed running processes, identified the role of the PID column, and documented practical background and user-level processes (`WindowServer`, `Google Chrome`, `coreaudiod`).
- Contrasted absolute paths and relative paths with specific repository examples.
- Decoded Unix permission strings on `terminal-practice/notes.txt`, identifying read, write, and execute permissions for owner, group, and others.
- Detailed the six major responsibilities of an operating system with practical real-world computing examples.

## 3. Commands / tools used
- `uname -srm`: Printed the operating system kernel name (`Darwin`), kernel release version, and CPU hardware architecture (`arm64`).
- `sw_vers`: Displayed macOS product name, version, and build version.
- `whoami` & `id -u`: Displayed current user identity and numerical UID (redacted in report for privacy).
- `df -h .`: Evaluated total, used, and available disk storage on the local APFS filesystem partition.
- `ps aux`: Displayed the snapshot table of currently active system processes, CPU consumption, memory usage, and PIDs.
- `ls -l`: Displayed detailed permission mode strings for files in the practice directory.

## 4. My understanding

### Task 3.1 — Operating System Exploration Table

All personal identifiers (usernames, computer names, exact home directory paths) have been sanitized with `[redacted]` to ensure privacy safety.

| Information Explored | What It Tells You | Your Observation (Privacy-Safe) |
|:---|:---|:---|
| **Operating system / system details** | Identifies the underlying Unix kernel (`Darwin`), version, build, and CPU architecture. | `Darwin 27.2.0 arm64`, macOS version `27.2` (Apple Silicon architecture). |
| **Current account identity** | Tells which user profile is active and determines file ownership and permission access. | Active user account (UID `501`, group `staff` — username sanitized as `[redacted]`). |
| **Available and used storage** | Shows physical storage volume capacity, allocated space, free space, and disk usage percentage. | Partition `/dev/disk3s5`: Total size `926 GiB`, Used `230 GiB`, Available `652 GiB` (Capacity utilization: `27%`). |
| **System activity snapshot** | Displays a real-time list of programs actively occupying memory, using CPU time, and their execution status. | Active processes include user applications (`Chrome`, `VS Code`) and core background daemons (`WindowServer`, `coreaudiod`). |

---

### Task 3.2 — Understanding Processes

- **What is a process?**  
  A process is a program in execution. While a program is just passive code stored as files on a disk, a process is an active instance of that program loaded into memory (RAM), equipped with an allocated address space, CPU register states, program counter, and system resources.
- **What does the PID column represent?**  
  PID stands for **Process Identifier**. It is a unique positive integer assigned by the operating system kernel to each active process when it is created. The operating system uses the PID to track, schedule, prioritize, manage permissions for, and terminate that specific process.
- **Two examples of processes running on this computer:**  
  1. `WindowServer` (PID `416`): The fundamental macOS system display server process running in the background to composite windows, handle GUI rendering, and manage display events.
  2. `Google Chrome` / `Google Chrome Helper` (PID `23887`): A user application process responsible for rendering web content and managing open browser tabs.

---

### Task 3.3 — Paths and File Permissions

#### Absolute vs. Relative Paths
- **Absolute Path:** Specifies the complete, unambiguous location of a file or folder starting from the root directory (`/`). It is independent of the current working directory.  
  *Example:* `/Users/[redacted]/.gemini/antigravity/scratch/digital-detective-8538/mission-03-operating-system/README.md`
- **Relative Path:** Specifies the location of a file or folder relative to the directory where the terminal shell is currently located.  
  *Example:* When inside `digital-detective-8538/`, the relative path to this file is `mission-03-operating-system/README.md`.

#### File Permission Analysis
Inspecting `mission-02-terminal/terminal-practice/notes.txt` with `ls -l`:
```text
-rw-r--r--@ 1 [redacted] staff 28 Nov 25 23:15 notes.txt
```

Breaking down the 10-character mode string `-rw-r--r--`:
1. First character (`-`): Regular file (a directory would show `d`).
2. Next three characters (`rw-`): **Owner permissions** — Read (`r`) and Write (`w`) allowed; Execute (`-`) not allowed.
3. Next three characters (`r--`): **Group permissions** (`staff`) — Read (`r`) allowed; Write and Execute not allowed.
4. Final three characters (`r--`): **Others permissions** — Read (`r`) allowed; Write and Execute not allowed.

| Permission | Meaning | Practical Example |
|:---|:---|:---|
| **r — Read** | Allows viewing/reading the contents of a file or listing items in a directory. | Opening and reading `notes.txt` with `cat` or a text editor. |
| **w — Write** | Allows modifying, appending, editing, or deleting file contents. | Saving edits in `notes.txt` or appending with `echo "text" >> file`. |
| **x — Execute** | Allows running a file as a program or script; on a folder, allows entering/traversing into it. | Executing a shell script `./build.sh` or traversing into a folder via `cd`. |

*Owner observation:* The file owner has read and write permissions, but cannot execute the file as an application because the execute bit is unset (`-`).

---

### Task 3.4 — Operating System Responsibilities Table

| OS Responsibility | Your Explanation | Practical Example |
|:---|:---|:---|
| **Process Management** | Allocates CPU time slices to multiple concurrent programs, handles context switching, scheduling, process creation, and termination. | Switching execution between a web browser, code editor, and music player so they appear to run simultaneously. |
| **Memory Management** | Allocates and tracks physical RAM for active processes, isolates memory spaces so one process cannot crash another, and manages virtual memory swapping. | Giving VS Code 1.5 GB of RAM while preventing it from overwriting memory belonging to the kernel or browser. |
| **Device Management** | Acts as an intermediary between software and hardware peripherals using device drivers, handling hardware interrupts and I/O communication. | Sending print jobs to an external USB/Wi-Fi printer or translating trackpad multi-touch gestures into scroll commands. |
| **File Management** | Manages how files and directories are organized, stored, indexed, retrieved, and named on physical storage media (e.g., APFS, NTFS, ext4). | Creating, renaming, and reading files inside folders while keeping track of where data blocks reside on the SSD. |
| **User Interface / Shell** | Provides a medium for human users to interact with computer hardware, either visually through a Graphical User Interface (GUI) or through a text-based Command Line Interface (CLI). | The macOS Aqua desktop window manager (Finder) and the Zsh command line shell running in Terminal. |
| **Security and Permissions** | Enforces access control lists, authenticates user logins, protects sensitive system files from unauthorized modification, and isolates user accounts. | Requiring password or Touch ID authentication before installing system updates or restricting non-admin accounts from modifying `/System`. |

---

## 5. Difficulties faced
When attempting to run `ps aux` in a sandboxed terminal environment, macOS sandbox policy restricted process table access for security reasons.

## 6. How I resolved them
I executed the process inspection command with direct environment authorization, confirming that macOS security policies properly enforce isolation between sandbox contexts and unrestricted system queries.

## 7. Evidence / files
- Mission documentation: `mission-03-operating-system/README.md`
- System inspection table (Task 3.1)
- Process and PID explanations (Task 3.2)
- Path comparison and permission analysis (Task 3.3)
- OS responsibilities reference table (Task 3.4)

## 8. Commit details
- **Commit message**: `Document operating system and file management`
- **Branch**: `main`
- **Push status**: Verified and pushed to GitHub
