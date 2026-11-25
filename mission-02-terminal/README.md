# Mission 2 — Become Comfortable with the Terminal

## 1. Task / objective
The objective of this mission is to build practical command-line interface (CLI) proficiency by navigating directories, managing files and folders safely inside a dedicated practice sandbox (`terminal-practice`), understanding the role of command options/flags and Unix pipes, and inspecting the system package manager (Homebrew on macOS).

## 2. Work completed
- Explored 9 fundamental Terminal commands (`pwd`, `ls`, `ls -l`, `cd`, `mkdir`, `touch`, `cp`, `mv`, `cat`) and recorded the purpose and practical output of each.
- Created an isolated `terminal-practice` directory inside the repository to safely perform file-management exercises.
- Demonstrated file creation, content appending (`>>`) versus overwriting (`>`), file copying (`cp`), and file renaming (`mv`).
- Examined the impact of flags (`-l`, `-a`, `-h`) on standard directory listings.
- Executed and explained a pipeline (`ls -lh | head -n 5`) connecting stdout to stdin.
- Verified the installed Homebrew package manager (`Homebrew 7.0.9`) and listed managed software packages without altering the system.

## 3. Commands / tools used
- `pwd`: Print working directory — outputs the full absolute path of the current directory.
- `ls`: List directory contents — displays names of files and folders in the current location.
- `ls -l`: Detailed long listing — displays file type, permissions, owner, group, size in bytes, timestamp, and name.
- `cd`: Change directory — navigates between parent and child directories in the directory tree.
- `mkdir`: Make directory — creates new folders.
- `touch`: Updates file access/modification timestamps; creates a new empty file if it does not already exist.
- `cp`: Copy — duplicates files or directories from a source path to a destination path.
- `mv`: Move / rename — changes the location or name of a file or directory.
- `cat`: Concatenate and print — displays the text contents of files directly to the terminal screen.
- `head`: Filters and outputs the beginning lines of input data.
- `brew`: Homebrew package manager for macOS.

## 4. My understanding

### Task 2.1 — Basic Terminal Operations Table

| Operation / Command Name | What It Does | What I Observed |
|:---|:---|:---|
| **Current-directory display (`pwd`)** | Prints the full absolute path of the directory I am currently working in. | Displayed `/Users/[redacted]/.../digital-detective-8538`. |
| **Directory listing (`ls`)** | Lists the visible files and folders inside the working directory in multi-column format. | Displayed all 9 mission folders, `README.md`, and `evidence`. |
| **Detailed listing (`ls -l`)** | Displays files in long format including permissions (`drwxr-xr-x`), owner, size in bytes, and last modified date. | Revealed that folders showed size `96` or `128` bytes and files showed exact byte sizes. |
| **Change directory (`cd`)** | Moves the active shell context to a different folder. | Running `cd mission-02-terminal/terminal-practice` changed my working folder to the practice subfolder. |
| **Create directory (`mkdir`)** | Creates a new folder at the specified path. | `mkdir terminal-practice` successfully created the practice directory. |
| **Create empty file (`touch`)** | Creates a new empty file or updates its timestamp. | `touch notes.txt` created a new 0-byte file ready for text entry. |
| **Copy file (`cp`)** | Creates an independent duplicate of a file under a new name or location. | `cp notes.txt notes_copy.txt` resulted in two distinct identical files. |
| **Move / rename file (`mv`)** | Renames a file or moves it to another directory without duplicating content. | `mv notes_copy.txt notes_renamed.txt` renamed the duplicate, leaving the original `notes.txt` intact. |
| **Display file contents (`cat`)** | Reads file contents and prints them directly to terminal stdout. | `cat notes.txt` outputted `Digital Detective Lab Notes` directly onto the terminal screen. |

---

### Task 2.2 — Safe File Changes Practice

Inside `mission-02-terminal/terminal-practice/`:
1. Created `log.txt` with initial text:
   ```bash
   echo "System initialized: Log entry 1" > log.txt
   ```
2. Appended a second line without erasing the first:
   ```bash
   echo "System update: Log entry 2" >> log.txt
   ```
3. Verified both lines with `cat log.txt`:
   ```text
   System initialized: Log entry 1
   System update: Log entry 2
   ```
4. Created a backup copy and renamed it:
   ```bash
   cp log.txt log_backup.txt
   mv log_backup.txt log_archive.txt
   ```

#### Analysis Questions:
- **What is the difference between replacing a file's contents and adding text to the end?**  
  The single redirect operator (`>`) truncates (erases) the destination file completely before writing the new text. The append redirect operator (`>>`) preserves all existing contents and adds the new text at the end of the file on a new line.
- **What is the difference between copying a file and moving a file?**  
  `cp` creates an independent second copy of the file on the storage drive, consuming additional disk space. `mv` relocates the file or changes its directory entry (name), keeping the exact same physical disk blocks and leaving no file at the original location.
- **What information does the current-directory display provide?**  
  `pwd` provides the complete, unambiguous absolute path from the root directory (`/`) to the exact folder where the shell is currently executing commands. This prevents accidental modifications in the wrong directory.
- **Why is a directory-listing operation useful?**  
  `ls` allows the user to explore filesystem contents, confirm file names, verify that files were created or moved as intended, and inspect file attributes (sizes and permissions) without opening a graphical window.

---

### Task 2.3 — Flags and Pipes

#### Flag Exploration:
- `ls`: Default compact multi-column listing showing only non-hidden file and folder names.
- `ls -l`: Long format displaying file mode/permissions (`-rw-r--r--`), hard link count, owner, group, raw size in bytes, modification timestamp, and name.
- `ls -la`: Includes hidden entries (files and directories starting with `.`, such as `.`, `..`, and `.git`).
- `ls -lh`: Formats file sizes into human-readable units (e.g., `3.2K`, `96B`, `128B`) instead of raw byte counts.

#### Pipe Demonstration:
Command:
```bash
ls -lh | head -n 5
```
Output:
```text
total 8
-rw-r--r--@ 1 [redacted]  staff   3.2K Nov 25 23:14 README.md
drwxr-xr-x@ 3 [redacted]  staff    96B Nov 25 23:14 evidence
drwxr-xr-x@ 3 [redacted]  staff    96B Nov 25 23:13 mission-00-setup
drwxr-xr-x@ 3 [redacted]  staff    96B Nov 25 23:14 mission-01-computer-basics
```

**How the pipe (`|`) works:**
- The pipe operator connects the standard output (stdout) of the command on its left directly to the standard input (stdin) of the command on its right via an inter-process memory buffer.
- **Left side (`ls -lh`):** Generates a formatted list of all items with human-readable file sizes and sends it down the stream.
- **Right side (`head -n 5`):** Reads the incoming stream and passes only the first 5 lines to the terminal screen, discarding the rest.

---

### Task 2.4 — Understanding Package Managers

On macOS, Homebrew was inspected:
```bash
brew --version
# Output: Homebrew 7.0.9
```
Listing installed packages (`brew list | head -n 5`) revealed managed tools like `ca-certificates`, `cairo`, `dav1d`, `ffmpeg`, and `fontconfig`.

**Why package managers are useful:**  
A package manager automates the process of finding, downloading, compiling, installing, configuring, and updating software from verified central repositories. Instead of manually searching websites, managing system paths, and compiling dependencies by hand, a user can run a single command (like `brew install git`) and the package manager automatically resolves all prerequisite libraries and keeps them updated safely.

---

## 5. Difficulties faced
When testing `ls -lh`, folder sizes on macOS APFS appeared as `96B` or `128B`. Initially this seemed confusing because folders contain files that are much larger.

## 6. How I resolved them
I researched filesystem directory representation and learned that on Unix/macOS, a directory is a special file containing index entries (pointers to child files/folders). The `96B` or `128B` indicates the size of this directory index metadata table itself, not the cumulative size of all child files inside it.

## 7. Evidence / files
- Mission documentation: `mission-02-terminal/README.md`
- Practice directory: `mission-02-terminal/terminal-practice/`
- Practice files:
  - `notes.txt` (Initial file with text)
  - `notes_renamed.txt` (Renamed duplicate)
  - `log.txt` (File with 2 appended entries)
  - `log_archive.txt` (Renamed backup)

## 8. Commit details
- **Commit message**: `Complete Terminal and file management mission`
- **Branch**: `main`
- **Push status**: Verified and pushed to GitHub
