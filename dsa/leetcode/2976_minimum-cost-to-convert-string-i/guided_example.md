# Guided Example: Minimum Cost to Convert String I

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"source": "abc", "target": "abc", "original": ["a"], "changed": ["b"], "cost": [5]}`
- **Required output:** `0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two **0-indexed** strings `source` and `target`, both of length `n` and consisting of **lowercase** English letters. You are also given two **0-indexed** character arrays `original` and `changed`, and an integer array `cost`, where $\text{cost}[i]$ represents the cost of changing the character $\text{original}[i]$ to the character $\text{changed}[i]$.

The objective is to compute `0` from `{"source": "abc", "target": "abc", "original": ["a"], "changed": ["b"], "cost": [5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Model letters as a directed weighted graph

Each lowercase English letter is a node. A rule saying that character `x` may become character `y` for cost `z` is a directed edge from `x` to `y` with weight `z`. Direction matters: permission to change `'a'` into `'b'` does not automatically permit the reverse change.

A position may undergo any number of operations. Therefore, the cheapest way to turn one letter into another is not necessarily a direct rule. It may be a path through intermediate letters. If `a -> c` costs one and `c -> b` costs two, then `a` can become `b` for three even when there is no direct `a -> b` rule.

The code converts a character to an integer from zero through 25 with `ord(character) - ord('a')`. It creates a $26 \times 26$ matrix `g`, initially filled with infinity. Entry `g[x][y]` means the smallest conversion cost currently known from letter $x$ to letter $y$.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"source": "abc", "target": "abc", "original": ["a"], "changed": ["b"], "cost": [5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Initialize the direct possibilities carefully

Every letter can remain itself for zero cost, so the diagonal is set with `g[i][i] = 0`. For every supplied rule, the code executes `g[x][y] = min(g[x][y], z)`.

The minimum is important because the description explicitly allows duplicate source/destination rule pairs. If one rule converts `a` to `b` for ten and another does so for three, retaining whichever rule appeared last would be unsafe. Keeping three is always at least as good in every future path.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Every letter can remain itself for zero cost, so the diagona... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Compute every cheapest letter-to-letter route

Floyd–Warshall considers each of the 26 letters as a possible intermediate. When processing intermediate $k$, it updates every ordered pair $(i,j)$ by comparing:

- the best route from $i$ to $j$ already known, and
- the route from $i$ to $k$, followed by the route from $k$ to $j$.

The update is `g[i][j] = min(g[i][j], g[i][k] + g[k][j])`. After intermediate letters zero through $k$ have been processed, `g[i][j]` is the least cost of a path whose internal nodes come from that processed set. This invariant starts with direct edges and zero-length diagonal routes. Adding one possible intermediate preserves it by dividing every newly allowed route at $k$. Once all 26 letters have served as intermediates, every possible conversion chain has been considered.

All costs are positive, so there are no negative cycles or incentives to repeat a cycle. Infinity behaves safely in the arithmetic: an unreachable partial path plus any finite cost remains infinity.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"source": "abc", "target": "abc", "original": ["a"], "changed": ["b"], "cost": [5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Run Dijkstra only when a pair is needed:** Pos:** - **Run Dijkstra only when a pair is needed:** Positive weights permit Dijkstra, but with only 26 nodes, one Floyd–Warshall pass is simpler and makes every later lookup constant time.
- **Use only direct rules:** This misses cheaper or uniquely possible multi-step conversions through intermediate letters.
- **Treat rules as undirected:** Conversions are directional. Adding reverse edges would invent operations not present in the input.
- **Duplicate rules:** The matrix must keep the cheapest direct edge before shortest paths are computed.
- **Matching characters:** Their cost is zero even if no explicit self-conversion rule exists; the diagonal and final skip both express this.
- **Unreachable position:** A single infinite lookup makes the entire conversion impossible, so returning `-1` immediately is correct.
- **Repeated character pairs:** Their shortest cost is computed once in `g` but added once per position, because each occurrence needs its own operations.
- **Large total cost:** The sum can exceed a 32-bit integer; Python integers represent it safely.
- **Input preservation:** The algorithm builds a separate matrix and only reads all supplied sequences.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N + K + A^3)$. Let $N$ be the common string length, $K$ the number of conversion rules, and $A=26$ the alphabet size. Matrix initialization costs $O(A^2)$. Loading rules costs $O(K)$. Floyd–Warshall costs $O(A^3)$, and the final position scan costs $O(N)$. The full bound is $O(N+K+A^3)$.
- **Auxiliary Space Complexity:** $O(A^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
