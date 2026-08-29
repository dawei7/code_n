# Guided Example: Maximum Hamming Distances

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [9, 12, 9, 11], "m": 4}`
- **Required output:** `[2, 3, 2, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array `nums` and an integer `m`, with each element $\text{nums}[i]$ satisfying $0 \le \text{nums}[i] < 2^m$, return an array `answer`. The `answer` array should be of the same length as `nums`, where each element $\text{answer}[i]$ represents the *maximum* **Hamming distance **between $\text{nums}[i]$ and any other element $\text{nums}[j]$ in the array.

The objective is to compute `[2, 3, 2, 3]` from `{"nums": [9, 12, 9, 11], "m": 4}` while avoiding redundant calculations and unnecessary overhead.

A naive or brute-force exploration risks evaluating infeasible states or repeating subproblem computations. The optimal method establishes a clear invariant that advances deterministically toward the goal.

---

## 2. Conceptual Foundation & Invariants

We maintain the core conceptual parameters and state variables:

| State Parameter | Role & Purpose | Initial State |
|---|---|---|
| Primary State | Tracks active elements, frontier indices, or DP table cells | Initialized at boundary |
| Accumulator | Preserves confirmed optimal sub-answers or counts | Empty / Neutral |

> **Invariant.** At every processing step, all previously evaluated subproblems strictly satisfy the problem constraints, and no viable candidate solution has been omitted.

---

## 3. Step-by-Step Worked Execution

### Step 1: Turn bit strings into vertices of a hypercube

Every legal number has exactly $m$ relevant binary positions after adding leading zeroes. Think of each $m$-bit number as a vertex of an $m$-dimensional hypercube. Two vertices share an edge when they differ in exactly one bit.

Moving along one edge flips one bit, so the shortest-path distance between two vertices is exactly their Hamming distance. This lets a breadth-first search compute minimum Hamming distances without comparing every pair in `nums`.

The array `dist` has one entry for every bit pattern from 0 through $2^m-1$. Every value appearing in `nums` is marked with distance zero. These are simultaneous BFS sources.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [9, 12, 9, 11], "m": 4}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Multi-source BFS

The initial frontier `q = nums` contains all source values. At BFS layer `k`, the code considers every bit position $i$ and forms

`y = x ^ (1 << i)`.

XOR toggles exactly bit $i$, so `y` is one hypercube neighbor of `x`. If `dist[y] == -1`, this is the first time any source reaches `y`. BFS's layer order guarantees that `k` is the minimum Hamming distance from `y` to any input value. The code records it and places `y` in the next frontier.

After the BFS completes,

$$
\texttt{dist[v]}=\min_{a\in\texttt{nums}}\operatorname{Ham}(v,a)
$$

for every $m$-bit pattern $v$.

Duplicate values in `nums` appear more than once in the initial frontier, but `dist` still marks them as the same source vertex. They may cause repeated checks during the first layer, yet `dist[y] == -1` ensures each nonsource vertex is enqueued only once.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Convert a maximum distance into a minimum distance

The desired value for input $x$ is

$$
\max_{a\in\texttt{nums}}\operatorname{Ham}(x,a).
$$

Multi-source BFS naturally gives minimum distances, not maxima. The fixed-width complement supplies the bridge.

Let

`mask = (1 << m) - 1`

and `c = x ^ mask`, the bitwise complement of $x$ within exactly $m$ positions. At every bit position, $x$ and $a$ differ exactly when $c$ and $a$ agree. Therefore,

$$
\operatorname{Ham}(x,a)+\operatorname{Ham}(c,a)=m.
$$

Rearranging and maximizing over $a$ gives

$$
\max_a \operatorname{Ham}(x,a)
=m-\min_a\operatorname{Ham}(c,a).
$$

The minimum on the right is precisely `dist[c]`. This yields the returned expression

`m - dist[x ^ ((1 << m) - 1)]`.


The BFS invariant says that before layer $k$ begins, every vertex at distance less than $k$ from the source set has its final distance, and no undiscovered vertex is closer than $k$. Flipping each of the $m$ bits enumerates every edge, so all vertices at distance $k$ are discovered from layer $k-1$. By induction, `dist` contains exact nearest-source Hamming distances.

For each query value $x$, the complement identity holds independently for every possible partner $a$. The partner minimizing distance from the complement is exactly a partner maximizing distance from $x$. Substituting the BFS result therefore produces the requested maximum.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 3, 2, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [9, 12, 9, 11], "m": 4}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 3, 2, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Compare every pair:** Compute `(a ^ b).bit_count()` for all pairs. It is simple but costs $O(n^2)$ time.
- **Run BFS from each input separately:** This repeats the same hypercube work $n$ times. Multi-source BFS combines all nearest-source computations in one traversal.
- **Bitwise trie search:** A trie can greedily prefer opposite bits to seek large Hamming distance, but maximizing total differing positions is not always captured by a single greedy path without richer state.
- **Subset transforms:** Min-plus or Boolean transforms over masks can propagate distance information, but BFS is the direct shortest-path interpretation.
- **Duplicate input values:** They receive identical answers. Duplicate initial frontier entries do not change distances, only some first-layer checks.
- **Complement also present:** If $x$'s exact complement is in `nums`, `dist[complement] = 0` and the answer is the maximum possible $m$.
- **All inputs identical:** The only available partner value is the same bit pattern, so every answer is zero, even if indices differ.
- **Leading zeroes:** The finite $m$-bit representation makes them real Hamming positions and is enforced by the mask.
- **m equal to one:** The hypercube has two vertices; answers are either zero or one depending on whether the opposite bit occurs.
- **Source list is nonempty:** The constraint has at least two entries, so BFS has sources and every hypercube vertex is eventually reached.
- **Frontier level value:** `k` starts at 1 because neighbors of source vertices are exactly one bit flip away.
- **Input preservation:** `q` initially references `nums`, but neither `pop` nor other mutation is used, so the caller's list remains unchanged.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(m2^m+n)$. There are $V=2^m$ hypercube vertices and $mV$ directed neighbor examinations. Every nonsource vertex is enqueued once, while duplicate initial sources can add at most $n$ extra frontier entries. Since $n\le2^m$, total time is $O(m2^m+n)$, usually written $O(m2^m)$.
- **Auxiliary Space Complexity:** $O(2^m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
