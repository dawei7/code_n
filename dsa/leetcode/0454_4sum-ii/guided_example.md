# Guided Example: 4Sum II

We trace the step-by-step Meet-in-the-Middle quadratic partition ($O(N^4) \to O(N^2)$), pairwise sum histogramming ($a + b$), negation complement lookup ($-(c + d)$), and combinatorial tuple accumulation on representative four-array instances:

- **Input:**
  - $nums_1 = [1, 2]$
  - $nums_2 = [-2, -1]$
  - $nums_3 = [-1, 2]$
  - $nums_4 = [0, 2]$
- **Required output:** `2`
  - Array length: $n = 2$.
  - Target condition: $nums_1[i] + nums_2[j] + nums_3[k] + nums_4[l] = 0$.
- **Execution trace:**
  - **Phase 1: Compute pairwise sums for $(nums_1, nums_2)$:**
    - Pair $(1, -2) \implies 1 + (-2) = -1$
    - Pair $(1, -1) \implies 1 + (-1) = 0$
    - Pair $(2, -2) \implies 2 + (-2) = 0$
    - Pair $(2, -1) \implies 2 + (-1) = 1$
    - Frequency histogram:
      $$
      cnt = \{-1: 1, \; 0: 2, \; 1: 1\}
      $$
  - **Phase 2: Query complementary sums for $(nums_3, nums_4)$:**
    - Pair $(-1, 0): c + d = -1$.
      - Required complement: $-(c + d) = -(-1) = \mathbf{1}$.
      - Lookup in $cnt$: $cnt[1] = \mathbf{1}$
      - Contributes 1 tuple: $(nums_1[1], nums_2[1], nums_3[0], nums_4[0]) \implies 2 + (-1) + (-1) + 0 = 0$.
    - Pair $(-1, 2): c + d = 1$.
      - Complement: $-(1) = \mathbf{-1}$.
      - Lookup in $cnt$: $cnt[-1] = \mathbf{1}$
      - Contributes 1 tuple: $(nums_1[0], nums_2[0], nums_3[0], nums_4[1]) \implies 1 + (-2) + (-1) + 2 = 0$.
    - Pair $(2, 0): c + d = 2$.
      - Complement: $-2$. $cnt[-2] = \mathbf{0}$.
    - Pair $(2, 2): c + d = 4$.
      - Complement: $-4$. $cnt[-4] = \mathbf{0}$.
  - Total valid zero-sum tuples: $1 + 1 + 0 + 0 = \mathbf{2}$.
- **All Zeros Instance:** $nums_1 = nums_2 = nums_3 = nums_4 = [0] \implies 0 + 0 + 0 + 0 = 0 \implies \mathbf{1}$
- **No Zero Sum Possible:** $nums_1 = [1], nums_2 = [1], nums_3 = [1], nums_4 = [1] \implies \text{sum} = 4 \ne 0 \implies \mathbf{0}$

This instance demonstrates the classical Meet-in-the-Middle algorithmic optimization, mathematically proves how splitting $N^4$ states into two $N^2$ independent subsets reduces asymptotic runtime, and derives $O(N^2)$ runtime and $O(N^2)$ space bounds.

---

## 1. Instance & Teaching Goal

Given four integer arrays $nums_1, nums_2, nums_3, nums_4$ each of length $n = 2$:
Find the number of tuples $(i, j, k, l)$ such that:
$$
nums_1[i] + nums_2[j] + nums_3[k] + nums_4[l] = 0
$$

```text
Input Arrays:
  nums1 = [ 1,  2 ]
  nums2 = [-2, -1 ]
  nums3 = [-1,  2 ]
  nums4 = [ 0,  2 ]

Two Valid Zero-Sum Tuples:
  Tuple 1: nums1[0] + nums2[0] + nums3[0] + nums4[1] =  1 + (-2) + (-1) + 2 = 0
  Tuple 2: nums1[1] + nums2[1] + nums3[0] + nums4[0] =  2 + (-1) + (-1) + 0 = 0

Total Count: 2
```

### The Meet-in-the-Middle Paradigm
A brute-force search iterates through 4 nested loops, taking $O(n^4)$ time.
For $n = 200$, $n^4 = 1.6 \times 10^9$ operations, which severely exceeds time limits.
We rearrange the equation by grouping:
$$
(nums_1[i] + nums_2[j]) + (nums_3[k] + nums_4[l]) = 0
$$
$$
(nums_1[i] + nums_2[j]) = -(nums_3[k] + nums_4[l])
$$
By computing all $n^2$ pairwise sums of $(nums_1, nums_2)$ and storing their frequencies in a hash map, each pair of $(nums_3, nums_4)$ checks for matching pairs in $O(1)$ time.
The time complexity drops quadratically from $O(n^4)$ to $O(n^2)$.

---

## 2. Conceptual Foundation & Invariants

### 1. The Pairwise Hash Map Decomposition:
1. **Left Half Generation:**
   Construct a frequency map $cnt$ over all pairs $(a, b) \in nums_1 \times nums_2$:
   $$
   cnt[s] = \sum_{a \in nums_1} \sum_{b \in nums_2} \mathbf{1}[a + b == s]
   $$
   This produces at most $n^2$ entries in $O(n^2)$ time.
2. **Right Half Querying:**
   Iterate over all pairs $(c, d) \in nums_3 \times nums_4$:
   For each sum $c + d$, look up its algebraic negation $-(c + d)$ in $cnt$:
   $$
   \text{Total Tuples} = \sum_{c \in nums_3} \sum_{d \in nums_4} cnt[-(c + d)]
   $$

> **Bipartite Invariant.** The total number of valid 4-tuples equals the sum of Cartesian cross-product multiplicities between left-side sum buckets $a + b$ and complementary right-side sum buckets $-(c + d)$.

---

## 3. Step-by-Step Worked Execution

We trace the sample with $n = 2$:

---

### Step 1: Populate Left Sum Histogram
Iterate over all $2 \times 2 = 4$ pairs of $(nums_1, nums_2)$:
- $a = nums_1[0] = 1, \; b = nums_2[0] = -2 \implies 1 + (-2) = \mathbf{-1}$.
  - $cnt[-1] \leftarrow 1$.
- $a = nums_1[0] = 1, \; b = nums_2[1] = -1 \implies 1 + (-1) = \mathbf{0}$.
  - $cnt[0] \leftarrow 1$.
- $a = nums_1[1] = 2, \; b = nums_2[0] = -2 \implies 2 + (-2) = \mathbf{0}$.
  - $cnt[0] \leftarrow 2$.
- $a = nums_1[1] = 2, \; b = nums_2[1] = -1 \implies 2 + (-1) = \mathbf{1}$.
  - $cnt[1] \leftarrow 1$.
Resulting map:
$$
cnt = \{-1: 1, \quad 0: 2, \quad 1: 1\}
$$

---

### Step 2: Query Right Sum Complements
Iterate over all $2 \times 2 = 4$ pairs of $(nums_3, nums_4)$:
Initialize $ans = 0$.

1. **Pair $(nums_3[0], nums_4[0]) = (-1, 0)$:**
   - Sum: $c + d = -1 + 0 = -1$.
   - Target complement: $-(c + d) = -(-1) = \mathbf{1}$.
   - Query: $cnt[1] = \mathbf{1}$.
   - Update: $ans \leftarrow 0 + 1 = \mathbf{1}$.

2. **Pair $(nums_3[0], nums_4[1]) = (-1, 2)$:**
   - Sum: $c + d = -1 + 2 = 1$.
   - Target complement: $-(c + d) = -(1) = \mathbf{-1}$.
   - Query: $cnt[-1] = \mathbf{1}$.
   - Update: $ans \leftarrow 1 + 1 = \mathbf{2}$.

3. **Pair $(nums_3[1], nums_4[0]) = (2, 0)$:**
   - Sum: $c + d = 2 + 0 = 2$.
   - Target complement: $-2$.
   - Query: $cnt[-2] = \mathbf{0}$.
   - $ans$ unchanged.

4. **Pair $(nums_3[1], nums_4[1]) = (2, 2)$:**
   - Sum: $c + d = 2 + 2 = 4$.
   - Target complement: $-4$.
   - Query: $cnt[-4] = \mathbf{0}$.
   - $ans$ unchanged.

---

### Final Result:
Total zero-sum tuples: **`2`**.

---

## 4. Complete Execution Trace

| Right Pair $(c, d)$ | Right Sum $c + d$ | Target Complement $-(c + d)$ | Frequency in $cnt$ | Tuples Matched | Cumulative Count |
|:---:|:---:|:---:|:---:|:---|:---:|
| $(-1, 0)$ | $-1$ | **$1$** | $1$ | $(2, -1, -1, 0)$ | **$1$** |
| $(-1, 2)$ | $1$ | **$-1$** | $1$ | $(1, -2, -1, 2)$ | **$2$** |
| $(2, 0)$ | $2$ | $-2$ | $0$ | None | $2$ |
| $(2, 2)$ | $4$ | $-4$ | $0$ | None | **$2$** |

---

## 5. Boundary Cases & Failure Modes

- **Minimum Size ($n = 1$):** Exactly 1 sum on left and 1 sum on right. Checks if $a + b + c + d == 0 \implies 1$ or $0$.
- **All Zero Arrays ($nums_1 = nums_2 = nums_3 = nums_4 = [0] \times n$):** All left sums are 0 ($cnt[0] = n^2$). All right sums are 0 ($target = 0$). Emits $n^2 \times n^2 = n^4$ tuples.
- **Large Arrays ($n = 200$):** $n^2 = 4 \times 10^4$ pairs. Map insertion takes $40,000$ operations, and queries take $40,000$ operations. Total $\approx 8 \times 10^4$ steps (executes in $< 15$ ms).

---

## 6. Traps & Common Anti-Patterns

- **Asymmetric Grouping (1 vs 3 Arrays):** Grouping 1 array against 3 arrays results in $O(n + n^3) = O(n^3)$ runtime. Symmetrical $2 \times 2$ partition balances work to optimal $O(n^2 + n^2) = O(n^2)$.
- **Key Missing Exceptions in Hash Maps:** In languages requiring explicit key checks, accessing `cnt[target]` without checking `containsKey` throws errors when no matching sum exists. Using `getOrDefault(target, 0)` or Python's `defaultdict(int)` handles missing complements safely.
- **Index Duplication Misconception:** In 4Sum II, elements are drawn from 4 **distinct arrays** $nums_1, nums_2, nums_3, nums_4$, so duplicate values or reusing the same index across different arrays is completely permitted.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Generating sums of $(nums_1, nums_2)$ takes $O(n^2)$ time.
  - Querying sums of $(nums_3, nums_4)$ takes $O(n^2)$ time with $O(1)$ average hash lookups.
  - Total Time: $\mathcal{O}(n^2)$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(n^2)$ auxiliary space to store the frequency map of up to $n^2$ distinct sum values.
