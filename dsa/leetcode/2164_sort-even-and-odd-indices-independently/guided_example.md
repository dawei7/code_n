# Guided Example: Sort Even and Odd Indices Independently

We analyze and execute the decoupled parity-subsequence sorting algorithm on a representative problem instance, demonstrating how partitioning elements by index parity allows dual opposing orderings before interleaved reconstruction.

- **Input:** `nums = [4, 1, 2, 3]`
- **Output:** `[2, 3, 4, 1]`

This instance illustrates extracting disjoint parity subsequences, ascending sort on even indices, descending sort on odd indices, and zip-interleaving.

---

## 1. Problem Overview & Representative Instance

Given a 0-indexed integer array `nums` of length $n$, we must rearrange its values according to the parity of their indices:
1. **Even-indexed elements ($0, 2, 4, \dots$):** Must be sorted in **non-decreasing (ascending)** order.
2. **Odd-indexed elements ($1, 3, 5, \dots$):** Must be sorted in **non-increasing (descending)** order.
3. Values may not cross parity boundaries: an element initially at an even position remains at an even position, and an element at an odd position remains at an odd position.

In our representative instance:
- `nums = [4, 1, 2, 3]` ($n = 4$).
- Even-positioned elements: $nums[0] = 4, nums[2] = 2$.
- Odd-positioned elements: $nums[1] = 1, nums[3] = 3$.

We must sort the even positions to $[2, 4]$, sort the odd positions to $[3, 1]$, and merge them to yield $[2, 3, 4, 1]$.

---

## 2. Mathematical & Algorithmic Principles

### Parity Decomposition & Invariance

The index set $\mathcal{I} = \{0, 1, \dots, n - 1\}$ decomposes into two disjoint subsets:
$$\mathcal{E} = \{2k \mid 0 \le 2k < n\} \quad \text{and} \quad \mathcal{O} = \{2k + 1 \mid 0 \le 2k + 1 < n\}$$

We extract the two independent subsequences:
- $E = \langle \text{nums}[2k] \rangle_{k=0}^{\lfloor (n-1)/2 \rfloor}$
- $O = \langle \text{nums}[2k+1] \rangle_{k=0}^{\lfloor (n-2)/2 \rfloor}$

### Independent Dual-Sort Permutations

1. Apply an ascending permutation $\pi_E$ to $E$ such that:
   $$E^* = \text{sort\_ascending}(E) \implies E^*_0 \le E^*_1 \le E^*_2 \le \dots$$
2. Apply a descending permutation $\pi_O$ to $O$ such that:
   $$O^* = \text{sort\_descending}(O) \implies O^*_0 \ge O^*_1 \ge O^*_2 \ge \dots$$

### Interleaved Zip Reconstruction

Reconstruct the final array $A$ by placing elements back into their respective parity slots:
$$A[i] = \begin{cases} 
E^*[i / 2] & \text{if } i \equiv 0 \pmod 2 \\
O^*[(i - 1) / 2] & \text{if } i \equiv 1 \pmod 2
\end{cases}$$

| Parity Class | Mathematical Subsequence | Sorting Policy | Concrete Role in Instance |
|---|---|---|---|
| Even Indices $\mathcal{E}$ | $\{i \mid i \equiv 0 \pmod 2\}$ | Ascending ($\le$) | Sorts $\{4, 2\} \to [2, 4]$ |
| Odd Indices $\mathcal{O}$ | $\{i \mid i \equiv 1 \pmod 2\}$ | Descending ($\ge$) | Sorts $\{1, 3\} \to [3, 1]$ |
| Interleaved Merge | $A[2k] = E^*_k, \, A[2k+1] = O^*_k$ | Zip alignment | Merges $[2, 4]$ and $[3, 1] \to [2, 3, 4, 1]$ |

---

## 3. Step-by-Step Walkthrough with Intermediate State

We trace the algorithm on `nums = [4, 1, 2, 3]`.

```
Input: [4, 1, 2, 3]
Even positions (0, 2): [4, 2]
Odd positions  (1, 3): [1, 3]

Sort Even ascending:   [4, 2] -> [2, 4]
Sort Odd descending:   [1, 3] -> [3, 1]

Interleave back:
Index 0 (even): 2
Index 1 (odd):  3
Index 2 (even): 4
Index 3 (odd):  1
Result: [2, 3, 4, 1]
```

### Step 1: Subsequence Extraction
Iterate through `nums` and partition by index parity:
- Index $0$ (even): Append $4$ to $E \implies E = [4]$.
- Index $1$ (odd): Append $1$ to $O \implies O = [1]$.
- Index $2$ (even): Append $2$ to $E \implies E = [4, 2]$.
- Index $3$ (odd): Append $3$ to $O \implies O = [1, 3]$.

Extracted subsequences:
$$E = [4, 2], \quad O = [1, 3]$$

### Step 2: Sort Subsequences
- Sort even subsequence $E$ in non-decreasing order:
  $$E^* = \text{sort\_asc}([4, 2]) = [2, 4]$$
- Sort odd subsequence $O$ in non-increasing order:
  $$O^* = \text{sort\_desc}([1, 3]) = [3, 1]$$

### Step 3: Re-interleave into Output Array
Maintain write pointers $p_E = 0$ and $p_O = 0$:
- **Index 0 (Even):** Write $E^*[0] = 2$. Advance $p_E \leftarrow 1$. Result: $[2, \_, \_, \_]$.
- **Index 1 (Odd):** Write $O^*[0] = 3$. Advance $p_O \leftarrow 1$. Result: $[2, 3, \_, \_]$.
- **Index 2 (Even):** Write $E^*[1] = 4$. Advance $p_E \leftarrow 2$. Result: $[2, 3, 4, \_]$.
- **Index 3 (Odd):** Write $O^*[1] = 1$. Advance $p_O \leftarrow 2$. Result: $[2, 3, 4, 1]$.

### Step 4: Finalization
Output array complete: $[2, 3, 4, 1]$.

---

## 4. Comprehensive State Trace

The table below catalogs every index, its parity classification, original value, and reconstructed target value:

| Index $i$ | Parity Classification | Original Value $\text{nums}[i]$ | Parity Sequence Source | Subsequence Rank $k$ | Sorted Source Value | Output Assigned $A[i]$ |
|---|---|---|---|---|---|---|
| $0$ | Even | $4$ | $E^*$ (Ascending) | $k = 0$ | $E^*[0] = 2$ | **2** |
| $1$ | Odd | $1$ | $O^*$ (Descending) | $k = 0$ | $O^*[0] = 3$ | **3** |
| $2$ | Even | $2$ | $E^*$ (Ascending) | $k = 1$ | $E^*[1] = 4$ | **4** |
| $3$ | Odd | $3$ | $O^*$ (Descending) | $k = 1$ | $O^*[1] = 1$ | **1** |

### Condition Verification

- **Even Subsequence ($i = 0, 2$):** $A[0] = 2 \le A[2] = 4$. (Non-decreasing: True)
- **Odd Subsequence ($i = 1, 3$):** $A[1] = 3 \ge A[3] = 1$. (Non-increasing: True)
- **Parity Isolation:** All even-positioned values originate from initial even positions; all odd-positioned values originate from initial odd positions.

---

## 5. Algorithmic Correctness & Soundness

### Conservation of Parity Sets
Because elements are extracted strictly based on index parity and written back strictly to the same parity, no value can ever migrate from an even index to an odd index or vice versa. The multiset of values occupying $\mathcal{E}$ in the output is identical to the multiset of values occupying $\mathcal{E}$ in the input, and likewise for $\mathcal{O}$.

### Monotonicity Guarantee
Standard sorting algorithms guarantee that $E^*$ is sorted non-decreasingly and $O^*$ is sorted non-increasingly. Writing back via monotonic indices preserves these exact sorting relations across the full array.

---

## 6. Edge Cases & Anti-Patterns

### Edge Cases
1. **Single Element Array ($n = 1$):** `nums = [7]`. $E = [7], O = []$. Reconstructed array is `[7]`.
2. **Two Elements ($n = 2$):** `nums = [2, 1]`. $E = [2], O = [1]$. Neither sequence needs reordering; returns `[2, 1]`.
3. **Odd Length Array ($n = 5$):** `nums = [5, 8, 3, 6, 1]`.
   - Even positions (size 3): $[5, 3, 1] \to [1, 3, 5]$.
   - Odd positions (size 2): $[8, 6] \to [8, 6]$.
   - Merged output: $[1, 8, 3, 6, 5]$. Handled cleanly because $E$ has length $\lceil n/2 \rceil = 3$ and $O$ has length $\lfloor n/2 \rfloor = 2$.
4. **Duplicate Elements in Either Parity:** E.g., `nums = [3, 2, 3, 2]`. Stable or unstable sort both handle duplicates correctly.

### Common Anti-Patterns
- **Sorting Entire Array Directly:** Sorting all of `nums` scrambles even and odd elements together, violating parity isolation.
- **In-Place Bubble Swaps Across Wrong Strides:** Attempting to swap elements with stride $1$ mixes parities. Any in-place sorting must use stride $2$.
- **Sorting Both Subsequences in the Same Direction:** Accidental non-decreasing sorting of odd indices inverts the required descending order.

---

## 7. Complexity Analysis

### Time Complexity
- **Extraction Pass:** Iterating through $n$ elements to populate $E$ and $O$ takes $O(n)$ time.
- **Sorting:**
  - Sorting $E$ of size $\lceil n/2 \rceil$ takes $O(n \log n)$ time (or $O(n)$ with counting sort since values $\le 100$).
  - Sorting $O$ of size $\lfloor n/2 \rfloor$ takes $O(n \log n)$ time (or $O(n)$ with counting sort).
- **Interleaving Pass:** Writing back $n$ elements takes $O(n)$ time.
- Total time complexity is $O(n \log n)$ (or $O(n)$ with counting sort), taking less than $1$ millisecond for $n \le 100$.

### Auxiliary Space Complexity
- Two auxiliary lists $E$ and $O$ store $n$ integers combined.
- Total auxiliary space complexity is $O(n)$ memory.
