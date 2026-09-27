# Guided Example: Search Insert Position

We trace the step-by-step binary search insertion point determination (`bisect_left`) on representative array instances:

- **Target Present:** $\text{nums} = [1, 3, 5, 6]$, $\text{target} = 5 \implies 2$
- **Target Absent (Between Elements):** $\text{nums} = [1, 3, 5, 6]$, $\text{target} = 2 \implies 1$
- **Target Absent (Past Array End):** $\text{nums} = [1, 3, 5, 6]$, $\text{target} = 7 \implies 4$

This instance demonstrates finding the exact target match or the unique insertion position that preserves sorted order, proving why the terminating left pointer $L$ naturally converges to the insertion index in $O(\log N)$ time.

---

## 1. Instance & Teaching Goal

Given a sorted array of distinct integers $\text{nums}$ and a target value $\text{target}$, return the index if $\text{target}$ is found. If not, return the index where it would be if it were inserted in order. The runtime must be $O(\log N)$.

For $\text{nums} = [1, 3, 5, 6]$:
- If $\text{target} = 5$, it is already present at index $2$.
- If $\text{target} = 2$, it belongs between $1$ (index 0) and $3$ (index 1); inserting at index $1$ produces $[1, \mathbf{2}, 3, 5, 6]$.
- If $\text{target} = 7$, it exceeds all elements; inserting at index $4$ produces $[1, 3, 5, 6, \mathbf{7}]$.

A naive scan checks elements one by one in $O(N)$ time. Standard binary bisection finds the target or converges to the insertion position in $O(\log N)$ time with $O(1)$ space.

---

## 2. Conceptual Foundation & Invariants

### The Insertion Invariant of Binary Search
We maintain two pointers $L$ and $R$, initially spanning $[0, N - 1]$.
At each step, we evaluate midpoint $M = L + \lfloor (R - L) / 2 \rfloor$:
- If $\text{nums}[M] == \text{target}$: Return $M$ immediately.
- If $\text{nums}[M] < \text{target}$: All elements at indices $\le M$ are strictly smaller than $\text{target}$. The insertion point must be at index $\ge M + 1 \implies L \leftarrow M + 1$.
- If $\text{nums}[M] > \text{target}$: All elements at indices $\ge M$ are strictly greater than $\text{target}$. The insertion point must be at index $\le M \implies R \leftarrow M - 1$.

### Why $L$ is the Insertion Point
Throughout the loop:
1. Every element to the left of $L$ (indices $0 \dots L - 1$) is strictly $< \text{target}$.
2. Every element to the right of $R$ (indices $R + 1 \dots N - 1$) is strictly $> \text{target}$.

When the loop terminates with $L > R$, $L$ becomes equal to $R + 1$. Therefore, index $L$ is the exact boundary where all elements before it are $< \text{target}$ and all elements at or after it are $> \text{target}$. Thus, returning $L$ is mathematically guaranteed to be the correct insertion point.

---

## 3. Step-by-Step Worked Execution

We trace both present and absent target scenarios on $\text{nums} = [1, 3, 5, 6]$:

### Case 1: Target Present ($\text{target} = 5$)
- **Step 1 ($L = 0, R = 3$):**
  - Midpoint: $M = \lfloor (0 + 3) / 2 \rfloor = 1$.
  - Value: $\text{nums}[1] = 3$.
  - Compare: $3 < 5 \implies$ Target must be to the right.
  - Update: $L \leftarrow M + 1 = 2$.
- **Step 2 ($L = 2, R = 3$):**
  - Midpoint: $M = \lfloor (2 + 3) / 2 \rfloor = 2$.
  - Value: $\text{nums}[2] = 5$.
  - Compare: $\text{nums}[2] == 5 == \text{target}$.
  - Match found! Return index $2$.

---

### Case 2: Target Absent Between Elements ($\text{target} = 2$)
- **Step 1 ($L = 0, R = 3$):**
  - Midpoint: $M = \lfloor (0 + 3) / 2 \rfloor = 1$.
  - Value: $\text{nums}[1] = 3$.
  - Compare: $3 > 2 \implies$ Insertion point must be $\le 1$.
  - Update: $R \leftarrow M - 1 = 0$.
- **Step 2 ($L = 0, R = 0$):**
  - Midpoint: $M = \lfloor (0 + 0) / 2 \rfloor = 0$.
  - Value: $\text{nums}[0] = 1$.
  - Compare: $1 < 2 \implies$ Insertion point must be $> 0$.
  - Update: $L \leftarrow M + 1 = 1$.
- **Termination:** $L = 1 > R = 0$.
- Return insertion index $L = 1$.

---

### Case 3: Target Absent Past Array End ($\text{target} = 7$)
- **Step 1 ($L = 0, R = 3$):**
  - $M = 1, \text{nums}[1] = 3 < 7 \implies L \leftarrow 2$.
- **Step 2 ($L = 2, R = 3$):**
  - $M = 2, \text{nums}[2] = 5 < 7 \implies L \leftarrow 3$.
- **Step 3 ($L = 3, R = 3$):**
  - $M = 3, \text{nums}[3] = 6 < 7 \implies L \leftarrow 4$.
- **Termination:** $L = 4 > R = 3$.
- Return insertion index $L = 4$.

---

## 4. Complete Execution Trace

### Search Trace Table for $\text{target} = 2$

| Iteration | Left $L$ | Right $R$ | Midpoint $M$ | Value $\text{nums}[M]$ | Comparison to Target (2) | Pointer Update | Search Window After |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| 1 | 0 | 3 | 1 | 3 | $3 > 2$ | Shift right: $R \leftarrow 0$ | $[0, 0]$ |
| 2 | 0 | 0 | 0 | 1 | $1 < 2$ | Shift left: $L \leftarrow 1$ | Crosses ($L > R$) |
| Terminal | **1** | 0 | - | - | Loop exits ($L > R$) | **Emit $L = 1$** | Insertion index $1$ |

### Scenario Summary Table

| Input Target | Iterations Taken | Termination State $(L, R)$ | Emitted Answer | Array State After Insertion |
|:---:|:---:|:---:|:---:|:---|
| $\text{target} = 5$ | 2 | Early return at $M = 2$ | **2** | Element already at index $2$ |
| $\text{target} = 2$ | 2 | $L = 1, R = 0$ | **1** | $[1, \mathbf{2}, 3, 5, 6]$ |
| $\text{target} = 7$ | 3 | $L = 4, R = 3$ | **4** | $[1, 3, 5, 6, \mathbf{7}]$ |
| $\text{target} = 0$ | 2 | $L = 0, R = -1$ | **0** | $[\mathbf{0}, 1, 3, 5, 6]$ |

---

## 5. Algorithmic Correctness

**Soundness.** If the target is present, $\text{nums}[M] == \text{target}$ triggers an immediate return of the exact index. If absent, the loop invariant guarantees that all elements in $\text{nums}[0 \dots L-1]$ are $< \text{target}$ and all elements in $\text{nums}[L \dots N-1]$ are $> \text{target}$. Thus, placing $\text{target}$ at index $L$ preserves non-decreasing sorted order.

**Completeness.** Each iteration halves the search interval $R - L + 1$. The interval length strictly decreases toward zero, guaranteeing loop termination in at most $\lceil \log_2 N \rceil + 1$ steps.

---

## 6. Traps This Instance Exposes

- **Returning $M$ vs Returning $L$:** Returning $M$ after the loop is incorrect because $M$ could point to either side of the insertion boundary. $L$ is mathematically guaranteed to be the exact insertion point upon termination.
- **Midpoint Overflow:** Using $L + \lfloor (R - L) / 2 \rfloor$ avoids integer overflow when $L + R$ exceeds $2^{31}-1$.
- **Target Smaller Than First Element:** When $\text{target} < \text{nums}[0]$, $R$ decreases to $-1$, and $L$ remains $0$, correctly returning $0$ to prepend the element.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log N)$, where $N$ is the number of elements in $\text{nums}$. The bisection loop divides the search interval by 2 at each step.
- **Auxiliary Space Complexity:** $O(1)$. Binary search operates strictly with scalar index pointers ($L, R, M$).