# Guided Example: Minimum Number of Arrows to Burst Balloons

We trace the step-by-step end-coordinate greedy sorting ($x_{end}$), right-edge arrow stabbing point selection ($x = b$), overlapping interval absorption ($a \le last$), and new arrow triggering ($a > last$) on representative 1D balloon intervals:

- **Input:** $points = [[10, 16], [2, 8], [1, 6], [7, 12]]$
- **Required output:** `2`
  - Total balloons: $N = 4$
  - Step 1 (Sort ascending by end coordinate $b$):
    - Balloon 1: $[1, 6]$ (ends at $6$)
    - Balloon 2: $[2, 8]$ (ends at $8$)
    - Balloon 3: $[7, 12]$ (ends at $12$)
    - Balloon 4: $[10, 16]$ (ends at $16$)
  - Step 2 (Greedy arrow shooting):
    - Initial state: $ans = 0, \; last = -\infty$
    - **Inspect Balloon 1 ($[1, 6]$):**
      - Start $1 > last (-\infty) \implies$ Needs a new arrow!
      - Shoot Arrow 1 at right boundary: $x = 6$
      - $ans \leftarrow 1, \; last \leftarrow 6$
    - **Inspect Balloon 2 ($[2, 8]$):**
      - Start $2 \le last (6)$
      - Arrow 1 at $x = 6$ passes through $[2, 8]$ $\implies$ **Burst by Arrow 1!**
      - No new arrow needed. $last$ remains $6$.
    - **Inspect Balloon 3 ($[7, 12]$):**
      - Start $7 > last (6)$ $\implies$ Arrow 1 cannot reach Balloon 3!
      - Shoot Arrow 2 at right boundary: $x = 12$
      - $ans \leftarrow 2, \; last \leftarrow 12$
    - **Inspect Balloon 4 ($[10, 16]$):**
      - Start $10 \le last (12)$
      - Arrow 2 at $x = 12$ passes through $[10, 16]$ $\implies$ **Burst by Arrow 2!**
      - No new arrow needed.
  - Total arrows fired: $\mathbf{2}$
- **All Disjoint Intervals:** $points = [[1, 2], [3, 4], [5, 6]] \implies$ no overlaps $\implies \mathbf{3}$ arrows
- **All Overlapping at a Single Point:** $points = [[1, 10], [2, 9], [3, 8]] \implies$ single arrow at $x = 8$ bursts all $\implies \mathbf{1}$ arrow

This instance demonstrates interval stabbing and greedy scheduling, mathematically proves by exchange argument why shooting at the earliest ending balloon's right endpoint maximizes future coverage, and derives $O(N \log N)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an array $points = [[10, 16], [2, 8], [1, 6], [7, 12]]$:
Each balloon is an interval $[x_{start}, x_{end}]$.
An arrow shot vertically at $x$ bursts all balloons whose horizontal intervals contain $x$ ($x_{start} \le x \le x_{end}$).
Find the **minimum number of arrows** that must be shot to burst all balloons.

```text
Visualizing Balloon Intervals on the X-Axis:
  [1, 6]:    |-----------|
  [2, 8]:      |---------------|
             ^
             | Arrow 1 shot at x = 6 (Bursts [1, 6] and [2, 8])

  [7, 12]:                 |-----------|
  [10, 16]:                       |-------------|
                                       ^
                                       | Arrow 2 shot at x = 12 (Bursts [7, 12] and [10, 16])

Total Arrows Needed: 2
```

### The Greedy Stabbing Point Proof
- Every balloon must be burst by at least one arrow.
- Consider the balloon $B_{first}$ that ends earliest (smallest $x_{end}$).
- Any arrow that bursts $B_{first}$ must be positioned at some $x \le x_{end}$.
- To maximize the number of *other* balloons that this same arrow can burst, we should place $x$ as far to the right as possible!
- Setting $x = x_{end}$ is the optimal choice: moving the arrow any further to the left cannot burst any balloon that starts after $x_{end}$, and can only lose balloons that begin further right.
- Therefore, shooting greedily at $x = B_{first}.end$ is strictly optimal (Greedy Choice Property).

---

## 2. Conceptual Foundation & Invariants

### 1. End-Coordinate Sorting:
Sort all balloons ascending by their right endpoint $b$:
$$
b_1 \le b_2 \le \dots \le b_N
$$

### 2. The Frontier Stabbing Invariant:
Let $last$ be the x-coordinate of the most recently fired arrow:
- Initialize $last = -\infty, \; ans = 0$.
- For each balloon $[a, b]$ in sorted order:
  - **If $a \le last$:** The balloon spans over the arrow position $last$. Because $a \le last \le b$, the balloon is already burst. Skip without firing a new arrow.
  - **If $a > last$:** The balloon starts strictly after the previous arrow. A new arrow is required:
    $$
    ans \leftarrow ans + 1, \quad last \leftarrow b
    $$
    Position the new arrow at the rightmost boundary $b$ of this balloon.

> **Optimality Invariant.** At every step, $ans$ equals the minimum number of stabbing points required to cover all balloons processed so far, and the most recent arrow position $last$ is placed at the maximum allowable coordinate.

---

## 3. Step-by-Step Worked Execution

We trace $points = [[10, 16], [2, 8], [1, 6], [7, 12]]$ ($N = 4$):

---

### Step 1: Sort by Right Endpoint
Sort ascending by $b$:
$$
\text{Sorted Balloons: } [[1, 6], \; [2, 8], \; [7, 12], \; [10, 16]]
$$
Initialize:
$$
ans = 0, \quad last = -\infty
$$

---

### Step 2: Balloon 1 ($[1, 6]$)
- Start coordinate: $a = 1$.
- Test: $a > last \iff 1 > -\infty$ (**True**).
- Action: Shoot Arrow 1.
  $$
  ans \leftarrow 0 + 1 = 1, \quad last \leftarrow 6
  $$
- Arrow 1 is active at position $x = 6$.

---

### Step 3: Balloon 2 ($[2, 8]$)
- Start coordinate: $a = 2$.
- Test: $a > last \iff 2 > 6$ (**False**).
- Since $a = 2 \le last = 6 \le b = 8$, Balloon 2 is already pierced by Arrow 1.
- No new arrow needed. $last$ remains $6$.

---

### Step 4: Balloon 3 ($[7, 12]$)
- Start coordinate: $a = 7$.
- Test: $a > last \iff 7 > 6$ (**True**).
- Balloon 3 starts after Arrow 1. Shoot Arrow 2.
  $$
  ans \leftarrow 1 + 1 = 2, \quad last \leftarrow 12
  $$
- Arrow 2 is active at position $x = 12$.

---

### Step 5: Balloon 4 ($[10, 16]$)
- Start coordinate: $a = 10$.
- Test: $a > last \iff 10 > 12$ (**False**).
- Since $a = 10 \le last = 12 \le b = 16$, Balloon 4 is already pierced by Arrow 2.
- No new arrow needed.

---

### Termination:
All 4 balloons processed.
Total arrows fired: **`2`**.

---

## 4. Complete Execution Trace

| Balloon Inspected $[a, b]$ | Right End $b$ | Prior Arrow Position $last$ | Stabbing Test $a > last$ | Decision | Cumulative Arrows $ans$ | New Arrow Position $last$ |
|:---:|:---:|:---:|:---:|:---|:---:|:---:|
| **$[1, 6]$** | $6$ | $-\infty$ | $1 > -\infty$ (**True**) | **Shoot Arrow 1** | $1$ | $6$ |
| **$[2, 8]$** | $8$ | $6$ | $2 > 6$ (False) | Bursts in flight | $1$ | $6$ |
| **$[7, 12]$** | $12$ | $6$ | $7 > 6$ (**True**) | **Shoot Arrow 2** | $2$ | $12$ |
| **$[10, 16]$** | $16$ | $12$ | $10 > 12$ (False) | Bursts in flight | $2$ | $12$ |
| **Done** | — | — | — | — | **Result: $2$** | — |

---

## 5. Boundary Cases & Failure Modes

- **Single Balloon ($[[1, 2]]$):** Loop executes once $\implies ans = 1$.
- **Balloons Touching at Boundary ($[[1, 2], [2, 3]]$):** Arrow at $x = 2$ bursts both balloons because $2 \le 2$ (non-strict inequality). Condition $a > last \iff 2 > 2$ is False, correctly using $1$ arrow.
- **Negative Coordinates ($[[-10, -5], [-6, -2]]$):** Sorting handles negative coordinates without modification. Arrow at $-5$ bursts both.
- **Large Range Coordinates ($[-2^{31}, 2^{31}-1]$):** Using subtraction in comparator functions in C/C++ can overflow (`a[1] - b[1]`); using direct comparison (`<`) avoids 32-bit overflow bugs.

---

## 6. Traps & Common Anti-Patterns

- **Comparator Integer Overflow:** Writing custom comparators as `(a, b) -> a[1] - b[1]` causes signed 32-bit integer underflow when $b[1] = 2^{31}-1$ and $a[1] = -2^{31}$. Always use direct `<` comparison operators.
- **Sorting by Start Coordinate:** Sorting by start coordinate can place a long balloon $[0, 100]$ before $[1, 2]$. Shooting at $100$ misses $[1, 2]$, whereas shooting at $2$ covers both. Sorting by end coordinate is strictly required.
- **Strict vs Non-Strict Boundary:** Condition is $a > last$. Using $a \ge last$ shoots a redundant arrow when intervals share an endpoint ($[1, 2]$ and $[2, 3]$).

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Sorting $N$ interval pairs takes $O(N \log N)$ time.
  - The single-pass greedy scan inspects each balloon once in $O(1)$ time.
  - Total Time: $\mathcal{O}(N \log N)$. For $N = 10^5$, finishes in under 25 ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ extra space beyond language-level sorting storage.
