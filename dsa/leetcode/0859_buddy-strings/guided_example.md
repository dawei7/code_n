# Guided Example: Buddy Strings

We trace the step-by-step length verification, character frequency conservation, positional mismatch counting, transposition parity invariants, and pigeonhole duplicate detection on representative string pairs:

- **Input:**
  $$
  s = \text{"ab"}, \quad goal = \text{"ba"}
  $$
- **Required output:** `true`
  - Buddy string definition:
    - We must swap **exactly one pair of distinct indices** $(i, j)$ with $i \ne j$ in string $s$.
    - The resulting string must be strictly identical to $goal$.
    - For $s = \text{"ab"}$ and $goal = \text{"ba"}$:
      - Swap indices $0$ and $1$: $s[0]$ ('a') and $s[1]$ ('b') swap places.
      - Transformed string becomes $\text{"ba"}$.
      - Matches $goal$ identically!
      - Result: **`true`**.
- **The Two-Path Transposition Invariant:**
  - **Length Conservation:**
    - If $|s| \ne |goal|$, a swap cannot alter string length $\implies \mathbf{false}$.
  - **Character Multiset Invariant:**
    - Swapping only permutes characters without introducing or destroying letters.
    - If the multiset of characters in $s$ does not match $goal$, no swap can ever make them equal $\implies \mathbf{false}$.
  - **Case 1: $s \ne goal$ (Non-Identical Strings):**
    - A single swap alters characters at exactly **two positions**.
    - Therefore, the number of mismatch indices where $s[i] \ne goal[i]$ must be **exactly $2$**.
    - Let the two mismatch indices be $i$ and $j$.
    - We must have $s[i] == goal[j]$ and $s[j] == goal[i]$.
  - **Case 2: $s == goal$ (Already Identical Strings):**
    - A swap is **mandatory**; we cannot choose to skip the operation.
    - To swap two distinct positions $i \ne j$ without altering the string, we must swap two positions that contain the **exact same character** ($s[i] == s[j]$).
    - By the Pigeonhole Principle, this is possible if and only if at least one character appears with frequency $\ge 2$ in $s$!

---

## 1. Instance & Teaching Goal

Given strings $s = \text{"ab"}$ and $goal = \text{"ba"}$, decide if a single transposition transforms $s$ into $goal$.

```text
String s:    a  b
Goal:        b  a
Index:       0  1
Mismatch:    *  *  (Count = 2)

Indices of mismatch: [0, 1]
Cross-equality check:
  s[0] ('a') == goal[1] ('a')  -> Match!
  s[1] ('b') == goal[0] ('b')  -> Match!

Valid single transposition exists!
Output: true
```

The teaching goal is to contrast the two distinct structural requirements: resolving two misplaced characters versus absorbing a mandatory swap into identical duplicates.

---

## 2. Conceptual Foundation & Invariants

### 1. Hamming Distance Partition:
Let $D(s, goal) = \sum_{i=0}^{n-1} \mathbb{I}[s[i] \ne goal[i]]$.
A single transposition changes at most two positions:
$$
D(s, goal) \in \{0, 2\}
$$
- If $D = 0$: Valid $\iff \exists c \in \Sigma : \text{count}(c) \ge 2$.
- If $D = 2$: Valid $\iff (s[i] == goal[j] \land s[j] == goal[i])$ where $i, j$ are the two mismatch indices.
- If $D \notin \{0, 2\}$: Valid $\iff \mathbf{false}$.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"ab"}$ and $goal = \text{"ba"}$:

---

### Step 1: Length Validation
- $|s| = 2$.
- $|goal| = 2$.
- Both lengths equal $2$. Proceed.

---

### Step 2: Frequency Count Check
- Frequencies of $s$: $\{'a': 1, 'b': 1\}$.
- Frequencies of $goal$: $\{'a': 1, 'b': 1\}$.
- Multisets are identical. Proceed.

---

### Step 3: Positional Comparison
- **Index 0:**
  - $s[0] = \text{'a'}, \quad goal[0] = \text{'b'}$.
  - $s[0] \ne goal[0] \implies$ **Mismatch 1 at index 0**.
- **Index 1:**
  - $s[1] = \text{'b'}, \quad goal[1] = \text{'a'}$.
  - $s[1] \ne goal[1] \implies$ **Mismatch 2 at index 1**.
- Total mismatch count: $diff = 2$.

---

### Step 4: Transposition Feasibility Check
- Because $diff = 2$ and multiset frequencies match:
  $$
  s[0] == goal[1] = \text{'a'} \quad \text{and} \quad s[1] == goal[0] = \text{'b'}
  $$
- Swapping indices $0$ and $1$ in $s$ yields $\text{"ba"} == goal$.
- **Return: `true`**.

---

## 4. Complete Execution Trace Across Archetypes

| String $s$ | String $goal$ | Length Match? | Frequency Match? | Mismatches ($diff$) | Mismatch Indices | Duplicate Char Exists? | Result |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **`"ab"`** | **`"ba"`** | Yes ($2$) | Yes | **$2$** | $[0, 1]$ | No | **`true`** |
| `"ab"` | `"ab"` | Yes ($2$) | Yes | $0$ | $[\,]$ | No (all unique) | **`false`** |
| `"aa"` | `"aa"` | Yes ($2$) | Yes | $0$ | $[\,]$ | Yes (`'a'` count 2) | **`true`** |
| `"aaaaaaabc"` | `"aaaaaaacb"` | Yes ($9$) | Yes | **$2$** | $[7, 8]$ | Yes | **`true`** |
| `"abcd"` | `"badc"` | Yes ($4$) | Yes | $4$ | $[0, 1, 2, 3]$ | No | **`false`** |

---

## 5. Boundary Cases & Failure Modes

- **$s == goal$ with All Unique Characters (e.g. `"ab"`, `"ab"`):** A swap is mandatory. Swapping the only two letters turns `"ab"` into `"ba" \ne "ab"$. Must return `false`.
- **$s == goal$ with Duplicate Characters (e.g. `"aa"`, `"aa"`):** Swapping index $0$ and index $1$ (both `'a'`) leaves the string unchanged. Returns `true`.
- **Single Mismatch ($diff = 1$):** Mathematically impossible between two strings of identical character frequencies; if one position differs, another must also differ.
- **Different Lengths:** Immediate early exit `false`.

---

## 6. Traps & Common Anti-Patterns

- **Assuming $s == goal$ Always Returns True:** Forgetting that a swap must be physically executed. If all characters are unique, no valid swap preserves equality.
- **Brute-Force $\mathcal{O}(N^2)$ Pair Swapping:** Generating all $\binom{N}{2}$ strings and checking equality takes $\mathcal{O}(N^3)$ time, failing on $N = 2 \times 10^4$. Single-pass counting takes $\mathcal{O}(N)$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Length check: $\mathcal{O}(1)$.
  - Single pass to count character frequencies and mismatch positions: $\mathcal{O}(N)$.
  - Alphabet size $|\Sigma| = 26$.
  - Total Time: $\mathcal{O}(N)$, completing in $< 1$ ms for $N = 2 \times 10^4$.
- **Auxiliary Space Complexity:**
  - Frequency table for 26 lowercase English letters: $\mathcal{O}(|\Sigma|) = \mathcal{O}(1)$ space.
