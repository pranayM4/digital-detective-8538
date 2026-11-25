# Mission 1 — Know Your Computer

## 1. Task / objective
The objective of this mission is to understand and demonstrate how a computer system operates using the Input-Processing-Output-Storage (IPOS) model. This involves tracing a concrete everyday computer task across each IPOS stage, identifying and categorizing computer hardware and software (operating system, application, and utility), and exploring dedicated computer-based embedded systems encountered in daily life.

## 2. Work completed
- Traced the complete lifecycle of writing, executing, and saving a Python script across the four IPOS stages.
- Created a hardware and software classification table covering five hardware components and five distinct software tools categorized by software type.
- Analyzed three real-world embedded computer systems (ATM, Smart Traffic Controller, and Automated Metro Fare Gate), documenting their core function, primary input sensor/device, and primary output actuator/display.
- Documented all conceptual explanations and real-world examples in this mission README.

## 3. Commands / tools used
- Text Editor / VS Code: Used to author code and write Markdown documentation.
- macOS System Information (`About This Mac` / Terminal `system_profiler`): Referenced to identify physical hardware components such as Apple Silicon M-series processor, unified RAM, and NVMe SSD.
- Git: Used to track and stage documentation changes.

## 4. My understanding

### Task 1.1 — Tracing an Activity Using the IPOS Cycle

**Selected Activity:** Writing a Python program (`hello.py`), executing it in Terminal, and saving it to disk.

| Stage | What happens in your example? | Possible hardware / component |
|:---|:---|:---|
| **Input** | I press keys on the physical keyboard to type Python code into the editor, and click the mouse/trackpad to initiate saving or running. | Keyboard, Trackpad |
| **Processing** | The Central Processing Unit (CPU) receives the keypress scan codes, coordinates with the operating system to render the text in RAM, compiles/interprets the Python code instructions into machine commands, and executes logic. | CPU (Apple Silicon M-series), Unified RAM (Memory) |
| **Output** | The editor displays the typed characters in real time, and the Terminal prints the executed script's stdout (`Hello from Python`) onto the screen. | Liquid Retina Display (Built-in Screen) |
| **Storage** | The source code file is saved as persistent non-volatile bytes onto the internal solid-state drive so the file remains intact after the computer is shut down. | Internal NVMe SSD (Apple APFS file system) |

#### How the activity moves from input to output and storage:
1. **Input Phase:** Keypress signals are sent from the keyboard controller to the operating system's device driver as hardware interrupts.
2. **Processing Phase:** The OS forwards these events to the active text editor process stored in RAM. The CPU updates the document buffer in memory and prepares the graphics buffer.
3. **Output Phase:** The GPU/display controller reads the framebuffer from RAM and renders the visible glyphs on the screen at 60Hz/120Hz.
4. **Storage Phase:** When the save command (`Cmd + S`) is triggered, the CPU directs the filesystem driver to write the contents of the memory buffer onto permanent flash memory blocks on the SSD.

---

### Task 1.2 — Hardware and Software Classification

Hardware refers to the physical, tangible electronic and mechanical parts of a computer. Software refers to the set of programs, data, and instructions that tell the hardware how to perform tasks.

| Item / Software Name | Hardware or Software? | Software Type (if applicable) | Purpose |
|:---|:---|:---|:---|
| **Keyboard** | Hardware | Not applicable | Input peripheral used to type text, commands, and shortcuts into the system. |
| **Internal SSD** | Hardware | Not applicable | Non-volatile flash storage used to retain OS files, programs, and user data permanently. |
| **CPU (Central Processing Unit)** | Hardware | Not applicable | Executes instructions, performs arithmetic and logic calculations, and coordinates hardware components. |
| **Unified RAM (Memory)** | Hardware | Not applicable | Fast volatile storage that holds running programs and active data for immediate CPU access. |
| **macOS (Operating System)** | Software | Operating System | Manages computer hardware resources, manages memory and processes, and provides a platform for applications. |
| **Visual Studio Code** | Software | Application Software | A code editor that helps users write, edit, and debug program code. |
| **Google Chrome** | Software | Application Software | A web browser that retrieves and displays web pages from the internet. |
| **macOS Terminal** | Software | Utility Software | Provides a text-based command-line interface for direct communication with the operating system shell. |
| **Activity Monitor** | Software | Utility Software | System management utility used to view CPU usage, active processes, memory pressure, and disk activity. |

---

### Task 1.3 — Computer Systems Around You

Computers exist in many specialized forms beyond general-purpose laptops and smartphones:

| System | Main Purpose | One Input | One Output |
|:---|:---|:---|:---|
| **Automated Teller Machine (ATM)** | Allows bank customers to securely withdraw cash, check account balances, and deposit money without a human teller. | Keypad / Touchscreen (PIN and amount entry) or Magnetic Card Reader | Motorized Cash Dispenser, Receipt Printer, and Transaction Display |
| **Smart City Traffic Light Controller** | Automatically controls traffic flow at intersections based on real-time road conditions. | In-road inductive vehicle loop sensors or optical traffic camera feeds | Switched Signal Lights (Red, Yellow, Green LED lamps) |
| **Metro Automated Fare Collection (AFC) Gate** | Validates passenger transit tickets/cards and manages entry and exit to subway stations. | RFID / NFC Contactless Smart Card Reader | Mechanical Flap/Turnstile Barrier Actuator and LCD/Buzzer validation signal |

---

## 5. Difficulties faced
When classifying system software, it was initially easy to confuse utility software (such as Terminal or Activity Monitor) with general application software, because users interact directly with both through windows and graphical interfaces.

## 6. How I resolved them
I reviewed the core definition: application software is focused on accomplishing user-specific end tasks (like writing an essay or playing a video), whereas utility software is dedicated to maintaining, diagnosing, managing, or interacting with the computer system itself.

## 7. Evidence / files
- Mission documentation: `mission-01-computer-basics/README.md`
- Completed IPOS breakdown table (Task 1.1)
- Hardware and software classification table (Task 1.2)
- Everyday embedded computing systems table (Task 1.3)

## 8. Commit details
- **Commit message**: `Complete computer basics and IPOS mission`
- **Branch**: `main`
- **Push status**: Verified and pushed to GitHub
