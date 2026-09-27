# Guided Example: Intersection of Two Arrays II

We trace the step-by-step multiset frequency table construction (`Counter(nums1)`), decrement-on-match consumption (`cnt[x] -= 1`), duplicate multiplicity preservation ($\min(\text{count}_1, \text{count}_2)$), and common element accumulation on representative integer array instances:

- **Input:** $\text{nums1} = [1, 2, 2, 1], \quad \text{nums2} = [2, 2]$
- **Required output:** $[2, 2]$
  - Element $1$: occurs twice in `nums1`, zero times in `nums2` $\implies \min(2, 0) = 0$
  - Element $2$: occurs twice in `nums1`, twice in `nums2` $\implies \min(2, 2) = 2$
  - Result contains two $2$'s: $[2, 2]$
- **Unequal Multiplicity Instance:** $\text{nums1} = [4, 9, 5], \text{nums2} = [9, 4, 9, 8, 4]$
  - $4$: occurs 1 time in `nums1`, 2 times in `nums2` $\implies \min(1, 2) = 1$
  - $9$: occurs 1 time in `nums1`, 2 times in `nums2` $\implies \min(1, 2) = 1$
  - Result: $[9, 4]$ (or $[4, 9]$ in any order)
- **Completely Disjoint Arrays:** $\text{nums1} = [1, 2], \text{nums2} = [3, 4] \implies []$
- **Identical Arrays:** $\text{nums1} = [1, 1, 1], \text{nums2} = [1, 1, 1] \implies [1, 1, 1]$

This instance demonstrates multiset intersection algorithms, contrasts hash table counting with sorted two-pointer traversal, proves why decrementing frequency upon match guarantees that elements are not matched more times than available, and analyzes $O(N + M)$ linear time and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given two integer arrays:
$$
\text{nums1} = [1, 2, 2, 1], \quad \text{nums2} = [2, 2]
$$
Return an array of their intersection such that:
1. Each element appears **as many times as it shows in both arrays** (multiset intersection).
2. Elements may be returned in **any order**.

```text
nums1: [1, 2, 2, 1] -> Counts: {1: 2, 2: 2}
nums2: [2, 2]       -> Counts: {2: 2}

Multiset Intersection:
Count of 1: min(2, 0) = 0
Count of 2: min(2, 2) = 2

Output: [2, 2]
```

### Problem 349 vs Problem 350 Distinction
- In **Problem 349 (Set Intersection)**, every common value is included at most once ($[2]$).
- In **Problem 350 (Multiset Intersection)**, element multiplicity is preserved ($[2, 2]$).
- A simple hash set cannot preserve multiplicity; we must maintain a **frequency counter** where matches are consumed and decremented.

---

## 2. Conceptual Foundation & Invariants

### 1. Supply Counter Construction
Construct frequency table from the first array:
$$
cnt = \text{Counter}(\text{nums1})
$$
For our instance:
$$
cnt = \{1: 2, \; 2: 2\}
$$

### 2. Consumer Scan over `nums2`:
Iterate through each element $x \in \text{nums2}$:
- Check if an unmatched copy of $x$ remains in `cnt`:
  $$
  \text{if } cnt[x] > 0:
  $$
- If true:
  - Add $x$ to output: $ans.\text{append}(x)$.
  - Consume that copy: $cnt[x] \mathrel{-}= 1$.

> **Invariant.** For each distinct integer $x$, exactly $\min(\text{count}(x, \text{nums1}), \text{count}(x, \text{nums2}))$ occurrences of $x$ are appended to `ans`.

---

## 3. Step-by-Step Worked Execution

We trace $\text{nums1} = [1, 2, 2, 1]$ and $\text{nums2} = [2, 2]$:
Initialized:
- Frequency supply: $cnt = \{1: 2, \; 2: 2\}$.
- Output list: $ans = []$.

---

### Step 1: Process First Element of `nums2` ($x = 2$)
- Query available count: $cnt[2] = 2$.
- Condition $cnt[2] > 0$ is **True**.
- Action:
  - Append $2$ to $ans$: $ans = [\mathbf{2}]$.
  - Decrement remaining supply:
    $$
    cnt[2] \leftarrow 2 - 1 = \mathbf{1}
    $$
- Active supply: $cnt = \{1: 2, \; 2: 1\}$.

---

### Step 2: Process Second Element of `nums2` ($x = 2$)
- Query available count: $cnt[2] = 1$.
- Condition $cnt[2] > 0$ is **True**.
- Action:
  - Append $2$ to $ans$: $ans = [2, \; \mathbf{2}]$.
  - Decrement remaining supply:
    $$
    cnt[2] \leftarrow 1 - 1 = \mathbf{0}
    $$
- Active supply: $cnt = \{1: 2, \; 2: 0\}$.

---

### Step 3: Array Traversal Complete
All elements of `nums2` processed.
Return collected matches:
$$
ans = \mathbf{[2, 2]}
$$

---

## 4. Complete Execution Trace

```text
nums1 = [1, 2, 2, 1], nums2 = [2, 2]
cnt = {1: 2, 2: 2}
ans = []

Scan nums2:
x = 2: cnt[2] = 2 > 0 -> append 2, cnt[2] becomes 1, ans = [2]
x = 2: cnt[2] = 1 > 0 -> append 2, cnt[2] becomes 0, ans = [2, 2]

Result: [2, 2]
```

| Step in `nums2` | Element $x$ | Current Supply $cnt[x]$ | Match Available ($cnt[x] > 0$)? | Action Taken | Supply After Step $cnt[x]$ | Accumulator `ans` |
|:---:|:---:|:---:|:---:|:---|:---:|:---|
| Init | - | - | - | Built $cnt = \{1: 2, 2: 2\}$ | - | `[]` |
| **1** | **2** | **2** | **Yes** | Append $2$, decrement $cnt[2]$ | **1** | **`[2]`** |
| **2** | **2** | **1** | **Yes** | Append $2$, decrement $cnt[2]$ | **0** | **`[2, 2]`** |
| **Exit** | - | - | - | Traversal complete | - | **`[2, 2]` (Output)** |

---

## 5. Algorithmic Correctness

**Soundness.** An element $x$ is appended to $ans$ only when $cnt[x] > 0$. Because $cnt[x]$ is initialized with the exact count of $x$ in `nums1`, and decremented on every addition, $x$ can never be appended more than $\text{count}(x, \text{nums1})$ times. Furthermore, $x$ cannot be appended more than its occurrences in `nums2` because the loop visits each element of `nums2` once. Thus, the frequency in $ans$ never exceeds $\min(\text{count}_1, \text{count}_2)$.

**Completeness.** Whenever $x$ appears in both arrays, each occurrence in `nums2` will find $cnt[x] > 0$ until all $\text{count}(x, \text{nums1})$ copies are exhausted. The total number of successful matches is therefore exactly $\min(\text{count}(x, \text{nums1}), \text{count}(x, \text{nums2}))$, capturing the complete multiset intersection.

---

## 6. Traps This Instance Exposes

- **Missing Decrement on Match:** Forgetting `cnt[x] -= 1` matches every occurrence in `nums2` indefinitely as long as $x$ was present in `nums1`, producing too many duplicate elements.
- **Sorted Two-Pointer Follow-up:** If both arrays are already sorted, two pointers ($p_1, p_2$) can find the intersection in $O(N + M)$ time and $O(1)$ extra space without hash tables.
- **Memory Optimization for Skewed Sizes:** If `nums1` is significantly larger than `nums2`, counting the smaller array reduces hash map space complexity to $O(\min(N, M))$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N + M)$, where $N = \text{len}(nums1)$ and $M = \text{len}(nums2)$.
  - Counting `nums1` takes $O(N)$ time.
  - Scanning `nums2` takes $M$ iterations, with each hash table lookup and decrement taking $O(1)$ time.
  - Total time is strictly $O(N + M)$.
- **Auxiliary Space Complexity:** $O(U_1)$, where $U_1$ is the number of distinct elements in `nums1` ($U_1 \le N$), stored in the frequency map `cnt`.
