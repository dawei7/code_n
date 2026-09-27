# Guided Example: Palindromic Substrings

We trace the step-by-step $2n - 1$ symmetry center indexing ($k \in [0, 2n - 2]$), odd-length (character-centered) and even-length (inter-character) bilateral radius expansion, character match propagation ($s[i] == s[j]$), early mismatch termination, and cumulative palindrome count aggregation on representative string instances:

- **Input:** $s = \text{"aaa"}$
- **Required output:** `6`
  - Problem definition: A palindromic substring is a contiguous sequence of characters that reads identically forward and backward ($s[p \dots q] = s[p \dots q]^R$).
  - Enumeration for `"aaa"`:
    - 3 length-1 substrings: `"a"` (at index 0), `"a"` (at index 1), `"a"` (at index 2)
    - 2 length-2 substrings: `"aa"` (indices 0..1), `"aa"` (indices 1..2)
    - 1 length-3 substring: `"aaa"` (indices 0..2)
    - Total: $3 + 2 + 1 = \mathbf{6}$.
- **Symmetry Center Expansion Architecture:**
  - Every palindrome is strictly symmetric around its center point:
    - **Odd-length palindromes** have a center on a single character ($c = i$).
      - e.g. `"aba"` centered at `'b'`.
      - There are $n$ such centers.
    - **Even-length palindromes** have a center located *between* two adjacent characters ($c = i + 0.5$).
      - e.g. `"abba"` centered between `'b'` and `'b'`.
      - There are $n - 1$ such centers.
  - **Unified $2n - 1$ Center Coordinate System:**
    - A string of length $n$ contains exactly $2n - 1$ potential centers.
    - Parameterize centers by integer $k \in [0, \; 2n - 2]$:
      $$
      i = \lfloor k / 2 \rfloor, \quad j = \lfloor (k + 1) / 2 \rfloor
      $$
      - If $k$ is even: $i == j$ (Odd palindrome centered at character $k/2$).
      - If $k$ is odd: $j == i + 1$ (Even palindrome centered between $k//2$ and $k//2 + 1$).
    - Expand outward symmetrically by stepping $i \leftarrow i - 1$ and $j \leftarrow j + 1$:
      - As long as $i \ge 0, \; j < n$, and $s[i] == s[j]$, substring $s[i \dots j]$ is a palindrome.
      - Increment count: $ans \leftarrow ans + 1$.
      - As soon as $s[i] \ne s[j]$, no longer palindrome can be centered at this point $\implies$ **terminate expansion immediately**.
- **Step-by-Step Worked Execution Trace on $s = \text{"aaa"}$ ($n = 3$):**
  - Number of centers: $2n - 1 = 2(3) - 1 = \mathbf{5}$ (centers $k = 0, 1, 2, 3, 4$).
  - Initialize $ans = 0$.
  - **Center $k = 0$ (Odd center at index $0$):**
    - $i = 0, \; j = 0$.
    - Check $s[0] == s[0]$ (`'a' == 'a'`): $\mathbf{Match!}$
      - Palindrome found: `"a"` (index 0).
      - $ans \leftarrow 0 + 1 = \mathbf{1}$.
      - Expand: $i = -1, j = 1 \implies i < 0$ (Out of bounds, halts).
  - **Center $k = 1$ (Even center between indices $0$ and $1$):**
    - $i = 0, \; j = 1$.
    - Check $s[0] == s[1]$ (`'a' == 'a'`): $\mathbf{Match!}$
      - Palindrome found: `"aa"` (indices 0..1).
      - $ans \leftarrow 1 + 1 = \mathbf{2}$.
      - Expand: $i = -1, j = 2 \implies$ Out of bounds.
  - **Center $k = 2$ (Odd center at index $1$):**
    - $i = 1, \; j = 1$.
    - Check $s[1] == s[1]$ (`'a' == 'a'`): $\mathbf{Match!}$
      - Palindrome found: `"a"` (index 1).
      - $ans \leftarrow 2 + 1 = \mathbf{3}$.
    - Expand: $i = 0, \; j = 2$.
    - Check $s[0] == s[2]$ (`'a' == 'a'`): $\mathbf{Match!}$
      - Palindrome found: `"aaa"` (indices 0..2).
      - $ans \leftarrow 3 + 1 = \mathbf{4}$.
    - Expand: $i = -1, j = 3 \implies$ Out of bounds.
  - **Center $k = 3$ (Even center between indices $1$ and $2$):**
    - $i = 1, \; j = 2$.
    - Check $s[1] == s[2]$ (`'a' == 'a'`): $\mathbf{Match!}$
      - Palindrome found: `"aa"` (indices 1..2).
      - $ans \leftarrow 4 + 1 = \mathbf{5}$.
    - Expand: $i = 0, j = 3 \implies$ Out of bounds.
  - **Center $k = 4$ (Odd center at index $2$):**
    - $i = 2, \; j = 2$.
    - Check $s[2] == s[2]$ (`'a' == 'a'`): $\mathbf{Match!}$
      - Palindrome found: `"a"` (index 2).
      - $ans \leftarrow 5 + 1 = \mathbf{6}$.
    - Expand: $i = 1, j = 3 \implies$ Out of bounds.
  - **Step 6: Final Result:**
    - All 5 centers evaluated.
    - Total palindromic substrings:
      $$
      ans = \mathbf{6}
      $$
- **Distinct Characters Instance ($s = \text{"abc"}$):**
  - Odd centers ($k = 0, 2, 4$): find `"a"`, `"b"`, `"c"` ($+3$).
  - Even centers ($k = 1, 3$): $s[0] \ne s[1]$ (`'a' != 'b'`) and $s[1] \ne s[2]$ (`'b' != 'c'`) $\implies 0$ matches.
  - Total: $3 + 0 = \mathbf{3}$.

This instance demonstrates center-outward radial symmetry expansion, mathematically proves why bi-directional character parity covers all distinct substring reflection centers, and derives $O(N^2)$ worst-case runtime (optimal without Manacher's algorithm) and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a string $s$:
Count the **total number of palindromic substrings**.

```text
s = "aaa"

Centers:
  Center 0 (at 'a'):       "a"        -> +1
  Center 1 (between 'a','a'): "aa"       -> +1
  Center 2 (at middle 'a'): "a", "aaa" -> +2
  Center 3 (between 'a','a'): "aa"       -> +1
  Center 4 (at last 'a'):   "a"        -> +1

Total Palindromes = 1 + 1 + 2 + 1 + 1 = 6
```

### The Invariant of the $2n - 1$ Centers
- A string of length $n$ has exactly:
  - $n$ odd-length centers (at each character).
  - $n - 1$ even-length centers (between every adjacent pair).
- Total centers $= n + (n - 1) = 2n - 1$.
- Expanding outward from each center until characters differ finds all palindromes with zero duplicate counting.

---

## 2. Conceptual Foundation & Invariants

### 1. The Unified Center Indexing Formula:
For $k \in [0, 2n - 2]$:
$$
i = \lfloor k / 2 \rfloor, \quad j = \lfloor (k + 1) / 2 \rfloor
$$

### 2. Radial Expansion Invariant:
While $i \ge 0$ and $j < n$ and $s[i] == s[j]$:
$$
ans \leftarrow ans + 1
$$
$$
i \leftarrow i - 1, \quad j \leftarrow j + 1
$$

> **Concentric Symmetry Invariant.** A string $s[i \dots j]$ is palindromic if and only if $s[i+1 \dots j-1]$ is palindromic and $s[i] == s[j]$, establishing contiguous nested boundary intervals around the reflection axis.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"aaa"}$:

---

### Step 1: Center $k = 0$ (at 0)
- $s[0 \dots 0] = \text{"a"}$. Count $= 1$.

---

### Step 2: Center $k = 1$ (0 to 1)
- $s[0 \dots 1] = \text{"aa"}$. Count $= 2$.

---

### Step 3: Center $k = 2$ (at 1)
- $s[1 \dots 1] = \text{"a"}$.
- Expand: $s[0 \dots 2] = \text{"aaa"}$. Count $= 4$.

---

### Step 4: Center $k = 3$ (1 to 2)
- $s[1 \dots 2] = \text{"aa"}$. Count $= 5$.

---

### Step 5: Center $k = 4$ (at 2)
- $s[2 \dots 2] = \text{"a"}$. Count $= 6$.

---

### Step 6: Output
$$
\mathbf{6}
$$

---

## 4. Complete Execution Trace

| Center Index $k$ | Center Type | Initial $[i, j]$ | Matching Substrings Found | Expansion Steps | Subtotal Credited |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | Odd | $[0, 0]$ | `"a"` | $1$ | $+1$ |
| $1$ | Even | $[0, 1]$ | `"aa"` | $1$ | $+1$ |
| **$2$** | **Odd** | **$[1, 1]$** | **`"a"`, `"aaa"`** | **$2$** | **$+2$** |
| $3$ | Even | $[1, 2]$ | `"aa"` | $1$ | $+1$ |
| $4$ | Odd | $[2, 2]$ | `"a"` | $1$ | $+1$ |
| **Total** | — | — | — | — | **`6`** |

---

## 5. Boundary Cases & Failure Modes

- **Single Character ($s = \text{"a"}$):** Exactly 1 center ($k = 0$) $\implies 1$.
- **All Distinct Characters ($s = \text{"abc"}$):** Only singletons match $\implies n$.
- **Alternating Characters ($s = \text{"aba"}$):** Singletons `"a"`, `"b"`, `"a"` plus `"aba"` $\implies 4$.
- **Large Repeated Characters ($s = \text{"a"} \times 1000$):** Total is $\frac{n(n+1)}{2} = 500{,}500$.

---

## 6. Traps & Common Anti-Patterns

- **Checking Substrings via Reversal ($O(N^3)$):** Slicing all $\binom{N}{2}$ substrings and reversing each takes cubic time. Center expansion does it in $O(N^2)$ without string copying.
- **Missing Even-Length Centers:** Looking only at single-character centers misses all even palindromes like `"aa"` or `"abba"`.
- **Continuing Expansion After Mismatch:** If $s[i] \ne s[j]$, you **cannot** skip over the mismatch; expansion must stop immediately.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Exactly $2N - 1$ centers are tested.
  - From each center, the outward expansion runs at most $N / 2$ steps.
  - Total Time: $\mathcal{O}(N^2)$ in the worst case (all identical characters), and $\mathcal{O}(N)$ in the best case (all distinct). Completes in $< 15$ ms for $N = 1000$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ auxiliary space (in-place index checks, zero allocations).
