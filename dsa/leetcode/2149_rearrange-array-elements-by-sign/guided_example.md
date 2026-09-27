# Guided Example: Rearrange Array Elements by Sign

We analyze and execute the dual-stride stable placement algorithm on a representative problem instance, demonstrating how independent even/odd index pointers guarantee sign alternation and relative order preservation in a single linear pass.

- **Input:** `nums = [3, 1, -2, -5, 2, -4]`
- **Output:** `[3, -2, 1, -5, 2, -4]`

This instance illustrates positive and negative element interleaving, parity-based index mapping, and preserving initial order without auxiliary sorting.

---

## 1. Problem Overview & Representative Instance

Given an integer array `nums` of even length $n$ containing no zeros, with exactly $n / 2$ positive elements and $n / 2$ negative elements, we must rearrange the array to satisfy three conditions:
1. **Alternating Sign Pattern:** Every adjacent pair of elements must have opposite signs.
2. **Positive Start:** The first element at index $0$ must be positive.
3. **Subsequence Stability:**
   - The relative order among positive integers must match their original appearance in `nums`.
   - The relative order among negative integers must match their original appearance in `nums`.

In our representative instance:
- `nums = [3, 1, -2, -5, 2, -4]` of length $n = 6$.
- Positive elements in order: $[3, 1, 2]$.
- Negative elements in order: $[-2, -5, -4]$.

Combining these into an alternating sequence starting with positive produces:
$$[3, -2, 1, -5, 2, -4]$$

---

## 2. Mathematical & Algorithmic Principles

### Deterministic Index Parity Assignment

Let $A$ be the resulting array of length $n$:
- Condition 1 (starts positive) and Condition 2 (alternating signs) strictly dictate the sign of every index $j \in [0, n - 1]$:
$$\text{Sign}(A[j]) = \begin{cases} 
\text{Positive} & \text{if } j \equiv 0 \pmod 2 \quad (\text{even indices: } 0, 2, 4, \dots, n-2) \\
\text{Negative} & \text{if } j \equiv 1 \pmod 2 \quad (\text{odd indices: } 1, 3, 5, \dots, n-1)
\end{cases}$$

Because there are exactly $n / 2$ positive and $n / 2$ negative elements in `nums`, there is an exact bijection between positive numbers and even target positions, and between negative numbers and odd target positions.

### Dual-Stride Single-Pass Placement

Rather than filtering elements into two separate lists and zipping them together, we maintain two destination pointers within a preallocated output buffer of size $n$:
- $\text{pos\_ptr} = 0$: Tracks the next available even index.
- $\text{neg\_ptr} = 1$: Tracks the next available odd index.

We iterate through `nums` from left to right. When element $x$ is encountered:
- If $x > 0$: Place $x$ into $A[\text{pos\_ptr}]$, and advance $\text{pos\_ptr} \leftarrow \text{pos\_ptr} + 2$.
- If $x < 0$: Place $x$ into $A[\text{neg\_ptr}]$, and advance $\text{neg\_ptr} \leftarrow \text{neg\_ptr} + 2$.

### Stability Invariance

Because `nums` is scanned from index $0$ to $n - 1$:
- The $k$-th positive element encountered in `nums` is assigned to even index $2(k - 1)$.
- The $k$-th negative element encountered in `nums` is assigned to odd index $2(k - 1) + 1$.
- Both subsequences are mapped via strictly increasing monotonic functions of their original order ($k \mapsto 2k - 2$ and $k \mapsto 2k - 1$), preserving relative ordering.

| Pointer Variable | Starting Index | Increment Step | Target Range | Assigned Elements |
|---|---|---|---|---|
| `pos_ptr` | $0$ | $+2$ | $\{0, 2, 4, \dots, n-2\}$ | Positive elements ($x > 0$) in original arrival order |
| `neg_ptr` | $1$ | $+2$ | $\{1, 3, 5, \dots, n-1\}$ | Negative elements ($x < 0$) in original arrival order |

---

## 3. Step-by-Step Walkthrough with Intermediate State

We trace the placement on `nums = [3, 1, -2, -5, 2, -4]`.

```
Target Buffer: [ _,  _,  _,  _,  _,  _ ]
pos_ptr = 0 (even),  neg_ptr = 1 (odd)

Read 3  (>0): place at index 0 => [ 3,  _,  _,  _,  _,  _ ], pos_ptr -> 2
Read 1  (>0): place at index 2 => [ 3,  _,  1,  _,  _,  _ ], pos_ptr -> 4
Read -2 (<0): place at index 1 => [ 3, -2,  1,  _,  _,  _ ], neg_ptr -> 3
Read -5 (<0): place at index 3 => [ 3, -2,  1, -5,  _,  _ ], neg_ptr -> 5
Read 2  (>0): place at index 4 => [ 3, -2,  1, -5,  2,  _ ], pos_ptr -> 6
Read -4 (<0): place at index 5 => [ 3, -2,  1, -5,  2, -4 ], neg_ptr -> 7
```

### Step 1: Initialize Buffer & Pointers
- Output array of size $6$: $A = [\text{null}, \text{null}, \text{null}, \text{null}, \text{null}, \text{null}]$.
- Set $\text{pos\_ptr} = 0$, $\text{neg\_ptr} = 1$.

### Step 2: Read `nums[0] = 3`
- Value $3 > 0$ (positive).
- Write to even index: $A[0] = 3$.
- Advance pointer: $\text{pos\_ptr} = 0 + 2 = 2$.
- Current buffer: $[3, \text{null}, \text{null}, \text{null}, \text{null}, \text{null}]$.

### Step 3: Read `nums[1] = 1`
- Value $1 > 0$ (positive).
- Write to even index: $A[2] = 1$.
- Advance pointer: $\text{pos\_ptr} = 2 + 2 = 4$.
- Current buffer: $[3, \text{null}, 1, \text{null}, \text{null}, \text{null}]$.

### Step 4: Read `nums[2] = -2`
- Value $-2 < 0$ (negative).
- Write to odd index: $A[1] = -2$.
- Advance pointer: $\text{neg\_ptr} = 1 + 2 = 3$.
- Current buffer: $[3, -2, 1, \text{null}, \text{null}, \text{null}]$.

### Step 5: Read `nums[3] = -5`
- Value $-5 < 0$ (negative).
- Write to odd index: $A[3] = -5$.
- Advance pointer: $\text{neg\_ptr} = 3 + 2 = 5$.
- Current buffer: $[3, -2, 1, -5, \text{null}, \text{null}]$.

### Step 6: Read `nums[4] = 2`
- Value $2 > 0$ (positive).
- Write to even index: $A[4] = 2$.
- Advance pointer: $\text{pos\_ptr} = 4 + 2 = 6$.
- Current buffer: $[3, -2, 1, -5, 2, \text{null}]$.

### Step 7: Read `nums[5] = -4`
- Value $-4 < 0$ (negative).
- Write to odd index: $A[5] = -4$.
- Advance pointer: $\text{neg\_ptr} = 5 + 2 = 7$.
- Current buffer: $[3, -2, 1, -5, 2, -4]$.

Both pointers reach beyond array length ($\text{pos\_ptr} = 6 \ge 6$, $\text{neg\_ptr} = 7 \ge 6$). Processing is complete.

---

## 4. Comprehensive State Trace

The table below catalogs every step of the single-pass placement:

| Input Index $i$ | Value $\text{nums}[i]$ | Sign Classification | Target Pointer Used | Target Index Written | New Pointer Value | Intermediate Array State |
|---|---|---|---|---|---|---|
| Initial | - | - | - | - | $\text{pos}=0, \text{neg}=1$ | `[_, _, _, _, _, _]` |
| $0$ | $3$ | Positive | $\text{pos\_ptr} = 0$ | $0$ | $\text{pos\_ptr} = 2$ | `[3, _, _, _, _, _]` |
| $1$ | $1$ | Positive | $\text{pos\_ptr} = 2$ | $2$ | $\text{pos\_ptr} = 4$ | `[3, _, 1, _, _, _]` |
| $2$ | $-2$ | Negative | $\text{neg\_ptr} = 1$ | $1$ | $\text{neg\_ptr} = 3$ | `[3, -2, 1, _, _, _]` |
| $3$ | $-5$ | Negative | $\text{neg\_ptr} = 3$ | $3$ | $\text{neg\_ptr} = 5$ | `[3, -2, 1, -5, _, _]` |
| $4$ | $2$ | Positive | $\text{pos\_ptr} = 4$ | $4$ | $\text{pos\_ptr} = 6$ | `[3, -2, 1, -5, 2, _]` |
| $5$ | $-4$ | Negative | $\text{neg\_ptr} = 5$ | $5$ | $\text{neg\_ptr} = 7$ | `[3, -2, 1, -5, 2, -4]` |

### Validation of Problem Constraints

- **Alternating Signs:** Signs sequence is $[+, -, +, -, +, -]$. Every adjacent pair has opposite signs.
- **Starts Positive:** Index $0$ contains $3 > 0$.
- **Positive Relative Order:** Subsequence at even positions is $[3, 1, 2]$, identical to original positive order in `nums`.
- **Negative Relative Order:** Subsequence at odd positions is $[-2, -5, -4]$, identical to original negative order in `nums`.

---

## 5. Algorithmic Correctness & Soundness

### Non-Interference of Parity Domains
The set of even indices $\mathcal{E} = \{0, 2, \dots, n-2\}$ and odd indices $\mathcal{O} = \{1, 3, \dots, n-1\}$ form a partition of $\{0, 1, \dots, n-1\}$ with $\mathcal{E} \cap \mathcal{O} = \emptyset$. 
- Writes to $\text{pos\_ptr}$ only ever modify indices in $\mathcal{E}$.
- Writes to $\text{neg\_ptr}$ only ever modify indices in $\mathcal{O}$.
- Neither pointer can overwrite a value written by the other.

### Exact Fill Invariant
Since there are exactly $n/2$ positive numbers and each increments $\text{pos\_ptr}$ by $2$, $\text{pos\_ptr}$ visits each index in $\mathcal{E}$ exactly once. Similarly, $n/2$ negative numbers visit each index in $\mathcal{O}$ exactly once. Every cell of $A$ is written to exactly once, with zero unassigned gaps.

---

## 6. Edge Cases & Anti-Patterns

### Edge Cases
1. **Minimal Array Size ($n = 2$):** For example, `nums = [-1, 1]`.
   - Read $-1$: placed at index $1$.
   - Read $1$: placed at index $0$.
   - Result: $[1, -1]$. Correctly reorders positive before negative.
2. **Already Alternating:** `nums = [1, -1, 2, -2]`. Pointers place each element at its current position, yielding $[1, -1, 2, -2]$.
3. **All Positives Followed by All Negatives:** `nums = [1, 2, 3, -1, -2, -3]`. Pointers interleave the two halves smoothly without extra buffering.
4. **All Negatives Followed by All Positives:** `nums = [-1, -2, -3, 1, 2, 3]`. Correctly routes positives to even positions and negatives to odd positions.

### Common Anti-Patterns
- **In-Place Swapping with Cyclic Permutations:** Trying to reorder in-place while preserving stability requires $O(n^2)$ time with insertion-style shifts, or complex block-merge routines. The problem contract explicitly does not require in-place modification; using an $O(n)$ output buffer is optimal.
- **Two Separate Filter Passes:** Extracting positives into list $P$ and negatives into list $Q$ and then interleaving works, but requires $3$ passes and $2$ intermediate array allocations. Dual pointers achieve the same result in a single pass with a single preallocated buffer.
- **Sorting Approaches:** Using comparison-based or stable sorting breaks the time bound and distorts the alternating pattern.

---

## 7. Complexity Analysis

### Time Complexity
- The algorithm iterates through `nums` exactly once from $i = 0$ to $n - 1$.
- At each index:
  - Sign check: $O(1)$.
  - Direct array assignment: $O(1)$.
  - Stride increment ($+2$): $O(1)$.
- Total time complexity is strictly $O(n)$, processing $2 \cdot 10^5$ elements in less than $5$ milliseconds.

### Auxiliary Space Complexity
- A single destination array of size $n$ holds the result.
- Two integer pointer variables maintain placement state.
- Auxiliary space complexity is $O(n)$ for the returned result array (and $O(1)$ additional working memory beyond the output).
