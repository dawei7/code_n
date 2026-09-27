# Guided Example: Find K Closest Elements

We trace the step-by-step contiguous window invariant on sorted arrays, binary search over the window left boundary ($m \in [0, n - k]$), endpoint distance comparison ($|arr[m] - x|$ vs $|arr[m+k] - x|$), tie-breaking preference ($a < b$), and optimal $k$-element subarray extraction on representative integer arrays:

- **Input:** $arr = [1, 2, 3, 4, 5], \quad k = 4, \quad x = 3$
- **Required output:** `[1, 2, 3, 4]`
  - Closeness ranking criteria:
    - Number $a$ is closer to $x$ than $b$ if:
      1. $|a - x| < |b - x|$ (Strictly smaller distance).
      2. If $|a - x| == |b - x|$, then $a$ is closer if $a < b$ (Smaller numerical value breaks ties).
    - Result must contain exactly $k$ elements, sorted in ascending order.
- **Contiguous Window & Left-Boundary Binary Search Invariant:**
  - **The Contiguity Property:**
    - Since input array $arr$ is already **sorted in ascending order**, any set of $k$ closest elements must form a **contiguous subarray** of length $k$:
      $$
      arr[l \dots l + k - 1]
      $$
    - The search space is therefore reduced to finding the single optimal **starting index** $l \in [0, \; n - k]$.
  - **$\mathcal{O}(\log(n - k))$ Boundary Bisection:**
    - Consider a candidate window starting at index $m$, spanning $arr[m \dots m + k - 1]$.
    - We test whether shifting the window one position rightward (dropping $arr[m]$ and adding $arr[m + k]$) improves the closeness to $x$:
      - Distance from target $x$ to the leaving left endpoint:
        $$
        d_{left} = x - arr[m]
        $$
      - Distance from target $x$ to the entering right endpoint:
        $$
        d_{right} = arr[m + k] - x
        $$
      - **Decision Logic:**
        - If $x - arr[m] > arr[m + k] - x$:
          - The right element $arr[m + k]$ is strictly closer to $x$ than $arr[m]$!
          - The optimal window must shift rightward:
            $$
            l \leftarrow m + 1
            $$
        - If $x - arr[m] \le arr[m + k] - x$:
          - The left element $arr[m]$ is either closer or tied with a smaller value ($arr[m] < arr[m+k]$).
          - By the tie-breaking rule, we prefer the smaller value on the left!
          - The window cannot start further right:
            $$
            r \leftarrow m
            $$
- **Step-by-Step Worked Execution Trace on $[1, 2, 3, 4, 5], k = 4, x = 3$:**
  - Array length: $n = 5$. Window size: $k = 4$.
  - Range for left starting index $l$:
    $$
    [0, \; n - k] = [0, \; 5 - 4] = [0, \; 1]
    $$
  - **Bisection Step 1 ($l = 0, \; r = 1$):**
    - Midpoint:
      $$
      m = \lfloor (0 + 1) / 2 \rfloor = \mathbf{0}
      $$
    - Candidate window starts at index $0$, spanning $arr[0 \dots 3] = [1, 2, 3, 4]$.
    - Compare left boundary element $arr[m] = arr[0] = 1$ against the element immediately outside to the right $arr[m + k] = arr[4] = 5$:
      - Distance to left candidate $arr[0]$:
        $$
        d_{left} = x - arr[0] = 3 - 1 = \mathbf{2}
        $$
      - Distance to right candidate $arr[4]$:
        $$
        d_{right} = arr[4] - x = 5 - 3 = \mathbf{2}
        $$
    - Evaluate comparison:
      $$
      d_{left} > d_{right} \iff 2 > 2 \implies \mathbf{False!}
      $$
    - **Tie-Breaking Analysis:**
      - Both $1$ and $5$ are at distance $2$ from target $x = 3$.
      - But $1 < 5$!
      - The problem's tie-breaking rule explicitly mandates: *if distances are equal, pick the smaller number*.
      - Therefore, $arr[0] = 1$ strictly defeats $arr[4] = 5$!
      - We must keep $arr[0]$ in our window.
    - Update search range:
      $$
      r \leftarrow m = \mathbf{0}
      $$
  - **Bisection Termination:**
    - Now $l = 0$ and $r = 0$ ($l == r$).
    - Search terminates with optimal left index $l^* = \mathbf{0}$.
  - **Step 4: Slice Solution Window:**
    - Extract $k = 4$ elements starting at index $0$:
      $$
      arr[0 \dots 3] = [\mathbf{1}, \; \mathbf{2}, \; \mathbf{3}, \; \mathbf{4}]
      $$
    - Distances from $x = 3$:
      - $|1 - 3| = 2$
      - $|2 - 3| = 1$
      - $|3 - 3| = 0$
      - $|4 - 3| = 1$
    - Top 4 closest elements confirmed.
- **Target Below Array ($arr = [1, 2, 3, 4, 5], k = 4, x = -1$):**
  - All elements are $\ge 1 > -1$.
  - Leftmost elements are closest $\implies$ returns `[1, 2, 3, 4]`.
- **Target Above Array ($x = 10$):**
  - $x - arr[0] = 10 - 1 = 9 \gg arr[4] - x = 5 - 10 = -5$.
  - Window shifts right to the maximum extent $\implies$ returns `[2, 3, 4, 5]`.

This instance demonstrates unimodal distance minimization over sorted linear orders and direct binary search on interval boundaries, mathematically proves why contiguous window monotonicity preserves global metric optimality, and derives $O(\log(N - k) + k)$ runtime and $O(1)$ auxiliary space bounds.

---

## 1. Instance & Teaching Goal

Given a sorted array $arr$, window size $k$, and target $x$:
Find the **$k$ closest integers** to $x$, sorted ascending.
Closeness: $|a - x| < |b - x|$, tie broken by $a < b$.

```text
arr = [ 1, 2, 3, 4, 5 ], k = 4, x = 3

Candidate Windows of length 4:
  Window 0 (starts at 0): [ 1, 2, 3, 4 ]
    Distances to 3:        |1-3|=2, |2-3|=1, |3-3|=0, |4-3|=1

  Window 1 (starts at 1): [ 2, 3, 4, 5 ]
    Distances to 3:        |2-3|=1, |3-3|=0, |4-3|=1, |5-3|=2

Compare competing endpoints 1 and 5:
  |1 - 3| = 2
  |5 - 3| = 2
  Tied! Since 1 < 5, Window 0 WINS.

Result: [ 1, 2, 3, 4 ]
```

### The Invariant of the Competing Endpoints
- Since $arr$ is sorted, moving a window of size $k$ from $m$ to $m + 1$ always drops $arr[m]$ and adds $arr[m + k]$.
- Thus, the decision between window $m$ and window $m + 1$ depends **solely** on comparing $arr[m]$ and $arr[m + k]$.
- If $x - arr[m] > arr[m + k] - x$, the right element is strictly closer $\implies$ advance right.

---

## 2. Conceptual Foundation & Invariants

### 1. The Boundary Bisection Predicate:
Initialize $l = 0, r = n - k$.
While $l < r$:
$$
m = \lfloor (l + r) / 2 \rfloor
$$
$$
(x - arr[m]) > (arr[m + k] - x) \implies l \leftarrow m + 1
$$
$$
(x - arr[m]) \le (arr[m + k] - x) \implies r \leftarrow m
$$
Return $arr[l \dots l + k - 1]$.

> **Convex Distance Subarray Invariant.** The function $f(i) = \sum_{j=i}^{i+k-1} |arr[j] - x|$ is discretely convex with respect to the window origin $i$, ensuring that the pairwise comparison $x - arr[m] > arr[m+k] - x$ gives a strictly monotonic gradient sign for binary search.

---

## 3. Step-by-Step Worked Execution

We trace $arr = [1, 2, 3, 4, 5], k = 4, x = 3$:

---

### Step 1: Initialize Search Bounds
- $l = 0, r = 5 - 4 = 1$.

---

### Step 2: Test Midpoint $m = 0$
- Left element: $arr[0] = 1$.
- Right rival element: $arr[0 + 4] = arr[4] = 5$.
- Distance left: $3 - 1 = 2$.
- Distance right: $5 - 3 = 2$.
- Condition $2 > 2$ is **False**.
- By tie-breaker, prefer left endpoint $\implies r \leftarrow 0$.

---

### Step 3: Halt & Extract
- $l = 0, r = 0 \implies l = 0$.
- Slice: $arr[0 \dots 3] = \mathbf{[1, 2, 3, 4]}$.

---

## 4. Complete Execution Trace

| Search Step | Interval $[l, r]$ | Midpoint $m$ | Left Element $arr[m]$ | Rival Element $arr[m+k]$ | Distance Comparison | Search Next |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $1$ | $[0, 1]$ | $0$ | $1$ | $5$ | $3 - 1 \le 5 - 3$ ($2 \le 2$) | $r \leftarrow 0$ |
| **Converged** | $[0, 0]$ | $0$ | — | — | Optimal $l^* = 0$ | Extract $arr[0 \dots 3]$ |
| **Output** | — | — | — | — | — | **`[1, 2, 3, 4]`** |

---

## 5. Boundary Cases & Failure Modes

- **$k = n$:** Only 1 window exists $\implies$ returns full array immediately.
- **$x$ Smaller Than All Elements ($x \le arr[0]$):** Returns first $k$ elements.
- **$x$ Larger Than All Elements ($x \ge arr[-1]$):** Returns last $k$ elements.
- **All Elements Equal:** Ties resolve to the leftmost slice of length $k$.

---

## 6. Traps & Common Anti-Patterns

- **Full Array Re-Sorting ($O(N \log N)$):** Sorting all $N$ elements by $|v - x|$ ignores that the input is already sorted, taking $O(N \log N)$ instead of $O(\log N)$.
- **Incorrect Sign in Rival Difference:** Remember that $arr[m+k] \ge x$ when $x$ is inside the window, so write $arr[m+k] - x$. Comparing $x - arr[m] > arr[m+k] - x$ correctly tests without absolute values.
- **Two-Pointer Linear Shrinking ($O(N)$):** Shrinking from both ends takes $O(N - k)$ steps; binary search finds the exact window in $O(\log(N - k))$ steps.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Binary search runs in $\mathcal{O}(\log(N - k))$ iterations.
  - Slicing the $k$ elements to construct output: $\mathcal{O}(k)$.
  - Total Time: strictly optimal $\mathcal{O}(\log(N - k) + k)$. Completes in $< 0.1$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ auxiliary space (excluding the output list).
