# Guided Example: Maximum Distance in Arrays

We trace the step-by-step distinct-array element selection constraint ($i \ne j$), monotonic sorted endpoint extraction ($arr[0]$ and $arr[-1]$), online prefix extrema maintenance ($mi, mx$), dynamic candidate distance maximization ($\max(|arr[0] - mx|, |arr[-1] - mi|)$), and single-pass optimal gap evaluation on representative sorted array collections:

- **Input:** $arrays = [[1, 2, 3], \; [4, 5], \; [1, 2, 3]]$
- **Required output:** `4`
  - Problem specifications:
    - We are given $m$ arrays ($m \ge 2$), each sorted in ascending order.
    - We must choose one integer $a$ from array $i$ and one integer $b$ from array $j$ such that **$i \ne j$** (they must come from different arrays).
    - Maximize the absolute distance $|a - b|$.
- **Running Prefix Extrema & Distinct-Array Enforcement:**
  - Because each individual array is sorted in ascending order, the smallest element of an array is its first element $arr[0]$, and the largest is its last element $arr[-1]$.
  - The maximum distance between two arrays must occur between the **minimum of one array and the maximum of the other array**.
  - **The "Different Arrays" Trap:**
    - If we simply take the global minimum and global maximum across all arrays, they might both belong to the exact same array!
  - **Online Prefix Tracker Solution:**
    - Process arrays sequentially $i = 0, 1, \dots, m - 1$.
    - Maintain the minimum value $mi$ and maximum value $mx$ observed **strictly within the prefix of preceding arrays $0 \dots i - 1$**:
      $$
      mi = \min_{k < i} arrays[k][0], \quad mx = \max_{k < i} arrays[k][-1]
      $$
    - When inspecting array $i$:
      - Pair its smallest element $arr[0]$ with the largest preceding element $mx$:
        $$
        \Delta_1 = |arr[0] - mx|
        $$
      - Pair its largest element $arr[-1]$ with the smallest preceding element $mi$:
        $$
        \Delta_2 = |arr[-1] - mi|
        $$
      - Update global maximum distance:
        $$
        ans \leftarrow \max(ans, \; \Delta_1, \; \Delta_2)
        $$
      - Only **after** computing distances do we include array $i$'s endpoints into $mi$ and $mx$!
      - This ordering strictly guarantees that $arr[0]$ and $arr[-1]$ are never paired with an element from array $i$ itself.
- **Step-by-Step Worked Execution Trace on $[[1, 2, 3], [4, 5], [1, 2, 3]]$:**
  - **Step 1: Initialize with Array 0 ($[1, 2, 3]$):**
    - $mi = arrays[0][0] = \mathbf{1}$
    - $mx = arrays[0][-1] = \mathbf{3}$
    - $ans = 0$
  - **Step 2: Process Array 1 ($[4, 5]$):**
    - Current endpoints: $first = 4, \; last = 5$.
    - Candidate distances against preceding prefix:
      $$
      \Delta_1 = |first - mx| = |4 - 3| = \mathbf{1}
      $$
      $$
      \Delta_2 = |last - mi| = |5 - 1| = \mathbf{4}
      $$
    - Update best distance:
      $$
      ans = \max(0, 1, 4) = \mathbf{4}
      $$
    - Absorb Array 1 into running extrema:
      $$
      mi \leftarrow \min(1, 4) = \mathbf{1}
      $$
      $$
      mx \leftarrow \max(3, 5) = \mathbf{5}
      $$
    - Extrema for prefix $[0 \dots 1]$: $mi = 1, \; mx = 5$.
  - **Step 3: Process Array 2 ($[1, 2, 3]$):**
    - Current endpoints: $first = 1, \; last = 3$.
    - Candidate distances against preceding prefix:
      $$
      \Delta_1 = |first - mx| = |1 - 5| = \mathbf{4}
      $$
      $$
      \Delta_2 = |last - mi| = |3 - 1| = \mathbf{2}
      $$
    - Update best distance:
      $$
      ans = \max(4, 4, 2) = \mathbf{4}
      $$
    - Absorb Array 2 into running extrema:
      $$
      mi \leftarrow \min(1, 1) = \mathbf{1}
      $$
      $$
      mx \leftarrow \max(5, 3) = \mathbf{5}
      $$
  - **Step 4: Return Result:**
    $$
    ans = \mathbf{4}
    $$
    - Achieved by pairing $1$ from Array 0 with $5$ from Array 1 ($|5 - 1| = 4$).
- **Single Dominant Array Instance ($arrays = [[1, 100], [4, 5]]$):**
  - Array 0 gives $mi = 1, mx = 100$.
  - Array 1 has $first = 4, last = 5$.
  - Distances: $|4 - 100| = 96$, $|5 - 1| = 4$.
  - Global best $= 96$.
  - Notice that $|100 - 1| = 99$ is disallowed because both come from Array 0! The online tracker correctly returns $96$.
- **Identical Singleton Arrays ($[[1], [1]]$):**
  - $mi = 1, mx = 1$.
  - Array 1: $|1 - 1| = 0 \implies ans = \mathbf{0}$.

This instance demonstrates asymmetric online stream processing for constrained distinct-entity optimization, mathematically proves why pre-update distance comparisons decouple intra-group and inter-group extrema, and derives $O(M)$ runtime and $O(1)$ space bounds.

---

## 1. Instance & Teaching Goal

Given $m$ sorted arrays:
Find the **maximum distance** $|a - b|$ between two elements chosen from **two different arrays**.

```text
Arrays:
  0: [ 1, 2, 3 ]
  1: [ 4, 5 ]
  2: [ 1, 2, 3 ]

Pairs:
  min from array 0 (1) and max from array 1 (5) -> |5 - 1| = 4  <-- Maximum!
  min from array 2 (1) and max from array 1 (5) -> |5 - 1| = 4

Result: 4
```

### The Invariant of Online Decoupling
- In each array $k$, the candidate elements for the global maximum distance are exclusively the minimum $arr[0]$ and the maximum $arr[-1]$.
- If we update our tracking variables $mi$ and $mx$ **after** calculating the distance with the current array, we are mathematically guaranteed that the distance was formed with an element from an earlier array ($j < i$).
- Scanning the array list once captures all pairs $(j, i)$ with $j < i$.

---

## 2. Conceptual Foundation & Invariants

### 1. The Online Transition:
Initialize:
$$
mi = arrays[0][0], \quad mx = arrays[0][-1], \quad ans = 0
$$
For each $arr \in arrays[1 \dots m - 1]$:
$$
ans \leftarrow \max(ans, \; |arr[0] - mx|, \; |arr[-1] - mi|)
$$
$$
mi \leftarrow \min(mi, arr[0]), \quad mx \leftarrow \max(mx, arr[-1])
$$

> **Distinct Support Invariant.** Evaluating distances against the prefix extrema prior to incorporating the current array's boundaries ensures that the two values in $|u - v|$ belong to disjoint arrays.

---

## 3. Step-by-Step Worked Execution

We trace $arrays = [[1, 2, 3], [4, 5], [1, 2, 3]]$:

---

### Step 1: Initialize Prefix
- $mi = 1, mx = 3$.
- $ans = 0$.

---

### Step 2: Array 1 $[4, 5]$
- $\Delta_1 = |4 - 3| = 1$.
- $\Delta_2 = |5 - 1| = 4$.
- $ans = \max(0, 1, 4) = 4$.
- Update: $mi = \min(1, 4) = 1, \; mx = \max(3, 5) = 5$.

---

### Step 3: Array 2 $[1, 2, 3]$
- $\Delta_1 = |1 - 5| = 4$.
- $\Delta_2 = |3 - 1| = 2$.
- $ans = \max(4, 4, 2) = 4$.
- Update: $mi = 1, mx = 5$.

---

### Step 4: Final Output
$$
ans = \mathbf{4}
$$

---

## 4. Complete Execution Trace

| Array Index $i$ | Endpoints $[first, last]$ | $|first - mx|$ | $|last - mi|$ | Candidate Max | Running $ans$ | Prefix $mi$ After | Prefix $mx$ After |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| $0$ | $[1, 3]$ | (Init) | (Init) | — | $0$ | $1$ | $3$ |
| $1$ | $[4, 5]$ | $|4 - 3| = 1$ | $|5 - 1| = 4$ | $4$ | **$4$** | $1$ | $5$ |
| $2$ | $[1, 3]$ | $|1 - 5| = 4$ | $|3 - 1| = 2$ | $4$ | **`4`** | $1$ | $5$ |
| **Final** | — | — | — | — | **`4`** | — | — |

---

## 5. Boundary Cases & Failure Modes

- **Exactly Two Arrays ($m = 2$):** Loop runs once and evaluates the only possible pair combinations.
- **Negative Numbers ($[[-10, -5], [-2, 0]]$):** Absolute differences $|-10 - 0| = 10$ compute accurately.
- **Single-Element Arrays ($[[1], [1]]$):** First and last are identical $\implies$ distance is 0.
- **Identical Arrays ($[[1, 5], [1, 5]]$):** $|1 - 5| = 4$ across the two arrays.

---

## 6. Traps & Common Anti-Patterns

- **Comparing All Elements in an Array:** Because arrays are already sorted, interior elements ($arr[1 \dots -2]$) can never produce a larger distance than the endpoints. Checking internal elements wastes time.
- **Pairing Elements From the Same Array:** Finding the global min and max without index tracking fails on inputs like `[[1, 100], [2, 3]]` where 1 and 100 come from array 0.
- **Sorting All Endpoints ($O(M \log M)$):** Sorting endpoint tuples is valid, but the single-pass online scan is simpler, cleaner, and runs in strictly linear $O(M)$ time.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - We inspect only the first and last element of each of the $M$ arrays.
  - Exactly one comparison pass through $M - 1$ arrays: $\mathcal{O}(M)$ time.
  - Completes in $< 2$ ms for $M = 10^5$.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(1)$ auxiliary space (only a few integer scalar variables).
