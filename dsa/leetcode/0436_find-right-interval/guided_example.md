# Guided Example: Find Right Interval

We trace the step-by-step start-time index pairing, ordered search-array construction, binary search lower-bound probing (`bisect_left`), and original index back-mapping on representative interval collections:

- **Input:** $intervals = [[3, 4], [2, 3], [1, 2]]$
- **Required output:** `[-1, 0, 1]`
  - Interval indices:
    - Index 0: $[3, 4]$
    - Index 1: $[2, 3]$
    - Index 2: $[1, 2]$
  - Step 1 (Extract and sort start times with original indices):
    - Original pairs: $[(3, 0), (2, 1), (1, 2)]$
    - Sorted array: $arr = [(1, 2), (2, 1), (3, 0)]$
  - Step 2 (Binary search for each interval's end time):
    - **Interval 0 ($[3, 4]$):** End time $= 4$.
      - Binary search on start times in $arr$ for target $\ge 4$:
      - Probing range $[1, 2, 3] \implies$ all values $< 4$. Insertion index $j = 3 \ge N$.
      - No right interval exists $\implies ans[0] = \mathbf{-1}$.
    - **Interval 1 ($[2, 3]$):** End time $= 3$.
      - Binary search in $arr$ for target $\ge 3$:
      - First element with $start \ge 3$ is $(3, 0)$ at index $j = 2$.
      - Original index is $0 \implies ans[1] = \mathbf{0}$.
    - **Interval 2 ($[1, 2]$):** End time $= 2$.
      - Binary search in $arr$ for target $\ge 2$:
      - First element with $start \ge 2$ is $(2, 1)$ at index $j = 1$.
      - Original index is $1 \implies ans[2] = \mathbf{1}$.
  - Result assembled: `[-1, 0, 1]`
- **Single Interval Instance:** $intervals = [[1, 2]] \implies$ End $2 >$ Start $1 \implies \mathbf{[-1]}$
- **Overlapping Intervals with Same Start:** All start times are unique in the problem constraints.

This instance demonstrates binary search on transformed coordinate index pairs, mathematically proves why finding the lower bound on start times guarantees the minimal right interval, and derives $O(N \log N)$ runtime and $O(N)$ space bounds.

---

## 1. Instance & Teaching Goal

Given a list of intervals $intervals = [[3, 4], [2, 3], [1, 2]]$:
The **right interval** for an interval $i$ is an interval $j$ such that $start_j \ge end_i$ and $start_j$ is minimized.
Return an array where each position $i$ contains the index of the right interval for $intervals[i]$, or $-1$ if no such interval exists.

```text
Intervals and Coordinates:
  Index 0: [3, 4]  (End = 4)
  Index 1: [2, 3]  (End = 3)
  Index 2: [1, 2]  (End = 2)

Search for Right Interval (start_j >= end_i):
  For [3, 4]: Need start >= 4. Available starts: {1, 2, 3} -> None exist (-1)
  For [2, 3]: Need start >= 3. Interval [3, 4] has start = 3 >= 3 -> Index 0
  For [1, 2]: Need start >= 2. Interval [2, 3] has start = 2 >= 2 -> Index 1

Output Array: [-1, 0, 1]
```

### The Search Reduction
A naive search compares every interval against all others in $O(N^2)$ time.
For each interval $i$:
We need to find an interval $j$ that minimizes $start_j$ subject to the condition:
$$
start_j \ge end_i
$$
If we sort all start times into an ascending array while preserving their original index tags:
The minimal valid $start_j$ corresponds precisely to the **first element** in the sorted start array with value $\ge end_i$.
This is the standard **lower bound** query (`bisect_left`), executed in $O(\log N)$ time.

---

## 2. Conceptual Foundation & Invariants

### 1. Indexed Start Array Invariant:
Construct an auxiliary array of 2-tuples containing start times paired with their original array indices:
$$
arr = [(\text{intervals}[i][0], \; i) \quad \text{for } i \in 0 \dots N-1]
$$
Sort $arr$ in ascending order by start time:
$$
arr[0][0] < arr[1][0] < \dots < arr[N-1][0]
$$
Because the problem guarantees all start times are unique, $arr$ is strictly increasing.

### 2. Binary Search Lower Bound Query:
For interval $i$ with end time $ed = \text{intervals}[i][1]$:
Perform binary search over $arr$ to find the smallest index $j$ such that:
$$
arr[j][0] \ge ed
$$
- If $j < N$: $arr[j][0]$ is the minimal starting time $\ge ed$. The original index is $arr[j][1]$.
- If $j == N$: All intervals start strictly before $ed$. No right interval exists; assign $-1$.

> **Optimality Invariant.** Because $arr$ is sorted strictly ascending, the first index $j$ satisfying $arr[j][0] \ge ed$ guarantees both feasibility ($start \ge ed$) and minimality ($start$ is as small as possible).

---

## 3. Step-by-Step Worked Execution

We trace $intervals = [[3, 4], [2, 3], [1, 2]]$ ($N = 3$):

---

### Step 1: Auxiliary Array Construction & Sorting
Pair each start coordinate with its original index:
- $i = 0: [3, 4] \implies (3, 0)$
- $i = 1: [2, 3] \implies (2, 1)$
- $i = 2: [1, 2] \implies (1, 2)$
Sort by start time:
$$
arr = [(1, 2), \; (2, 1), \; (3, 0)]
$$

---

### Step 2: Query for Interval 0 ($[3, 4]$)
- Target end time: $ed = 4$.
- Binary search on start coordinates $[1, 2, 3]$:
  - $L = 0, R = 3$.
  - Mid $M = 1: arr[1] = (2, 1)$. Value $2 < 4 \implies L = 2$.
  - Mid $M = 2: arr[2] = (3, 0)$. Value $3 < 4 \implies L = 3$.
  - Loop terminates at $j = 3$.
- Boundary test: $j = 3 == N \implies$ Out of bounds.
- Result:
  $$
  ans[0] = \mathbf{-1}
  $$

---

### Step 3: Query for Interval 1 ($[2, 3]$)
- Target end time: $ed = 3$.
- Binary search on start coordinates $[1, 2, 3]$:
  - $L = 0, R = 3$.
  - Mid $M = 1: arr[1] = (2, 1)$. Value $2 < 3 \implies L = 2$.
  - Mid $M = 2: arr[2] = (3, 0)$. Value $3 \ge 3 \implies R = 2$.
  - Loop terminates at $j = 2$.
- Boundary test: $j = 2 < N \implies$ Valid.
- Fetch original index: $arr[2][1] = 0$.
- Result:
  $$
  ans[1] = \mathbf{0}
  $$

---

### Step 4: Query for Interval 2 ($[1, 2]$)
- Target end time: $ed = 2$.
- Binary search on start coordinates $[1, 2, 3]$:
  - $L = 0, R = 3$.
  - Mid $M = 1: arr[1] = (2, 1)$. Value $2 \ge 2 \implies R = 1$.
  - Mid $M = 0: arr[0] = (1, 2)$. Value $1 < 2 \implies L = 1$.
  - Loop terminates at $j = 1$.
- Boundary test: $j = 1 < N \implies$ Valid.
- Fetch original index: $arr[1][1] = 1$.
- Result:
  $$
  ans[2] = \mathbf{1}
  $$

---

### Termination:
All intervals evaluated.
Output array: **`[-1, 0, 1]`**.

---

## 4. Complete Execution Trace

| Original Index $i$ | Interval $[st, ed]$ | Target $ed$ | Bisection Search Range | Bisection Result $j$ | Match in $arr$? | Original Index Found | Output $ans[i]$ |
|:---:|:---:|:---:|:---|:---:|:---:|:---:|:---:|
| **$0$** | $[3, 4]$ | $4$ | $[1, 2, 3]$ | $j = 3$ | No ($j \ge N$) | — | **$-1$** |
| **$1$** | $[2, 3]$ | $3$ | $[1, 2, 3]$ | $j = 2$ | Yes ($arr[2]=(3,0)$) | $0$ | **$0$** |
| **$2$** | $[1, 2]$ | $2$ | $[1, 2, 3]$ | $j = 1$ | Yes ($arr[1]=(2,1)$) | $1$ | **$1$** |

---

## 5. Boundary Cases & Failure Modes

- **Single Interval ($intervals = [[1, 4]]$):** Target $4 > 1$. Bisection returns $j = 1 == N \implies [-1]$.
- **Zero-Length Intervals ($[1, 1]$):** $start = 1 \ge end = 1$. An interval can be its own right interval $\implies ans[i] = i$.
- **All Negative Coordinates ($[[-5, -4], [-3, -2], [-1, 0]]$):** Sorted starts: $[-5, -3, -1]$. Queries:
  - For $[-5, -4]$: target $-4 \implies -3$ at index 1.
  - For $[-3, -2]$: target $-2 \implies -1$ at index 2.
  - For $[-1, 0]$: target $0 \implies$ out of bounds ($-1$).
- **No Right Interval for Any Element ($[[1, 10], [2, 10], [3, 10]]$):** All end at 10, all starts $< 10 \implies [-1, -1, -1]$.

---

## 6. Traps & Common Anti-Patterns

- **Losing Original Array Indices:** Sorting the intervals directly scrambles the order, preventing correct population of the answer array. Storing pairs `(start_time, original_index)` before sorting preserves origin metadata.
- **Using Upper Bound (`bisect_right`) Instead of Lower Bound (`bisect_left`):** If an interval's start equals the target end time (e.g. $start = 3, end = 3$), `bisect_right` steps *past* the exact match, missing the optimal minimum right interval. `bisect_left` finds the exact match.
- **Linear Scan on Unsorted Intervals ($O(N^2)$):** For $N = 2 \times 10^4$, quadratic search requires $4 \times 10^8$ comparisons, triggering Time Limit Exceeded. Sorting with binary search runs in $O(N \log N)$ time ($\approx 3 \times 10^5$ operations).

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Creating the indexed start array takes $O(N)$ time.
  - Sorting $N$ pairs takes $O(N \log N)$ time.
  - Executing binary search for each of the $N$ intervals takes $O(\log N)$ time, totaling $O(N \log N)$.
  - Total Time: $\mathcal{O}(N \log N)$. For $N = 2 \times 10^4$, execution completes in $\approx 10$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N)$ to store the indexed array of pairs and the output list.