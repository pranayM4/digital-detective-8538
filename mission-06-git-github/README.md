# Mission 6 — Git and GitHub

## 1. Task / objective
The objective of this mission is to understand professional version control principles using Git and GitHub. This includes mastering the staging and commit lifecycle, inspecting repository status and logs, isolating experimental changes in a feature branch (`update-about`), publishing the branch to GitHub, opening a formal Pull Request (PR) for collaborative review, and assembling a concise glossary of essential Git operations.

## 2. Work completed
- Examined the four core stages of the Git workflow (Working Directory, Staging Area, Local Repository, Remote Repository).
- Formulated an in-depth comparison between staging changes (`git add`) and committing them (`git commit`).
- Created and checked out a dedicated feature branch named `update-about`.
- Updated the root `README.md` on `update-about` with an authentic "My Learning" section detailing three key insights from the assignment.
- Committed the update and published the branch to GitHub with upstream tracking.
- Created Pull Request #1 on GitHub targeting the `main` branch, wrote a clear technical description, and verified the diff online.
- Documented the Pull Request URL, branch structure, and verified status (`Open`).
- Compiled a nine-point reference glossary defining foundational Git commands in simple, precise terms.

## 3. Commands / tools used
- `git status`: Displays the state of the working directory and staging area, showing tracked, modified, and untracked files.
- `git add <file>`: Adds file modifications from the working directory into the Git index (staging area).
- `git commit -m "<msg>"`: Records staged snapshots permanently into the repository's commit history with a descriptive message.
- `git log --oneline`: Displays the condensed, chronological commit history with short SHAs.
- `git checkout -b <branch>` / `git switch -c <branch>`: Creates a new isolated branch and switches the working tree to it.
- `git push -u origin <branch>`: Uploads the local branch and commits to GitHub, establishing an upstream tracking reference.
- `git checkout main`: Switches back to the primary integration branch.
- GitHub Pull Request Interface / REST API: Used to create and track Pull Request #1.

## 4. My understanding

### Task 6.1 — The Git Workflow: Staging vs. Committing

| Git Operation | What It Does In Your Own Words |
|:---|:---|
| **Check repository status (`git status`)** | Shows which files have been modified, which changes are staged for the next commit, and which files are currently untracked by Git. |
| **Stage selected changes (`git add`)** | Selects and moves specific file modifications into the staging area (index), preparing them to be bundled into the next commit snapshot. |
| **Create a commit (`git commit`)** | Permanently records the staged changes as a new, immutable snapshot in the local Git repository history, labeled with a unique commit hash and message. |
| **View commit history (`git log`)** | Displays the chronological timeline of past commits, showing who authored each change, when it occurred, and the associated commit message. |

#### Difference Between Staging and Committing:
Staging (`git add`) is like packing a specific box of items before sealing it. It allows a developer to pick and choose exactly which modified lines or files belong together in a logical unit, leaving unfinished edits in the working directory untouched. Committing (`git commit`) is like sealing, labeling, and stamping that box with an indelible barcode into the permanent archive. Staging creates the draft snapshot; committing makes it an immutable part of the project history.

---

### Tasks 6.2 & 6.3 — Branches and Pull Requests

#### Branch Details:
- **Branch Name:** `update-about`
- **Creation Command:** `git checkout -b update-about`
- **Modifications Made:** Added the `## My Learning` section to `README.md` highlighting insights on CLI power, binary systems, and version control discipline.
- **Branch Commit Message:** `Add My Learning section to root README`
- **Remote Push:** `git push -u origin update-about`

#### Pull Request Details:
- **PR Number:** `#1`
- **PR Title:** `Update root README with My Learning section`
- **PR URL:** https://github.com/pranayM4/digital-detective-8538/pull/1
- **Source Branch (Head):** `update-about`
- **Target Branch (Base):** `main`
- **PR Status:** `Open` (retained in open state as specified by instructor guidelines for faculty review).

#### Why Branches and Pull Requests Are Essential in Team Projects:
- **Branches** allow developers to work on new features, bug fixes, or experiments in complete isolation without risking the stability of the main production code (`main`). If a feature is broken or abandoned, the branch can simply be discarded without affecting other team members.
- **Pull Requests (PRs)** provide a formal collaborative review mechanism. Instead of pushing code directly into production, a developer submits a PR asking teammates to inspect the visual diff, review code quality, test changes, and discuss improvements before merging the code into `main`.

---

### Task 6.4 — Git Command Glossary

1. **`git init`**: Initializes a brand-new, empty Git version control repository inside the current folder.
2. **`git status`**: Shows the current state of files, identifying untracked, modified, and staged changes.
3. **`git add`**: Adds chosen file modifications from the working directory into the staging area.
4. **`git commit`**: Saves staged changes as a permanent snapshot in the repository's commit history.
5. **`git log`**: Displays the historical list of past commits, their authors, timestamps, and messages.
6. **`git branch`**: Lists existing local branches or creates a new branch pointer when given a name.
7. **`git switch` / `git checkout`**: Switches the working directory between different branches or commits.
8. **`git push`**: Transmits local commits from your computer up to a remote repository on GitHub.
9. **`git pull`**: Fetches the newest changes from the remote repository on GitHub and merges them into the local branch.

---

## 5. Difficulties faced
When attempting to run `git checkout -b update-about` in the sandbox, Git reported an access error accessing the user's global configuration file.

## 6. How I resolved them
I ran the branch creation with appropriate environment permissions, allowing Git to recognize the author identity configured in the local repository configuration and successfully create and switch branches.

## 7. Evidence / files
- Mission documentation: `mission-06-git-github/README.md`
- Active GitHub Pull Request: https://github.com/pranayM4/digital-detective-8538/pull/1
- Published feature branch: `update-about`
- Git command glossary (Task 6.4)

## 8. Commit details
- **Commit message**: `Complete Git and GitHub collaboration mission`
- **Branch**: `main`
- **Push status**: Verified and pushed to GitHub
