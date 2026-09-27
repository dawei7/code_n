# Guided Example: Android Unlock Patterns

We trace the step-by-step backtracking search with obstacle jumping logic (`cross[i][j]`), 4-fold rotational/reflection symmetry grouping (Corners, Edges, Center), dynamic length thresholding ($m \le cnt \le n$), and pattern counting on representative Android grid instances:

- **Input:** $m = 1, \quad n = 1$
- **Required output:** $9$
  - Each individual key $(1 \dots 9)$ is a valid length-1 pattern
  - Total valid patterns: $9$
- **Two-Step Unlock Instance:** $m = 1, n = 2 \implies 65$
  - Length 1 patterns: $9$
  - Length 2 patterns:
    - From a corner ($1, 3, 7, 9$): 5 legal moves each ($4 \times 5 = 20$)
    - From an edge ($2, 4, 6, 8$): 7 legal moves each ($4 \times 7 = 28$)
    - From center ($5$): 8 legal moves ($1 \times 8 = 8$)
    - Total length 2 patterns: $20 + 28 + 8 = 56$
    - Overall sum: $9 + 56 = 65$
- **Jumping Over Visited Keys:** Pattern `1 -> 5 -> 9` is legal. Once `5` has been visited, `9 -> 1` or `1 -> 9` can jump directly through `5`!

This instance demonstrates backtracking on graphs with dynamic state-dependent edge availability, mathematically proves how spatial symmetry reduces search branching by a factor of 4, details obstacle adjacency matrices, and analyzes finite graph search complexity.

---

## 1. Instance & Teaching Goal

Android's 3x3 lock screen consists of 9 distinct numeric keys:
$$
\begin{matrix}
1 & 2 & 3 \\
4 & 5 & 6 \\
7 & 8 & 9
\end{matrix}
$$
An unlock pattern connects a sequence of distinct keys of length between $m$ and $n$ inclusive:
1. All keys must be **distinct**.
2. If the straight line segment between consecutive keys passes through an intermediate key, that intermediate key **must have been previously visited** in the sequence.

```text
3x3 Keypad:
1 --- 2 --- 3
|  \  |  /  |
4 --- 5 --- 6
|  /  |  \  |
7 --- 8 --- 9

Obstacle Pairs (Intermediate Key Required):
1 <-> 3 : passes through 2
4 <-> 6 : passes through 5
7 <-> 9 : passes through 8
1 <-> 7 : passes through 4
2 <-> 8 : passes through 5
3 <-> 9 : passes through 6
1 <-> 9 : passes through 5 (diagonal)
3 <-> 7 : passes through 5 (diagonal)
```

---

## 2. Conceptual Foundation & Invariants

### 1. The Obstacle Matrix `cross[10][10]`
We store the intermediate obstacle required between any pair of keys $(i, j)$:
- `cross[1][3] = cross[3][1] = 2`
- `cross[4][6] = cross[6][4] = 5`
- `cross[7][9] = cross[9][7] = 8`
- `cross[1][7] = cross[7][1] = 4`
- `cross[2][8] = cross[8][2] = 5`
- `cross[3][9] = cross[9][3] = 6`
- `cross[1][9] = cross[9][1] = 5`
- `cross[3][7] = cross[7][3] = 5`
For all other pairs (adjacent keys or knight moves like $1 \to 6$ or $1 \to 8$), `cross[i][j] = 0` (no obstacle).

### 2. Transition Validity Rule
A transition from key $i$ to key $j$ is valid if and only if:
1. $j$ is not visited: `not vis[j]`
2. Either no obstacle lies between them ($cross[i][j] == 0$) OR the obstacle has already been visited (`vis[cross[i][j]] == True`).

### 3. Exploiting 8-Fold Geometric Symmetry
The 9 keys fall into 3 symmetric classes:
- **Corners (4 keys):** $\{1, 3, 7, 9\}$ — Identical pattern counts: $4 \times dfs(1)$
- **Edges (4 keys):** $\{2, 4, 6, 8\}$ — Identical pattern counts: $4 \times dfs(2)$
- **Center (1 key):** $\{5\}$ — Unique pattern count: $1 \times dfs(5)$

$$
\text{Total Patterns} = 4 \cdot dfs(1) + 4 \cdot dfs(2) + dfs(5)
$$

---

## 3. Step-by-Step Worked Execution

We trace $m = 1, n = 2$ using symmetry classes:

---

### Step 1: Search from Corner Class ($i = 1$)
- Initial state: $cnt = 1$. Since $cnt \ge m$ ($1 \ge 1$), increment $ans \mathrel{+}= 1$ (Pattern `[1]`).
- Evaluate candidate transitions $j \in [2 \dots 9]$ with $cnt = 2 \le n$:
  - $j = 2$: $cross[1][2] = 0 \implies$ **Valid** (`[1, 2]`)
  - $j = 3$: $cross[1][3] = 2$, but `vis[2]` is False $\implies$ **Blocked!**
  - $j = 4$: $cross[1][4] = 0 \implies$ **Valid** (`[1, 4]`)
  - $j = 5$: $cross[1][5] = 0 \implies$ **Valid** (`[1, 5]`)
  - $j = 6$: knight move, $cross[1][6] = 0 \implies$ **Valid** (`[1, 6]`)
  - $j = 7$: $cross[1][7] = 4$, `vis[4]` is False $\implies$ **Blocked!**
  - $j = 8$: knight move, $cross[1][8] = 0 \implies$ **Valid** (`[1, 8]`)
  - $j = 9$: $cross[1][9] = 5$, `vis[5]` is False $\implies$ **Blocked!**
- Total valid sequences starting at $1$:
  $$
  dfs(1) = 1 \; (\text{len 1}) + 5 \; (\text{len 2}) = \mathbf{6}
  $$
- Corner contribution ($4$ corners): $4 \times 6 = \mathbf{24}$.

---

### Step 2: Search from Edge Class ($i = 2$)
- Initial state: $cnt = 1 \implies ans = 1$ (Pattern `[2]`).
- Evaluate candidate transitions $j \in \{1, 3, 4, 5, 6, 7, 8, 9\}$ at $cnt = 2$:
  - $j \in \{1, 3, 4, 5, 6, 7, 9\}$: All have $cross[2][j] = 0 \implies \mathbf{7 \text{ Valid Moves}}$.
  - $j = 8$: $cross[2][8] = 5$, but `vis[5]` is False $\implies$ **Blocked!**
- Total valid sequences starting at $2$:
  $$
  dfs(2) = 1 \; (\text{len 1}) + 7 \; (\text{len 2}) = \mathbf{8}
  $$
- Edge contribution ($4$ edges): $4 \times 8 = \mathbf{32}$.

---

### Step 3: Search from Center Class ($i = 5$)
- Initial state: $cnt = 1 \implies ans = 1$ (Pattern `[5]`).
- Evaluate candidate transitions at $cnt = 2$:
  - Center key 5 has direct line of sight with all other 8 keys!
  - $cross[5][j] = 0$ for all $j \in \{1, 2, 3, 4, 6, 7, 8, 9\} \implies \mathbf{8 \text{ Valid Moves}}$.
- Total valid sequences starting at $5$:
  $$
  dfs(5) = 1 + 8 = \mathbf{9}
  $$
- Center contribution ($1$ center): $1 \times 9 = \mathbf{9}$.

---

### Step 4: Total Aggregation
Sum contributions across all symmetry groups:
$$
\text{Total} = (4 \times 6) + (4 \times 8) + (1 \times 9) = 24 + 32 + 9 = \mathbf{65}
$$

For instance $m = 1, n = 1$:
$dfs(1) = 1, dfs(2) = 1, dfs(5) = 1 \implies 4(1) + 4(1) + 1 = \mathbf{9}$.

---

## 4. Complete Execution Trace

```text
Grid Dimensions: 3x3, Targets: m = 1, n = 2

Corner Start (Key 1):
  Length 1: [1]
  Length 2: [1,2], [1,4], [1,5], [1,6], [1,8] (5 branches)
  dfs(1) = 6  -> 4 Corners: 4 * 6 = 24

Edge Start (Key 2):
  Length 1: [2]
  Length 2: [2,1], [2,3], [2,4], [2,5], [2,6], [2,7], [2,9] (7 branches)
  dfs(2) = 8  -> 4 Edges: 4 * 8 = 32

Center Start (Key 5):
  Length 1: [5]
  Length 2: [5,1], [5,2], [5,3], [5,4], [5,6], [5,7], [5,8], [5,9] (8 branches)
  dfs(5) = 9  -> 1 Center: 1 * 9 = 9

Total Valid Patterns: 24 + 32 + 9 = 65
```

| Class | Representative Key | Length 1 Count | Length 2 Legal Branches | Subtree Total | Class Multiplier | Total Contribution |
|:---:|:---:|:---:|:---|:---:|:---:|:---:|
| Corner | 1 | 1 | $\{2, 4, 5, 6, 8\}$ (5) | 6 | 4 | **24** |
| Edge | 2 | 1 | $\{1, 3, 4, 5, 6, 7, 9\}$ (7) | 8 | 4 | **32** |
| Center | 5 | 1 | $\{1, 2, 3, 4, 6, 7, 8, 9\}$ (8) | 9 | 1 | **9** |
| **Sum** | - | - | - | - | - | **$\mathbf{65}$ (Total)** |

---

## 5. Algorithmic Correctness

**Soundness.** The condition `x == 0 or vis[x]` faithfully models the Android lock screen specification: two keys can be connected if they are adjacent/knight-connected or if every key lying directly on the straight segment between them has already been tapped. Backtracking via `vis[i] = False` ensures that visited state is properly reset across different paths.

**Completeness.** By exploring all valid transitions recursively up to depth $n$, and recording all paths reaching depth $\ge m$, no valid pattern is omitted. Multiplying the 3 symmetry roots by their equivalence class sizes ($4, 4, 1$) is mathematically exact because rotation and reflection preserve all pairwise colinearities.

---

## 6. Traps This Instance Exposes

- **Knight's Moves Have No Obstacle:** A transition like $1 \to 6$ or $2 \to 7$ does not pass through any other key on the 3x3 grid. It is immediately valid even if 5 or any other key is unvisited.
- **Previously Visited Obstacles Become Transparent:** If key 5 has been visited, moving directly $1 \to 9$ is legal. Forgetting to allow `vis[x] == True` for obstacles causes massive undercounting.
- **Forgetting to Backtrack `vis[i] = False`:** Failing to unmark visited nodes after returning from the recursive call would corrupt state for sibling branches.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(9!)$, bounded by $\sum_{k=m}^n \frac{9!}{(9-k)!} \le 985,824$ states. Exploiting symmetry reduces the constant factor by approximately 4, completing in under 20 milliseconds.
- **Auxiliary Space Complexity:** $O(n)$, where $n \le 9$ is the maximum call stack depth, alongside fixed $O(1)$ size arrays for `cross` and `vis`.