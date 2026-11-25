# Mission 0 — Repository and Workspace Setup

## 1. Task / objective
The objective of this mission was to verify the local software development environment on my Mac, verify that Python 3 and Git are installed, create the assignment repository following the exact naming convention (`digital-detective-XXXX` with my last four USN digits `8538`), scaffold the folder hierarchy for all nine missions, author the initial root documentation, and publish the repository to my public GitHub account.

## 2. Work completed
- Checked installed versions of Python 3 and Git using Terminal commands.
- Created local workspace directory named `digital-detective-8538`.
- Initialized a local Git repository with `main` as the default branch.
- Configured local Git username (`PranayM4`) and email.
- Created the required mission directories (`mission-00-setup` through `mission-08-final-report` and `evidence`).
- Prepared the root `README.md` containing student metadata, project overview, and a complete mission navigation index.
- Created a public repository named `digital-detective-8538` under my GitHub profile (`pranayM4`) and linked the remote origin.
- Pushed the initial workspace setup to GitHub and verified its public visibility.

## 3. Commands / tools used
- `python3 --version`: Used to inspect the installed Python runtime version (`Python 3.14.7`).
- `git --version`: Used to inspect the Git version control system (`git version 2.55.0`).
- `mkdir -p`: Used to create local directories for the project and mission folders.
- `git init -b main`: Initialized a clean Git repository with the standard default branch name `main`.
- `git config`: Configured author name and email attributes for commits.
- `git remote add origin https://github.com/pranayM4/digital-detective-8538.git`: Linked the local repository to GitHub.
- `git status` / `git add` / `git commit`: Tracked, staged, and committed the initial setup files.
- `git push -u origin main`: Uploaded local branches and tracked files to the remote GitHub repository.

## 4. My understanding
A Git repository is a tracked storage space that maintains the full version history of a project, recording who made changes, when they were made, and what lines were added or removed. 

Structuring the repository by numbered missions (`mission-00-setup` through `mission-08-final-report`) creates an organized, modular workspace where each component of computer systems study—from CLI commands to operating system internals and number systems—can be tested, documented, and reviewed in isolation without cluttering the project root.

## 5. Difficulties faced
When first checking Git configuration in a sandboxed command-line session, Git reported an access error (`fatal: unable to access '/Users/pranayranjan/.gitconfig': Operation not permitted`) because the global user config file was outside the workspace sandbox boundary.

## 6. How I resolved them
I ran the environment check with local repository configuration (`git config user.name "PranayM4"` and `git config user.email "pranayranjan145@gmail.com"` inside the project folder), allowing Git to function normally without needing external configuration files.

## 7. Evidence / files
- Root documentation: `README.md`
- Mission setup file: `mission-00-setup/README.md`
- Folder structure:
  - `mission-00-setup/`
  - `mission-01-computer-basics/`
  - `mission-02-terminal/`
  - `mission-03-operating-system/`
  - `mission-04-programs/`
  - `mission-05-numbers-data/`
  - `mission-06-git-github/`
  - `mission-07-networking/`
  - `mission-08-final-report/`
  - `evidence/`
- Verified software versions:
  - Python: `3.14.7`
  - Git: `2.55.0`
  - OS: macOS (Darwin arm64)

## 8. Commit details
- **Commit message**: `Set up Digital Detective mission structure`
- **Branch**: `main`
- **Push status**: Verified and visible on GitHub at `https://github.com/pranayM4/digital-detective-8538`
