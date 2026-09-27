# Guided Example: Contiguous Array

We trace the step-by-step binary transformation mapping ($0 \to -1, \; 1 \to +1$), zero-sum subarray equivalence, prefix displacement tracking ($s_i = \sum \pm 1$), earliest-seen index hash map caching ($d[s] = \min(index)$), sentinel grounding ($d[0] = -1$), and maximum span extension on representative binary arrays:

- **Input:** $nums = [0, 1, 0]$
- **Required output:** `2`
  - Array length: $n = 3$
  - Objective: Find the maximum length of a contiguous subarray containing an equal count of zeroes and ones.
- **$\pm 1$ Prefix Displacement Trace:**
  - Map each binary element:
    $$
    x = 1 \implies +1, \quad x = 0 \implies -1
    $$
  - Subarray zero-balance theorem:
    $$
    \text{Count}(0) = \text{Count}(1) \iff \sum (+1) + \sum (-1) = 0 \iff s_i - s_j = 0 \iff s_i = s_j
    $$
    A subarray from index $j + 1$ to $i$ is balanced if and only if the cumulative sum at index $i$ equals the cumulative sum at index $j$.
  - Subarray span length:
    $$
    L = i - j
    $$
  - To maximize $L = i - j$, for any sum $s$, we must match with the **smallest possible $j$** (the earliest index where $s$ first appeared).
  - Initialize hash map with virtual index for prefix sum 0:
    $$
    d = \{0: -1\}
    $$
    Running sum $s = 0$, maximum length $ans = 0$.
  - **Index 0 ($nums[0] = 0 \implies -1$):**
    - Running sum: $s \leftarrow 0 + (-1) = \mathbf{-1}$
    - Is $-1 \in d$? No.
    - Record earliest appearance:
      $$
      d[-1] = 0
      $$
    - State: $d = \{0: -1, \; -1: 0\}, \; ans = 0$.
  - **Index 1 ($nums[1] = 1 \implies +1$):**
    - Running sum: $s \leftarrow -1 + 1 = \mathbf{0}$
    - Is $0 \in d$? **Yes!**
    - Earliest seen index: $d[0] = -1$.
    - Balanced segment length:
      $$
      L = i - d[0] = 1 - (-1) = \mathbf{2}
      $$
    - Elements: $nums[0 \dots 1] = [0, 1]$ (one 0, one 1).
    - Update maximum length:
      $$
      ans \leftarrow \max(0, 2) = \mathbf{2}
      $$
    - *Do NOT overwrite $d[0]$! Keep $-1$.*
  - **Index 2 ($nums[2] = 0 \implies -1$):**
    - Running sum: $s \leftarrow 0 + (-1) = \mathbf{-1}$
    - Is $-1 \in d$? **Yes!**
    - Earliest seen index: $d[-1] = 0$.
    - Balanced segment length:
      $$
      L = i - d[-1] = 2 - 0 = \mathbf{2}
      $$
    - Elements: $nums[1 \dots 2] = [1, 0]$ (one 1, one 0).
    - Update maximum length:
      $$
      ans \leftarrow \max(2, 2) = \mathbf{2}
      $$
  - Array exhausted.
  - Final maximum length: **`2`**.
- **Longer Symmetric Balanced Array ($nums = [0, 0, 1, 0, 0, 0, 1, 1]$):**
  - Spans across multiple fluctuations $\implies$ identifies balanced window of length $\mathbf{6}$.
- **All Identical Elements ($nums = [0, 0, 0]$ or $[1, 1, 1]$):**
  - Sum increases or decreases monotonically; no sum ever repeats $\implies ans = \mathbf{0}$.
- **Exact Balanced Pair ($nums = [0, 1]$):** Returns $\mathbf{2}$.

This instance demonstrates geometric 1D random walk displacement balance, mathematically proves why prefix sum collisions define zero-sum intervals, and derives $O(N)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a binary array $nums = [0, 1, 0]$:
Find the **maximum length** of a contiguous subarray with an equal number of `0` and `1`.

```text
Binary Array:   [  0,   1,   0 ]
Values (+1/-1): [ -1,  +1,  -1 ]

Cumulative Displacement:
  Index -1: Sum =  0
  Index  0: Sum = -1
  Index  1: Sum =  0  <- Matches index -1 (span = 1 - (-1) = 2)
  Index  2: Sum = -1  <- Matches index  0 (span = 2 -   0  = 2)

Maximum Balanced Length = 2
```

### The $0 \to -1$ Transformation Trick
- Direct counting of zeros and ones inside subarrays requires checking $O(N^2)$ ranges.
- By reinterpreting each element:
  $$
  x \to
  \begin{cases}
  +1 & \text{if } x == 1 \\
  -1 & \text{if } x == 0
  \end{cases}
  $$
- An equal number of zeros and ones means:
  $$
  \text{Count}(1) \times (+1) + \text{Count}(0) \times (-1) = 0
  $$
- The problem is transformed into: **Find the longest subarray whose sum is exactly 0**!

---

## 2. Conceptual Foundation & Invariants

### 1. Prefix Sum Collision:
Let $s_i$ be the cumulative sum of the transformed values up to index $i$:
$$
\sum_{k=j+1}^i \text{transformed}[k] = s_i - s_j
$$
- If $s_i - s_j = 0$, then $s_i = s_j$.
- Any time the cumulative sum $s$ at index $i$ is equal to the cumulative sum at some previous index $j$, the subarray $nums[j+1 \dots i]$ has a sum of 0, meaning it contains **an equal number of 0s and 1s**.
- Length of this balanced subarray is $i - j$.

### 2. Earliest Occurrence Invariant:
To maximize the span $i - j$:
- We must pick the **smallest possible $j$** for that sum $s$.
- In the hash map $d$, record index $i$ for sum $s$ **only the first time $s$ appears**.
- Never overwrite $d[s]$ on subsequent visits!

### 3. Sentinel Grounding:
Initialize $d[0] = -1$.
If the prefix sum from the very beginning of the array ($j = 0$) reaches 0 at index $i$, the length is $i - (-1) = i + 1$.

> **Span Maximization Invariant.** Because $d[s]$ stores the absolute earliest index of sum $s$, any future collision $s_i == s$ yields the maximal possible balanced interval ending at index $i$.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [0, 1, 0]$ ($n = 3$):

---

### Step 1: Initialization
- $d = \{0: -1\}$
- $ans = 0, \; s = 0$

---

### Step 2: Index 0 ($nums[0] = 0 \implies -1$)
- Update sum:
  $$
  s \leftarrow 0 - 1 = \mathbf{-1}
  $$
- Is $-1$ in $d$? No.
- Store first occurrence:
  $$
  d[-1] = 0
  $$
- State: $d = \{0: -1, \; -1: 0\}, \; ans = 0$.

---

### Step 3: Index 1 ($nums[1] = 1 \implies +1$)
- Update sum:
  $$
  s \leftarrow -1 + 1 = \mathbf{0}
  $$
- Is $0$ in $d$? **Yes!**
- Retrieve earliest appearance: $d[0] = -1$.
- Calculate span:
  $$
  \text{span} = i - d[0] = 1 - (-1) = \mathbf{2}
  $$
- Update answer:
  $$
  ans \leftarrow \max(0, 2) = \mathbf{2}
  $$
- State: $d = \{0: -1, \; -1: 0\}, \; ans = 2$.

---

### Step 4: Index 2 ($nums[2] = 0 \implies -1$)
- Update sum:
  $$
  s \leftarrow 0 - 1 = \mathbf{-1}
  $$
- Is $-1$ in $d$? **Yes!**
- Retrieve earliest appearance: $d[-1] = 0$.
- Calculate span:
  $$
  \text{span} = i - d[-1] = 2 - 0 = \mathbf{2}
  $$
- Update answer:
  $$
  ans \leftarrow \max(2, 2) = \mathbf{2}
  $$

---

### Final Output:
$$
ans = \mathbf{2}
$$

---

## 4. Complete Execution Trace

| Index $i$ | Value $nums[i]$ | Transformed | Running Sum $s$ | $s$ in Hash Map? | Earliest Index $d[s]$ | Span $i - d[s]$ | Max Length $ans$ |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **Init** | — | — | $0$ | Yes (Sentinel) | $-1$ | — | $0$ |
| **$0$** | $0$ | $-1$ | $-1$ | No | Store $d[-1]=0$ | — | $0$ |
| **$1$** | $1$ | $+1$ | **$0$** | **Yes** | $-1$ | $1 - (-1) = \mathbf{2}$ | **$2$** |
| **$2$** | $0$ | $-1$ | **$-1$** | **Yes** | $0$ | $2 - 0 = \mathbf{2}$ | **$2$** |
| **Result** | — | — | — | — | — | — | **$2$** |

---

## 5. Boundary Cases & Failure Modes

- **Minimal Balanced Pair ($[0, 1]$ or $[1, 0]$):** Sum returns to 0 at index 1 $\implies ans = 2$.
- **No Balanced Subarray Possible ($[0, 0, 0]$ or $[1, 1, 1]$):** No sum repeats $\implies ans = 0$.
- **Entire Array Balanced ($[0, 1, 0, 1]$):** Final index $3$ collides with $d[0] = -1 \implies 3 - (-1) = \mathbf{4}$.
- **Single Element ($[0]$ or $[1]$):** Length cannot even reach 2 $\implies ans = 0$.

---

## 6. Traps & Common Anti-Patterns

- **Overwriting the Hash Map on Duplicate Sums:**
  Writing `d[s] = i` unconditionally updates the index to the most recent occurrence. This shrinks $i - d[s]$ to small intervals (or 0), failing to find the *longest* contiguous subarray.
- **Forgetting Sentinel $d[0] = -1$:**
  If an entire prefix from index 0 is balanced (e.g. $[0, 1]$), the sum reaches 0 at index 1. Without $d[0] = -1$, the algorithm records $d[0] = 1$ and outputs 0 instead of 2.
- **Quadratic Brute-Force Counting ($O(N^2)$):**
  Checking all pairs $(i, j)$ requires $O(N^2)$ time, timing out for $N = 10^5$. Prefix sum hashing executes in linear $O(N)$ time.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - A single linear pass processes the $N$ elements.
  - Each step performs arithmetic, hash map lookup, and integer comparison in $O(1)$ amortized time.
  - Total Time: $\mathcal{O}(N)$. For $N = 10^5$, completes in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space to store at most $2N + 1$ possible prefix sum values in hash map $d$.
