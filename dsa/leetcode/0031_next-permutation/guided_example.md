# Guided Example: Next Permutation

We trace the step-by-step execution of the three-phase lexicographical successor algorithm on a representative array instance:

- **Input:** $\text{nums} = [1, 3, 5, 4, 2]$
- **Required output:** $[1, 4, 2, 3, 5]$

This instance demonstrates finding the rightmost strictly increasing pivot, locating the smallest larger successor within the descending suffix, swapping to advance lexicographical rank minimally, and reversing the suffix to obtain the smallest permutation of the remaining elements.

---

## 1. Instance & Teaching Goal

Given an integer array $\text{nums}$ of length $N = 5$:
$$
[1, 3, 5, 4, 2]
$$

We must rearrange the numbers into the lexicographically next greater permutation of numbers. If no greater permutation is possible (i.e. the array is sorted in descending order), we must rearrange it to the lowest possible order (sorted in ascending order). The replacement must be made strictly in-place with $O(1)$ extra memory.

For $[1, 3, 5, 4, 2]$:
- The suffix $[5, 4, 2]$ is sorted in descending order, meaning no rearrangement of this suffix alone can produce a larger value.
- To make the entire number larger with the minimal increase, we must modify the element immediately before this suffix (pivot $3$ at index 1).
- Swapping $3$ with the next larger number in the suffix ($4$) yields $[1, 4, 5, 3, 2]$.
- Reversing the remaining suffix $[5, 3, 2]$ into ascending order $[2, 3, 5]$ produces the minimal possible suffix, resulting in $[1, 4, 2, 3, 5]$.

---

## 2. Conceptual Foundation & Invariants

### Narayana Pandita's Permutation Generation
The algorithm proceeds in four strictly ordered phases:

```text
Array:    [1,   3,   5,   4,   2]
               ^    |--- suffix ---|
            pivot i     descending
```

1. **Phase 1: Identify Pivot $i$**
   Scan backwards from $N - 2$ to $0$. Find the first index $i$ such that $\text{nums}[i] < \text{nums}[i+1]$.
   - If no such $i$ exists ($i = -1$), the entire array is descending (maximal). Reverse the entire array and return.
2. **Phase 2: Identify Successor $j$**
   Scan backwards from $N - 1$ down to $i + 1$. Find the first index $j$ such that $\text{nums}[j] > \text{nums}[i]$.
   - Because the suffix is descending, scanning from the right finds the smallest element in the suffix strictly greater than $\text{nums}[i]$.
3. **Phase 3: Swap Pivot and Successor**
   Swap $\text{nums}[i]$ and $\text{nums}[j]$.
   - The prefix through $i$ has now taken the smallest possible increment.
   - The suffix $\text{nums}[i+1 \dots N-1]$ remains in strictly descending order.
4. **Phase 4: Invert Suffix to Ascending**
   Reverse the subarray $\text{nums}[i+1 \dots N-1]$ in place.
   - Reversing a descending subarray produces an ascending subarray, minimizing its numerical contribution.

> **Invariant.** The reversed suffix $\text{nums}[i+1 \dots N-1]$ is the lexicographically smallest possible arrangement of the remaining elements, guaranteeing that the resulting permutation is the immediate successor.

---

## 3. Step-by-Step Worked Execution

We trace $\text{nums} = [1, 3, 5, 4, 2]$:

### Phase 1: Locate Rightmost Ascent ($i$)
Scan from right to left comparing adjacent elements:
- Index 3 vs 4: $\text{nums}[3] = 4 > \text{nums}[4] = 2$ (descending)
- Index 2 vs 3: $\text{nums}[2] = 5 > \text{nums}[3] = 4$ (descending)
- Index 1 vs 2: $\text{nums}[1] = 3 < \text{nums}[2] = 5$ (**Ascent found!**)
- Pivot established at index $i = 1$ with value $\text{nums}[1] = 3$.
- Suffix is $\text{nums}[2 \dots 4] = [5, 4, 2]$.

---

### Phase 2: Find Successor in Suffix ($j$)
Scan suffix from right ($N - 1 = 4$) down to $i + 1 = 2$ for the first element $> \text{nums}[i] = 3$:
- Index 4: $\text{nums}[4] = 2 \not> 3$.
- Index 3: $\text{nums}[3] = 4 > 3$. **Successor found!**
- Successor index $j = 3$ with value $4$.

---

### Phase 3: Swap Pivot and Successor
Swap $\text{nums}[i]$ and $\text{nums}[j]$:
- Before swap: $[1, \mathbf{3}, 5, \mathbf{4}, 2]$
- Swap $\text{nums}[1] \leftrightarrow \text{nums}[3]$
- After swap: $[1, \mathbf{4}, 5, \mathbf{3}, 2]$
- Suffix at indices $2 \dots 4$ is now $[5, 3, 2]$, which remains non-increasing.

---

### Phase 4: Reverse Suffix
Reverse subarray $\text{nums}[2 \dots 4]$ using two pointers $l = 2, r = 4$:
- Swap $\text{nums}[2]$ and $\text{nums}[4]$: swap $5$ and $2$.
- Subarray $[5, 3, 2]$ becomes $[2, 3, 5]$.
- Final array configuration: $[1, 4, 2, 3, 5]$.

---

## 4. Complete Execution Trace

| Phase | Target Indices | Values Inspected | Decision / Action Taken | Resulting Array State |
|:---:|:---:|:---:|:---|:---|
| 1 | Suffix $[2 \dots 4]$ | $5 > 4 > 2$ | Descending order; cannot be enlarged | $[1, 3, 5, 4, 2]$ |
| 1 | $i = 1, i+1 = 2$ | $3 < 5$ | First ascent from right; Pivot $i = 1$ | $[1, 3, 5, 4, 2]$ |
| 2 | Scan $j$ from $4 \to 2$ | $\text{nums}[3] = 4 > 3$ | Smallest element in suffix larger than pivot; $j = 3$ | $[1, 3, 5, 4, 2]$ |
| 3 | Swap $i$ and $j$ | Swap $\text{nums}[1]$ and $\text{nums}[3]$ | Increment prefix minimally: $3 \to 4$ | $[1, \mathbf{4}, 5, \mathbf{3}, 2]$ |
| 4 | Reverse $[2 \dots 4]$ | Reverse $[5, 3, 2]$ | Convert descending suffix to ascending: $[2, 3, 5]$ | $[1, 4, \mathbf{2}, \mathbf{3}, \mathbf{5}]$ |

### Boundary Case: Entirely Descending Array

| Input Array | Pivot Search Result | Action | Output (Smallest Permutation) |
|:---:|:---:|:---|:---:|
| $[3, 2, 1]$ | No ascent found ($i = -1$) | Reverse entire array in place | $[1, 2, 3]$ |
| $[1, 1, 5]$ | Pivot at $i = 1$ ($1 < 5$) | Swap $1$ and $5$, reverse suffix | $[1, 5, 1]$ |

---

## 5. Algorithmic Correctness

**Soundness.** Swapping $\text{nums}[i]$ with the smallest element in the suffix strictly greater than $\text{nums}[i]$ ensures the new prefix $\text{nums}[0 \dots i]$ is the immediate lexicographical successor among all permutations sharing that prefix length. Reversing the suffix converts it from descending (maximal) to ascending (minimal), ensuring no intermediate permutation is skipped.

**Completeness.** Every finite sequence has a well-defined lexicographical successor, or wraps to the minimal sequence if already maximal. The pivot search identifies the longest unchanged prefix. By monotonicity, no valid successor exists with a longer common prefix.

---

## 6. Traps This Instance Exposes

- **Searching for Successor from Left:** Scanning for $j$ from left to right in the suffix can mistakenly select a much larger element (such as $5$ instead of $4$). Because the suffix is descending, scanning from right to left guarantees finding the smallest element strictly greater than $\text{nums}[i]$.
- **Strict vs Non-Strict Inequality:** Elements may be equal (e.g. $[1, 5, 1]$). The pivot requires $\text{nums}[i] < \text{nums}[i+1]$ (strict). The successor search requires $\text{nums}[j] > \text{nums}[i]$ (strict).
- **All-Descending Input:** When the input is $[3, 2, 1]$, $i$ ends at $-1$. Skipping the swap step and proceeding directly to reverse the whole array correctly produces the lowest permutation $[1, 2, 3]$.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N$ is the length of $\text{nums}$. The backward scan to find $i$ takes at most $N$ steps. The scan to find $j$ takes at most $N$ steps. Swapping takes $O(1)$. Reversing the suffix takes at most $N/2$ swaps. Total time is bounded by $3N = O(N)$.
- **Auxiliary Space Complexity:** $O(1)$. All operations are performed in place using two-pointer swaps without allocating additional arrays.
