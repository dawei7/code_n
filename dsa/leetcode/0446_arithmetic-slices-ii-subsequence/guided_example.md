# Guided Example: Arithmetic Slices II - Subsequence

We trace the step-by-step pair-difference dynamic programming table construction ($f[i][d]$), weak arithmetic progression extension (length $\ge 2$), valid slice counting ($\ge 3$ elements), and difference hash map transitions on representative subsequence arrays:

- **Input:** $nums = [2, 4, 6, 8, 10]$
- **Required output:** `7`
  - Array length: $N = 5$
  - The 7 valid arithmetic subsequences of length $\ge 3$:
    - Common difference $d = 2$:
      - Length 3: $[2, 4, 6], \; [4, 6, 8], \; [6, 8, 10]$ (3 slices)
      - Length 4: $[2, 4, 6, 8], \; [4, 6, 8, 10]$ (2 slices)
      - Length 5: $[2, 4, 6, 8, 10]$ (1 slice)
    - Common difference $d = 4$:
      - Length 3: $[2, 6, 10]$ (1 slice)
    - Total: $3 + 2 + 1 + 1 = \mathbf{7}$
- **Dynamic programming execution trace:**
  - Let $f[i][d]$ count arithmetic subsequences of length $\ge 2$ ending at index $i$ with common difference $d$.
  - **Index 0 ($nums[0] = 2$):** $f[0] = \{\}$
  - **Index 1 ($nums[1] = 4$):**
    - Pair $(0, 1): d = 4 - 2 = 2$.
    - $f[0][2] = 0 \implies ans += 0$.
    - $f[1][2] \leftarrow f[0][2] + 1 = 1$ (Represents $[2, 4]$)
  - **Index 2 ($nums[2] = 6$):**
    - Pair $(0, 2): d = 6 - 2 = 4$. $f[0][4] = 0 \implies ans += 0, \; f[2][4] \leftarrow 1$ ($[2, 6]$)
    - Pair $(1, 2): d = 6 - 4 = 2$.
      - $f[1][2] = 1 \implies \mathbf{ans += 1}$ (Extends $[2, 4]$ to $[2, 4, 6]$!)
      - $f[2][2] \leftarrow f[1][2] + 1 = 1 + 1 = 2$ (Holds $[4, 6]$ and $[2, 4, 6]$)
  - **Index 3 ($nums[3] = 8$):**
    - Pair $(1, 3): d = 8 - 4 = 4$. $f[1][4] = 0 \implies f[3][4] \leftarrow 1$
    - Pair $(2, 3): d = 8 - 6 = 2$.
      - $f[2][2] = 2 \implies \mathbf{ans += 2}$ (Extends $[4, 6] \to [4, 6, 8]$ and $[2, 4, 6] \to [2, 4, 6, 8]$!)
      - $f[3][2] \leftarrow f[2][2] + 1 = 2 + 1 = 3$
  - **Index 4 ($nums[4] = 10$):**
    - Pair $(0, 4): d = 10 - 2 = 8 \implies f[4][8] \leftarrow 1$
    - Pair $(2, 4): d = 10 - 6 = 4$.
      - $f[2][4] = 1 \implies \mathbf{ans += 1}$ (Extends $[2, 6] \to [2, 6, 10]$!)
      - $f[4][4] \leftarrow 1 + 1 = 2$
    - Pair $(3, 4): d = 10 - 8 = 2$.
      - $f[3][2] = 3 \implies \mathbf{ans += 3}$ (Extends $[6, 8] \to [6, 8, 10]$, $[4, 6, 8] \to [4, 6, 8, 10]$, $[2, 4, 6, 8] \to [2, 4, 6, 8, 10]$!)
      - $f[4][2] \leftarrow 3 + 1 = 4$
  - Final accumulated count:
    $$
    ans = 0 + 1 + 2 + 1 + 3 = \mathbf{7}
    $$
- **All Identical Elements Instance:** $nums = [7, 7, 7, 7, 7] \implies$ all differences $d = 0$, every subset of size $\ge 3$ forms an arithmetic slice $\implies \binom{5}{3} + \binom{5}{4} + \binom{5}{5} = 10 + 5 + 1 = \mathbf{16}$
- **Short Input ($N < 3$):** $nums = [1, 2] \implies \mathbf{0}$

This instance demonstrates dynamic programming over non-contiguous subsequence spaces, mathematically proves how tracking 2-element weak progressions avoids overcounting while cleanly adding length $\ge 3$ slices, and derives $O(N^2)$ runtime and $O(N^2)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums = [2, 4, 6, 8, 10]$:
A sequence is called **arithmetic** if it consists of at least **three elements** and the difference between any two consecutive elements is the same.
Return the number of all **arithmetic subsequences** in $nums$ (subsequences need not be contiguous).

```text
Input Elements: [ 2,  4,  6,  8,  10 ]
Indices:          0   1   2   3    4

Valid Arithmetic Subsequences (Length >= 3):
  Difference d = 2:
    - Length 3: [2, 4, 6],  [4, 6, 8],  [6, 8, 10]    (3)
    - Length 4: [2, 4, 6, 8],  [4, 6, 8, 10]          (2)
    - Length 5: [2, 4, 6, 8, 10]                      (1)
  Difference d = 4:
    - Length 3: [2, 6, 10]                            (1)

Total Count: 3 + 2 + 1 + 1 = 7
```

### The Subsequence Counting Dilemma
In Problem 413, arithmetic slices had to be contiguous subarrays, allowing an $O(N)$ running pointer.
Here, subsequences can skip arbitrary elements.
A naive generation of all $2^N$ subsequences is exponential.
To solve this in polynomial time:
We define a DP state parameterized by **the last element index $i$** and **the common difference $d$**.

---

## 2. Conceptual Foundation & Invariants

### 1. The Weak vs Valid Progression Distinction:
A valid arithmetic slice requires **at least 3 elements**.
However, any 2 elements $[nums[j], nums[i]]$ form a "weak progression" of length 2 with difference $d = nums[i] - nums[j]$.
If we define:
$$
f[i][d] = \text{number of arithmetic subsequences of length } \ge 2 \text{ ending at } i \text{ with difference } d
$$
Then for any prior index $j < i$ with difference $d = nums[i] - nums[j]$:
- Every sequence of length $\ge 2$ ending at $j$ with difference $d$ can append $nums[i]$ to form a new sequence of length $\ge 3$!
- The number of such newly created **valid** slices of length $\ge 3$ is exactly $f[j][d]$.
- Therefore, we accumulate:
  $$
  ans \leftarrow ans + f[j][d]
  $$
- To maintain the DP state for future indices $k > i$:
  - The newly created length $\ge 3$ sequences count: $f[j][d]$.
  - The new 2-element sequence $[nums[j], nums[i]]$ also ends at $i$ with difference $d$: $+1$.
  - Transition formula:
    $$
    f[i][d] \leftarrow f[i][d] + f[j][d] + 1
    $$

> **DP Invariant.** $f[i][d]$ counts all arithmetic subsequences of length $\ge 2$ ending at index $i$, while $ans$ accumulates strictly those transitions that produce sequences of length $\ge 3$.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [2, 4, 6, 8, 10]$ ($N = 5$):

---

### Step 1: Pair Transitions at $i = 1$ ($nums[1] = 4$)
- $j = 0$ ($nums[0] = 2$):
  - Difference: $d = 4 - 2 = 2$.
  - Existing slices of length $\ge 2$ ending at 0 with $d = 2$: $f[0][2] = 0$.
  - Contribution to answer: $ans += 0$.
  - Update DP table: $f[1][2] \leftarrow f[1][2] + f[0][2] + 1 = 0 + 0 + 1 = \mathbf{1}$ (Represents $[2, 4]$).

---

### Step 2: Pair Transitions at $i = 2$ ($nums[2] = 6$)
- $j = 0$ ($nums[0] = 2$):
  - $d = 6 - 2 = 4$.
  - $f[0][4] = 0 \implies ans += 0$.
  - $f[2][4] \leftarrow 0 + 1 = \mathbf{1}$ (Represents $[2, 6]$).
- $j = 1$ ($nums[1] = 4$):
  - $d = 6 - 4 = 2$.
  - Existing at $j=1$: $f[1][2] = 1$ (the pair $[2, 4]$).
  - Appending $nums[2]$ forms $[2, 4, 6]$ (length 3!).
  - **Contribution to answer:** $ans \leftarrow 0 + 1 = \mathbf{1}$.
  - Update DP table: $f[2][2] \leftarrow f[2][2] + f[1][2] + 1 = 0 + 1 + 1 = \mathbf{2}$ (Represents $[4, 6]$ and $[2, 4, 6]$).

---

### Step 3: Pair Transitions at $i = 3$ ($nums[3] = 8$)
- $j = 0$ ($nums[0] = 2$): $d = 6 \implies ans += 0, \; f[3][6] \leftarrow 1$.
- $j = 1$ ($nums[1] = 4$): $d = 4 \implies f[1][4] = 0 \implies ans += 0, \; f[3][4] \leftarrow 1$.
- $j = 2$ ($nums[2] = 6$):
  - $d = 8 - 6 = 2$.
  - Existing at $j=2$: $f[2][2] = 2$ (the sequences $[4, 6]$ and $[2, 4, 6]$).
  - Appending $nums[3]$ forms $[4, 6, 8]$ and $[2, 4, 6, 8]$ (both length $\ge 3$!).
  - **Contribution to answer:** $ans \leftarrow 1 + 2 = \mathbf{3}$.
  - Update DP table: $f[3][2] \leftarrow f[3][2] + f[2][2] + 1 = 0 + 2 + 1 = \mathbf{3}$.

---

### Step 4: Pair Transitions at $i = 4$ ($nums[4] = 10$)
- $j = 0$ ($nums[0] = 2$): $d = 8 \implies ans += 0, \; f[4][8] \leftarrow 1$.
- $j = 1$ ($nums[1] = 4$): $d = 6 \implies ans += 0, \; f[4][6] \leftarrow 1$.
- $j = 2$ ($nums[2] = 6$):
  - $d = 10 - 6 = 4$.
  - Existing at $j=2$: $f[2][4] = 1$ (the pair $[2, 6]$).
  - Appending $nums[4]$ forms $[2, 6, 10]$ (length 3!).
  - **Contribution to answer:** $ans \leftarrow 3 + 1 = \mathbf{4}$.
  - Update DP table: $f[4][4] \leftarrow 0 + 1 + 1 = \mathbf{2}$.
- $j = 3$ ($nums[3] = 8$):
  - $d = 10 - 8 = 2$.
  - Existing at $j=3$: $f[3][2] = 3$ ($[6, 8], [4, 6, 8], [2, 4, 6, 8]$).
  - Appending $nums[4]$ forms $[6, 8, 10], [4, 6, 8, 10], [2, 4, 6, 8, 10]$ (all length $\ge 3$!).
  - **Contribution to answer:** $ans \leftarrow 4 + 3 = \mathbf{7}$.
  - Update DP table: $f[4][2] \leftarrow 0 + 3 + 1 = \mathbf{4}$.

---

### Termination:
All pairs evaluated. Total answer: **`7`**.

---

## 4. Complete Execution Trace

| Pair $(j, i)$ | Values $(nums[j], nums[i])$ | Diff $d$ | Prior Count $f[j][d]$ | New Valid Slices ($\ge 3$) Formed | Cumulative $ans$ | Table Update $f[i][d]$ |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|
| $(0, 1)$ | $(2, 4)$ | $2$ | $0$ | None | $0$ | $f[1][2] \leftarrow 1$ |
| $(0, 2)$ | $(2, 6)$ | $4$ | $0$ | None | $0$ | $f[2][4] \leftarrow 1$ |
| $(1, 2)$ | $(4, 6)$ | $2$ | $1$ | $[2, 4, 6]$ | **$1$** | $f[2][2] \leftarrow 2$ |
| $(0, 3)$ | $(2, 8)$ | $6$ | $0$ | None | $1$ | $f[3][6] \leftarrow 1$ |
| $(1, 3)$ | $(4, 8)$ | $4$ | $0$ | None | $1$ | $f[3][4] \leftarrow 1$ |
| $(2, 3)$ | $(6, 8)$ | $2$ | $2$ | $[4, 6, 8], \; [2, 4, 6, 8]$ | **$3$** | $f[3][2] \leftarrow 3$ |
| $(0, 4)$ | $(2, 10)$| $8$ | $0$ | None | $3$ | $f[4][8] \leftarrow 1$ |
| $(1, 4)$ | $(4, 10)$| $6$ | $0$ | None | $3$ | $f[4][6] \leftarrow 1$ |
| $(2, 4)$ | $(6, 10)$| $4$ | $1$ | $[2, 6, 10]$ | **$4$** | $f[4][4] \leftarrow 2$ |
| $(3, 4)$ | $(8, 10)$| $2$ | $3$ | $[6, 8, 10], \; [4, 6, 8, 10], \; [2, 4, 6, 8, 10]$ | **$7$** | $f[4][2] \leftarrow 4$ |

---

## 5. Boundary Cases & Failure Modes

- **Length Less Than 3 ($nums = [1, 2]$):** Outer loop runs for $(0, 1)$, but $f[0][1] = 0 \implies ans = 0$.
- **All Elements Equal ($nums = [7, 7, 7, 7, 7]$):** $d = 0$ for all pairs. Every combination of 3 or more elements forms an arithmetic subsequence:
  $$
  \sum_{k=3}^5 \binom{5}{k} = 10 + 5 + 1 = \mathbf{16}
  $$
- **Extreme Differences / Integer Overflow:** Differences between elements can be up to $2^{31} - (-2^{31}) = 2^{32}$. Using 64-bit integer differences prevents arithmetic sign overflow.
- **Negative Elements ($nums = [-3, -1, 1, 3]$):** Arithmetic transitions with negative values and steps behave identically without adjustments.

---

## 6. Traps & Common Anti-Patterns

- **Adding 1 Directly to Answer:** Adding $1$ to $ans$ at every pair $(j, i)$ counts 2-element pairs as valid arithmetic slices. The $+1$ belongs strictly in $f[i][d]$ to account for future extensions, while $ans$ receives only $f[j][d]$.
- **Static 2D Matrix for DP:** The range of possible differences $d$ is $[-2 \times 10^9, 2 \times 10^9]$, making a direct 2D array impossible. Using an array of hash maps `f = [defaultdict(int) for _ in nums]` stores only observed differences.
- **Overwriting Instead of Accumulating:** Writing $f[i][d] = f[j][d] + 1$ instead of $f[i][d] \mathrel{+}= f[j][d] + 1$ destroys counts when multiple prior elements $j_1, j_2$ produce the same difference $d$ (e.g. duplicate values).

---

## 7. Complexity Derivation

- **Time Complexity:**
  - The nested loops iterate over all $\binom{N}{2} = \frac{N(N-1)}{2}$ pairs $(j, i)$.
  - Hash map lookups and additions take $O(1)$ average time.
  - Total Time: $\mathcal{O}(N^2)$. For $N = 1000$, $\approx 5 \times 10^5$ operations, completing in under 40 ms.
- **Auxiliary Space Complexity:**
  - Each of the $N$ hash maps holds at most $N$ difference keys.
  - Total Auxiliary Space: $\mathcal{O}(N^2)$ to store the DP table.
