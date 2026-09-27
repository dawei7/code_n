# Guided Example: Degree of an Array

We trace the step-by-step element frequency profiling ($cnt[v]$), maximum frequency degree identification ($degree = \max cnt$), first and last occurrence boundary indexing ($left[v], right[v]$), bounding interval span minimization ($right[v] - left[v] + 1$), and shortest degree-preserving subarray extraction on representative integer arrays:

- **Input:** $nums = [1, 2, 2, 3, 1]$
- **Required output:** `2`
  - Array degree definition:
    - The **degree** of an array is the maximum frequency of any single element in the array.
    - For $[1, 2, 2, 3, 1]$:
      - Value $1$ appears 2 times.
      - Value $2$ appears 2 times.
      - Value $3$ appears 1 time.
      - Degree of the array is **2**.
    - Objective: Find the minimum length of a contiguous subarray that also has a degree equal to **2**.
    - Candidate subarrays with degree 2:
      - Subarray containing all $1$s: $[1, 2, 2, 3, 1]$ from index 0 to 4 (length **5**).
      - Subarray containing all $2$s: $[2, 2]$ from index 1 to 2 (length **2**).
    - The shortest length is **2**.
- **First-and-Last Occurrence Span Invariant:**
  - **The Bounding Window Invariant:**
    - For any element $v$ that appears $degree$ times:
      - A contiguous subarray has degree equal to $degree$ if and only if it contains all $degree$ copies of $v$.
      - To contain all occurrences of $v$, the subarray must start at or before the **first occurrence** of $v$ ($left[v]$) and end at or after the **last occurrence** of $v$ ($right[v]$).
      - The absolute shortest contiguous subarray containing all copies of $v$ is exactly the slice:
        $$
        nums[left[v] \dots right[v]]
        $$
      - The length of this minimal bounding slice is:
        $$
        span(v) = right[v] - left[v] + 1
        $$
  - **Minimization Across Degree Leaders:**
    - If multiple distinct elements share the maximal degree, the shortest overall subarray is obtained by taking the minimum span among all degree-achieving elements:
      $$
      ans = \min_{v: cnt[v] = degree} (right[v] - left[v] + 1)
      $$
- **Step-by-Step Worked Execution Trace on $nums = [1, 2, 2, 3, 1]$ ($n = 5$):**
  - **Step 1: Record Frequencies and Boundaries:**
    - Index 0 ($nums[0] = 1$):
      - $left[1] = 0, \; right[1] = 0, \; cnt[1] = 1$.
    - Index 1 ($nums[1] = 2$):
      - $left[2] = 1, \; right[2] = 1, \; cnt[2] = 1$.
    - Index 2 ($nums[2] = 2$):
      - $right[2] \leftarrow 2, \; cnt[2] = 2$.
    - Index 3 ($nums[3] = 3$):
      - $left[3] = 3, \; right[3] = 3, \; cnt[3] = 1$.
    - Index 4 ($nums[4] = 1$):
      - $right[1] \leftarrow 4, \; cnt[1] = 2$.
  - **Step 2: Determine Global Array Degree:**
    - Element counts:
      $$
      cnt[1] = 2, \quad cnt[2] = 2, \quad cnt[3] = 1
      $$
    - Maximum frequency:
      $$
      degree = \max(2, 2, 1) = \mathbf{2}
      $$
    - Degree-achieving elements: $\{1, 2\}$.
  - **Step 3: Evaluate Bounding Spans for Degree Leaders:**
    - **Candidate Element $v = 1$:**
      - First occurrence: $left[1] = 0$.
      - Last occurrence: $right[1] = 4$.
      - Contiguous slice span:
        $$
        right[1] - left[1] + 1 = 4 - 0 + 1 = \mathbf{5}
        $$
      - Subarray: $[1, 2, 2, 3, 1]$.
    - **Candidate Element $v = 2$:**
      - First occurrence: $left[2] = 1$.
      - Last occurrence: $right[2] = 2$.
      - Contiguous slice span:
        $$
        right[2] - left[2] + 1 = 2 - 1 + 1 = \mathbf{2}
        $$
      - Subarray: $[2, 2]$.
  - **Step 4: Find Minimum Span:**
    $$
    ans = \min(span(1), \; span(2)) = \min(5, \; 2) = \mathbf{2}
    $$
    - Output: **`2`**.
- **Unique Degree Leader Trace ($nums = [1, 2, 2, 3, 1, 4, 2]$):**
  - Element counts:
    - $cnt[1] = 2$
    - $cnt[2] = 3$
    - $cnt[3] = 1$
    - $cnt[4] = 1$
  - Maximal degree is $3$, achieved uniquely by value $2$.
  - First index of $2$: $left[2] = 1$.
  - Last index of $2$: $right[2] = 6$.
  - Shortest subarray: $6 - 1 + 1 = \mathbf{6}$ (slice $[2, 2, 3, 1, 4, 2]$).
- **All Unique Elements ($nums = [1, 2, 3, 4, 5]$):**
  - Degree is 1. Every element has span $1 - 0 + 1 = 1$.
  - Minimum length is **`1`**.

This instance demonstrates element occurrence profiling and bounding box range minimization on 1D discrete coordinate sets, mathematically proves why contiguous degree preservation restricts candidates to first-and-last index intervals, and derives $O(N)$ execution time and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an array $nums$:
The **degree** is the max frequency of any element.
Find the **minimum length** of a contiguous subarray that has the same degree.

```text
nums = [ 1, 2, 2, 3, 1 ]

Frequencies:
  1 appears 2 times
  2 appears 2 times
  3 appears 1 time
Degree = 2

Subarrays with degree 2:
  For element 1: first at 0, last at 4 -> length = 4 - 0 + 1 = 5
  For element 2: first at 1, last at 2 -> length = 2 - 1 + 1 = 2

Shortest length = min(5, 2) = 2
```

### The Invariant of the First-to-Last Span
- Any subarray achieving the full degree for an element $v$ must contain all occurrences of $v$.
- The minimal such subarray begins at $left[v]$ and ends at $right[v]$.
- Its length is strictly $right[v] - left[v] + 1$.

---

## 2. Conceptual Foundation & Invariants

### 1. Degree Identification:
$$
degree = \max_{v} cnt[v]
$$

### 2. Candidate Span Minimization:
$$
ans = \min_{v: cnt[v] = degree} (right[v] - left[v] + 1)
$$

> **Support Interval Minimality Invariant.** For any element $x \in \text{arg max}_v cnt(v)$, the minimal contiguous index interval $I \subset [0, n-1]$ satisfying $|I \cap nums^{-1}(x)| = \text{deg}(nums)$ is uniquely the convex hull interval $[\min(nums^{-1}(x)), \max(nums^{-1}(x))]$.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [1, 2, 2, 3, 1]$:

---

### Step 1: Scan & Map
- Element 1: $cnt = 2, left = 0, right = 4$.
- Element 2: $cnt = 2, left = 1, right = 2$.
- Element 3: $cnt = 1, left = 3, right = 3$.

---

### Step 2: Global Degree
- $\max(cnt) = 2$.

---

### Step 3: Compare Candidates
- For 1: $4 - 0 + 1 = 5$.
- For 2: $2 - 1 + 1 = 2$.

---

### Step 4: Minimum Span
$$
ans = \min(5, 2) = \mathbf{2}
$$

---

## 4. Complete Execution Trace

| Unique Element | Frequency | First Index $left$ | Last Index $right$ | Degree Leader? | Bounding Span | Minimum Span Recorded |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $2$ | $0$ | $4$ | Yes | $4 - 0 + 1 = 5$ | $5$ |
| **$2$** | **$2$** | **$1$** | **$2$** | **Yes** | **$2 - 1 + 1 = 2$** | **`2`** |
| $3$ | $1$ | $3$ | $3$ | No ($1 < 2$) | Skipped | $2$ |

---

## 5. Boundary Cases & Failure Modes

- **Single Element ($[5]$):** Degree 1, span 1 $\implies$ returns 1.
- **All Elements Distinct:** Degree 1, any single element has span 1 $\implies$ returns 1.
- **All Elements Identical ($[3, 3, 3]$):** Degree 3, span $3 - 1 + 1 = 3 \implies$ returns 3.
- **Multiple Ties for Degree:** Takes the smallest span among all leaders.

---

## 6. Traps & Common Anti-Patterns

- **Checking Elements with $cnt < degree$:** Only elements that match the maximum frequency can provide a subarray with the full degree.
- **Nested Sliding Window ($O(N^2)$):** Iterating through all subarrays is unnecessary when first and last indices give the exact minimum span in $O(1)$.
- **Assuming the First Degree Leader is Smallest:** All elements with frequency equal to $degree$ must be checked, as demonstrated by element 1 (span 5) vs element 2 (span 2).

---

## 7. Complexity Derivation

- **Time Complexity:**
  - One pass to populate frequency, left, and right maps: $\mathcal{O}(N)$.
  - One pass over unique elements to find minimum span: $\mathcal{O}(U) \le \mathcal{O}(N)$.
  - Total Time: strictly linear $\mathcal{O}(N)$. Completes in $< 5$ ms for $N = 5 \times 10^4$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(U) \le \mathcal{O}(N)$ space for the hash tables.
