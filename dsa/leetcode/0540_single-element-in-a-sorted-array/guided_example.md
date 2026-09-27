# Guided Example: Single Element in a Sorted Array

We trace the step-by-step index parity pairing invariant ($2k \leftrightarrow 2k+1$), bitwise XOR neighbor mapping ($mid \oplus 1$), binary search boundary bisection ($nums[mid] \ne nums[mid \oplus 1] \implies r = mid$), and logarithmic singleton isolation on representative sorted arrays:

- **Input:** $nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]$
- **Required output:** `2`
  - Array properties:
    - Sorted in non-decreasing order.
    - Exactly one element appears once; all other elements appear exactly twice.
    - Array length: $n = 9$ (always odd: $2k + 1$).
  - Target complexity: $\mathcal{O}(\log N)$ runtime, $\mathcal{O}(1)$ space.
- **Index Parity Pairing Invariant:**
  - In an undisturbed sequence of pairs, each pair occupies consecutive slots:
    $$
    (0, 1), \; (2, 3), \; (4, 5), \; (6, 7), \dots
    $$
    - The first element of each pair is at an **even index** $2m$.
    - The second element is at the adjacent **odd index** $2m + 1$.
  - **Bitwise XOR Companion Property ($i \oplus 1$):**
    - If $i$ is even: $i \oplus 1 = i + 1$ (its twin to the right).
    - If $i$ is odd: $i \oplus 1 = i - 1$ (its twin to the left).
    - Therefore, for any element in a valid pair:
      $$
      nums[i] == nums[i \oplus 1]
      $$
  - **Shift by the Singleton Element:**
    - To the left of the single element: Every element satisfies $nums[i] == nums[i \oplus 1]$.
    - At and to the right of the single element: The single element shifts all subsequent pair indices by $1$, causing the pairing condition to **fail**:
      $$
      nums[i] \ne nums[i \oplus 1]
      $$
    - The single element is the **first index** where this condition fails!
- **Binary Search execution trace:**
  - Search range: $l = 0, \; r = 8$.
  - **Iteration 1 ($l = 0, \; r = 8$):**
    - Midpoint:
      $$
      mid = (0 + 8) // 2 = \mathbf{4}
      $$
    - Element at $mid$: $nums[4] = 3$.
    - Partner index: $mid \oplus 1 = 4 \oplus 1 = \mathbf{5}$.
    - Element at partner: $nums[5] = 4$.
    - Check pairing:
      $$
      nums[4] \ne nums[5] \quad (3 \ne 4)
      $$
    - The parity relationship has broken at or before index $4$!
    - Narrow right bound:
      $$
      r \leftarrow mid = \mathbf{4}
      $$
  - **Iteration 2 ($l = 0, \; r = 4$):**
    - Midpoint:
      $$
      mid = (0 + 4) // 2 = \mathbf{2}
      $$
    - Element at $mid$: $nums[2] = 2$.
    - Partner index: $mid \oplus 1 = 2 \oplus 1 = \mathbf{3}$.
    - Element at partner: $nums[3] = 3$.
    - Check pairing:
      $$
      nums[2] \ne nums[3] \quad (2 \ne 3)
      $$
    - Condition fails at index $2$!
    - Narrow right bound:
      $$
      r \leftarrow mid = \mathbf{2}
      $$
  - **Iteration 3 ($l = 0, \; r = 2$):**
    - Midpoint:
      $$
      mid = (0 + 2) // 2 = \mathbf{1}
      $$
    - Element at $mid$: $nums[1] = 1$.
    - Partner index: $mid \oplus 1 = 1 \oplus 1 = \mathbf{0}$.
    - Element at partner: $nums[0] = 1$.
    - Check pairing:
      $$
      nums[1] == nums[0] \quad (1 == 1)
      $$
    - Pairing is completely intact at index $1$!
    - The singleton must lie strictly to the right of index $1$:
      $$
      l \leftarrow mid + 1 = 1 + 1 = \mathbf{2}
      $$
  - **Termination:**
    - $l = 2, \; r = 2 \implies l == r$.
    - Converged index: $l = \mathbf{2}$.
    - Singleton value:
      $$
      nums[2] = \mathbf{2}
      $$
- **Singleton at Array Head ($nums = [5, 1, 1, 2, 2]$):**
  - $mid = 2 \implies 2 \oplus 1 = 3 \implies nums[2] == 1, nums[3] == 2 \implies$ fails $\implies$ converges to index 0 $\implies \mathbf{5}$.
- **Singleton at Array Tail ($nums = [1, 1, 2, 2, 3]$):**
  - All left pairs intact $\implies$ advances $l$ to index 4 $\implies \mathbf{3}$.
- **Single Element Alone ($nums = [42]$):**
  - $l = 0, r = 0 \implies$ loop terminates immediately $\implies \mathbf{42}$.

This instance demonstrates binary search on parity-induced phase shifts, mathematically proves why bitwise XOR partner mapping eliminates case analysis for odd vs even midpoints, and derives $\mathcal{O}(\log N)$ runtime and $\mathcal{O}(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a sorted integer array $nums$ where every element appears twice except one element which appears once:
Find the single element in **$\mathcal{O}(\log N)$ time** and **$\mathcal{O}(1)$ space**.

```text
Indices:  0  1  2  3  4  5  6  7  8
Array:   [1, 1, 2, 3, 3, 4, 4, 8, 8]
          \ /   |  \ /   \ /   \ /
Pairs:   (0,1)  ?  (3,4) (5,6) (7,8)

Before the single element:
  Pairs start at EVEN indices: (0, 1)
After the single element:
  Pairs start at ODD indices:  (3, 4), (5, 6), (7, 8)

The singleton at index 2 shifts all subsequent pair parities!
```

### The Binary Search Parity Property
- In a normal array of pairs:
  - For any even index $2k$, its duplicate is at $2k + 1$.
  - For any odd index $2k + 1$, its duplicate is at $2k$.
- The presence of the single element causes an index shift of $+1$:
  - Every element before the single element matches its partner.
  - Every element at or after the single element fails to match its original partner.
- This creates a **monotonic boolean predicate**:
  $$
  P(i) = (nums[i] \ne nums[i \oplus 1])
  $$
  which is `False` for the prefix and `True` everywhere after.
  Binary search finds the boundary in $O(\log N)$ steps.

---

## 2. Conceptual Foundation & Invariants

### 1. Bitwise Partner Mapping ($i \oplus 1$):
- $0 \oplus 1 = 1$, and $1 \oplus 1 = 0$.
- $2 \oplus 1 = 3$, and $3 \oplus 1 = 2$.
- In general, $i \oplus 1$ flips the lowest bit, pointing an even index to its right neighbor and an odd index to its left neighbor.
- Evaluating $nums[mid] == nums[mid \oplus 1]$ works identically for both even and odd values of $mid$!

### 2. Binary Search Reduction:
Initialize $l = 0, \; r = |nums| - 1$:
While $l < r$:
1. $mid = \lfloor (l + r) / 2 \rfloor$.
2. If $nums[mid] \ne nums[mid \oplus 1]$:
   The disruption is at or to the left of $mid$:
   $$
   r \leftarrow mid
   $$
3. Else:
   Pairs are fully preserved up through $mid$; the disruption is strictly to the right:
   $$
   l \leftarrow mid + 1
   $$
Return $nums[l]$.

> **Parity Partition Invariant.** Index $l$ is guaranteed to be the first index in the array where $nums[i] \ne nums[i \oplus 1]$, which is the exact location of the unique singleton.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [1, 1, 2, 3, 3, 4, 4, 8, 8]$ ($n = 9$):

---

### Step 1: Initialize
- $l = 0, \; r = 8$.

---

### Step 2: Bisection Step 1
- $mid = (0 + 8) // 2 = 4$.
- Partner: $4 \oplus 1 = 5$.
- Compare:
  $$
  nums[4] = 3, \quad nums[5] = 4 \implies 3 \ne 4
  $$
- Pairing broken! Single element is at or to the left of 4.
- $r \leftarrow 4$.

---

### Step 3: Bisection Step 2
- $l = 0, \; r = 4$.
- $mid = (0 + 4) // 2 = 2$.
- Partner: $2 \oplus 1 = 3$.
- Compare:
  $$
  nums[2] = 2, \quad nums[3] = 3 \implies 2 \ne 3
  $$
- Pairing broken!
- $r \leftarrow 2$.

---

### Step 4: Bisection Step 3
- $l = 0, \; r = 2$.
- $mid = (0 + 2) // 2 = 1$.
- Partner: $1 \oplus 1 = 0$.
- Compare:
  $$
  nums[1] = 1, \quad nums[0] = 1 \implies 1 == 1
  $$
- Pairing intact! Disruption lies strictly to the right of index 1.
- $l \leftarrow mid + 1 = 1 + 1 = \mathbf{2}$.

---

### Step 5: Loop Terminates
- $l = 2, \; r = 2$.
- Result:
  $$
  nums[l] = nums[2] = \mathbf{2}
  $$

---

## 4. Complete Execution Trace

| Step | Range $[l, r]$ | $mid$ | Partner $mid \oplus 1$ | $nums[mid]$ | $nums[mid \oplus 1]$ | Equality Match? | Boundary Update |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **$1$** | $[0, 8]$ | $4$ | $5$ | $3$ | $4$ | No ($3 \ne 4$) | $r \leftarrow 4$ |
| **$2$** | $[0, 4]$ | $2$ | $3$ | $2$ | $3$ | No ($2 \ne 3$) | $r \leftarrow 2$ |
| **$3$** | $[0, 2]$ | $1$ | $0$ | $1$ | $1$ | **Yes ($1 == 1$)** | $l \leftarrow 2$ |
| **Done** | $[2, 2]$ | — | — | — | — | — | **Output: $nums[2] = 2$** |

---

## 5. Boundary Cases & Failure Modes

- **Singleton at Index 0 ($[9, 1, 1, 2, 2]$):** $mid=2, 2\oplus 1=3 \implies$ match $\implies r \leftarrow 0$, converges to index 0 $\implies \mathbf{9}$.
- **Singleton at Last Index ($[1, 1, 2, 2, 7]$):** All tested midpoints match their partners $\implies l$ advances until index 4 $\implies \mathbf{7}$.
- **Single Element Array ($[10]$):** $l = 0, r = 0 \implies$ loop terminates without executing $\implies \mathbf{10}$.
- **Three Elements ($[1, 2, 2]$ or $[1, 1, 2]$):** Resolves in a single binary search step.

---

## 6. Traps & Common Anti-Patterns

- **Linear Scanning with Bitwise XOR ($O(N)$):** XOR-ing the entire array finds the single element, but runs in $O(N)$ linear time. The problem strictly requires an $O(\log N)$ binary search.
- **Manual Even/Odd Conditional Branching:** Branching on `if mid % 2 == 0:` vs `else:` doubles the code and easily introduces off-by-one errors. The $mid \oplus 1$ trick unifies both branches into a single clean line.
- **Using $r = mid - 1$ on Mismatch:** If $mid$ itself is the single element, setting $r = mid - 1$ excludes the answer! Since $nums[mid]$ might be the singleton, the right bound must be set to $r = mid$.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Binary search halves the search space in each iteration: $N \to N/2 \to N/4 \to \dots \to 1$.
  - Number of iterations is strictly $\lceil \log_2 N \rceil$.
  - Each iteration performs $O(1)$ arithmetic and array index operations.
  - Total Time: strictly $\mathcal{O}(\log N)$. For $N = 10^5$, completes in $\le 17$ steps ($< 1$ microsecond).
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ auxiliary space using two pointer integers.