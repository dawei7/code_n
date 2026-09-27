# Guided Example: Remove Boxes

We trace the step-by-step 3D interval dynamic programming formulation ($dfs(i, j, k)$), trailing identical box run-length compression ($j \leftarrow j - 1, k \leftarrow k + 1$), immediate harvest trade-off ($dfs(i, j-1, 0) + (k+1)^2$), delayed bridge merge exploration across intermediate intervals ($dfs(h+1, j-1, 0) + dfs(i, h, k+1)$), and global maximum score optimization on representative box sequences:

- **Input:** $boxes = [1, 3, 2, 2, 2, 3, 4, 3, 1]$
- **Required output:** `23`
  - Scoring mechanism: Removing $m$ contiguous boxes of the same color awards $m^2$ points.
  - Strategic dilemma:
    - Removing boxes immediately scores smaller squared points ($m_1^2 + m_2^2$).
    - Eliminating intermediate obstacle boxes allows distant boxes of the same color to merge together, scoring a much larger combined square ($(m_1 + m_2)^2 > m_1^2 + m_2^2$).
- **The 3D State Definition ($dfs(i, j, k)$):**
  - Let $dfs(i, j, k)$ be the maximum points obtainable from subsegment $boxes[i \dots j]$ given that there are already **$k$ boxes** to the right of index $j$ that share the **exact same color** as $boxes[j]$.
- **Execution trace on $[1, 3, 2, 2, 2, 3, 4, 3, 1]$ ($n = 9$):**
  - Initial call: $dfs(0, 8, 0)$
    - $boxes[8] = 1$. Currently $k = 0$ trailing 1s.
  - **Branch Choice Analysis:**
    - **Option A (Harvest Rightmost 1 Immediately):**
      - Score: $(0 + 1)^2 = 1$.
      - Remaining subsegment: $boxes[0 \dots 7] = [1, 3, 2, 2, 2, 3, 4, 3]$.
      - Does not allow the two `'1'`s at index 0 and index 8 to merge!
    - **Option B (Bridge Merge with Earlier Color 1 at Index $h = 0$):**
      - Intermediate obstacle segment: $boxes[1 \dots 7] = [3, 2, 2, 2, 3, 4, 3]$.
      - First, solve the obstacle segment independently:
        $$
        \text{Obstacle points} = dfs(1, 7, 0)
        $$
      - Once the obstacle is cleared, $boxes[8] = 1$ merges with $boxes[0] = 1$, giving index $0$ a trailing count of $k = 0 + 1 = 1$:
        $$
        \text{Merged points} = dfs(0, 0, 1) = (1 + 1)^2 = \mathbf{4}
        $$
  - **Evaluating the Obstacle Segment $boxes[1 \dots 7] = [3, 2, 2, 2, 3, 4, 3]$:**
    - Rightmost box is $boxes[7] = 3$.
    - Earlier instances of color 3 exist at index $h = 5$ and index $h = 1$.
    - **Sub-Step 1: Clear the internal three 2s ($boxes[2 \dots 4] = [2, 2, 2]$):**
      - Three identical 2s removed together:
        $$
        3 \times 3 = \mathbf{9} \text{ points}
      $$
      - Segment collapses to: $[3, 3, 4, 3]$.
    - **Sub-Step 2: Clear the isolated 4 ($boxes[6] = 4$):**
      - Single 4 removed:
        $$
        1 \times 1 = \mathbf{1} \text{ point}
      $$
      - Segment collapses to: $[3, 3, 3]$.
    - **Sub-Step 3: Harvest the three merged 3s:**
      - Three 3s removed together:
        $$
        3 \times 3 = \mathbf{9} \text{ points}
      $$
    - Total points from obstacle segment:
      $$
      9 + 1 + 9 = \mathbf{19}
      $$
  - **Sub-Step 4: Final Harvest of Merged 1s:**
    - With the middle completely cleared, the original $boxes[0] = 1$ and $boxes[8] = 1$ are now adjacent:
      $$
      [1, 1] \to 2 \times 2 = \mathbf{4} \text{ points}
      $$
  - **Global Point Summation:**
    $$
    \text{Total Score} = 19 + 4 = \mathbf{23}
    $$
- **Uniform Segment Instance ($boxes = [1, 1, 1]$):**
  - Run-length compression contracts $j$ to $0$ with $k = 2 \implies (2 + 1)^2 = \mathbf{9}$.
- **Strictly Alternating Colors ($boxes = [1, 2, 1, 2]$):**
  - Merge the two 1s ($2^2 = 4$) and two 2s ($2^2 = 4$) $\implies 4 + 4 = \mathbf{8}$.

This instance demonstrates higher-dimensional interval dynamic programming with carrying states, mathematically proves why tracking trailing identical counts decouples non-contiguous subproblem interactions, and derives $O(N^4)$ runtime and $O(N^3)$ space bounds.

---

## 1. Instance & Teaching Goal

Given an array of integers $boxes$ where each integer denotes a color:
In each round, you choose a contiguous block of $m$ boxes of the same color, remove them, and score $m^2$ points.
The remaining boxes shift together to fill the vacated space.
Find the **maximum points** you can obtain.

```text
Initial Array: [ 1,  3,  2,  2,  2,  3,  4,  3,  1 ]

Sequence of Moves:
  1. Remove three '2's:  [2, 2, 2] -> 3^2 = 9 points
     Remaining: [ 1,  3,  3,  4,  3,  1 ]

  2. Remove single '4':  [4]       -> 1^2 = 1 point
     Remaining: [ 1,  3,  3,  3,  1 ]

  3. Remove three '3's:  [3, 3, 3] -> 3^2 = 9 points
     Remaining: [ 1,  1 ]

  4. Remove two '1's:    [1, 1]    -> 2^2 = 4 points
     Remaining: []

Total Score = 9 + 1 + 9 + 4 = 23 points
```

### Why Standard 2D Interval DP $dp[i][j]$ Fails
- In standard interval DP (e.g. Matrix Chain Multiplication or Burst Balloons), subproblems are strictly independent: removing a subproblem $boxes[i \dots j]$ does not affect the rest of the array.
- In Remove Boxes, removing an intermediate segment allows boxes on the left and right to **collide and merge into a larger contiguous group**.
- Because the score is quadratic ($m^2$), merging two groups of sizes $a$ and $b$ yields $(a + b)^2 = a^2 + b^2 + 2ab > a^2 + b^2$.
- We must add a 3rd dimension $k$: **the count of trailing boxes attached to the right of $j$ with color $boxes[j]$**.

---

## 2. Conceptual Foundation & Invariants

### 1. The State $dfs(i, j, k)$:
- $i, j$: The current subsegment under consideration ($boxes[i \dots j]$).
- $k$: The number of boxes to the right of $j$ that have already been cleared of obstacles and have color equal to $boxes[j]$.

### 2. Run-Length Pre-Aggregation:
If the boxes immediately preceding $j$ share its color:
$$
\text{While } i < j \text{ and } boxes[j] == boxes[j - 1]: \quad j \leftarrow j - 1, \; k \leftarrow k + 1
$$
This groups contiguous identical blocks immediately, pruning duplicate DP states.

### 3. State Transition Recurrence:
1. **Strategy 1 (Harvest Now):**
   Remove $boxes[j]$ and its $k$ attached twins immediately, scoring $(k + 1)^2$ points:
   $$
   ans_1 = dfs(i, j - 1, 0) + (k + 1)^2
   $$
2. **Strategy 2 (Bridge Merge with Previous $boxes[h] == boxes[j]$):**
   For any index $h \in [i, j - 1]$ where $boxes[h] == boxes[j]$:
   - Clear the obstacle segment $boxes[h+1 \dots j-1]$ to expose $boxes[h]$: $dfs(h+1, j-1, 0)$.
   - Combine $boxes[h]$ with $boxes[j]$ and the $k$ trailing boxes, so $boxes[h]$ now has $k + 1$ trailing twins: $dfs(i, h, k+1)$.
   $$
   ans_2 = \max_{h} (dfs(h + 1, j - 1, 0) + dfs(i, h, k + 1))
   $$
3. Overall State:
   $$
   dfs(i, j, k) = \max(ans_1, \; ans_2)
   $$

> **Bridge Merge Invariant.** Passing $k+1$ into $dfs(i, h, k+1)$ defers the evaluation of the merged color block until all intermediate obstacles have been optimally removed.

---

## 3. Step-by-Step Worked Execution

We trace the key decisions on $[1, 3, 2, 2, 2, 3, 4, 3, 1]$:

---

### Step 1: Initial Outer Call
- $dfs(0, 8, 0)$ on $[1, 3, 2, 2, 2, 3, 4, 3, 1]$.
- $boxes[8] = 1, \; k = 0$.
- Candidate earlier match: $h = 0$ ($boxes[0] = 1$).
- Bridge transition:
  $$
  \text{Score} = dfs(1, 7, 0) + dfs(0, 0, 0 + 1)
  $$

---

### Step 2: Solve Suffix $dfs(0, 0, 1)$
- Subsegment: $boxes[0 \dots 0] = [1]$.
- Trailing matching boxes: $k = 1$.
- Total matching boxes: $k + 1 = 2$.
- Points: $(1 + 1)^2 = \mathbf{4}$.

---

### Step 3: Solve Middle Segment $dfs(1, 7, 0)$ on $[3, 2, 2, 2, 3, 4, 3]$
- $boxes[7] = 3, \; k = 0$.
- Matches at $h = 5$ ($boxes[5] = 3$) and $h = 1$ ($boxes[1] = 3$).
- **Isolate $boxes[6] = 4$:**
  - $dfs(6, 6, 0) = (0 + 1)^2 = \mathbf{1}$.
- **Isolate $boxes[2 \dots 4] = [2, 2, 2]$:**
  - Compressed to $j = 2, k = 2$:
  - $dfs(2, 2, 2) = (2 + 1)^2 = \mathbf{9}$.
- **Combine three 3s:**
  - $boxes[1], boxes[5], boxes[7]$ merge into group of size 3:
  - $(2 + 1)^2 = \mathbf{9}$.
- Total middle score:
  $$
  1 + 9 + 9 = \mathbf{19}
  $$

---

### Step 4: Final Summation
$$
ans = 19 + 4 = \mathbf{23}
$$

---

## 4. Complete Execution Trace

| Subproblem Range $[i, j]$ | Trailing Count $k$ | Action Chosen | Segment Removed | Points Scored | Next State |
|:---:|:---:|:---:|:---:|:---:|:---:|
| $[2, 4]$ | $0 \to 2$ | Run-length collapse | Three `'2'`s: $[2, 2, 2]$ | $3^2 = 9$ | Collapsed |
| $[6, 6]$ | $0$ | Direct harvest | Single `'4'`: $[4]$ | $1^2 = 1$ | Collapsed |
| $[1, 7]$ | $0$ | Bridge merge at $h=5, 1$ | Three `'3'`s: $[3, 3, 3]$ | $3^2 = 9$ | Collapsed |
| $[0, 8]$ | $0$ | Bridge merge at $h=0$ | Two `'1'`s: $[1, 1]$ | $2^2 = 4$ | Collapsed |
| **Total** | — | — | — | — | **$9 + 1 + 9 + 4 = \mathbf{23}$** |

---

## 5. Boundary Cases & Failure Modes

- **$i > j$:** Empty range $\implies 0$ points.
- **Single Element ($[5]$):** $k = 0 \implies (0 + 1)^2 = \mathbf{1}$.
- **All Elements Same Color ($[7, 7, 7, 7]$):** Compressed to $k = 3 \implies (3 + 1)^2 = \mathbf{16}$.
- **All Elements Distinct ($[1, 2, 3, 4]$):** No bridge matches possible; each box is removed individually $\implies 1 + 1 + 1 + 1 = \mathbf{4}$.

---

## 6. Traps & Common Anti-Patterns

- **Greedy Strategy (Always remove largest group first):** For `[1, 3, 2, 2, 2, 3, 4, 3, 1]`, greedily removing the three 2s happens to work, but for `[1, 2, 1, 2, 1]` removing the two 2s yields $(1+1+1)^2 + 2^2 = 9 + 4 = 13$, whereas greedily clearing 1s first gives less. DP explores both choices optimally.
- **Omitting State Memoization:** The number of states is $O(N^3)$. Without `@cache` or a 3D memo table, the recursive tree explodes into exponential $O(2^N)$ calls.
- **Skipping Run-Length Compression:** Evaluating $j \leftarrow j - 1$ sequentially without compressing consecutive identical elements causes significant memoization table bloat and unnecessary subproblem evaluations.

---

## 7. Complexity Derivation

- **Time Complexity:**
  - Number of states $(i, j, k)$: $i \in [0, N-1], \; j \in [i, N-1], \; k \in [0, N-1] \implies \mathcal{O}(N^3)$ states.
  - Inside each state, the loop over $h$ runs at most $j - i \le N$ times.
  - Total Time: $\mathcal{O}(N^4)$. For $N = 100$, highly pruned memoization visits only a small fraction of legal states, completing in $< 150$ ms.
- **Auxiliary Space Complexity:**
  - $\mathcal{O}(N^3)$ space to store memoized results in the cache table.