# Mission 4 — How Programs Run

## 1. Task / objective
The objective of this mission is to write and execute a simple Python program (`hello.py`), verify its stdout execution in the terminal using Python 3, and examine the fundamental differences between compiled and interpreted execution models, including how modern hybrid languages translate source code into machine instructions.

## 2. Work completed
- Authored `mission-04-programs/hello.py` containing a single `print("Hello from Python")` statement.
- Executed the script via Terminal using Python 3 and verified the exact expected standard output.
- Formulated a comprehensive comparison table contrasting compilers and interpreters across translation timing, output format, language examples, and execution advantages.
- Wrote an original explanation detailing how compilers and interpreters work and how languages like Python combine elements of both.

## 3. Commands / tools used
- `python3`: The Python 3 runtime interpreter used to execute `hello.py`.
- Text Editor / VS Code: Used to create and edit Python source code and documentation.
- Git: Used to stage, commit, and push mission artifacts.

## 4. My understanding

### Task 4.1 — Program Execution Verification

Script content (`mission-04-programs/hello.py`):
```python
print("Hello from Python")
```

Execution command and terminal output:
```bash
$ python3 mission-04-programs/hello.py
Hello from Python
```

Observation: The operating system launched the Python 3 binary, which parsed the source code file, loaded the built-in `print` function, sent the string characters `Hello from Python\n` to the standard output stream (file descriptor 1), and terminated with exit code `0`.

---

### Task 4.2 — Compiler vs. Interpreter Comparison

| Point | Compiler | Interpreter |
|:---|:---|:---|
| **When translation / execution happens** | Translates the entire high-level source code into low-level machine code or binary object files in advance, *before* the program is run. | Translates and executes high-level source code instructions line by line on the fly at *runtime*. |
| **Typical output** | Produces a standalone, executable binary machine-code file (such as `.exe` on Windows, or an ELF/Mach-O binary on Linux/macOS). | Does not produce a standalone machine-code executable; requires the interpreter runtime to read and run the script every time. |
| **One example** | C, C++, Rust, Go. | Python, JavaScript, Ruby, PHP. |
| **One advantage** | Exceptional runtime performance and execution speed, since the CPU executes native machine instructions directly without translation overhead. | Platform independence and ease of debugging, allowing developers to test code immediately without an explicit compilation build cycle. |

#### Detailed Explanation of the Difference:
A compiler processes the entire source code file before execution begins, converting human-readable programming syntax into native CPU machine instructions and catching syntax errors ahead of time. In contrast, an interpreter reads, analyzes, and executes program instructions statement by statement during runtime, meaning execution halts only when it encounters an error at that specific line. 

While pure compilers produce fast standalone binaries and pure interpreters offer flexible interactive execution, many modern languages employ a hybrid model. For example, Python first compiles source code (`.py`) into intermediate bytecode (`.pyc`), which is then executed by the Python Virtual Machine (PVM) interpreter, combining portable bytecode with runtime flexibility.

---

## 5. Difficulties faced
When learning about execution models, it is common to hear that "Python is an interpreted language" and assume that it never compiles anything.

## 6. How I resolved them
By inspecting Python's execution architecture, I learned that CPython (the standard Python implementation) actually compiles source code into internal bytecode instructions before the Python Virtual Machine interprets those bytecode instructions, clarifying that compilation and interpretation frequently work together.

## 7. Evidence / files
- Python program: `mission-04-programs/hello.py`
- Mission documentation: `mission-04-programs/README.md`
- Terminal execution output: `Hello from Python`

## 8. Commit details
- **Commit message**: `Compare compilers and interpreters`
- **Branch**: `main`
- **Push status**: Verified and pushed to GitHub
