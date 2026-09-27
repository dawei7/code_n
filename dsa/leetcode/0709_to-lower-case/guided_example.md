# Guided Example: To Lower Case

We trace the step-by-step ASCII character code evaluation ($\text{ord}(c)$), uppercase character range classification ($c \in ['A', 'Z'] \iff 65 \le \text{ord}(c) \le 90$), bitwise bit-5 activation ($\text{ord}(c) \mid 32$), ASCII offset addition ($\text{ord}(c) + 32$), non-alphabetic character preservation, and lowercase string synthesis on representative character sequences:

- **Input:** $s = \text{"Hello"}$
- **Required output:** `"hello"`
  - Transformation specifications:
    - Convert every uppercase English letter ($'A'$ through $'Z'$) to its corresponding lowercase English letter ($'a'$ through $'z'$).
    - All other characters (lowercase letters, digits, punctuation, whitespace) must remain completely unaltered.
    - For $s = \text{"Hello"}$:
      - Character $'H'$ is uppercase $\implies$ converts to $'h'$.
      - Characters $'e', 'l', 'l', 'o'$ are already lowercase $\implies$ remain unchanged.
      - Output is `"hello"`.
- **ASCII Character Encoding & Bitwise Invariant:**
  - **The ASCII Encoding Relationship:**
    - Standard ASCII assigns consecutive integer codes to the English alphabet:
      - Uppercase alphabet: $'A' \to 65, \; 'B' \to 66, \; \dots, \; 'Z' \to 90$.
      - Lowercase alphabet: $'a' \to 97, \; 'b' \to 98, \; \dots, \; 'z' \to 122$.
    - Observe the constant numerical distance between case counterparts:
      $$
      \text{ord}('a') - \text{ord}('A') = 97 - 65 = \mathbf{32}
      $$
  - **The Bit-5 Masking Invariant ($2^5 = 32$):**
    - Inspect the 7-bit binary representations of uppercase and lowercase letters:
      - $'A' = 65 = \mathbf{0}1000001_2$
      - $'a' = 97 = \mathbf{0}1\mathbf{1}00001_2$
      - $'H' = 72 = \mathbf{0}1001000_2$
      - $'h' = 104 = \mathbf{0}1\mathbf{1}01000_2$
    - Notice that bit 5 (value $32 = 00100000_2$) is **0** for all uppercase letters and **1** for all lowercase letters. All other 6 bits are identical!
    - Setting bit 5 transforms any uppercase letter into its lowercase equivalent:
      $$
      \text{ord}(c_{lower}) = \text{ord}(c_{upper}) \mid 32
      $$
  - **Transformation Function:**
    $$
    f(c) = \begin{cases} \text{chr}(\text{ord}(c) \mid 32) & \text{if } 'A' \le c \le 'Z' \\ c & \text{otherwise} \end{cases}
    $$
- **Step-by-Step Worked Execution Trace on $s = \text{"Hello"}$ ($N = 5$):**
  - **Character 0 ($s[0] = \text{'H'}$):**
    - ASCII code: $\text{ord}('H') = 72$.
    - Range check: $65 \le 72 \le 90 \implies \mathbf{Uppercase\ Letter!}$
    - Apply bitwise OR with 32:
      $$
      72 \mid 32 = 01001000_2 \mid 00100000_2 = 01101000_2 = \mathbf{104}
      $$
    - Character conversion: $\text{chr}(104) = \mathbf{'h'}$.
    - Output stream accumulates: `['h']`.
  - **Character 1 ($s[1] = \text{'e'}$):**
    - ASCII code: $\text{ord}('e') = 101$.
    - Range check: $101 > 90 \implies$ Not uppercase.
    - Preserved unaltered: $'e'$.
    - Output stream accumulates: `['h', 'e']`.
  - **Character 2 ($s[2] = \text{'l'}$):**
    - ASCII code: $\text{ord}('l') = 108$.
    - Range check: Not uppercase.
    - Preserved unaltered: $'l'$.
    - Output stream accumulates: `['h', 'e', 'l']`.
  - **Character 3 ($s[3] = \text{'l'}$):**
    - Preserved unaltered: $'l'$.
    - Output stream accumulates: `['h', 'e', 'l', 'l']`.
  - **Character 4 ($s[4] = \text{'o'}$):**
    - ASCII code: $\text{ord}('o') = 111$.
    - Preserved unaltered: $'o'$.
    - Output stream accumulates: `['h', 'e', 'l', 'l', 'o']`.
  - **Step 6: Concatenate Output String:**
    $$
    ans = \mathbf{\text{"hello"}}
    $$
- **All Uppercase Trace ($s = \text{"LOVELY"}$):**
  - $'L' (76) \to 76 \mid 32 = 108 \to 'l'$
  - $'O' (79) \to 79 \mid 32 = 111 \to 'o'$
  - $'V' (86) \to 86 \mid 32 = 118 \to 'v'$
  - $'E' (69) \to 69 \mid 32 = 101 \to 'e'$
  - $'L' (76) \to 76 \mid 32 = 108 \to 'l'$
  - $'Y' (89) \to 89 \mid 32 = 121 \to 'y'$
  - Result: `"lovely"`.
- **Special Characters and Digits ($s = \text{"Hello, World! 123"}$):**
  - Comma `','` ($44$), space `' '` ($32$), and digits `'1', '2', '3'` are outside $[65, 90]$ and remain untouched.
  - Result: `"hello, world! 123"`.

This instance demonstrates low-level character encoding manipulation and bitwise bit-plane projection, mathematically proves why bit-5 disjunction performs a uniform translation between Latin case alphabets, and derives $O(N)$ execution time and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a string $s$:
Convert all **uppercase letters** to **lowercase letters**.
Non-uppercase characters remain unchanged.

```text
s = "Hello"

Index 0: 'H' (ASCII 72) -> uppercase -> 72 | 32 = 104 ('h')
Index 1: 'e' (ASCII 101) -> lowercase -> keep 'e'
Index 2: 'l' (ASCII 108) -> lowercase -> keep 'l'
Index 3: 'l' (ASCII 108) -> lowercase -> keep 'l'
Index 4: 'o' (ASCII 111) -> lowercase -> keep 'o'

Result: "hello"
```

### The Invariant of ASCII Bit 5
- The difference between lowercase and uppercase Latin letters is exactly $32 = 2^5$.
- Setting bit 5 (`ord(c) | 32`) or adding 32 converts any uppercase character to its lowercase counterpart.

---

## 2. Conceptual Foundation & Invariants

### 1. ASCII Interval Classification:
$$
\text{is\_upper}(c) \iff 65 \le \text{ord}(c) \le 90
$$

### 2. Bitwise Case Conversion:
$$
c_{lower} = \begin{cases} \text{chr}(\text{ord}(c) \mid 32) & \text{if } \text{is\_upper}(c) \\ c & \text{otherwise} \end{cases}
$$

> **Affine Monoid Homomorphism Invariant.** The case projection operator $\pi: \Sigma^* \to \Sigma^*$ acts element-wise via the bitwise affine shift $\pi(x) = x \lor 00100000_2$ restricted to the sub-alphabet $[65, 90]$, preserving string length and word monoid structure.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"Hello"}$:

---

### Step 1: Character 'H'
- $\text{ord}('H') = 72 \in [65, 90]$.
- $72 \mid 32 = 104 \implies \text{'h'}$.

---

### Step 2: Characters 'e', 'l', 'l', 'o'
- Not in $[65, 90] \implies$ kept as `'e', 'l', 'l', 'o'`.

---

### Step 3: Combine
- **`"hello"`**.

---

## 4. Complete Execution Trace

| Index | Character $c$ | ASCII Code | In Range $[65, 90]$? | Bitwise OR ($code \mid 32$) | Transformed Character |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | `'H'` | $72$ | **Yes (Uppercase)** | $72 \mid 32 = 104$ | **`'h'`** |
| $1$ | `'e'` | $101$ | No | — | `'e'` |
| $2$ | `'l'` | $108$ | No | — | `'l'` |
| $3$ | `'l'` | $108$ | No | — | `'l'` |
| $4$ | `'o'` | $111$ | No | — | `'o'` |
| **Output** | — | — | — | — | **`"hello"`** |

---

## 5. Boundary Cases & Failure Modes

- **Already All Lowercase ($s = \text{"here"}$):** Returns unchanged `"here"`.
- **All Uppercase ($s = \text{"LOVELY"}$):** Every character converts $\implies$ `"lovely"`.
- **Numbers and Symbols ($s =$ `"123!@#"`):** Unaltered.
- **Empty String ($s = \text{""}$):** Returns empty string `""`.

---

## 6. Traps & Common Anti-Patterns

- **Unconditional `ord(c) | 32`:** Applying `ord(c) | 32` to characters outside $[65, 90]$ corrupts symbols (e.g. `'@'` is 64, $64 \mid 32 = 96 =$ ``'` ``). Always check $65 \le \text{ord}(c) \le 90$ before applying the bitmask.
- **Repeated String Concatenation (`res += c`):** In immutable string languages, repeated concatenation creates $O(N^2)$ memory copies. Use a list join `"".join(...)` for linear $O(N)$ performance.
- **Locale Dependency:** The problem uses standard English ASCII ($'A' \dots 'Z'$). Avoid locale-specific case transformations that alter non-Latin characters.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - One pass through the string $s$ of length $N$: $\mathcal{O}(N)$.
  - Each character undergoes constant time $O(1)$ bitwise operations.
  - Total Time: strictly linear $\mathcal{O}(N)$. Completes in $< 0.1$ ms for $N = 100$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space to build the transformed output string.
