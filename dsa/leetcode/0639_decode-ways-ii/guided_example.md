# Guided Example: Decode Ways II

We trace the step-by-step wildcard alphabet expansion ($* \in [1, 9]$), single-digit decoding branch multipliers ($1 \to 9$), two-digit boundary classification ($10 \le \text{pair} \le 26$), joint wildcard pairing combinatorial explosion ($** \to 15$ combinations), rolling dynamic programming state transitions ($dp[i-2], dp[i-1] \to dp[i]$), and modulo $10^9 + 7$ arithmetic on representative wildcard string messages:

- **Input:** $s = \text{"1*"}$
- **Required output:** `18`
  - Encoding rules:
    - `'A'` through `'Z'` are encoded as numbers $1$ through $26$.
    - The wildcard character `'*'` can represent **any digit from $1$ to $9$** (note: `'*'` can never represent `'0'`).
  - Decoding options for string `"1*"`:
    1. **Decoded as two separate single digits:**
       - First character `'1'` decodes to `'A'`.
       - Second character `'*'` can be any digit $1 \dots 9$, decoding to `'A'` through `'I'` ($9$ distinct outcomes: `AA`, `AB`, ..., `AI`).
    2. **Decoded as a single combined two-digit number:**
       - The pair `"1*"` can be any integer in the range $11 \dots 19$.
       - All 9 numbers $11 \dots 19$ are valid letters ($'K'$ through $'S'$), giving $9$ additional distinct outcomes.
    - Total valid decodings:
      $$
      9 + 9 = \mathbf{18}
      $$
- **Wildcard Combinatorial Transition Matrix:**
  - Let $dp[i]$ be the number of valid decodings for the prefix of length $i$.
  - Every step computes $dp[i]$ as the sum of **1-digit decodings** using $s[i-1]$ plus **2-digit decodings** using $s[i-2 \dots i-1]$:
  - **1-Digit Transition ($s[i-1]$ alone, scaled by $dp[i-1]$):**
    - If $s[i-1] == \text{'*'}\text{:}$ Can be digits $1 \dots 9 \implies \mathbf{9 \times dp[i-1]}$.
    - If $s[i-1] \in [\text{'1'}, \text{'9'}]\text{:}$ Exactly one letter $\implies \mathbf{1 \times dp[i-1]}$.
    - If $s[i-1] == \text{'0'}\text{:}$ `'0'` cannot decode alone $\implies \mathbf{0}$.
  - **2-Digit Transition ($s[i-2 \dots i-1]$ pair, scaled by $dp[i-2]$):**
    - **Case A: Both are wildcards (`"**"`):**
      - First star can be $1$ ($11 \dots 19 \implies 9$ options) or $2$ ($21 \dots 26 \implies 6$ options).
      - Total valid pairings: $9 + 6 = \mathbf{15 \times dp[i-2]}$.
    - **Case B: First is wildcard, second is digit (`"*D"`):**
      - If $D \le 6$: can prefix with $1$ ($1D \le 16$) or $2$ ($2D \le 26$) $\implies \mathbf{2 \times dp[i-2]}$.
      - If $D > 6$: can only prefix with $1$ ($17, 18, 19$) because $27 > 26 \implies \mathbf{1 \times dp[i-2]}$.
    - **Case C: First is digit, second is wildcard (`"D*"`):**
      - If $D == \text{'1'}$: can form $11 \dots 19 \implies \mathbf{9 \times dp[i-2]}$.
      - If $D == \text{'2'}$: can form $21 \dots 26 \implies \mathbf{6 \times dp[i-2]}$.
      - If $D \ge \text{'3'}$ or $D == \text{'0'}\text{:}$ No values $\le 26 \implies \mathbf{0}$.
    - **Case D: Neither is wildcard (`"D_1 D_2"`):**
      - If $10 \le int(D_1 D_2) \le 26 \implies \mathbf{1 \times dp[i-2]}$, else $\mathbf{0}$.
- **Step-by-Step Worked Execution Trace on $s = \text{"1*"}$:**
  - Initialize rolling variables:
    $$
    a = dp[0] = 1, \quad b = dp[1] = 0, \quad c = 0
    $$
  - **Step 1: Process Character 1 ($s[0] = \text{'1'}$):**
    - 1-digit decode of `'1'`:
      - `'1'` $\ne$ `'0'` and $\ne$ `'*'` $\implies c = 1 \times a = 1 \times 1 = \mathbf{1}$.
    - 2-digit decode: Not applicable ($i = 1$).
    - Advance rolling states:
      $$
      a \leftarrow 1 \quad (dp[0]), \quad b \leftarrow 1 \quad (dp[1])
      $$
  - **Step 2: Process Character 2 ($s[1] = \text{'*'}$):**
    - **Sub-step 1: Single-Digit Decode of $s[1]$ (`'*'`):**
      - $s[1] == \text{'*'} \implies$ can be any digit $1 \dots 9$.
      - Contribution from $dp[1]$ ($b = 1$):
        $$
        c_{single} = 9 \times b = 9 \times 1 = \mathbf{9}
        $$
    - **Sub-step 2: Two-Digit Decode of $s[0 \dots 1]$ (`"1*"`):**
      - $s[0] = \text{'1'}$ and $s[1] = \text{'*'}$.
      - Follows **Case C** with prefix `'1'`:
        - Can form all 9 numbers from $11$ to $19$.
        - All 9 numbers satisfy $11 \le x \le 19 \le 26$.
      - Multiplier: $9$.
      - Contribution from $dp[0]$ ($a = 1$):
        $$
        c_{pair} = 9 \times a = 9 \times 1 = \mathbf{9}
        $$
    - **Sub-step 3: Combine Contributions:**
      $$
      c = c_{single} + c_{pair} = 9 + 9 = \mathbf{18}
      $$
    - Update state: $a \leftarrow 1, \; b \leftarrow 18$.
  - **Step 3: Emit Final Answer:**
    $$
    ans = b = \mathbf{18}
    $$
- **Prefix with 2 Wildcards ($s = \text{"2*"}$):**
  - Single-digit: $9 \times 1 = 9$.
  - Two-digit `"2*"`: $21 \dots 26 \implies 6 \times 1 = 6$.
  - Total: $9 + 6 = \mathbf{15}$.
- **Double Wildcard ($s = \text{"**"}$):**
  - $dp[1] = 9$.
  - For $dp[2]$:
    - Single-digit: $9 \times dp[1] = 9 \times 9 = 81$.
    - Two-digit `"**"`: $15 \times dp[0] = 15 \times 1 = 15$.
    - Total: $81 + 15 = \mathbf{96}$.

This instance demonstrates grammar decomposition and dynamic programming under wildcard alphabet alphabets, mathematically proves why partitioning by single and double-character production rules covers all non-overlapping decodings, and derives $O(N)$ execution time and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a string $s$ containing digits and `'*'` wildcards:
Find the total number of valid decodings into letters `'A'`–`'Z'` ($1$–$26$) modulo $10^9 + 7$.
`'*'` represents any digit from $1$ to $9$.

```text
s = "1*"

Branch 1 (Two separate letters):
  '1' -> 'A'
  '*' -> 9 possibilities ('A' through 'I')
  Total = 1 * 9 = 9 ways

Branch 2 (One two-digit letter):
  "1*" -> numbers 11 through 19 (all valid: 'K' through 'S')
  Total = 9 ways

Overall Decodings = 9 + 9 = 18
```

### The Invariant of Character Multipliers
- In standard Decode Ways, transitions add either $1 \times dp[i-1]$ or $1 \times dp[i-2]$.
- With wildcards, the transitions become **weighted sums**:
  $$
  dp[i] = w_1 \cdot dp[i-1] + w_2 \cdot dp[i-2]
  $$
- The weights $w_1 \in \{0, 1, 9\}$ and $w_2 \in \{0, 1, 2, 6, 9, 15\}$ depend strictly on the local 2-character slice.

---

## 2. Conceptual Foundation & Invariants

### 1. The Multiplier Table:
| Slice Pattern | Sub-Cases | Weight $w_2$ |
|:---:|:---:|:---:|
| `"**"` | $11 \dots 19$ (9) and $21 \dots 26$ (6) | **15** |
| `"*D"` | $D \in [0, 6]$ $\implies 1D, 2D$ | **2** |
| `"*D"` | $D \in [7, 9]$ $\implies 1D$ only | **1** |
| `"1*"` | $11 \dots 19$ | **9** |
| `"2*"` | $21 \dots 26$ | **6** |
| `"[3-9]*"` | Exceeds 26 | **0** |
| `"D_1 D_2"` | $10 \le D_1 D_2 \le 26$ | **1** |

### 2. Recurrence Relation:
$$
dp[i] = (w_1 \cdot dp[i-1] + w_2 \cdot dp[i-2]) \pmod{10^9 + 7}
$$

> **Markovian Horizon Invariant.** Because valid letter encodings span at most 2 digits ($\le 26$), the probability mass of prefix $i$ depends exclusively on the previous two boundary states $dp[i-1]$ and $dp[i-2]$.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"1*"}$:

---

### Step 1: Base State
- $dp[0] = 1$.

---

### Step 2: First Character `'1'`
- Single digit: $w_1 = 1$.
- $dp[1] = 1 \times 1 = 1$.

---

### Step 3: Second Character `'*'`
- Single-digit on `'*'`: $w_1 = 9 \implies 9 \times dp[1] = 9$.
- Two-digit on `"1*"`: $w_2 = 9 \implies 9 \times dp[0] = 9$.
- Total $dp[2] = 9 + 9 = \mathbf{18}$.

---

### Step 4: Final Output
$$
\mathbf{18}
$$

---

## 4. Complete Execution Trace

| Position $i$ | Substring $s[i-1]$ | 1-Digit Multiplier $w_1$ | 1-Digit Term $w_1 \cdot b$ | 2-Digit Slice | 2-Digit Multiplier $w_2$ | 2-Digit Term $w_2 \cdot a$ | New $dp[i]$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | (Base) | — | — | — | — | — | $1$ |
| $1$ | `'1'` | $1$ | $1 \times 1 = 1$ | — | — | — | **$1$** |
| **$2$** | **`'*'`** | **$9$** | **$9 \times 1 = 9$** | **`"1*"`** | **$9$** | **$9 \times 1 = 9$** | **`18`** |
| **Final** | — | — | — | — | — | — | **`18`** |

---

## 5. Boundary Cases & Failure Modes

- **Leading Zero (`"0*"`):** $dp[1] = 0 \implies$ Entire chain evaluates to 0.
- **Single Wildcard (`"*"`):** $9 \times 1 = 9$.
- **Impossible Pair (`"3*"`):** $w_2 = 0 \implies$ only 1-digit decodings contribute.
- **Long Sequence ($10^5$ characters):** Modulo $10^9 + 7$ applied at every addition prevents integer overflow.

---

## 6. Traps & Common Anti-Patterns

- **Treating `'*'` as Zero:** The problem explicitly states that `'*'` can only represent digits $1$ through $9$, never $0$.
- **Assuming `"**"` Yields $9 \times 9 = 81$ Pairings:** While $9 \times 9 = 81$ is the total pairs of digits, only numbers $\le 26$ are valid letters ($11 \dots 19$ and $21 \dots 26$, totaling 15).
- **Allocating Full $O(N)$ Array When $O(1)$ Space Suffices:** Tracking 3 rolling variables ($a, b, c$) eliminates array overhead.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Single pass through string of length $N$.
  - At each index, evaluates a constant number of branch conditions and arithmetic products: $\mathcal{O}(1)$ time.
  - Total Time: strictly linear $\mathcal{O}(N)$. For $N = 10^5$, completes in $< 10$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ auxiliary space (only 3 integer variables).