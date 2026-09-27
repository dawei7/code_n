# Guided Example: 132 Pattern

We trace the step-by-step right-to-left monotonic stack scan, candidate middle-value tracking ($v_k$, the '2'), peak-value absorption ($nums[j]$, the '3'), and minimum-value detection ($nums[i] < v_k$, the '1') on representative numerical arrays:

- **Input:** $nums = [3, 1, 4, 2]$
- **Required output:** `true`
  - A 132 pattern requires three indices $i < j < k$ such that:
    $$
    nums[i] < nums[k] < nums[j]
    $$
  - Subsequence $[1, 4, 2]$ at indices $(1, 2, 3)$ satisfies $1 < 2 < 4$.
- **Right-to-left monotonic stack trace:**
  - Initialize: stack $stk = []$, largest candidate '2' value $v_k = -\infty$
  - **Step 1 (Scan $nums[3] = 2$):**
    - Check $x < v_k$: $2 < -\infty$ (False).
    - Stack empty. Push $2 \implies stk = [2], \; v_k = -\infty$.
  - **Step 2 (Scan $nums[2] = 4$):**
    - Check $x < v_k$: $4 < -\infty$ (False).
    - Stack top is $2 < 4$. Pop $2$ and update candidate '2':
      $$
      v_k \leftarrow 2
      $$
    - Push candidate '3' onto stack $\implies stk = [4], \; v_k = 2$.
    - Meaning: We have established a valid $(j, k)$ pair: $(nums[j]=4, nums[k]=2)$ with $j < k$ and $4 > 2$.
  - **Step 3 (Scan $nums[1] = 1$):**
    - Check $x < v_k$:
      $$
      1 < 2 \quad (\mathbf{True!})
      $$
    - We have found $nums[i] = 1 < v_k = 2 < nums[j] = 4$ with $i < j < k$!
    - Full 132 pattern verified: $[1, 4, 2]$.
    - Return **`true`** immediately.
- **Strictly Increasing Sequence:** $nums = [1, 2, 3, 4] \implies$ right-to-left scan never pops anything ($v_k$ remains $-\infty$) $\implies \mathbf{false}$
- **Strictly Decreasing Sequence:** $nums = [4, 3, 2, 1] \implies$ each element is smaller than preceding right elements $\implies v_k$ is updated but no element $< v_k$ exists to the left $\implies \mathbf{false}$

This instance demonstrates reverse monotonic stack filtering, mathematically proves why maximizing $v_k$ maximizes the probability of finding a valid $nums[i] < v_k$, and derives $O(N)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an integer array $nums = [3, 1, 4, 2]$:
A **132 pattern** is a subsequence of three integers $nums[i], nums[j], nums[k]$ such that:
$$
i < j < k \quad \text{and} \quad nums[i] < nums[k] < nums[j]
$$
Return `true` if there is a 132 pattern in $nums$, otherwise return `false`.

```text
Elements along Array Indices:
  Index 0: 3
  Index 1: 1  <- '1' (Smallest: nums[i])
  Index 2: 4  <- '3' (Peak:     nums[j])
  Index 3: 2  <- '2' (Middle:   nums[k])

Subsequence [1, 4, 2] satisfies 1 < 2 < 4 with indices 1 < 2 < 3.
```

### The Inverted Role Assignment
- Trying to fix $i$ and search forward for $j$ and $k$ leads to $O(N^2)$ checks.
- **Scanning Backwards (Right to Left):**
  - We encounter elements from right to left, meaning we see candidates for $k$ before candidates for $j$, and finally candidates for $i$.
  - We maintain a variable $v_k$ that records the **largest valid '2' candidate** discovered so far.
  - To maximize the chance that a future element $nums[i]$ satisfies $nums[i] < v_k$, **we want $v_k$ to be as large as possible**.
  - A monotonic decreasing stack of potential '3's allows us to pop smaller elements into $v_k$ whenever a larger peak $nums[j]$ is found.
  - Once $v_k$ is set, any subsequent element $x$ scanned to the left satisfying $x < v_k$ instantly triggers the 132 pattern.

---

## 2. Conceptual Foundation & Invariants

### 1. Reverse Monotonic Stack Mechanics:
Scan $nums$ from index $n - 1$ down to $0$:
1. **Target Check:** If current element $x < v_k$:
   - $x$ serves as $nums[i]$.
   - $v_k$ serves as $nums[k]$.
   - The element that previously popped $v_k$ from the stack serves as $nums[j]$.
   - The 132 pattern is complete $\implies$ Return `True`.
2. **Stack Maintenance (Popping Candidate '2's):**
   - While the stack is non-empty and $stk[\text{top}] < x$:
     - Current element $x$ is larger than the stack top.
     - The popped element was situated to the right of $x$, so it is a valid $nums[k]$ with $nums[j] = x > nums[k]$.
     - Update $v_k \leftarrow stk.\text{pop}()$.
     - By the end of the while loop, $v_k$ holds the largest element to the right of $x$ that is smaller than $x$.
3. **Pushing Candidate '3':**
   - Push $x$ onto the stack: $stk.\text{append}(x)$.

> **Maximality Invariant.** At any point in the backward scan, $v_k$ represents the maximum value among all elements that have a strictly larger element positioned somewhere between their index and the current scan cursor.

---

## 3. Step-by-Step Worked Execution

We trace $nums = [3, 1, 4, 2]$:
Initialize $stk = [], \; v_k = -\infty$. Scan in reverse: $2, 4, 1, 3$.

---

### Step 1: Scan $x = nums[3] = 2$
- Test condition $x < v_k \iff 2 < -\infty$ (False).
- Stack is empty $\implies$ While loop does not run.
- Push $2$ onto stack:
  $$
  stk = [2], \quad v_k = -\infty
  $$

---

### Step 2: Scan $x = nums[2] = 4$
- Test condition $x < v_k \iff 4 < -\infty$ (False).
- While loop: $stk$ top is $2 < x (4)$:
  - Pop $2$ from stack.
  - Update:
    $$
    v_k \leftarrow 2
    $$
- Stack is now empty.
- Push $4$ onto stack:
  $$
  stk = [4], \quad v_k = 2
  $$
- Interpretation: Node $4$ is active as candidate '3', and $v_k = 2$ is active as candidate '2'.

---

### Step 3: Scan $x = nums[1] = 1$
- Test condition $x < v_k$:
  $$
  1 < 2 \quad (\mathbf{True!})
  $$
- We have:
  - $nums[i] = 1$ (index 1)
  - $nums[j] = 4$ (index 2)
  - $nums[k] = 2$ (index 3)
  - Indices: $1 < 2 < 3$.
  - Values: $1 < 2 < 4$.
- The 132 pattern is fully satisfied.
- Return **`true`**.

---

## 4. Complete Execution Trace

| Reverse Step | Scanned $x$ | Check $x < v_k$ | Stack Before | Elements Popped to $v_k$ | New $v_k$ Value | Stack After | Action Taken |
|:---:|:---:|:---:|:---|:---|:---:|:---|:---|
| **1** | $2$ (idx 3) | $2 < -\infty$ (No) | `[]` | None | $-\infty$ | `[2]` | Push 2 |
| **2** | $4$ (idx 2) | $4 < -\infty$ (No) | `[2]` | Pop $2$ | **$2$** | `[4]` | $v_k$ becomes 2, Push 4 |
| **3** | $1$ (idx 1) | $1 < 2$ (**YES**) | `[4]` | — | $2$ | — | **Pattern Found: [1, 4, 2] -> True** |

---

## 5. Boundary Cases & Failure Modes

- **Length Less Than 3 ($N < 3$):** Cannot form a triplet $\implies$ loop exits $\implies \mathbf{false}$.
- **Strictly Increasing ($[1, 2, 3, 4]$):** Reverse scan is $[4, 3, 2, 1]$. Each element is smaller than the stack top, so nothing is ever popped to $v_k$. $v_k$ remains $-\infty$, returns $\mathbf{false}$.
- **Strictly Decreasing ($[4, 3, 2, 1]$):** Reverse scan is $[1, 2, 3, 4]$. Each element pops the previous smaller element, so $v_k$ updates ($1 \to 2 \to 3$), but every subsequent element scanned to the left is larger than $v_k$. Returns $\mathbf{false}$.
- **Duplicate Values ($[1, 1, 1]$):** Non-strict inequality in while loop does not pop equals. Returns $\mathbf{false}$.

---

## 6. Traps & Common Anti-Patterns

- **Forward Scan with Minimum Array ($O(N^2)$):** Maintaining running prefix minimums for $nums[i]$ and searching for pairs $(j, k)$ often degenerates to $O(N^2)$ unless paired with balanced binary search trees. The reverse monotonic stack guarantees $O(N)$ linear time.
- **Forgetting to Initialize $v_k$ to $-\infty$:** Initializing $v_k = 0$ fails on arrays with negative numbers (e.g. $[-2, 1, 2, -1]$).
- **Popping with `<=` Instead of `<`:** If $x == stk[\text{top}]$, popping causes duplicate values to become $v_k$, potentially matching equal elements when strict inequality $nums[i] < nums[k] < nums[j]$ is required.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - The array of length $N$ is scanned once in reverse.
  - Each element is pushed onto the stack at most once and popped at most once.
  - Total operations across all while-loop iterations are bounded by $N$.
  - Total Time: $\mathcal{O}(N)$. For $N = 2 \times 10^5$, executes in $< 15$ ms.
- **Auxiliary Space Complexity:**
  - The monotonic stack stores at most $N$ integers in the worst case.
  - Total Auxiliary Space: $\mathcal{O}(N)$.
