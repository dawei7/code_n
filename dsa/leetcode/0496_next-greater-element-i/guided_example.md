# Guided Example: Next Greater Element I

We trace the step-by-step reverse monotonic stack traversal, smaller-element shadow popping ($stk[-1] \le x$), immediate rightward successor recording ($d[x] = stk[-1]$), default fallback assignment ($-1$), and $O(1)$ query resolution on representative integer arrays:

- **Input:**
  - Query array: $nums1 = [4, 1, 2]$
  - Source array: $nums2 = [1, 3, 4, 2]$
- **Required output:** `[-1, 3, -1]`
  - Query resolution requirement: For each $x \in nums1$, find the first element strictly greater than $x$ that appears to the right of $x$ in $nums2$.
- **Reverse Monotonic Stack Trace on $nums2$:**
  - Scan $nums2$ in reverse order: $[2, \; 4, \; 3, \; 1]$
  - Stack invariant: Elements are strictly decreasing from bottom to top.
  - **Step 1 (Element $x = 2$, index 3):**
    - Stack is empty: no element exists to the right of $2$.
    - Next greater: none $\implies d[2] = -1$
    - Push $2$ onto stack: $stk = [2]$
  - **Step 2 (Element $x = 4$, index 2):**
    - Top of stack is $2 < 4$:
      - Element $2$ is both smaller than $4$ and further to the right.
      - Any element to the left of $4$ looking rightward will see $4$ before it could ever see $2$. Element $2$ is permanently shadowed!
      - Pop $2$ from stack.
    - Stack is now empty: no element to the right of $4$ is larger than $4$.
    - Next greater: none $\implies d[4] = -1$
    - Push $4$ onto stack: $stk = [4]$
  - **Step 3 (Element $x = 3$, index 1):**
    - Top of stack is $4 > 3$:
      - $4$ is strictly greater than $3$!
      - First greater element to the right: $d[3] = \mathbf{4}$
    - Push $3$ onto stack: $stk = [4, 3]$
  - **Step 4 (Element $x = 1$, index 0):**
    - Top of stack is $3 > 1$:
      - First greater element to the right: $d[1] = \mathbf{3}$
    - Push $1$ onto stack: $stk = [4, 3, 1]$
  - Precomputed successor dictionary $d$:
    $$
    d = \{2: -1, \; 4: -1, \; 3: 4, \; 1: 3\}
    $$
- **Step 5: Answer Queries in $nums1 = [4, 1, 2]$:**
  - For $x = 4 \implies d[4] = \mathbf{-1}$
  - For $x = 1 \implies d[1] = \mathbf{3}$
  - For $x = 2 \implies d[2] = \mathbf{-1}$
  - Combined result: **`[-1, 3, -1]`**.
- **Strictly Increasing Source Instance ($nums2 = [1, 2, 3, 4]$):**
  - Every element's next greater is its immediate right neighbor $\implies [2, 3, 4, -1]$
- **Strictly Decreasing Source Instance ($nums2 = [4, 3, 2, 1]$):**
  - No element has any greater element to its right $\implies$ all map to $-1$

This instance demonstrates monotonic stack filtering and shadow elimination, mathematically proves why obsolete smaller elements never serve as future rightward successors, and derives $O(M + N)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given two distinct integer arrays $nums1$ and $nums2$ where $nums1$ is a subset of $nums2$:
The **next greater element** of $x$ in $nums2$ is the first element to the right of $x$ that is strictly greater than $x$.
For each element in $nums1$, find its next greater element in $nums2$. If no such element exists, return `-1`.

```text
nums2: [ 1,   3,   4,   2 ]
         |    |    |    |
         v    v    v    v
Next:    3    4   -1   -1

Querying nums1 = [4, 1, 2]:
  4 -> -1
  1 ->  3
  2 -> -1
Output: [-1, 3, -1]
```

### The Shadowing Principle of Monotonic Stacks
Why traverse backwards from right to left?
- When considering a candidate $x$, any element $y$ to the right of $x$ that is **smaller than or equal to $x$ ($y \le x$) can never be the next greater element for any future element to the left of $x$**!
- Why? Because $x$ is both larger than $y$ and positioned closer to any future element on the left. $x$ completely "shadows" $y$.
- By popping all elements $\le x$, the stack maintains a strictly decreasing sequence of candidates.
- The top of the stack is guaranteed to be the **closest greater element** to the right of $x$.

---

## 2. Conceptual Foundation & Invariants

### 1. Reverse Traversal & Stack Invariant:
Traversing $nums2$ from index $n - 1$ down to $0$:
- The stack stores a monotonically decreasing subsequence of elements to the right of the current index:
  $$
  stk[0] > stk[1] > \dots > stk[-1]
  $$
- For current element $x$:
  1. Pop while $stk \text{ is non-empty and } stk[-1] < x$.
  2. If $stk$ is non-empty:
     $$
     d[x] \leftarrow stk[-1]
     $$
  3. If $stk$ is empty:
     $$
     d[x] \leftarrow -1
     $$
  4. Push $x$ onto stack: $stk.\text{append}(x)$.

### 2. Query Lookup:
For each $q \in nums1$:
Retrieve $d.get(q, -1)$ in $O(1)$ time.

> **Monotonic Invariant.** At all steps, every element currently in $stk$ is strictly greater than all elements above it, ensuring the topmost element is the unique closest greater rightward successor.

---

## 3. Step-by-Step Worked Execution

We trace $nums2 = [1, 3, 4, 2]$ in reverse: $[2, 4, 3, 1]$:
Initialize $stk = [], \; d = \{\}$.

---

### Step 1: Element $x = 2$ (Index 3)
- Stack is empty.
- No larger element to the right:
  $$
  d[2] = -1
  $$
- Push $2$: $stk = [2]$.

---

### Step 2: Element $x = 4$ (Index 2)
- Top of stack is $2 < 4$.
  - Pop $2$ (shadowed by $4$).
- Stack is now empty.
- No larger element to the right:
  $$
  d[4] = -1
  $$
- Push $4$: $stk = [4]$.

---

### Step 3: Element $x = 3$ (Index 1)
- Top of stack is $4 > 3$.
  - $4$ is strictly greater than $3$.
  - Assign next greater:
    $$
    d[3] = \mathbf{4}
    $$
- Push $3$: $stk = [4, 3]$.

---

### Step 4: Element $x = 1$ (Index 0)
- Top of stack is $3 > 1$.
  - $3$ is strictly greater than $1$.
  - Assign next greater:
    $$
    d[1] = \mathbf{3}
    $$
- Push $1$: $stk = [4, 3, 1]$.

---

### Step 5: Answer Queries in $nums1 = [4, 1, 2]$
- Query $4 \implies d[4] = \mathbf{-1}$
- Query $1 \implies d[1] = \mathbf{3}$
- Query $2 \implies d[2] = \mathbf{-1}$
Output: **`[-1, 3, -1]`**.

---

## 4. Complete Execution Trace

| Processed $x \in nums2$ | Stack Before | Elements Popped ($\le x$) | Stack Top After Pop | Next Greater $d[x]$ | Stack After Push |
|:---:|:---:|:---:|:---:|:---:|:---:|
| **$2$** | `[]` | None | None | **$-1$** | `[2]` |
| **$4$** | `[2]` | $2$ | None | **$-1$** | `[4]` |
| **$3$** | `[4]` | None | $4$ | **$4$** | `[4, 3]` |
| **$1$** | `[4, 3]` | None | $3$ | **$3$** | `[4, 3, 1]` |

---

## 5. Boundary Cases & Failure Modes

- **Single Element ($nums2 = [10]$):** Stack empty $\implies d[10] = -1$.
- **All Decreasing ($nums2 = [5, 4, 3, 2, 1]$):** Every element is smaller than previous elements, but to their *right* all elements are smaller $\implies$ every query returns $-1$.
- **All Increasing ($nums2 = [1, 2, 3, 4, 5]$):** Each element's successor is the number immediately to its right ($d[x] = x + 1$).
- **$nums1$ Size 1:** Single $O(1)$ dictionary lookup.

---

## 6. Traps & Common Anti-Patterns

- **Searching Linearly for Every Query ($O(M \cdot N)$):** For each number in $nums1$, searching $nums2$ to the right takes $O(M \cdot N)$ time. When $M, N = 10^4$, this requires $10^8$ comparisons. Monotonic stack precomputes all answers in $O(N)$ time.
- **Using Strict Greater vs Greater-or-Equal in Pop:** Because elements are distinct, `stk[-1] < x` and `stk[-1] <= x` are equivalent. If duplicates were present, popping $\le x$ would correctly retain only strictly greater elements.
- **Forward Traversal Without Index Tracking:** A forward traversal with a monotonic stack is also possible, but requires storing values waiting for their match. Reverse traversal directly assigns each element's answer on the spot.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - In the reverse pass of $nums2$, each of the $N$ elements is pushed onto the stack exactly once.
  - Each element is popped from the stack at most once across the entire loop.
  - Precomputation takes $O(N)$ amortized time.
  - Answering $M$ queries in $nums1$ takes $O(M)$ hash map lookups.
  - Total Time: $\mathcal{O}(M + N)$. Completes in $< 5$ ms for $M, N \le 1000$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space for the hash map $d$ and the monotonic stack $stk$.
