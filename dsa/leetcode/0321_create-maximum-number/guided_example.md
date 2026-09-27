# Guided Example: Create Maximum Number

We trace the step-by-step split partition enumeration ($x \in [\max(0, k-n), \min(k, m)]$), monotonic stack single-array maximum subsequence extraction, lexicographical suffix tie-breaking merge, and global maximum number construction on representative two-array instances:

- **Input:**
  $$
  \text{nums1} = [3, 4, 6, 5], \quad \text{nums2} = [9, 1, 2, 5, 8, 3], \quad k = 5
  $$
- **Required output:** $[9, 8, 6, 5, 3]$
  - Split $x = 2$ digits from $\text{nums1}$ and $k - x = 3$ digits from $\text{nums2}$:
    - Optimal subsequence of length 2 from $\text{nums1}$: $[6, 5]$
    - Optimal subsequence of length 3 from $\text{nums2}$: $[9, 8, 3]$
    - Lexicographical suffix merge of $[6, 5]$ and $[9, 8, 3]$ produces $\mathbf{[9, 8, 6, 5, 3]}$
- **All Digits From One Array:** When $k \le n$, a split of $x = 0$ takes all $k$ digits from $\text{nums2}$
- **Suffix Tie-Breaking Trap:** With candidates $[6, 7]$ and $[6, 0, 4]$, comparing only the head ($6 == 6$) is insufficient; comparing full remaining suffixes correctly picks from $[6, 7]$ first

This instance demonstrates three-tier greedy decomposition: split-range bounding, monotonic stack subsequence reduction, and lookahead suffix merging. It mathematically proves why greedy suffix comparison is necessary to prevent premature suboptimal commitments, and analyzes $O(k \cdot (m + n + k))$ time and $O(k)$ space bounds.

---

## 1. Instance & Teaching Goal

Given two digit arrays:
- $\text{nums1} = [3, 4, 6, 5]$ ($m = 4$)
- $\text{nums2} = [9, 1, 2, 5, 8, 3]$ ($n = 6$)
- $k = 5$

Form the largest 5-digit number possible by taking a subsequence of digits from $\text{nums1}$ and $\text{nums2}$ while preserving their relative order within each original array:

```text
nums1: [3, 4, 6, 5]
nums2: [9, 1, 2, 5, 8, 3]
Target: 5 digits

Candidate Splits:
x = 0: []            + [9, 2, 5, 8, 3] -> [9, 2, 5, 8, 3]
x = 1: [6]           + [9, 5, 8, 3]    -> [9, 6, 5, 8, 3]
x = 2: [6, 5]        + [9, 8, 3]       -> [9, 8, 6, 5, 3]  (GLOBAL MAXIMUM!)
x = 3: [4, 6, 5]     + [9, 8]          -> [9, 8, 4, 6, 5]
x = 4: [3, 4, 6, 5]  + [9]             -> [9, 3, 4, 6, 5]

Optimal Result: [9, 8, 6, 5, 3]
```

### The Three-Phase Decomposition:
1. **Split Enumeration:** Test all valid counts $x$ of digits taken from $\text{nums1}$, where $k - x$ digits are taken from $\text{nums2}$.
2. **Subsequence Optimization $f(nums, len)$:** Use a monotonic stack to extract the single best subsequence of length $len$ from each array in linear time.
3. **Lexicographical Merge:** Merge the two extracted subsequences into the largest combined sequence by always taking from whichever array has the lexicographically larger remaining suffix.

---

## 2. Conceptual Foundation & Invariants

### 1. Feasible Split Bounds
$x$ digits are chosen from $\text{nums1}$ (length $m$) and $k - x$ from $\text{nums2}$ (length $n$):
- $0 \le x \le m$
- $0 \le k - x \le n \iff k - n \le x \le k$
Combining yields the inclusive bounds:
$$
\max(0, k - n) \le x \le \min(k, m)
$$
For $m = 4, n = 6, k = 5$:
$l = \max(0, 5 - 6) = 0$, $r = \min(5, 4) = 4$. So $x \in [0, 4]$.

### 2. Monotonic Stack Subsequence Extraction `f(nums, k)`
To keep $k$ digits from an array of length $N$, we must discard exactly $remain = N - k$ digits:
- As we iterate through $x \in nums$:
  - While $top \ge 0$, and $stk[top] < x$, and $remain > 0$:
    - Pop $stk[top]$ and decrement $remain \mathrel{-}= 1$.
  - If $top + 1 < k$: push $x$.
  - Else: discard $x$ and decrement $remain \mathrel{-}= 1$.
- Returns the lexicographically maximal subsequence of length $k$.

### 3. Suffix Comparison Merge
When merging `arr1` and `arr2`, if `arr1[i] == arr2[j]`, taking arbitrarily can cause wrong answers!
We must compare the entire remaining suffixes:
$$
\text{compare}(arr_1[i \dots], \; arr_2[j \dots])
$$
Take the head element from whichever remaining suffix is lexicographically larger.

> **Invariant.** For a fixed split $(x, k-x)$, the independently optimal subsequences $arr_1$ and $arr_2$ merged via suffix lookahead produce the globally optimal sequence for that split.

---

## 3. Step-by-Step Worked Execution

We trace the candidate splits for $\text{nums1} = [3, 4, 6, 5]$, $\text{nums2} = [9, 1, 2, 5, 8, 3]$, $k = 5$:

---

### Step 1: Evaluate Split $x = 0$ ($0$ from $\text{nums1}$, $5$ from $\text{nums2}$)
- $arr_1 = f(\text{nums1}, 0) = []$.
- $arr_2 = f(\text{nums2}, 5)$:
  - Length $n = 6$, budget $remain = 6 - 5 = 1$ deletion.
  - Traverse $[9, 1, 2, 5, 8, 3]$: digit $1$ is popped when $2$ arrives ($1$ deletion spent).
  - $arr_2 = [9, 2, 5, 8, 3]$.
- Merged: $[9, 2, 5, 8, 3]$.

---

### Step 2: Evaluate Split $x = 1$ ($1$ from $\text{nums1}$, $4$ from $\text{nums2}$)
- $arr_1 = f(\text{nums1}, 1) = [6]$ (Maximum single digit).
- $arr_2 = f(\text{nums2}, 4)$:
  - Budget $remain = 6 - 4 = 2$ deletions.
  - Digits $1$ and $2$ popped when $5$ arrives.
  - $arr_2 = [9, 5, 8, 3]$.
- Suffix merge of $[6]$ and $[9, 5, 8, 3]$:
  - $9 > 6 \implies$ pick $9$ from $\text{nums2}$.
  - Remaining: $[6]$ vs $[5, 8, 3] \implies 6 > 5 \implies$ pick $6$ from $\text{nums1}$.
  - Remaining $\text{nums2}$ flushes: $[5, 8, 3]$.
  - Candidate: $[9, 6, 5, 8, 3]$.

---

### Step 3: Evaluate Split $x = 2$ ($2$ from $\text{nums1}$, $3$ from $\text{nums2}$)
- $arr_1 = f(\text{nums1}, 2)$:
  - $m = 4$, $remain = 4 - 2 = 2$ deletions.
  - In $[3, 4, 6, 5]$, digits $3$ and $4$ are popped when $6$ arrives.
  - $arr_1 = [6, 5]$.
- $arr_2 = f(\text{nums2}, 3)$:
  - $n = 6$, $remain = 6 - 3 = 3$ deletions.
  - In $[9, 1, 2, 5, 8, 3]$, digits $1, 2, 5$ are deleted before $8$.
  - $arr_2 = [9, 8, 3]$.
- Suffix merge of $[6, 5]$ and $[9, 8, 3]$:
  1. Compare $[6, 5]$ vs $[9, 8, 3] \implies 9 > 6 \implies$ pick **9** (from $\text{nums2}$).
  2. Compare $[6, 5]$ vs $[8, 3] \implies 8 > 6 \implies$ pick **8** (from $\text{nums2}$).
  3. Compare $[6, 5]$ vs $[3] \implies 6 > 3 \implies$ pick **6** (from $\text{nums1}$).
  4. Compare $[5]$ vs $[3] \implies 5 > 3 \implies$ pick **5** (from $\text{nums1}$).
  5. Remaining from $\text{nums2}$: pick **3**.
- Merged Candidate:
  $$
  \mathbf{[9, 8, 6, 5, 3]}
  $$

---

### Step 4: Evaluate Split $x = 3$ ($3$ from $\text{nums1}$, $2$ from $\text{nums2}$)
- $arr_1 = f(\text{nums1}, 3) = [4, 6, 5]$.
- $arr_2 = f(\text{nums2}, 2) = [9, 8]$.
- Merged Candidate: $[9, 8, 4, 6, 5]$.

---

### Step 5: Evaluate Split $x = 4$ ($4$ from $\text{nums1}$, $1$ from $\text{nums2}$)
- $arr_1 = f(\text{nums1}, 4) = [3, 4, 6, 5]$.
- $arr_2 = f(\text{nums2}, 1) = [9]$.
- Merged Candidate: $[9, 3, 4, 6, 5]$.

---

### Step 6: Global Maximum Selection
Comparing all 5 merged candidates lexicographically:
- $x = 0: [9, 2, 5, 8, 3]$
- $x = 1: [9, 6, 5, 8, 3]$
- $x = 2: \mathbf{[9, 8, 6, 5, 3]}$ (Maximum!)
- $x = 3: [9, 8, 4, 6, 5]$
- $x = 4: [9, 3, 4, 6, 5]$

Winner:
$$
\mathbf{[9, 8, 6, 5, 3]}
$$

---

## 4. Complete Execution Trace

```text
nums1 = [3, 4, 6, 5], nums2 = [9, 1, 2, 5, 8, 3], k = 5
Split range: x in [0, 4]

Split x=0: arr1=[],         arr2=[9,2,5,8,3] -> merge: [9, 2, 5, 8, 3]
Split x=1: arr1=[6],        arr2=[9,5,8,3]   -> merge: [9, 6, 5, 8, 3]
Split x=2: arr1=[6, 5],     arr2=[9,8,3]     -> merge: [9, 8, 6, 5, 3] (MAX!)
Split x=3: arr1=[4, 6, 5],  arr2=[9,8]       -> merge: [9, 8, 4, 6, 5]
Split x=4: arr1=[3,4,6,5],  arr2=[9]         -> merge: [9, 3, 4, 6, 5]

Global Best: [9, 8, 6, 5, 3]
```

| Split $x$ | $arr_1 = f(\text{nums1}, x)$ | $arr_2 = f(\text{nums2}, k-x)$ | Suffix Comparisons During Merge | Merged Result | Better than Current Best? |
|:---:|:---:|:---:|:---|:---:|:---:|
| 0 | `[]` | `[9, 2, 5, 8, 3]` | `nums2` copied | `[9, 2, 5, 8, 3]` | Yes (`[9, 2, ...]`) |
| 1 | `[6]` | `[9, 5, 8, 3]` | $9 > 6$, then $6 > 5$ | `[9, 6, 5, 8, 3]` | Yes (`[9, 6, ...]`) |
| **2** | **`[6, 5]`** | **`[9, 8, 3]`** | **$9>6$, $8>6$, $6>3$, $5>3$** | **`[9, 8, 6, 5, 3]`** | **Yes (`[9, 8, 6, ...]`)** |
| 3 | `[4, 6, 5]` | `[9, 8]` | $9>4$, $8>4$, rest from `nums1` | `[9, 8, 4, 6, 5]` | No ($4 < 6$) |
| 4 | `[3, 4, 6, 5]` | `[9]` | $9>3$, rest from `nums1` | `[9, 3, 4, 6, 5]` | No ($3 < 8$) |

---

## 5. Algorithmic Correctness

**Soundness.** For any fixed split $x$, the monotonic stack extracts the lexicographically largest subsequence from each array. When merging, comparing remaining suffixes guarantees that ties at the current heads are broken by the first differing downstream digit. This greedy choice is provably optimal because placing a larger digit earlier yields a larger number.

**Completeness.** Any valid combination of $k$ digits must draw some count $x$ from $\text{nums1}$ and $k - x$ from $\text{nums2}$. Since $x$ ranges over all mathematically feasible integers in $[\max(0, k-n), \min(k, m)]$, the global maximum across all possible selections is guaranteed to be evaluated.

---

## 6. Traps This Instance Exposes

- **Local Head Comparison in Merge:** If `arr1[i] == arr2[j]`, choosing from `arr1` vs `arr2` arbitrarily leads to incorrect results. For example, merging `[6, 7]` and `[6, 0, 4]`: both heads are $6$. Choosing from `[6, 0, 4]` produces `[6, 6, 7, 0, 4]`, but choosing from `[6, 7]` produces `[6, 7, 6, 0, 4]`, which is larger. Comparing full suffixes (`compare(nums1, nums2, i, j)`) is mandatory.
- **Split Bound Calculation:** Hardcoding $x$ from $0$ to $k$ causes out-of-bounds requests when $k > n$ (demanding negative digits from `nums2`) or $k > m$. The bounds $\max(0, k - n) \le x \le \min(k, m)$ must be strictly enforced.
- **Monotonic Stack Deletion Budget:** Without tracking `remain = N - k`, popping smaller digits could leave fewer than $k$ elements in the stack.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(k \cdot (m + n + k^2))$.
  - Number of splits $x$ tested is at most $k + 1 = O(k)$.
  - For each split:
    - Subsequence extraction $f$ runs in $O(m + n)$ time.
    - Suffix merge performs $k$ steps; each step compares suffixes of length at most $k$, taking $O(k^2)$ time.
  - For $m, n \le 500, k \le 1000$, total operations are on the order of $10^6$, executing comfortably within 0.1 seconds.
- **Auxiliary Space Complexity:** $O(k)$ auxiliary memory to store intermediate subsequences and merge buffers.
