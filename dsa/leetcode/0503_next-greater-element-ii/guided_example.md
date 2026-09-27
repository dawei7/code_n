# Guided Example: Next Greater Element II

We trace the step-by-step circular array virtual doubling ($2N$ iteration space), modular index addressing ($i \pmod n$), reverse monotonic stack filtering ($stk[-1] \le nums[i]$), wrap-around successor discovery, and final array population on representative circular arrays:

- **Input:** $nums = [1, 2, 1]$
- **Required output:** `[2, -1, 2]`
  - Array length: $n = 3$
  - Circular rule: The search wraps around past the end of the array to the front ($nums[2]$ is followed by $nums[0]$).
  - Objective: Find the first strictly greater element in circular clockwise traversal for each element.
- **Reverse Monotonic Stack with Virtual Doubling ($2n - 1 \dots 0$):**
  - Loop index ranges from $5$ down to $0$ (traversing the virtual concatenated array $[1, 2, 1, 1, 2, 1]$).
  - Initialize stack $stk = []$ and result $ans = [-1, -1, -1]$.
  - **Pass 1: Priming the Stack with Wrap-Around Candidates ($i = 5 \dots 3$):**
    - **Step 1 ($i = 5$, $idx = 2$, value $nums[2] = 1$):**
      - Stack is empty. Push $1 \implies stk = [1]$.
    - **Step 2 ($i = 4$, $idx = 1$, value $nums[1] = 2$):**
      - Top is $1 \le 2 \implies$ pop $1$.
      - Stack empty. Push $2 \implies stk = [2]$.
    - **Step 3 ($i = 3$, $idx = 0$, value $nums[0] = 1$):**
      - Top is $2 > 1$. Stack retains $[2]$.
      - Push $1 \implies stk = [2, 1]$.
    - *At the end of Pass 1, $stk$ contains all elements from the front of the array ready to serve as wrap-around targets!*
  - **Pass 2: Resolving Final Answers ($i = 2 \dots 0$):**
    - **Step 4 ($i = 2$, $idx = 2$, value $nums[2] = 1$):**
      - Top of stack is $1 \le 1 \implies$ pop $1$.
      - Top of stack is now $2 > 1$.
      - Next greater for $nums[2]$ is $stk[-1] = \mathbf{2}$!
      - Update: $ans[2] = \mathbf{2}$.
      - Push $1 \implies stk = [2, 1]$.
    - **Step 5 ($i = 1$, $idx = 1$, value $nums[1] = 2$):**
      - Top of stack is $1 \le 2 \implies$ pop $1$.
      - Top of stack is $2 \le 2 \implies$ pop $2$.
      - Stack is now empty: no element in the entire circular array is strictly greater than the maximum value $2$.
      - Next greater remains: $ans[1] = \mathbf{-1}$.
      - Push $2 \implies stk = [2]$.
    - **Step 6 ($i = 0$, $idx = 0$, value $nums[0] = 1$):**
      - Top of stack is $2 > 1$.
      - Next greater for $nums[0]$ is $stk[-1] = \mathbf{2}$!
      - Update: $ans[0] = \mathbf{2}$.
      - Push $1 \implies stk = [2, 1]$.
  - Final results array: **`[2, -1, 2]`**.
- **Mixed Successors Instance ($nums = [1, 2, 3, 4, 3]$):**
  - Local successors: $1 \to 2, 2 \to 3, 3 \to 4$.
  - Maximum element $4 \to -1$.
  - Trailing element $3$ wraps around to find $4 \implies [2, 3, 4, -1, 4]$.
- **All Elements Equal ($nums = [5, 5, 5]$):**
  - Strict inequality requires $stk[-1] > nums[i]$; since all equal elements are popped $\implies \mathbf{[-1, -1, -1]}$.

This instance demonstrates circular buffer unfolding via virtual concatenation, mathematically proves why a 2-pass reverse monotonic scan resolves all circular forward dependencies, and derives $O(N)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a circular integer array $nums = [1, 2, 1]$:
Find the **next greater element** for every element in $nums$.
The next greater number of $nums[i]$ is the first number strictly greater than $nums[i]$ traversing clockwise, wrapping around from the end of the array to the beginning.
If no greater element exists, return `-1`.

```text
Circular Array: [ 1,  2,  1 ]
                     ^
       1  ----->  2  ----->  1
       ^                     |
       |---------------------| (Wraps around!)

For nums[0] = 1: Next greater is 2.
For nums[1] = 2: No element is greater -> -1.
For nums[2] = 1: Looks right, wraps around to front, finds 2 -> 2.

Output: [2, -1, 2]
```

### The $2N$ Array Unfolding Concept
Rather than creating complex circular pointer logic:
- A circular array of length $n$ can be conceptually duplicated into a linear array of length $2n$:
  $$
  [nums[0], \dots, nums[n-1], \; nums[0], \dots, nums[n-1]]
  $$
- Any element $nums[i]$ only needs to look at the next $n - 1$ elements in this doubled array.
- By running a reverse monotonic stack over the virtual index range $2n - 1$ down to $0$ with modulo indexing $i \pmod n$:
  - The first pass ($2n-1 \dots n$) loads the rightward circular wrap-around candidates into the stack.
  - The second pass ($n-1 \dots 0$) reads the exact answers into $ans[i]$.

---

## 2. Conceptual Foundation & Invariants

### 1. Reverse Traversal with Modulo Arithmetic:
Loop virtual index $k$ from $2n - 1$ down to $0$:
$$
i = k \pmod n
$$
- While $stk$ is non-empty and $stk[-1] \le nums[i]$:
  Pop obsolete smaller or equal elements: $stk.\text{pop}()$.
- If $stk$ is non-empty:
  $$
  ans[i] \leftarrow stk[-1]
  $$
- Push current element:
  $$
  stk.\text{append}(nums[i])
  $$

### 2. Strict Inequality Invariant:
Because we need elements **strictly greater**, we pop all elements that are less than OR equal to $nums[i]$ (`stk[-1] <= nums[i]`). This ensures that duplicate numbers cannot falsely serve as their own next greater element.

> **Circular Coverage Invariant.** Traversing $2n$ virtual indices guarantees that when the second pass evaluates $nums[i]$, the stack contains precisely the monotonic rightward horizon wrapping around the entire ring.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [1, 2, 1]$ ($n = 3$):
Virtual loop runs $k = 5$ down to $0$. Initialize $ans = [-1, -1, -1], stk = []$.

---

### Phase 1: Priming the Stack ($k = 5 \dots 3$)

- **Step 1 ($k = 5, i = 2$, value $nums[2] = 1$):**
  - Stack empty.
  - Push $1 \implies stk = [1]$.

- **Step 2 ($k = 4, i = 1$, value $nums[1] = 2$):**
  - Top $1 \le 2 \implies$ pop $1$.
  - Stack empty.
  - Push $2 \implies stk = [2]$.

- **Step 3 ($k = 3, i = 0$, value $nums[0] = 1$):**
  - Top $2 > 1$.
  - Push $1 \implies stk = [2, 1]$.

---

### Phase 2: Computing Final Answers ($k = 2 \dots 0$)

- **Step 4 ($k = 2, i = 2$, value $nums[2] = 1$):**
  - Top is $1 \le 1 \implies$ pop $1$.
  - Top is now $2 > 1$.
  - Valid successor found!
    $$
    ans[2] = stk[-1] = \mathbf{2}
    $$
  - Push $1 \implies stk = [2, 1]$.

- **Step 5 ($k = 1, i = 1$, value $nums[1] = 2$):**
  - Top $1 \le 2 \implies$ pop $1$.
  - Top $2 \le 2 \implies$ pop $2$.
  - Stack empty $\implies$ no element strictly greater in the entire array.
  - $ans[1]$ remains $\mathbf{-1}$.
  - Push $2 \implies stk = [2]$.

- **Step 6 ($k = 0, i = 0$, value $nums[0] = 1$):**
  - Top is $2 > 1$.
  - Valid successor found!
    $$
    ans[0] = stk[-1] = \mathbf{2}
    $$
  - Push $1 \implies stk = [2, 1]$.

---

### Final Result:
$$
ans = \mathbf{[2, -1, 2]}
$$

---

## 4. Complete Execution Trace

| Virtual Step $k$ | Real Index $i = k \pmod n$ | Value $nums[i]$ | Popped Elements ($\le nums[i]$) | Stack Top After Pop | $ans[i]$ Assigned | Final Stack State |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| **$5$** | $2$ | $1$ | None | None | — | `[1]` |
| **$4$** | $1$ | $2$ | $1$ | None | — | `[2]` |
| **$3$** | $0$ | $1$ | None | $2$ | — | `[2, 1]` |
| **$2$** | $2$ | $1$ | $1$ | $2$ | **$2$** | `[2, 1]` |
| **$1$** | $1$ | $2$ | $1, 2$ | None | **$-1$** | `[2]` |
| **$0$** | $0$ | $1$ | None | $2$ | **$2$** | `[2, 1]` |

---

## 5. Boundary Cases & Failure Modes

- **Single Element ($nums = [10]$):** Loop runs twice with same element $\implies$ popped itself $\implies \mathbf{[-1]}$.
- **All Identical Values ($nums = [3, 3, 3]$):** Equality condition `stk[-1] <= nums[i]` pops all copies $\implies \mathbf{[-1, -1, -1]}$.
- **Strictly Decreasing ($nums = [5, 4, 3, 2, 1]$):** Every element wraps around to find $5$, except $5$ itself $\implies \mathbf{[-1, 5, 5, 5, 5]}$.
- **Strictly Increasing ($nums = [1, 2, 3, 4, 5]$):** Each element finds its right neighbor; $5$ wraps around but finds nothing larger $\implies \mathbf{[2, 3, 4, 5, -1]}$.

---

## 6. Traps & Common Anti-Patterns

- **Using Strict Inequality in Pop (`stk[-1] < nums[i]`):** If duplicates exist (e.g. $[1, 2, 2, 1]$), popping only $< x$ allows an identical value $2$ to be treated as "greater than" $2$. Popping $\le x$ enforces strictly greater successors.
- **Physically Duplicating the Array ($nums + nums$):** Allocating a physical array of size $2N$ wastes memory. Virtual indexing $i = k \pmod n$ achieves identical behavior with zero extra array allocation.
- **Stopping at $N$ Iterations:** A single linear pass cannot find wrap-around successors that appear before an element. Exactly $2N$ virtual steps are necessary and sufficient to cover the full circle.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - The virtual loop runs $2N$ iterations.
  - Each virtual element is pushed onto the stack once and popped at most once.
  - Total Time: $\mathcal{O}(N)$ amortized. For $N = 10^4$, $2 \times 10^4$ operations, completing in $< 5$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ space to store the monotonic stack and output array.
