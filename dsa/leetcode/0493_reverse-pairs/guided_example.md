# Guided Example: Reverse Pairs

We trace the step-by-step Divide and Conquer recursion, modified merge sort partition, two-pointer cross-boundary condition evaluation ($nums[i] > 2 \cdot nums[j]$), suffix prefix count accumulation ($mid - i + 1$), and sorted merge consolidation on representative numeric arrays:

- **Input:** $nums = [1, 3, 2, 3, 1]$
- **Required output:** `2`
  - Array length: $N = 5$
  - Target condition: Count index pairs $(i, j)$ such that:
    $$
    i < j \quad \text{and} \quad nums[i] > 2 \times nums[j]
    $$
  - Direct valid pairs:
    1. Pair $(i=1, j=4)$: $nums[1] = 3, \; nums[4] = 1 \implies 3 > 2(1) = 2$ (**Valid**)
    2. Pair $(i=3, j=4)$: $nums[3] = 3, \; nums[4] = 1 \implies 3 > 2(1) = 2$ (**Valid**)
    - Other comparisons: $2 \ngtr 2(1)$, $1 \ngtr 2(1)$.
  - Total valid reverse pairs: **`2`**.
- **Divide and Conquer execution trace:**
  - Partition at $mid = 2$:
    - Left half: $nums[0 \dots 2] = [1, 3, 2]$
    - Right half: $nums[3 \dots 4] = [3, 1]$
  - **Left Half Sort & Count ($[1, 3, 2]$):**
    - Subproblems sorted: $[1, 3]$ and $[2]$.
    - Cross count between $[1, 3]$ and $[2]$:
      - $j$ points to $2$ (threshold $2 \times 2 = 4$).
      - $1 \le 4$, $3 \le 4 \implies 0$ reverse pairs.
    - Sorted left half becomes: $[1, 2, 3]$. Internal pairs: $0$.
  - **Right Half Sort & Count ($[3, 1]$):**
    - Subproblems $[3]$ and $[1]$.
    - Cross check: $3 > 2(1) = 2 \implies \mathbf{+1}$ pair!
    - Sorted right half becomes: $[1, 3]$. Internal pairs: $1$.
  - **Cross Merge Between Left $[1, 2, 3]$ and Right $[1, 3]$:**
    - Left indices $i \in [0, 2]$, Right indices $j \in [3, 4]$
    - **At $j = 3$ (Value $nums[j] = 1$, Threshold $2 \times 1 = 2$):**
      - Compare $i = 0$ ($nums[0] = 1$): $1 \le 2 \implies$ advance $i \leftarrow 1$
      - Compare $i = 1$ ($nums[1] = 2$): $2 \le 2 \implies$ advance $i \leftarrow 2$
      - Compare $i = 2$ ($nums[2] = 3$):
        $$
        3 > 2 \times 1 = 2
        $$
      - Since left array is sorted, all elements from $i$ to $mid$ satisfy the condition!
      - Suffix count:
        $$
        mid - i + 1 = 2 - 2 + 1 = \mathbf{1} \text{ pair} \quad ((3, 1))
        $$
      - Add to count: $ans \leftarrow 1 + 1 = 2$.
      - Advance right pointer $j \leftarrow 4$.
    - **At $j = 4$ (Value $nums[j] = 3$, Threshold $2 \times 3 = 6$):**
      - Compare $i = 2$ ($nums[2] = 3$): $3 \le 6 \implies$ advance $i \leftarrow 3 > mid$.
      - Loop terminates.
  - Final accumulated reverse pairs:
    $$
    ans = 0 (\text{left}) + 1 (\text{right}) + 1 (\text{cross}) = \mathbf{2}
    $$
- **Three Pairs Instance ($nums = [2, 4, 3, 5, 1]$):**
  - Pairs exceeding $2 \times 1 = 2$: $(4, 1), (3, 1), (5, 1) \implies \mathbf{3}$
- **All Strictly Increasing ($nums = [1, 2, 3, 4]$):** No reverse pairs $\implies \mathbf{0}$

This instance demonstrates Divide and Conquer inversion counting with non-standard comparison predicates, mathematically proves why pre-sorted subarrays enable $O(N)$ two-pointer batch interval summation, and derives $O(N \log N)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums = [1, 3, 2, 3, 1]$:
A **reverse pair** is an index pair $(i, j)$ such that:
$$
0 \le i < j < n \quad \text{and} \quad nums[i] > 2 \times nums[j]
$$
Return the number of reverse pairs in the array.

```text
Array: [ 1,  3,  2,  3,  1 ]

Pair (1, 4): nums[1] = 3, nums[4] = 1 -> 3 > 2 * 1 = 2 (Valid!)
Pair (3, 4): nums[3] = 3, nums[4] = 1 -> 3 > 2 * 1 = 2 (Valid!)

Total Reverse Pairs: 2
```

### The Bottleneck of Quadratic Pairwise Checking
A double loop testing every pair $(i, j)$ takes $O(N^2)$ time.
For $N = 5 \times 10^4$, $N^2 \approx 2.5 \times 10^9$ operations, triggering Time Limit Exceeded.
To achieve $O(N \log N)$:
We use **Divide and Conquer** (Merge Sort framework):
1. Count pairs wholly within the left half $[l \dots mid]$.
2. Count pairs wholly within the right half $[mid + 1 \dots r]$.
3. Count cross-pairs where $i$ is in the left half and $j$ is in the right half.
Because both halves are already sorted, **all cross-pairs can be counted in a single linear two-pointer sweep**!

---

## 2. Conceptual Foundation & Invariants

### 1. Two-Pointer Batch Inversion Counting:
Suppose both $nums[l \dots mid]$ and $nums[mid + 1 \dots r]$ are sorted in ascending order:
- Let pointer $i \in [l, mid]$ and pointer $j \in [mid + 1, r]$.
- If $nums[i] \le 2 \times nums[j]$:
  $nums[i]$ is too small to form a reverse pair with $nums[j]$.
  Advance $i \leftarrow i + 1$.
- If $nums[i] > 2 \times nums[j]$:
  Because the left subarray is sorted in ascending order:
  $$
  nums[i] \le nums[i + 1] \le \dots \le nums[mid]
  $$
  Every element from index $i$ to $mid$ is strictly greater than $2 \times nums[j]$!
  The number of valid left partners for this specific $j$ is exactly:
  $$
  \text{Count} = mid - i + 1
  $$
  Add $(mid - i + 1)$ to the answer and advance $j \leftarrow j + 1$.

### 2. Preserving Array Sortedness:
After counting cross-pairs, merge the two sorted halves into temporary array $t$ in standard $O(N)$ merge sort fashion, restoring the sorted invariant for the parent recursive level.

> **Sorted Suffix Invariant.** Because $nums[k] \ge nums[i]$ for all $k \in [i, mid]$, establishing $nums[i] > 2 \cdot nums[j]$ simultaneously validates all $mid - i + 1$ pairs in $O(1)$ time.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [1, 3, 2, 3, 1]$:

---

### Step 1: Recursive Subdivision
```text
               [1, 3, 2, 3, 1]
             /                 \
        [1, 3, 2]            [3, 1]
        /       \            /    \
     [1, 3]     [2]        [3]    [1]
     /    \
   [1]    [3]
```

---

### Step 2: Solve Base Intervals
- Subarray $[3, 1]$:
  - Left $[3]$, Right $[1]$.
  - Check $3 > 2(1) = 2 \implies$ Found 1 pair!
  - Sorted: $[1, 3]$. Pairs $= 1$.
- Subarray $[1, 3, 2]$:
  - Left $[1, 3]$, Right $[2]$.
  - Cross pairs: $1 \le 4$, $3 \le 4 \implies 0$ pairs.
  - Sorted: $[1, 2, 3]$. Pairs $= 0$.

---

### Step 3: Top-Level Cross Merge
Left sorted: $[1, 2, 3]$ (indices $l = 0, mid = 2$).
Right sorted: $[1, 3]$ (indices $mid + 1 = 3, r = 4$).

- **Pointer Initialization:** $i = 0, \; j = 3$.
- **Round 1 (Inspect $nums[j] = nums[3] = 1$):**
  - Threshold: $2 \times 1 = \mathbf{2}$.
  - At $i = 0$ ($nums[0] = 1$): $1 \le 2 \implies i \leftarrow 1$.
  - At $i = 1$ ($nums[1] = 2$): $2 \le 2 \implies i \leftarrow 2$.
  - At $i = 2$ ($nums[2] = 3$):
    $$
    3 > 2
    $$
    Valid! Add suffix size:
    $$
    mid - i + 1 = 2 - 2 + 1 = \mathbf{1}
    $$
    Advance $j \leftarrow 4$.

- **Round 2 (Inspect $nums[j] = nums[4] = 3$):**
  - Threshold: $2 \times 3 = \mathbf{6}$.
  - At $i = 2$ ($nums[2] = 3$): $3 \le 6 \implies i \leftarrow 3 > mid$.
  - Left pointer exhausted. Search halts.

---

### Step 4: Total Accumulation
$$
ans = ans_{left} + ans_{right} + ans_{cross} = 0 + 1 + 1 = \mathbf{2}
$$

---

## 4. Complete Execution Trace

| Merge Stage | Left Subarray | Right Subarray | Left Pointer $i$ | Right Pointer $j$ | Comparison $nums[i] > 2 \times nums[j]$ | Pairs Added ($mid - i + 1$) |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| Leaf | `[3]` | `[1]` | $3$ | $1$ | $3 > 2(1)$ (**Yes**) | $+1$ |
| Mid | `[1, 3]` | `[2]` | $1, 3$ | $2$ | $1 \le 4, 3 \le 4$ (**No**) | $0$ |
| **Top** | `[1, 2, 3]` | `[1, 3]` | $i = 0 \to 1 \to 2$ | $j = 3$ ($1$) | $3 > 2(1)$ (**Yes**) | **$+1$** |
| **Top** | `[1, 2, 3]` | `[1, 3]` | $i = 2 \to 3$ | $j = 4$ ($3$) | $3 \le 6$ (**No**) | $0$ |
| **Total** | — | — | — | — | — | **Result: $2$** |

---

## 5. Boundary Cases & Failure Modes

- **Single Element ($N = 1$):** Returns $0$ pairs.
- **Strictly Decreasing Array ($[5, 4, 3, 2, 1]$):** Multiple reverse pairs counted across every recursive partition $\implies \mathbf{4}$.
- **Integer Overflow in $2 \times nums[j]$:** If $nums[j] \approx 2 \times 10^9$, doubling it exceeds $2^{31} - 1$. Using 64-bit integers (`long long` in C++ or Python's native arbitrary precision) prevents overflow.
- **Duplicate Elements ($[2, 2, 2, 2]$):** $2 \ngtr 2(2) = 4$, correctly returns $0$.

---

## 6. Traps & Common Anti-Patterns

- **Interleaving Counting and Merging in One Pointer:** Because the condition $nums[i] > 2 \times nums[j]$ differs from the sorting condition $nums[i] > nums[j]$, attempting to count during standard merge sort pointer advancement causes pointer desynchronization. Running the two-pointer count pass *first*, and then executing the standard merge pass *second*, guarantees exact counts.
- **32-Bit Signed Integer Overflow:** In languages like Java or C++, `2 * nums[j]` overflows when $nums[j] > 10^9$. Explicitly casting to `long` before multiplication is strictly required.
- **Naive Binary Indexed Tree Without Coordinate Compression:** Using a Fenwick tree requires discretizing and coordinate-compressing all numbers and their doubles, adding complexity. Merge sort naturally operates in $O(N \log N)$ with zero coordinate mapping overhead.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Standard merge sort tree has depth $\log_2 N$.
  - At each level, the two-pointer counting sweep traverses each element at most once: $O(R - L)$.
  - The merging step traverses each element once: $O(R - L)$.
  - Total Time: $\mathcal{O}(N \log N)$. For $N = 5 \times 10^4$, $5 \times 10^4 \times 16 \approx 8 \times 10^5$ operations, completing in $< 45$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ temporary buffer space during merge sort.