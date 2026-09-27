# Guided Example: Jump Game II

We trace the step-by-step execution of the greedy BFS level-frontier expansion on a representative array instance:

- **Input:** $\text{nums} = [2, 3, 1, 1, 4]$
- **Required output:** $2$

This instance demonstrates modeling jump intervals as implicit breadth-first search (BFS) tiers, tracking current-tier reach versus next-tier horizon ($\text{cur\_end}$ vs $\text{cur\_farthest}$), incrementing jumps only upon exhausting the current boundary, and achieving $O(N)$ time with $O(1)$ space.

---

## 1. Instance & Teaching Goal

Given an array of non-negative integers $\text{nums}$ of length $N = 5$ where each element $\text{nums}[i]$ represents your maximum jumping length from position $i$, we must reach the last index ($N - 1 = 4$) in the minimum number of jumps. The problem guarantees that the target is reachable.

For $\text{nums} = [2, 3, 1, 1, 4]$:
- From index 0 ($\text{nums}[0] = 2$), we can reach indices 1 or 2.
- From index 1 ($\text{nums}[1] = 3$), we can jump directly to index 4 ($1 + 3 = 4$).
- The minimum number of jumps is $2$: $0 \to 1 \to 4$.

A naive dynamic programming approach computes $DP[i] = 1 + \min_{j}(DP[j])$ in $O(N^2)$ time. The greedy BFS approach observes that all indices reachable in $k$ jumps form a contiguous frontier interval. Expanding this frontier takes $O(N)$ time with $O(1)$ auxiliary space.

---

## 2. Conceptual Foundation & Invariants

### Implicit BFS Layers
We view the problem as a BFS on an unweighted directed graph where each edge represents a valid jump:
- **Layer 0:** Index 0 (0 jumps).
- **Layer 1:** Indices reachable in 1 jump: $[1, 2]$ (since $0 + 2 = 2$).
- **Layer 2:** Indices reachable in 2 jumps: $[3, 4]$ (since $\max(1 + 3, 2 + 1) = 4$).

```text
Layer 0:  [0]
           |
Layer 1:  [1, 2]
           |  \
Layer 2:  [3, 4]  -> Target reached!
```

### Greedy Frontier Variables
We maintain:
- `cur_end`: The boundary of the current BFS tier (furthest index reachable with the current number of jumps).
- `cur_farthest`: The maximum reachable index discovered so far for the *next* jump tier.
- `jumps`: Number of jumps taken.

While iterating $i$ from $0$ to $N - 2$:
1. Update next horizon: $\text{cur\_farthest} \leftarrow \max(\text{cur\_farthest}, i + \text{nums}[i])$.
2. If $i == \text{cur\_end}$: We have exhausted all starting positions of the current jump tier. We must commit to another jump:
   - $\text{jumps} \leftarrow \text{jumps} + 1$
   - $\text{cur\_end} \leftarrow \text{cur\_farthest}$

> **Invariant.** At any point, `cur_end` is the maximal index reachable in `jumps` steps, and `cur_farthest` is the maximal index reachable in `jumps + 1` steps.

---

## 3. Step-by-Step Worked Execution

We trace $\text{nums} = [2, 3, 1, 1, 4]$ with $N = 5$:

### Initialization
- $\text{jumps} = 0$.
- $\text{cur\_end} = 0$.
- $\text{cur\_farthest} = 0$.

---

### Step 0 ($i = 0, \text{nums}[0] = 2$)
- Candidate reach from index 0: $0 + \text{nums}[0] = 0 + 2 = 2$.
- Update horizon: $\text{cur\_farthest} = \max(0, 2) = 2$.
- Boundary check: $i == \text{cur\_end}$ ($0 == 0$).
  - Frontier exhausted! Commit Jump 1.
  - $\text{jumps} \leftarrow 0 + 1 = 1$.
  - Update current tier boundary: $\text{cur\_end} \leftarrow 2$.
  - State: With 1 jump, we can cover the entire interval $[1, 2]$.

---

### Step 1 ($i = 1, \text{nums}[1] = 3$)
- Candidate reach from index 1: $1 + \text{nums}[1] = 1 + 3 = 4$.
- Update horizon: $\text{cur\_farthest} = \max(2, 4) = 4$.
- Boundary check: $i = 1 \ne \text{cur\_end} = 2$.
  - Still within Layer 1. No jump increment yet.

---

### Step 2 ($i = 2, \text{nums}[2] = 1$)
- Candidate reach from index 2: $2 + \text{nums}[2] = 2 + 1 = 3$.
- Update horizon: $\text{cur\_farthest} = \max(4, 3) = 4$.
- Boundary check: $i == \text{cur\_end}$ ($2 == 2$).
  - Frontier exhausted! Commit Jump 2.
  - $\text{jumps} \leftarrow 1 + 1 = 2$.
  - Update current tier boundary: $\text{cur\_end} \leftarrow 4$.
  - State: With 2 jumps, we can cover up to index $4$ (target).

---

### Step 3 ($i = 3, \text{nums}[3] = 1$)
- Loop terminates because $i$ only needs to iterate up to $N - 2 = 3$. Once $\text{cur\_end} \ge N - 1$, the destination is already reachable.

Final output: $\text{jumps} = 2$.

---

## 4. Complete Execution Trace

| Step $i$ | $\text{nums}[i]$ | Reach from $i$ ($i + \text{nums}[i]$) | Next Horizon $\text{cur\_farthest}$ | Current Boundary $\text{cur\_end}$ | Tier End Reached? | Jump Count $\text{jumps}$ | Active Tier Interval |
|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---|
| Start | - | - | 0 | 0 | - | 0 | $[0, 0]$ (Tier 0) |
| 0 | 2 | 2 | 2 | 0 | **Yes ($i == 0$)** | **1** | $[1, 2]$ (Tier 1) |
| 1 | 3 | 4 | 4 | 2 | No ($1 < 2$) | 1 | $[1, 2]$ (Tier 1) |
| 2 | 1 | 3 | 4 | 2 | **Yes ($i == 2$)** | **2** | $[3, 4]$ (Tier 2) |
| 3 | 1 | 4 | 4 | 4 | No ($3 < 4$) | 2 | Target reached |

### Layer Decomposition of the Same Instance

The scan above is written in index order. The table below regroups exactly the same work by breadth-first layer, which is the view the invariant is stated in: every position assigned to layer $k$ is reachable in at least $k$ jumps, and the frontier interval of layer $k$ is precisely the set of positions whose minimum jump count is $k$.

| BFS layer $k$ | Positions whose minimum cost is $k$ | Reach offered at each scanned position | Best reach $\max(i + \text{nums}[i])$ | Frontier interval | $\text{jumps}$ after the layer | Contains destination (index 4)? |
|:---:|:---|:---|:---:|:---:|:---:|:---|
| 0 | $\{0\}$ | $0 + 2 = 2$ | 2 | $[0, 0]$ | 0 | No |
| 1 | $\{1, 2\}$ | $1 + 3 = 4$ and $2 + 1 = 3$ | 4 | $[1, 2]$ | 1 | No |
| 2 | $\{3, 4\}$ | $3 + 1 = 4$; position 4 is itself the destination and is never scanned | 4 | $[3, 4]$ | 2 | Yes, so the scan halts |

Layer 1 is where the answer is decided: position 1 offers reach $4$ while position 2 offers only $3$, so the layer's horizon is $4$ even though position 2 is the later of the two. A method that committed to a landing position before finishing the layer — say by taking position 2 because it is further right — would still need three jumps and would only discover its mistake later.

---

## 5. Algorithmic Correctness

**Soundness.** Every increment of `jumps` corresponds to moving to the next BFS depth. Because `cur_farthest` greedily tracks the maximal reachable index from all nodes visited within the current tier, `cur_end` expands as far as possible at every step, ensuring the minimal number of jumps.

**Completeness.** Since all elements up to `cur_end` are inspected before taking another jump, no potential jump choice is overlooked. The algorithm stops at $N - 2$ because any jump reaching or exceeding $N - 1$ has already satisfied the goal.

---

## 6. Traps This Instance Exposes

- **Iterating Up to $N - 1$ Instead of $N - 2$:** If the loop runs to $N - 1$, encountering $i == \text{cur\_end}$ at the destination index would mistakenly trigger an extra unnecessary jump. Halting at $N - 2$ guarantees that reaching the final index does not add a redundant jump.
- **Single-Element Array ($N = 1$):** When $N = 1$, the loop over `range(N - 1)` does not execute at all, correctly returning $\text{jumps} = 0$ because no jumps are needed to start at the destination.
- **Greedy Subproblem Fallacy:** Jumping greedily to the immediate largest value ($\text{argmax}(\text{nums}[j])$) is suboptimal; the algorithm must maximize $j + \text{nums}[j]$ (future reach), not $\text{nums}[j]$ alone.

### Boundary and Degenerate Inputs

| Boundary scenario | Input | Required result | Why the frontier rule still holds |
|:---|:---|:---:|:---|
| Already standing on the destination | $[0]$ | 0 | The scan range excludes the final index, so it is empty; $\text{cur\_end}$ is never reached and $\text{jumps}$ stays $0$. |
| First jump reaches the destination | $[5, 0, 0, 0, 0, 0]$ | 1 | At $i = 0$ the horizon becomes $0 + 5 = 5 \ge N - 1 = 5$, and the single boundary commit raises $\text{jumps}$ to $1$. |
| Maximum legal jump length | $[1000, 0]$ | 1 | $\text{nums}[0] = 1000 \ge N - 1 = 1$, so layer 1 already covers the whole array. |
| Every step is mandatory | $[1, 1, 1, 1]$ | 3 | Each layer contains exactly one position, so every scanned index is simultaneously a tier boundary; the jump counts along the scan are $1, 2, 3$. |
| A zero inside a reachable layer | $[2, 3, 0, 1, 4]$ | 2 | Position 2 contributes $2 + 0 = 2$, which loses to position 1's $1 + 3 = 4$; the dead element is simply outbid. |
| The furthest position in a layer is not the strongest | $[3, 5, 1, 4, 0, 0, 0, 0]$ | 2 | Layer 1 is $\{1, 2, 3\}$; the maximum $i + \text{nums}[i]$ is $3 + 4 = 7 = N - 1$, so layer 2 already contains the destination. |

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$, where $N = |\text{nums}|$. The algorithm traverses the array from index $0$ to $N - 2$ in a single linear pass. Each element performs $O(1)$ scalar updates.
- **Auxiliary Space Complexity:** $O(1)$. Memory consumption is strictly constant, using only three integer variables (`jumps`, `cur_end`, `cur_farthest`).

### Alternative Formulations

| Approach | State carried | Time | Auxiliary space | Behaviour on a concrete input |
|:---|:---|:---|:---|:---|
| Frontier expansion (this lesson) | $\text{jumps}$, $\text{cur\_end}$, $\text{cur\_farthest}$ | $O(N)$ | $O(1)$ | On $[2, 3, 1, 1, 4]$ it commits two jumps, the second horizon being supplied by position 1 rather than position 2. |
| Explicit BFS over the jump graph | Queue of positions plus a visited set | $O(N^2)$ edge enumerations in the worst case, since an index may connect to as many as $\text{nums}[i]$ successors | $O(N)$ | Also returns $2$ on $[2, 3, 1, 1, 4]$, finding index 4 at depth 2. |
| Quadratic dynamic programming | Minimum jump count for every prefix | $O(N^2)$ | $O(N)$ | On $[2, 3, 1, 1, 4]$ the table is $[0, 1, 1, 2, 2]$, so the answer is the last entry, $2$. |
| Immediate-largest-value greedy | Current position only | $O(N)$ | $O(1)$ | Coincidentally returns $2$ on $[2, 3, 1, 1, 4]$, where the largest value also maximises the reach; but on $[4, 4, 1, 1, 3, 0, 0, 0]$ it moves $0 \to 1$, then $1 \to 4$, then $4 \to 5$, and stalls at index 5 after three jumps, even though $0 \to 4 \to 7$ needs only two. |

The failure on the last row is the reason the lesson tracks a horizon instead of a landing position: the greedy choice must be deferred until the whole layer has been inspected, because two positions can offer the same value while offering very different remaining reach.