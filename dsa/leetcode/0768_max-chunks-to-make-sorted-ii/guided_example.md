# Guided Example: Max Chunks To Make Sorted II

We trace the step-by-step array partition sorting invariant, chunk maximum abstraction, monotonic increasing stack of chunk upper bounds ($stk$), backward chunk coalescence on inversion ($v < stk[-1] \implies \text{merge}$), maximum retention ($mx = \max(merged)$), and final chunk count maximization on representative integer arrays with duplicates:

- **Input:** $arr = [2, 1, 3, 4, 4]$
- **Required output:** `4`
  - Chunk sorting conditions:
    - Partition array $arr$ into contiguous sub-arrays (chunks) $C_1, C_2, \dots, C_m$.
    - Individually sort each chunk in non-decreasing order.
    - Concatenating the sorted chunks must yield the globally sorted array:
      $$
      \text{sort}(C_1) + \text{sort}(C_2) + \dots + \text{sort}(C_m) = \text{sort}(arr)
      $$
    - Invariant: Every element in chunk $C_k$ must be $\le$ every element in chunk $C_{k + 1}$.
      - Equivalently:
        $$
        \max(C_k) \le \min(C_{k + 1}) \quad \forall k
        $$
    - Objective: Find the **maximum number of chunks** $m$.
    - For $[2, 1, 3, 4, 4]$:
      - Chunk 1: $[2, 1] \implies \text{sorted: } [1, 2]$ (max is 2).
      - Chunk 2: $[3] \implies \text{sorted: } [3]$ (min is 3, max is 3; $2 \le 3$).
      - Chunk 3: $[4] \implies \text{sorted: } [4]$ (min is 4, max is 4; $3 \le 4$).
      - Chunk 4: $[4] \implies \text{sorted: } [4]$ (min is 4, max is 4; $4 \le 4$).
      - Concatenation: $[1, 2, 3, 4, 4]$ (perfectly sorted!).
      - Total chunks formed: **4**.
- **Monotonic Stack of Chunk Maximums Invariant:**
  - **The Representative Maximum Representation:**
    - Each active chunk can be uniquely represented by its **maximum element**.
    - In a valid sequence of chunks, their maximums must form a **monotonically non-decreasing sequence**:
      $$
      stk[0] \le stk[1] \le \dots \le stk[m - 1]
      $$
  - **Processing Incoming Value $v$:**
    1. **Independent Chunk Creation ($v \ge stk[-1]$):**
       - If $v$ is greater than or equal to the maximum of the preceding chunk, $v$ can safely form its own standalone chunk:
         $$
         stk.\text{push}(v)
         $$
    2. **Chunk Collapse & Merge ($v < stk[-1]$):**
       - If $v$ is strictly smaller than the preceding chunk's maximum, it belongs to the same sorted range as that chunk and cannot stand alone!
       - In fact, $v$ must be merged backward with **all preceding chunks** whose maximum exceeds $v$.
       - The newly merged composite chunk spans from the earliest affected chunk to $v$.
       - Crucially, the maximum element of this merged chunk remains the **highest maximum encountered so far**:
         $$
         mx = stk.\text{pop}()
         $$
         $$
         \text{while } stk \ne \emptyset \text{ and } stk.\text{top}() > v: \quad stk.\text{pop}()
         $$
         $$
         stk.\text{push}(mx)
         $$
  - **Output:** The total number of valid chunks is strictly the stack size: $|stk|$.
- **Step-by-Step Worked Execution Trace on $arr = [2, 1, 3, 4, 4]$:**
  - Initialize empty stack: $stk = []$.
  - **Element 0 ($v = 2$):**
    - Stack empty $\implies$ create first chunk with maximum 2:
      $$
      stk = [\mathbf{2}]
      $$
  - **Element 1 ($v = 1$):**
    - Compare: $v < stk[-1] \iff 1 < 2 \implies \mathbf{Inversion\ Detected!}$
    - Element 1 must merge into the chunk containing 2.
    - Save chunk maximum:
      $$
      mx = stk.\text{pop}() = \mathbf{2}
      $$
    - Stack is now empty. No further previous chunks to absorb.
    - Re-insert the composite chunk's maximum:
      $$
      stk.\text{push}(mx) \implies stk = [\mathbf{2}]
      $$
    - Represents single merged chunk $[2, 1]$ with maximum 2.
  - **Element 2 ($v = 3$):**
    - Compare: $v \ge stk[-1] \iff 3 \ge 2 \implies \mathbf{Independent\ Chunk!}$
    - Push new chunk maximum:
      $$
      stk = [2, \; \mathbf{3}]
      $$
  - **Element 3 ($v = 4$):**
    - Compare: $v \ge stk[-1] \iff 4 \ge 3 \implies \mathbf{Independent\ Chunk!}$
    - Push new chunk maximum:
      $$
      stk = [2, \; 3, \; \mathbf{4}]
      $$
  - **Element 4 ($v = 4$):**
    - Compare: $v \ge stk[-1] \iff 4 \ge 4 \implies \mathbf{Independent\ Chunk!}$
    - Push new chunk maximum:
      $$
      stk = [2, \; 3, \; 4, \; \mathbf{4}]
      $$
  - **Final Output:**
    $$
    ans = |stk| = \mathbf{4}
    $$
- **Strictly Descending Sequence Trace ($arr = [5, 4, 3, 2, 1]$):**
  - Starts with $stk = [5]$.
  - Every subsequent element $4, 3, 2, 1$ is smaller than 5.
  - Each element collapses into the single existing chunk, retaining maximum 5.
  - Final stack: $[5] \implies ans = \mathbf{1}$.
- **Duplicate Elements Split Trace ($arr = [1, 1, 1, 1]$):**
  - Every element satisfies $v \ge stk[-1]$ ($1 \ge 1$).
  - Forms 4 separate chunks of size 1 $\implies ans = \mathbf{4}$.

This instance demonstrates greedy chunk boundary optimization and monotonic stack interval condensation, mathematically proves why retaining the supremum over merged intervals maintains the necessary and sufficient sorted concatenation condition, and derives $O(N)$ execution time and $O(N)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given an array $arr$ (with possible duplicates):
Find the **maximum number of chunks** such that sorting each chunk individually sorts the entire array.

```text
arr = [ 2, 1, 3, 4, 4 ]

Step 1: 2 enters -> stack: [ 2 ]
Step 2: 1 < 2 -> 1 must merge with 2! Max remains 2 -> stack: [ 2 ]
Step 3: 3 >= 2 -> can be its own chunk! -> stack: [ 2, 3 ]
Step 4: 4 >= 3 -> can be its own chunk! -> stack: [ 2, 3, 4 ]
Step 5: 4 >= 4 -> can be its own chunk! -> stack: [ 2, 3, 4, 4 ]

Total chunks = stack size = 4
Chunks: [2, 1], [3], [4], [4]
Result: 4
```

### The Invariant of the Monotonic Chunk Maximum Stack
- Each entry in the stack represents the maximum value of one chunk.
- If $v \ge stk[-1]$, $v$ can start a new chunk.
- If $v < stk[-1]$, $v$ must merge into all previous chunks whose max exceeds $v$, keeping the largest maximum $mx$ of the merged group.

---

## 2. Conceptual Foundation & Invariants

### 1. Inversion Merge Operation:
$$
\text{if } stk \ne \emptyset \ \land \ v < stk.\text{top}():
$$
$$
mx \leftarrow stk.\text{pop}(), \quad \text{while } stk \ne \emptyset \land stk.\text{top}() > v: \; stk.\text{pop}(), \quad stk.\text{push}(mx)
$$

### 2. Monotonic Chain Property:
$$
stk = [\mu_1, \mu_2, \dots, \mu_m] \quad \text{where } \mu_1 \le \mu_2 \le \dots \le \mu_m
$$
$$
ans = |stk|
$$

> **Poset Chunk Decomposition Invariant.** The maximum number of valid chunks is the length of the longest chain in the quotient poset of interval contractions satisfying $\max C_i \le \min C_{i+1}$, maintained dynamically by the monotonic stack.

---

## 3. Step-by-Step Worked Execution

We trace $arr = [2, 1, 3, 4, 4]$:

---

### Step 1: Elements 2 and 1
- Push 2 $\implies [2]$.
- $1 < 2 \implies$ merge with 2, keep max 2 $\implies [2]$.

---

### Step 2: Elements 3, 4, 4
- $3 \ge 2 \implies$ push 3 $\implies [2, 3]$.
- $4 \ge 3 \implies$ push 4 $\implies [2, 3, 4]$.
- $4 \ge 4 \implies$ push 4 $\implies [2, 3, 4, 4]$.

---

### Step 3: Output
- Length of stack: **`4`**.

---

## 4. Complete Execution Trace

| Element $v$ | Previous Stack $stk$ | Condition $v \ge stk[-1]$? | Action Taken | Preserved Maximum $mx$ | New Stack State |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $2$ | `[]` | Base | Push $2$ | — | `[2]` |
| $1$ | `[2]` | No ($1 < 2$) | Collapse with 2 | $2$ | `[2]` |
| $3$ | `[2]` | Yes ($3 \ge 2$) | Push $3$ | — | `[2, 3]` |
| $4$ | `[2, 3]` | Yes ($4 \ge 3$) | Push $4$ | — | `[2, 3, 4]` |
| **$4$** | **`[2, 3, 4]`** | **Yes ($4 \ge 4$)** | **Push $4$** | **—** | **`[2, 3, 4, 4]`** |
| **Final** | — | — | — | — | **Length = `4`** |

---

## 5. Boundary Cases & Failure Modes

- **Strictly Descending ($[5, 4, 3, 2, 1]$):** Collapses into 1 single chunk $\implies$ returns 1.
- **Strictly Increasing ($[1, 2, 3, 4, 5]$):** Each element is its own chunk $\implies$ returns $N$.
- **All Equal Elements ($[2, 2, 2, 2]$):** $v \ge stk[-1]$ holds everywhere $\implies$ returns $N$.
- **Single Element ($[1]$):** Returns 1.

---

## 6. Traps & Common Anti-Patterns

- **Discarding the Largest Maximum on Pop:** When popping elements $> v$, setting the new maximum to $v$ loses the true maximum of the merged chunk. You must store $mx = stk.pop()$ first and push $mx$ back!
- **Stopping Merge at First Predecessor:** If $arr = [4, 2, 1, 3]$, when 3 arrives it is $< 4$. If multiple previous chunks exist with max $> v$, the while loop must pop all of them.
- **Using Prefix Max vs Suffix Min:** Comparing `max_left[i] <= min_right[i+1]` is an alternative valid $O(N)$ approach, but requires 3 passes and auxiliary arrays. The monotonic stack solves it online in a single pass.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Each of the $N$ elements is pushed to the stack at most once.
  - Each element is popped from the stack at most once.
  - Total Time: strictly amortized linear $\mathcal{O}(N)$. Completes in $< 1$ ms for $N = 2000$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ memory in the worst case for the monotonic stack (when array is already sorted).
