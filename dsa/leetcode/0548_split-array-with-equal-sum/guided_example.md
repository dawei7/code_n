# Guided Example: Split Array with Equal Sum

We trace the step-by-step 4-way partition geometry ($0 < i < j < k < n-1$), excluded divider elements ($nums[i], nums[j], nums[k]$), middle-pivot decomposition ($j$), prefix sum interval calculation ($s[r] - s[l]$), left candidate sum set caching ($seen$), right candidate congruence matching, and $O(N^2)$ bipartite verification on representative arrays:

- **Input:** $nums = [1, 2, 1, 2, 1, 2, 1]$
- **Required output:** `true`
  - Array length: $n = 7$ (minimal valid length for 4 non-empty partitions and 3 divider elements).
  - Triplet divider specification: Three indices $(i, j, k)$ satisfying:
    $$
    0 < i, \quad i + 1 < j, \quad j + 1 < k, \quad k < n - 1
    $$
  - Excluded divider elements: $nums[i], \; nums[j], \; nums[k]$.
  - The 4 resulting non-empty contiguous segments must have equal sum:
    1. $S_1 = \sum_{m=0}^{i-1} nums[m]$
    2. $S_2 = \sum_{m=i+1}^{j-1} nums[m]$
    3. $S_3 = \sum_{m=j+1}^{k-1} nums[m]$
    4. $S_4 = \sum_{m=k+1}^{n-1} nums[m]$
    Requirement: $S_1 = S_2 = S_3 = S_4$.
- **Middle-Pivot Decomposition Trace:**
  - Prefix sum array $s$ of size $n + 1 = 8$:
    $$
    s = [0, \; 1, \; 3, \; 4, \; 6, \; 7, \; 9, \; 10]
    $$
  - Iterate middle divider $j \in [3, n - 4] = [3, 3]$:
    - **Fix $j = 3$ ($nums[3] = 2$):**
      - Left half encompasses indices $0 \dots 2$ (`[1, 2, 1]`).
      - Right half encompasses indices $4 \dots 6$ (`[1, 2, 1]`).
      - **Step A: Search Left Divider $i \in [1, j - 2] = [1, 1]$:**
        - Test $i = 1$ ($nums[1] = 2$):
          - Segment 1 ($0 \dots 0$):
            $$
            S_1 = s[1] - s[0] = 1 - 0 = \mathbf{1}
            $$
          - Segment 2 ($2 \dots 2$):
            $$
            S_2 = s[3] - s[2] = 6 - 4 = 2 \text{ ? Wait, } s[i+1] = s[2] = 3 \implies 6 - 3 = \mathbf{1}
            $$
            Let's verify: $nums[2 \dots 2]$ contains $[1]$, sum is $1$.
          - $S_1 == S_2 == 1$!
          - Record valid left sum in hash set:
            $$
            seen = \{\mathbf{1}\}
            $$
      - **Step B: Search Right Divider $k \in [j + 2, n - 2] = [5, 5]$:**
        - Test $k = 5$ ($nums[5] = 2$):
          - Segment 3 ($4 \dots 4$):
            $$
            S_3 = s[5] - s[4] = 7 - 6 = \mathbf{1} \quad (nums[4] = 1)
            $$
          - Segment 4 ($6 \dots 6$):
            $$
            S_4 = s[7] - s[6] = 10 - 9 = \mathbf{1} \quad (nums[6] = 1)
            $$
          - Check right equality: $S_3 == S_4 == 1$.
          - Check left-right congruence: Is $1 \in seen$? **Yes!**
          - All 4 segments equal $1$:
            $$
            S_1 = S_2 = S_3 = S_4 = \mathbf{1}
            $$
          - Triplet $(i=1, j=3, k=5)$ verified!
          - Early return: **`true`**.
- **Structural Partition Breakdown:**
  ```text
  nums:      [ 1,   (2),   1,   (2),   1,   (2),   1 ]
  Dividers:         i=1         j=3         k=5
  Segment 1: [ 1 ]             -> sum = 1
  Segment 2:        [ 1 ]      -> sum = 1
  Segment 3:              [ 1 ] -> sum = 1
  Segment 4:                    [ 1 ] -> sum = 1
  ```
- **Failing Parity Instance ($nums = [1, 2, 1, 2, 1, 2, 2]$):**
  - Left segments equal 1, but right segments equal 1 and 2 $\implies$ no match $\implies \mathbf{false}$.
- **Length Too Short ($n < 7$):**
  - 4 segments $\ge 1$ plus 3 dividers requires at least $4 + 3 = 7$ elements. Any $n < 7 \implies \mathbf{false}$.

This instance demonstrates middle-pivot divide-and-conquer decoupling, mathematically proves why anchoring the middle divider reduces 3D search space from $O(N^3)$ to $O(N^2)$, and derives $O(N^2)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums$ of length $n$:
Determine if there exists a triplet of indices $(i, j, k)$ with:
$$
0 < i < i + 1 < j < j + 1 < k < n - 1
$$
such that removing $nums[i], nums[j], nums[k]$ leaves four subarrays with equal sums:
$$
\sum(0 \dots i-1) = \sum(i+1 \dots j-1) = \sum(j+1 \dots k-1) = \sum(k+1 \dots n-1)
$$

```text
Array: [ 1,  2,  1,  2,  1,  2,  1 ]
          \  |   /   |    \  |   /
Segment 1:  [1]     i=1
Segment 2:      [1]      j=3
Segment 3:          [1]     k=5
Segment 4:              [1]

All 4 segments sum to 1 -> Valid split!
```

### The Middle-Pivot Decoupling Principle
- A brute-force search over all triplets $(i, j, k)$ takes $O(N^3)$ time, causing TLE for $N = 2000$ ($2000^3 = 8 \times 10^9$).
- By **fixing the middle divider $j$**:
  - The left half (indices $0 \dots j - 1$) and the right half (indices $j + 1 \dots n - 1$) become **completely independent**!
  - We scan all candidates for $i \in [1, j - 2]$ and store every valid equal sum in a hash set `seen`.
  - We then scan candidates for $k \in [j + 2, n - 2]$; if the two right segments are equal AND their sum is in `seen`, we have found a valid split!
  - Complexity drops from $O(N^3)$ to $O(N^2)$.

---

## 2. Conceptual Foundation & Invariants

### 1. Prefix Sum Representation:
Let $s$ be the prefix sum array: $s[m] = \sum_{p=0}^{m-1} nums[p]$.
The sum of subarray $nums[l \dots r]$ is $s[r + 1] - s[l]$.
- Segment 1: $s[i]$
- Segment 2: $s[j] - s[i + 1]$
- Segment 3: $s[k] - s[j + 1]$
- Segment 4: $s[n] - s[k + 1]$

### 2. The Middle-Pivot Algorithm:
For each middle pivot $j \in [3, n - 4]$:
1. Initialize `seen = set()`.
2. For $i \in [1, j - 2]$:
   If $s[i] == s[j] - s[i + 1]$:
   Add $s[i]$ to `seen`.
3. For $k \in [j + 2, n - 2]$:
   If $s[k] - s[j + 1] == s[n] - s[k + 1]$ and $(s[n] - s[k + 1]) \in seen$:
   Return `True`.
If no valid triplet is found, return `False`.

> **Independent Subproblem Invariant.** Because $i < j < k$, choice of $i$ depends only on $j$, and choice of $k$ depends only on $j$. Factoring through $j$ eliminates all cross-term dependencies between $i$ and $k$.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [1, 2, 1, 2, 1, 2, 1]$ ($n = 7$):

---

### Step 1: Precompute Prefix Sums
$$
s = [0, \; 1, \; 3, \; 4, \; 6, \; 7, \; 9, \; 10]
$$

---

### Step 2: Evaluate Pivot $j = 3$ ($nums[3] = 2$)
Valid ranges:
- $i \in [1, 3 - 2] = [1, 1]$.
- $k \in [3 + 2, 7 - 2] = [5, 5]$.

#### Part A: Left Scan ($i = 1$)
- Segment 1: $s[1] = 1$.
- Segment 2: $s[3] - s[2] = 4 - 3 = 1$.
- Sums match: $1 == 1$.
- Add to set:
  $$
  seen = \{1\}
  $$

#### Part B: Right Scan ($k = 5$)
- Segment 3: $s[5] - s[4] = 7 - 6 = 1$.
- Segment 4: $s[7] - s[6] = 10 - 9 = 1$.
- Sums match: $1 == 1$.
- Membership check: Is $1 \in seen$? **Yes!**

---

### Step 3: Emit Output
All 4 segments equal $1$.
Return **`True`**.

---

## 4. Complete Execution Trace

| Pivot $j$ | Left Divider $i$ | Seg 1 Sum $s[i]$ | Seg 2 Sum $s[j] - s[i+1]$ | $seen$ Set | Right Divider $k$ | Seg 3 Sum | Seg 4 Sum | Match Found? |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **$3$** | **$1$** | $1$ | $4 - 3 = 1$ | $\{1\}$ | **$5$** | $7 - 6 = 1$ | $10 - 9 = 1$ | **Yes ($1 \in seen$)** |
| **Result** | — | — | — | — | — | — | — | **`True`** |

---

## 5. Boundary Cases & Failure Modes

- **Minimum Length Array ($n = 7$):** Only one choice: $i=1, j=3, k=5$. Handled cleanly.
- **Length $< 7$:** Impossible to have 4 non-empty segments and 3 dividers $\implies$ loop range $[3, n-4]$ is empty $\implies$ returns $\mathbf{False}$.
- **Zero Values in Array ($[0, 0, 0, 0, 0, 0, 0]$):** All 4 segments sum to 0 $\implies$ returns $\mathbf{True}$.
- **Negative Elements:** Prefix sum subtraction correctly computes signed sums; hash set handles negative sums seamlessly.

---

## 6. Traps & Common Anti-Patterns

- **Searching Triplets with $O(N^3)$ Loops:** Running three nested loops causes TLE for $N = 2000$. Middle-pivot hashing reduces runtime to $O(N^2)$.
- **Including Divider Elements in Subarray Sums:** The dividers $nums[i], nums[j], nums[k]$ are dropped from the sum. Using $s[i]$ for Segment 1 and $s[j] - s[i+1]$ for Segment 2 excludes $nums[i]$ correctly.
- **Reusing `seen` Set Across Different $j$ Pivots:** The set `seen` must be re-initialized for each value of $j$. Carrying over seen values from an earlier $j$ would allow left segments from one pivot to pair with right segments from a different pivot.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Prefix sum array calculation: $O(N)$.
  - Outer loop runs $N - 6$ times ($O(N)$).
  - Inside the loop, left scan runs at most $j$ times ($O(N)$) and right scan runs at most $N - j$ times ($O(N)$).
  - Total Time: $\mathcal{O}(N^2)$. For $N = 2000$, $2000^2 / 2 \approx 2 \times 10^6$ operations, completing in $< 40$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space for the prefix sum array and candidate set `seen`.
