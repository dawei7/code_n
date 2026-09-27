# Guided Example: Largest Rectangle in Histogram

We trace the step-by-step monotonic increasing stack and sentinel boundary calculation on a representative histogram:

- **Input:** $\text{heights} = [2, 1, 5, 6, 2, 3]$
- **Required output:** $10$

This instance demonstrates monotonic increasing stack mechanics, using sentinel indices ($-1$ and $N$) to eliminate boundary branches, popping bars to compute maximal width spans ($w = i - \text{stack}[-1] - 1$), and finding the optimal $2 \times 5 = 10$ rectangular area in $O(N)$ time.

---

## 1. Instance & Teaching Goal

Given an array of $N = 6$ integers $\text{heights} = [2, 1, 5, 6, 2, 3]$ where each bar has width $1$, find the area of the largest rectangle in the histogram.

For any rectangle spanning from bar $L$ to bar $R$, its height is limited by the minimum bar height in that range:
$$
\text{Area}(L, R) = (R - L + 1) \times \min_{L \le k \le R}(\text{heights}[k])
$$
In this histogram:
- A rectangle of height 6 has width 1 (at index 3) $\implies 6 \times 1 = 6$.
- A rectangle of height 5 has width 2 (spans indices 2 and 3) $\implies 5 \times 2 = 10$.
- A rectangle of height 2 has width 4 (spans indices 2 through 5) $\implies 2 \times 4 = 8$.
- A rectangle of height 1 spans the entire histogram (width 6) $\implies 1 \times 6 = 6$.
The maximum area is $10$.

A brute-force search evaluating all $O(N^2)$ intervals takes $O(N^2)$ time.
A monotonic increasing stack allows us to determine both the left and right limiting boundaries for every bar in a single $O(N)$ linear pass.

---

## 2. Conceptual Foundation & Invariants

### The Monotonic Stack Invariant
We maintain a stack of indices whose heights are strictly increasing from bottom to top.
- We append a sentinel value $0$ at the end of $\text{heights}$:
  $$
  \text{heights} = [2, 1, 5, 6, 2, 3, \mathbf{0}]
  $$
- We seed the stack with sentinel index $-1$: $\text{stack} = [-1]$.

### Popping & Width Derivation
When index $i$ is encountered with height $h_i$:
While $\text{stack}[-1] \ne -1$ and $\text{heights}[i] < \text{heights}[\text{stack}[-1]]$:
1. Pop the top index: $\text{mid} = \text{stack.pop()}$.
2. The height of the rectangle bounded by $\text{mid}$ is:
   $$
   h = \text{heights}[\text{mid}]
   $$
3. Because the stack is strictly increasing, the nearest smaller bar to the left is the new stack top $\text{stack}[-1]$.
4. The nearest smaller bar to the right is the current index $i$.
5. The maximal width for height $h$ is:
   $$
   w = i - \text{stack}[-1] - 1
   $$
6. Calculate candidate area:
   $$
   \text{max\_area} = \max(\text{max\_area}, \, h \times w)
   $$

Once all taller bars are popped, push index $i$ onto the stack.

> **Invariant.** For every popped index `mid`, $\text{stack}[-1]$ is the exact first index to the left with height smaller than `heights[mid]`, and $i$ is the exact first index to the right with height smaller than or equal to `heights[mid]`.

---

## 3. Step-by-Step Worked Execution

We trace $[2, 1, 5, 6, 2, 3, 0]$ with initial $\text{stack} = [-1]$:

### Step 1 ($i = 0, \text{height} = 2$)
- Stack top is $-1$. Push $0$.
- Stack: `[-1, 0]`.

---

### Step 2 ($i = 1, \text{height} = 1$)
- $\text{heights}[1] = 1 < \text{heights}[0] = 2$.
- **Pop $\text{mid} = 0$ ($h = 2$):**
  - Left smaller boundary: $\text{stack}[-1] = -1$.
  - Right smaller boundary: $i = 1$.
  - Width: $w = 1 - (-1) - 1 = 1$.
  - Area: $2 \times 1 = 2$. $\text{max\_area} \leftarrow 2$.
- Stack: `[-1]`. Push $1$.
- Stack: `[-1, 1]`.

---

### Step 3 ($i = 2, \text{height} = 5$)
- $5 > \text{heights}[1] = 1$. Push $2$.
- Stack: `[-1, 1, 2]`.

---

### Step 4 ($i = 3, \text{height} = 6$)
- $6 > \text{heights}[2] = 5$. Push $3$.
- Stack: `[-1, 1, 2, 3]`.

---

### Step 5 ($i = 4, \text{height} = 2$)
- $\text{heights}[4] = 2 < \text{heights}[3] = 6$.
  - **Pop $\text{mid} = 3$ ($h = 6$):**
    - Left boundary: $\text{stack}[-1] = 2$. Right: $i = 4$.
    - Width: $w = 4 - 2 - 1 = 1$.
    - Area: $6 \times 1 = 6$. $\text{max\_area} \leftarrow \max(2, 6) = 6$.
- Still $2 < \text{heights}[2] = 5$:
  - **Pop $\text{mid} = 2$ ($h = 5$):**
    - Left boundary: $\text{stack}[-1] = 1$. Right: $i = 4$.
    - Width: $w = 4 - 1 - 1 = 2$.
    - Area: $5 \times 2 = \mathbf{10}$! $\text{max\_area} \leftarrow \max(6, 10) = 10$.
- Now $2 > \text{heights}[1] = 1$. Stop popping.
- Push $4$. Stack: `[-1, 1, 4]`.

---

### Step 6 ($i = 5, \text{height} = 3$)
- $3 > \text{heights}[4] = 2$. Push $5$.
- Stack: `[-1, 1, 4, 5]`.

---

### Step 7 ($i = 6, \text{height} = 0$, Sentinel)
- Sentinel forces all remaining bars off the stack:
  - **Pop $\text{mid} = 5$ ($h = 3$):**
    - Left: $\text{stack}[-1] = 4$. Right: $6$. Width: $6 - 4 - 1 = 1$. Area: $3 \times 1 = 3$.
  - **Pop $\text{mid} = 4$ ($h = 2$):**
    - Left: $\text{stack}[-1] = 1$. Right: $6$. Width: $6 - 1 - 1 = 4$. Area: $2 \times 4 = 8$.
  - **Pop $\text{mid} = 1$ ($h = 1$):**
    - Left: $\text{stack}[-1] = -1$. Right: $6$. Width: $6 - (-1) - 1 = 6$. Area: $1 \times 6 = 6$.
- Stack empty down to sentinel $[-1]$. Loop finishes.

Global maximum area: $\mathbf{10}$.

---

## 4. Complete Execution Trace

| Index $i$ | Bar $\text{heights}[i]$ | Stack State (Indices) | Popped $\text{mid}$ | Popped Height $h$ | Left Bound | Right Bound $i$ | Width $w$ | Computed Area | New Max Area |
|:---:|:---:|:---|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | 2 | `[-1, 0]` | - | - | - | - | - | - | 0 |
| 1 | 1 | `[-1]` | 0 | 2 | -1 | 1 | 1 | $2 \times 1 = 2$ | 2 |
| - | - | `[-1, 1]` | - | - | - | - | - | - | 2 |
| 2 | 5 | `[-1, 1, 2]` | - | - | - | - | - | - | 2 |
| 3 | 6 | `[-1, 1, 2, 3]` | - | - | - | - | - | - | 2 |
| 4 | 2 | `[-1, 1, 2]` | 3 | 6 | 2 | 4 | 1 | $6 \times 1 = 6$ | 6 |
| - | - | `[-1, 1]` | 2 | 5 | 1 | 4 | 2 | $5 \times 2 = \mathbf{10}$ | **10 (Max)** |
| - | - | `[-1, 1, 4]` | - | - | - | - | - | - | 10 |
| 5 | 3 | `[-1, 1, 4, 5]` | - | - | - | - | - | - | 10 |
| 6 | 0 (Sent) | `[-1, 1, 4]` | 5 | 3 | 4 | 6 | 1 | $3 \times 1 = 3$ | 10 |
| - | - | `[-1, 1]` | 4 | 2 | 1 | 6 | 4 | $2 \times 4 = 8$ | 10 |
| - | - | `[-1]` | 1 | 1 | -1 | 6 | 6 | $1 \times 6 = 6$ | 10 |

---

## 5. Algorithmic Correctness

**Soundness.** For any popped bar `mid`, all bars strictly between $\text{stack}[-1]$ and $i$ have heights $\ge \text{heights}[\text{mid}]$. Therefore, a rectangle of height $\text{heights}[\text{mid}]$ and width $i - \text{stack}[-1] - 1$ is guaranteed physically contained within the histogram bars.

**Completeness.** Every histogram bar is pushed onto the stack exactly once and popped exactly once. The maximal rectangle under every single bar is evaluated at the moment it is popped, ensuring no candidate rectangle can be missed.

---

## 6. Traps This Instance Exposes

- **Sentinel Simplification:** Without sentinel values ($-1$ at the bottom of the stack and $0$ appended at the end), one must write separate cleanup loops after the main pass and add conditional branches for empty stacks. The dual sentinels unify all edge cases into a single loop.
- **Equal Heights Handling:** If adjacent bars have equal heights (e.g. $[2, 2, 2]$), popping on $\le$ computes a suboptimal width for the earlier bars, but the final bar of the duplicate run evaluates the full correct width. The global maximum remains correct.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N = |\text{heights}|$. Each index is pushed onto the stack exactly once and popped at most once.
- **Auxiliary Space Complexity:** $O(N)$ to store the monotonic index stack of size at most $N + 2$.
