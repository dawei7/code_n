# Guided Example: Contains Duplicate

We trace the step-by-step hash set early-exit membership tracking and sorted adjacent equality comparison on representative integer arrays:

- **Input:** $\text{nums} = [1, 2, 3, 1]$
- **Required output:** `true` (Element $1$ appears at indices $0$ and $3$)
- **All Distinct Instance:** $\text{nums} = [1, 2, 3, 4] \implies \text{false}$ (All 4 integers are distinct)
- **Multi-Duplicate Instance:** $\text{nums} = [1, 1, 1, 3, 3, 4, 3, 2, 4, 2] \implies \text{true}$
- **Single Element Instance:** $\text{nums} = [42] \implies \text{false}$ (Minimum array size 1 cannot contain duplicates)

This instance demonstrates set membership invariants, compares the $O(N)$ hash set approach (with instant short-circuiting) against $O(N \log N)$ in-place sorting, proves why hash collisions provide exact equality guarantees, and analyzes time-space tradeoffs.

---

## 1. Instance & Teaching Goal

Given an integer array $\text{nums} = [1, 2, 3, 1]$ of length $N = 4$:
Determine whether any value appears **at least twice** in the array.
Return `true` if a duplicate exists, and `false` if every element is distinct.

In an unsorted list, duplicate elements can appear arbitrarily far apart (here, at indices $0$ and $3$).
- A brute-force nested loop checks all $\binom{N}{2} = \frac{N(N-1)}{2}$ pairs, taking quadratic $O(N^2)$ time.
- A **Hash Set** provides $O(1)$ expected lookups, allowing duplicates to be flagged in a single forward pass ($O(N)$ time).
- A **Sorting** approach groups identical values into contiguous adjacent blocks ($O(N \log N)$ time, $O(1)$ extra space).

---

## 2. Conceptual Foundation & Invariants

### Method A: Single-Pass Hash Set (Optimal $O(N)$ Time)
Maintain a set `seen` of observed elements:
1. Initialize $\text{seen} = \emptyset$.
2. For each element $x \in \text{nums}$:
   - If $x \in \text{seen}$: return `true` immediately (early short-circuit!).
   - Else: $\text{seen}.\text{add}(x)$.
3. If the loop completes without finding duplicates, return `false`.

### Method B: Adjacent Sorting Comparison ($O(1)$ Space)
1. Sort `nums` in non-decreasing order:
   $$
   [1, 2, 3, 1] \implies [1, 1, 2, 3]
   $$
2. Any duplicated values must now occupy adjacent indices ($i$ and $i+1$).
3. Scan for $i$ from $0$ to $N - 2$:
   If $\text{nums}[i] == \text{nums}[i+1]$, return `true`.
4. If no adjacent elements match, return `false`.

> **Invariant.** After inspecting prefix $0 \dots i$, the set `seen` contains exactly the distinct values present in $\text{nums}[0 \dots i]$. A duplicate is detected the very first time an element matches an existing set member.

---

## 3. Step-by-Step Worked Execution

We trace the Hash Set execution on $\text{nums} = [1, 2, 3, 1]$:

### Step 0: Initialize
- $\text{seen} = \emptyset$.

---

### Step 1: Element $x = 1$ (Index 0)
- Check $1 \in \text{seen}$: `False`.
- Add to set:
  $$
  \text{seen} = \{1\}
  $$

---

### Step 2: Element $x = 2$ (Index 1)
- Check $2 \in \text{seen}$: `False`.
- Add to set:
  $$
  \text{seen} = \{1, 2\}
  $$

---

### Step 3: Element $x = 3$ (Index 2)
- Check $3 \in \text{seen}$: `False`.
- Add to set:
  $$
  \text{seen} = \{1, 2, 3\}
  $$

---

### Step 4: Element $x = 1$ (Index 3) — Duplicate Found!
- Check $1 \in \text{seen}$: **True!**
- Element $1$ has already been observed.
- **Short-circuit exit: Return `true`.**

---

## 4. Complete Execution Trace

```text
nums = [1, 2, 3, 1]

Hash Set Trace:
i = 0: x = 1 -> seen = {1}
i = 1: x = 2 -> seen = {1, 2}
i = 2: x = 3 -> seen = {1, 2, 3}
i = 3: x = 1 -> 1 in seen! -> RETURN TRUE (Early exit)

Sorting Trace:
Sort nums -> [1, 1, 2, 3]
Pair (nums[0], nums[1]) = (1, 1) -> 1 == 1 -> RETURN TRUE
```

| Index $i$ | Element $x$ | `seen` Set Before Step | Membership Test (`x in seen`) | Action Taken | Result Status |
|:---:|:---:|:---|:---:|:---|:---:|
| 0 | 1 | $\emptyset$ | False | Insert 1 | Active |
| 1 | 2 | $\{1\}$ | False | Insert 2 | Active |
| 2 | 3 | $\{1, 2\}$ | False | Insert 3 | Active |
| **3** | **1** | **$\{1, 2, 3\}$** | **True** | **Trigger early return** | **`true` (Duplicate: 1)** |

### Contrast: Distinct Input $\text{nums} = [1, 2, 3, 4]$
- At indices $0, 1, 2, 3$, all elements are absent from `seen`.
- Set grows to $\{1, 2, 3, 4\}$ of size 4.
- Loop exhausts all elements $\implies$ Returns `false`.

---

## 5. Algorithmic Correctness

**Soundness.** If $x \in \text{seen}$ evaluates to `true`, then element $x$ appeared at some earlier index $j < i$, proving that $x$ appears at least twice in `nums`. The method never reports `true` on distinct arrays.

**Completeness.** If a duplicate value exists, let the first pair of identical values appear at indices $j < i$. When the scan reaches index $i$, the value is already present in `seen` from index $j$. The algorithm immediately halts and returns `true`.

---

## 6. Traps This Instance Exposes

- **Length of Set Shortcut:** In Python, `len(set(nums)) < len(nums)` is concise, but it converts the entire list to a set even if the duplicate is at indices 0 and 1! A streaming loop with early return achieves optimal best-case $O(1)$ time.
- **Array Value Range Constraints:** In LeetCode 217, $-10^9 \le \text{nums}[i] \le 10^9$. A frequency array or bitset cannot be sized to $2 \times 10^9$ elements. A hash table or sorting is required.
- **Single Element Arrays:** When $N = 1$, the loop terminates after 1 step and returns `false`. No special-case guard is needed.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Hash Set: $O(N)$ average time. Each hash lookup and insertion takes $O(1)$ amortized time. In the best case, an early duplicate exits in $O(1)$ steps.
  - Sorting: $O(N \log N)$ deterministic time using introsort or Timsort.
- **Auxiliary Space Complexity:**
  - Hash Set: $O(N)$ auxiliary space in the worst case (when all elements are distinct).
  - Sorting: $O(1)$ auxiliary space if sorted in place (`nums.sort()`), or $O(N)$ if a copy is made.
