# Guided Example: Positions of Large Groups

We trace the step-by-step contiguous identical character run scanning, two-pointer window expansion ($[i, j-1]$), large group threshold filtering ($j - i \ge 3$), inclusive index boundary recording ($[start, end]$), and linear sorted interval collection on representative character sequences:

- **Input:**
  $$
  s = \text{"abbxxxxzzy"}
  $$
- **Required output:**
  $$
  [[3, 6]]
  $$
  - Consecutive character group rules:
    - A string consists of contiguous groups of identical consecutive characters.
    - Each group is defined by its inclusive start and end index pair $[start, end]$.
    - A group is defined as **large** if it contains **3 or more** characters:
      $$
      \text{length} = end - start + 1 \ge 3
      $$
    - Objective: Return the list of $[start, end]$ intervals for all large groups, ordered by start index.
    - For $s = \text{"abbxxxxzzy"}$ (length $10$):
      - Group 1: `'a'` at indices $[0, 0]$ (length $1 < 3$).
      - Group 2: `'b'` at indices $[1, 2]$ (length $2 < 3$).
      - Group 3: `'x'` at indices $[3, 6]$ (length $4 \ge 3$) $\implies \mathbf{[3, 6]}.$
      - Group 4: `'z'` at indices $[7, 8]$ (length $2 < 3$).
      - Group 5: `'y'` at indices $[9, 9]$ (length $1 < 3$).
      - Result: `[[3, 6]]`.
- **Two-Pointer Run-Length Invariant:**
  - **The Sliding Segment Search:**
    - Initialize start pointer $i = 0$.
    - While $i < n$:
      - Extend right pointer $j = i$ while $j < n$ and $s[j] = s[i]$.
      - Upon loop termination, index $j$ is the first character different from $s[i]$ (or the string end $n$).
      - The homogeneous block spans:
        $$
        [start, \; end] = [i, \; j - 1]
        $$
      - Length of the block:
        $$
        L = j - i
        $$
      - **Large Group Filter:**
        - If $j - i \ge 3$: Record interval $[i, j - 1]$.
      - Advance directly to the next block:
        $$
        i \leftarrow j
        $$
  - Because pointer $i$ strictly jumps forward to $j$ without backtracking, the scan completes in a single linear pass $\mathcal{O}(N)$.
- **Step-by-Step Worked Execution Trace on $s = \text{"abbxxxxzzy"}$ ($n = 10$):**
  - Initialize: $i = 0, ans = []$.
  - **Iteration 1 (Starts at $i = 0$, Character `'a'`):**
    - $j$ scans while $s[j] = \text{'a'}$:
      - $j = 0$: $s[0] = \text{'a'}$.
      - $j = 1$: $s[1] = \text{'b'} \ne \text{'a'} \implies \mathbf{Stop.}$
    - Span: $[0, 0]$. Length: $j - i = 1 - 0 = \mathbf{1}$.
    - Sizing check: $1 < 3 \implies \mathbf{Small\ Group\ (Ignored).}$
    - Advance: $i \leftarrow 1$.
  - **Iteration 2 (Starts at $i = 1$, Character `'b'`):**
    - $j$ scans while $s[j] = \text{'b'}$:
      - $j = 1$: $s[1] = \text{'b'}$.
      - $j = 2$: $s[2] = \text{'b'}$.
      - $j = 3$: $s[3] = \text{'x'} \ne \text{'b'} \implies \mathbf{Stop.}$
    - Span: $[1, 2]$. Length: $j - i = 3 - 1 = \mathbf{2}$.
    - Sizing check: $2 < 3 \implies \mathbf{Small\ Group\ (Ignored).}$
    - Advance: $i \leftarrow 3$.
  - **Iteration 3 (Starts at $i = 3$, Character `'x'`):**
    - $j$ scans while $s[j] = \text{'x'}$:
      - $j = 3$: $s[3] = \text{'x'}$.
      - $j = 4$: $s[4] = \text{'x'}$.
      - $j = 5$: $s[5] = \text{'x'}$.
      - $j = 6$: $s[6] = \text{'x'}$.
      - $j = 7$: $s[7] = \text{'z'} \ne \text{'x'} \implies \mathbf{Stop.}$
    - Span: $[start, end] = [3, 7 - 1] = \mathbf{[3, 6]}$.
    - Length: $j - i = 7 - 3 = \mathbf{4}$.
    - Sizing check:
      $$
      4 \ge 3 \implies \mathbf{Large\ Group\ Discovered!}
      $$
    - Record interval: $ans.\text{append}([3, 6])$.
    - Advance: $i \leftarrow 7$.
  - **Iteration 4 (Starts at $i = 7$, Character `'z'`):**
    - $j$ scans while $s[j] = \text{'z'}$:
      - $j = 7, 8$ are `'z'`.
      - $j = 9$: $s[9] = \text{'y'} \ne \text{'z'} \implies \mathbf{Stop.}$
    - Span: $[7, 8]$. Length: $9 - 7 = \mathbf{2} < 3$.
    - Advance: $i \leftarrow 9$.
  - **Iteration 5 (Starts at $i = 9$, Character `'y'`):**
    - $j$ scans while $s[j] = \text{'y'}$:
      - $j = 9$ is `'y'`.
      - $j = 10 == n \implies \mathbf{Stop.}$
    - Span: $[9, 9]$. Length: $10 - 9 = \mathbf{1} < 3$.
    - Advance: $i \leftarrow 10$.
  - **End of String Reached ($i == n$):**
    - Output:
      $$
      ans = [[3, 6]]
      $$
- **Multiple Large Groups Trace ($s = \text{"abcdddeeeeaabbbcd"}$):**
  - `"ddd"`: $j - i = 3 \implies \mathbf{[3, 5]}$.
  - `"eeee"`: $j - i = 4 \implies \mathbf{[6, 9]}$.
  - `"bbb"`: $j - i = 3 \implies \mathbf{[12, 14]}$.
  - Result: `[[3, 5], [6, 9], [12, 14]]`.
- **No Large Groups Trace ($s = \text{"abc"}$):**
  - All run lengths are 1 $\implies ans = []$.
- **Entire String is One Group ($s = \text{"aaaa"}$):**
  - Span: $[0, 3]$, length $4 \ge 3 \implies [[0, 3]]$.

This instance demonstrates run-length factorization of strings and monotone pointer segmentation, mathematically proves why advancing the anchor pointer to the boundary token preserves exhaustive partition coverage without redundant character comparisons, and derives $O(N)$ execution time and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given string $s$:
Find all contiguous runs of the same character of length $\ge 3$.
Return their inclusive intervals `[start, end]` sorted by start.

```text
s = "abbxxxxzzy"

Runs:
  "a"    -> [0, 0] (length 1)
  "bb"   -> [1, 2] (length 2)
  "xxxx" -> [3, 6] (length 4 >= 3) -> LARGE GROUP!
  "zz"   -> [7, 8] (length 2)
  "y"    -> [9, 9] (length 1)

Result: [ [3, 6] ]
```

### The Invariant of Run-Length Windowing
- Start pointer $i$ anchors the group; right pointer $j$ advances while characters match $s[i]$.
- The group length is $j - i$ and the inclusive interval is $[i, j - 1]$.
- If $j - i \ge 3$, record $[i, j - 1]$ and jump $i \leftarrow j$.

---

## 2. Conceptual Foundation & Invariants

### 1. Equivalence Block Partition:
$$
s = \prod_{k = 1}^K c_k^{L_k}, \quad \text{where } c_k \ne c_{k+1}
$$

### 2. Threshold Filtering:
$$
ans = \left\{ [start_k, \; end_k] \;\middle|\; end_k - start_k + 1 \ge 3 \right\}
$$

> **Maximal Monotone Partition Invariant.** The relation $x \sim y \iff \forall z \in [\min(x,y), \max(x,y)]: s[z] = s[x]$ is an equivalence relation whose equivalence classes are convex intervals in $[0, n - 1]$. The two-pointer greedy procedure extracts exactly the set of classes with $|C_k| \ge 3$.

---

## 3. Step-by-Step Worked Execution

We trace $s = \text{"abbxxxxzzy"}$:

---

### Step 1: Run 1 (`'a'`)
- $i = 0, j = 1 \implies$ length 1 (ignored).

---

### Step 2: Run 2 (`'b'`)
- $i = 1, j = 3 \implies$ length 2 (ignored).

---

### Step 3: Run 3 (`'x'`)
- $i = 3, j = 7 \implies$ length 4.
- $4 \ge 3 \implies$ record **$[3, 6]$**.

---

### Step 4: Runs 4 & 5 (`'z'`, `'y'`)
- Lengths 2 and 1 (ignored).

---

### Step 5: Output
$$
[[3, 6]]
$$

---

## 4. Complete Execution Trace

| Group Character | Start Index $i$ | End Boundary $j$ | Run Length $j - i$ | Length $\ge 3$? | Recorded Interval $[i, j-1]$ |
|:---:|:---:|:---:|:---:|:---:|:---:|
| `'a'` | $0$ | $1$ | $1$ | No | — |
| `'b'` | $1$ | $3$ | $2$ | No | — |
| **`'x'`** | **$3$** | **$7$** | **$4$** | **Yes** | **`[3, 6]`** |
| `'z'` | $7$ | $9$ | $2$ | No | — |
| `'y'` | $9$ | $10$ | $1$ | No | — |
| **Final** | — | — | — | — | **`[[3, 6]]`** |

---

## 5. Boundary Cases & Failure Modes

- **No Large Groups ($s = \text{"abc"}$):** Returns `[]`.
- **Entire String is One Character ($s = \text{"aaaa"}$):** Returns `[[0, 3]]`.
- **Large Group at the Very End ($s = \text{"aaabbb"}$):** Condition $j < n$ safely terminates at string boundary, recording $[3, 5]$ correctly.
- **Short String ($N < 3$):** Never contains any group of length $\ge 3 \implies []$.

---

## 6. Traps & Common Anti-Patterns

- **Missing the Final Group:** If the large group reaches the end of the string ($j == n$), ensure it is evaluated before loop termination.
- **Off-By-One on End Index:** The inclusive end index is $j - 1$, NOT $j$.
- **Backtracking the Pointers:** Once $j$ is found, set $i = j$; re-checking characters inside the group is unnecessary and degrades runtime.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Pointers $i$ and $j$ only move forward from $0$ to $N$.
  - Each character is inspected at most twice.
  - Total Time: strictly linear $\mathcal{O}(N)$ where $N \le 1000$. Completes in $< 0.05$ ms.
- **Auxiliary Space Complexity:**
  - Strictly $\mathcal{O}(1)$ auxiliary space beyond the output array.
