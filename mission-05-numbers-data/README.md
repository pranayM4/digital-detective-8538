# Mission 5 — Numbers and Data

## 1. Task / objective
The objective of this mission is to master positional number systems (decimal, binary, hexadecimal), perform manual step-by-step conversions showing all intermediate calculations, verify them using Python's built-in conversion functions, build an interactive number converter program (`number_converter.py`), and analyze how characters and text are digitally represented using encoding standards (ASCII and UTF-8).

## 2. Work completed
- Worked through seven manual number conversions step-by-step using repeated division and weighted positional powers.
- Verified all manual mathematical results using Python's interactive functions (`bin()`, `hex()`, `int()`).
- Developed a clean, beginner-friendly Python program (`number_converter.py`) that accepts a decimal integer and outputs its binary and hexadecimal equivalents.
- Executed and validated `number_converter.py` against four distinct positive integers (`13`, `25`, `255`, `42`).
- Researched ASCII decimal and binary codes for uppercase `A` and lowercase `a`, explained the necessity of character encodings, and documented multi-byte characters in UTF-8.

## 3. Commands / tools used
- `python3`: Used to run `number_converter.py` and test mathematical expressions.
- `input()`: Built-in Python function that pauses execution and captures keyboard input from the user as a string.
- `int(value, [base])`: Converts numeric strings or floats into integer objects in base 10 (or a specified base like 2 or 16).
- `bin(number)`: Converts an integer into a binary string prefixed with `0b`.
- `hex(number)`: Converts an integer into a hexadecimal string prefixed with `0x`.
- `ord(char)`: Returns the integer Unicode/ASCII code point of a given character.

## 4. My understanding

### Task 5.1 — Manual Number Conversions

#### 1. Convert decimal 13 to binary ($13_{10} \rightarrow ?_2$)
We perform successive division by 2, recording each quotient and remainder until the quotient is 0:
- $13 \div 2 = 6$ with remainder **1** (Least Significant Bit - LSB)
- $6 \div 2 = 3$ with remainder **0**
- $3 \div 2 = 1$ with remainder **1**
- $1 \div 2 = 0$ with remainder **1** (Most Significant Bit - MSB)

Reading remainders from bottom to top: **$1101_2$**

---

#### 2. Convert decimal 25 to binary ($25_{10} \rightarrow ?_2$)
- $25 \div 2 = 12$ with remainder **1** (LSB)
- $12 \div 2 = 6$ with remainder **0**
- $6 \div 2 = 3$ with remainder **0**
- $3 \div 2 = 1$ with remainder **1**
- $1 \div 2 = 0$ with remainder **1** (MSB)

Reading remainders from bottom to top: **$11001_2$**

---

#### 3. Convert binary 1010 to decimal ($1010_2 \rightarrow ?_{10}$)
We calculate the sum of each bit multiplied by its positional weight ($2^n$):
$$\begin{aligned}
1010_2 &= (1 \times 2^3) + (0 \times 2^2) + (1 \times 2^1) + (0 \times 2^0) \\
&= (1 \times 8) + (0 \times 4) + (1 \times 2) + (0 \times 1) \\
&= 8 + 0 + 2 + 0 \\
&= \mathbf{10_{10}}
\end{aligned}$$

---

#### 4. Convert binary 1101 to decimal ($1101_2 \rightarrow ?_{10}$)
$$\begin{aligned}
1101_2 &= (1 \times 2^3) + (1 \times 2^2) + (0 \times 2^1) + (1 \times 2^0) \\
&= (1 \times 8) + (1 \times 4) + (0 \times 2) + (1 \times 1) \\
&= 8 + 4 + 0 + 1 \\
&= \mathbf{13_{10}}
\end{aligned}$$

---

#### 5. Convert hexadecimal A to decimal ($A_{16} \rightarrow ?_{10}$)
In base 16, digits $0$–$9$ represent values $0$–$9$, and letters $A$–$F$ represent values $10$–$15$.
$$A_{16} = (10 \times 16^0) = 10 \times 1 = \mathbf{10_{10}}$$

---

#### 6. Convert hexadecimal 1F to decimal ($1F_{16} \rightarrow ?_{10}$)
In hexadecimal, digit $1$ is at position $1$ ($16^1$) and digit $F$ (value 15) is at position $0$ ($16^0$):
$$\begin{aligned}
1F_{16} &= (1 \times 16^1) + (F \times 16^0) \\
&= (1 \times 16) + (15 \times 1) \\
&= 16 + 15 \\
&= \mathbf{31_{10}}
\end{aligned}$$

---

#### 7. Convert binary 1111 to hexadecimal ($1111_2 \rightarrow ?_{16}$)
Each hexadecimal digit corresponds exactly to a 4-bit binary group (nibble):
$$\begin{aligned}
1111_2 &= (1 \times 2^3) + (1 \times 2^2) + (1 \times 2^1) + (1 \times 2^0) \\
&= 8 + 4 + 2 + 1 = 15_{10}
\end{aligned}$$
Since $15_{10}$ in hexadecimal is represented by the letter $F$:
$$1111_2 = \mathbf{F_{16}}$$

---

### Task 5.2 — Python Verification Table

| Question / Problem | Expression Tested in Python | Python Output | Matches Manual Calculation? |
|:---|:---|:---|:---:|
| Decimal 13 to binary | `bin(13)` | `'0b1101'` | Yes ($1101_2$) |
| Decimal 25 to binary | `bin(25)` | `'0b11001'` | Yes ($11001_2$) |
| Binary 1010 to decimal | `int("1010", 2)` | `10` | Yes ($10_{10}$) |
| Binary 1101 to decimal | `int("1101", 2)` | `13` | Yes ($13_{10}$) |
| Hexadecimal A to decimal | `int("A", 16)` | `10` | Yes ($10_{10}$) |
| Hexadecimal 1F to decimal | `int("1F", 16)` | `31` | Yes ($31_{10}$) |
| Binary 1111 to hexadecimal | `hex(0b1111)` | `'0xf'` | Yes ($F_{16}$) |

*Note:* Python prefixes binary outputs with `0b` and hexadecimal outputs with `0x` to denote the base.

---

### Task 5.3 — Number Converter Program & Testing

The program `mission-05-numbers-data/number_converter.py` prompts the user for an integer, casts the string input to an integer via `int()`, and then utilizes `bin()` and `hex()` to produce representations.

#### Test Results Table

| Test Number (Input) | Binary Output | Hexadecimal Output | Verified |
|:---:|:---:|:---:|:---:|
| **13** | `0b1101` | `0xd` | Yes |
| **25** | `0b11001` | `0x19` | Yes |
| **255** | `0b11111111` | `0xff` | Yes |
| **42** | `0b101010` | `0x2a` | Yes |

#### Purpose of Functions:
- `input()`: Reads user keystrokes from standard input and returns them as a `str` datatype.
- `int()`: Parses the string into a numerical base-10 integer so arithmetic and bitwise representations can be calculated.
- `bin()`: Computes the base-2 binary equivalent of the integer and formats it with a leading `0b`.
- `hex()`: Computes the base-16 hexadecimal equivalent of the integer and formats it with a leading `0x`.

---

### Task 5.4 — Character Encoding and Text Storage

#### ASCII Codes for Uppercase and Lowercase Letters:
- **Uppercase 'A':** Decimal ASCII code **65** (Binary: `01000001`)
- **Lowercase 'a':** Decimal ASCII code **97** (Binary: `01100001`)
- *Pattern:* Lowercase `a` is exactly 32 greater than uppercase `A`. In binary, this represents a single bit change at position 5 ($2^5 = 32$), which allows computers to convert case simply by flipping a single bit.

#### Why Computers Need Encoding Standards:
Computers are physical electronic devices whose digital circuits only recognize binary electrical states (high and low voltage, represented as 0s and 1s). Because computers cannot natively store letters, symbols, or punctuation, an encoding standard establishes an agreed-upon lookup dictionary that maps each character to a unique numeric binary code.

#### Beyond Basic ASCII:
Basic ASCII uses 7 bits per character, limiting it to only 128 unique symbols ($0$ to $127$), which covers the English alphabet, numbers, and basic punctuation, but completely lacks support for non-Latin alphabets, currency symbols, and emojis.
- **Example character not in ASCII:** The Indian Rupee symbol **`₹`** (Unicode code point `U+20B9`).
- In UTF-8, `₹` is represented using 3 bytes: `0xE0 0x82 0xB9` (`11100010 10000010 10111001`), demonstrating how UTF-8 dynamically expands to encode symbols across all human languages.

---

## 5. Difficulties faced
When reading remainders during decimal-to-binary manual division, it is easy to accidentally record them from top to bottom (which would write the number backwards) instead of bottom to top.

## 6. How I resolved them
I reviewed the positional math rule: the first division produces the remainder for the $2^0$ unit column (least significant bit), while the final division produces the highest power of 2 (most significant bit). Therefore, reading from bottom to top guarantees correct place value ordering.

## 7. Evidence / files
- Python program: `mission-05-numbers-data/number_converter.py`
- Mission documentation: `mission-05-numbers-data/README.md`
- Manual calculation steps for 7 conversions
- Python verification table and 4 live program test cases

## 8. Commit details
- **Commit message**: `Build number converter and practise data representation`
- **Branch**: `main`
- **Push status**: Verified and pushed to GitHub
