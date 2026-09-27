# Guided Example: Validate IP Address

We trace the step-by-step structural delimiter dispatch (`.` vs `:`), IPv4 4-octet numerical parsing (decimal digits, range $[0, 255]$, leading zero prohibition), IPv6 8-hextet hexadecimal verification ($1 \le |t| \le 4$, hex alphabet), and invalid pattern rejection on representative network address strings:

- **Input:** $queryIP = \text{"172.16.254.1"}$
- **Required output:** `"IPv4"`
  - Delimiter inspection: contains `.` and does not contain `:` $\implies$ Test IPv4 grammar
  - **IPv4 Octet Parsing (Split on `.`):**
    - Total parts: $4$ (`["172", "16", "254", "1"]`)
    - Part 1 (`"172"`): length 3, no leading zero, digits only, value $172 \in [0, 255]$ (**Valid**)
    - Part 2 (`"16"`): length 2, no leading zero, digits only, value $16 \in [0, 255]$ (**Valid**)
    - Part 3 (`"254"`): length 3, no leading zero, digits only, value $254 \in [0, 255]$ (**Valid**)
    - Part 4 (`"1"`): length 1, no leading zero, digits only, value $1 \in [0, 255]$ (**Valid**)
    - All 4 octets satisfy all constraints $\implies$ Return **`"IPv4"`**
- **Valid IPv6 Instance:** $queryIP = \text{"2001:0db8:85a3:0:0:8A2E:0370:7334"}$
  - Split on `:` $\implies$ exactly 8 tokens
  - Each token has length between $1$ and $4$
  - Each character belongs to the hexadecimal set $\{0 \dots 9, a \dots f, A \dots F\}$
  - Return **`"IPv6"`**
- **Out of Range Instance:** $queryIP = \text{"256.256.256.256"}$
  - Value $256 > 255 \implies$ Return **`"Neither"`**
- **Leading Zero Rejection Instance:** $queryIP = \text{"192.168.01.1"}$
  - Octet `"01"` has length $> 1$ with leading `'0'` $\implies$ Forbidden $\implies$ Return **`"Neither"`**

This instance demonstrates syntactic tokenization and protocol validation, mathematically proves why strict delimiter and numerical boundary checks prevent parsing ambiguities, and derives $O(N)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a string $queryIP$:
Determine whether it is a valid **IPv4** address, a valid **IPv6** address, or **Neither**:
- **IPv4 Specification:**
  - Form: $x_1.x_2.x_3.x_4$ (exactly 4 decimal octets separated by single dots).
  - Each $x_i$ is an integer in $[0, 255]$.
  - No leading zeros (e.g. `"0"` is allowed, but `"01"` and `"00"` are invalid).
  - Only decimal digits allowed (no sign characters, letters, or spaces).
- **IPv6 Specification:**
  - Form: $y_1:y_2:y_3:y_4:y_5:y_6:y_7:y_8$ (exactly 8 hexadecimal hextets separated by single colons).
  - Each $y_i$ has length between $1$ and $4$.
  - Only hexadecimal characters allowed ($0 \dots 9, a \dots f, A \dots F$).
  - Leading zeros are allowed, but extra delimiters or empty fields are invalid.

```text
IPv4 Grammar:
  "172.16.254.1"
   |___| |__| |___| |_|
     4 decimal octets, each in [0, 255], no leading zeros -> "IPv4"

IPv6 Grammar:
  "2001:0db8:85a3:0:0:8A2E:0370:7334"
   8 hexadecimal blocks of 1-4 chars -> "IPv6"
```

---

## 2. Conceptual Foundation & Invariants

### 1. The IPv4 Validator Pipeline:
Split string by dot `.` into array $ss$:
1. **Octet Count:** $|ss| == 4$.
2. **Leading Zero Rule:** For each token $t$:
   $$
   |t| > 1 \implies t[0] \ne \text{'0'}
   $$
3. **Digit & Range Rule:**
   - Every character in $t$ must be a decimal digit (`t.isdigit()`).
   - Numerical value must satisfy:
     $$
     0 \le \text{int}(t) \le 255
     $$

### 2. The IPv6 Validator Pipeline:
Split string by colon `:` into array $ss$:
1. **Hextet Count:** $|ss| == 8$.
2. **Length Rule:** For each token $t$:
   $$
   1 \le |t| \le 4
   $$
3. **Hexadecimal Character Set Rule:**
   Every character $c \in t$ must satisfy:
   $$
   c \in \{0, 1, \dots, 9, a, b, c, d, e, f, A, B, C, D, E, F\}
   $$

> **Delimiter Mutuality.** An IPv4 address cannot contain colons, and an IPv6 address cannot contain dots. Verifying the delimiter partitions the validator into two mutually exclusive branches.

---

## 3. Step-by-Step Worked Execution

We trace $queryIP = \text{"172.16.254.1"}$:

---

### Step 1: Delimiter Branching
- String contains `.`, does not contain `:`: Test IPv4.

---

### Step 2: IPv4 Token Validation
Split on `.`: $ss = [\text{"172"}, \; \text{"16"}, \; \text{"254"}, \; \text{"1"}]$.
Check count: $|ss| = 4$ (**Pass**).

- **Token 1: `"172"`**
  - Length check: $3 > 1$. First character: `'1'` $\ne$ `'0'` (No leading zero: Pass).
  - Digit check: `"172".isdigit()` (Pass).
  - Range check: $172 \in [0, 255]$ (Pass).
- **Token 2: `"16"`**
  - Length check: $2 > 1$. First character: `'1'` $\ne$ `'0'` (Pass).
  - Digit check: `"16".isdigit()` (Pass).
  - Range check: $16 \in [0, 255]$ (Pass).
- **Token 3: `"254"`**
  - Length check: $3 > 1$. First character: `'2'` $\ne$ `'0'` (Pass).
  - Digit check: `"254".isdigit()` (Pass).
  - Range check: $254 \in [0, 255]$ (Pass).
- **Token 4: `"1"`**
  - Length check: $1 \ngtr 1$ (Pass).
  - Digit check: `"1".isdigit()` (Pass).
  - Range check: $1 \in [0, 255]$ (Pass).

---

### Step 3: Conclusion
All 4 tokens satisfy all IPv4 grammar rules.
Return **`"IPv4"`**.

---

## 4. Complete Execution Trace

| Test Address | Candidate Protocol | Delimiter Tokens | Token Validations | Result |
|:---:|:---:|:---:|:---|:---:|
| `"172.16.254.1"` | IPv4 | 4 parts | All in $[0, 255]$, no leading zero | **`"IPv4"`** |
| `"2001:0db8:...:7334"` | IPv6 | 8 parts | All lengths in $[1, 4]$, valid hex | **`"IPv6"`** |
| `"256.256.256.256"` | IPv4 | 4 parts | $256 > 255$ fails range | **`"Neither"`** |
| `"192.168.01.1"` | IPv4 | 4 parts | `"01"` has illegal leading zero | **`"Neither"`** |
| `"2001:0db8::85a3"` | IPv6 | 3 parts (`::` splits to empty) | $\lvert ss \rvert = 3 \ne 8$ | **`"Neither"`** |
| `"1.1.1.1."` | IPv4 | 5 parts (trailing dot) | $\lvert ss \rvert = 5 \ne 4$ | **`"Neither"`** |

---

## 5. Boundary Cases & Failure Modes

- **Trailing / Leading Delimiters (`"1.1.1.1."` or `":2001:..."`):** Splitting preserves empty tokens, causing part count to be 5 or 9 $\implies \mathbf{\text{"Neither"}}$.
- **Signs (+/-):** Input `"172.16.254.+1"` is not pure digits $\implies \mathbf{\text{"Neither"}}$.
- **Case Sensitivity in IPv6:** Characters `'a'` through `'f'` are allowed in both uppercase and lowercase.
- **Single Zero in IPv4 (`"192.168.0.1"`):** Octet `"0"` has length 1. Condition `len(t) > 1 and t[0] == '0'` does not trigger, correctly accepting single zeros.

---

## 6. Traps & Common Anti-Patterns

- **Using Built-in Socket Libraries (`inet_aton`):** In some programming languages, `inet_aton` treats `"192.168.01.1"` as octal and parses `"127.1"` as valid IPv4 shorthand. The problem strictly enforces RFC dotted-quad and colon-hexadecimal standards.
- **Allowing IPv6 Zero Compression (`::`):** Real-world IPv6 allows `::` to omit sequences of zeros. The LeetCode problem specification strictly requires all 8 hextets to be explicitly written.
- **Integer Parsing Exception Crashes:** Calling `int(t)` without verifying `t.isdigit()` throws runtime exceptions on inputs like `"1a.2.3.4"`. Always guard parsing with digit checks.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Splitting the string of length $N \le 50$ takes $O(N)$ time.
  - Character checks and integer conversion take $O(N)$ time.
  - Total Time: $\mathcal{O}(N)$. Completes in $< 1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space to store the parsed tokens.
