# Guided Example: Most Stones Removed with Same Row or Column

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"stones": [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]}`
- **Required output:** `5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

On a 2D plane, we place `n` stones at some integer coordinate points. Each coordinate point may have at most one stone.

The objective is to compute `5` from `{"stones": [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: View removable relationships as connected components

Make each stone a graph vertex. Connect two stones when they share a row or share a column. Stones joined through several such edges belong to the same connected component, even if the endpoints do not directly share a coordinate.

Within a connected component containing `k` stones, exactly `k - 1` stones can be removed. At least one must remain because the final stone has no other remaining stone in its component. Conversely, the other `k - 1` can be removed by preserving a suitable connected backbone until the end.

If the graph has `c` components among `n` stones, the maximum removals are:

`n - c`.

The solution obtains this quantity indirectly by counting successful union operations.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"stones": [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Union-Find representation

The `UnionFind` object begins with every stone in its own component:

- `p[i] = i` makes each stone its own parent;
- `size[i] = 1` records one stone in each initial tree.

Method `find(x)` follows parent links to the component root. Its recursive assignment `p[x] = find(p[x])` performs path compression: after finding the root, every node on that path points directly to it. Later searches become very fast.

Method `union(a, b)` finds roots `pa` and `pb`. If they are equal, the stones already belong to the same component, so the method returns false.

Otherwise, it attaches the smaller component tree beneath the larger one using `size` and returns true. This union-by-size rule keeps trees shallow.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The `UnionFind` object begins with every stone in its own co... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How the stone pairs are examined

The outer loop processes stone `i` with coordinates `x1, y1`.

The inner enumeration ranges over `stones[:i]`, so it compares stone `i` with every earlier stone exactly once. It does not compare a stone with itself and does not later repeat the pair in reverse order.

When `x1 == x2` or `y1 == y2`, the two vertices have an edge and should be in one component. The code calls `uf.union(i, j)`.

The Boolean return value participates directly in arithmetic. In Python, true contributes one and false contributes zero:

`ans += uf.union(i, j)`.

Thus `ans` counts only unions that merge two previously separate components. Redundant edges inside an already-connected component do not increase it.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"stones": [[0, 0], [0, 1], [1, 0], [1, 2], [2, 1], [2, 2]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Row and column representative maps:** Union ea:** - **Row and column representative maps:** Union each stone with a previously seen stone in its row and column. This avoids all-pairs comparison and can achieve `O(n alpha(n))` expected time.
- **Coordinate-node Union-Find:** Treat each row and each encoded column as graph nodes and union a stone's row with its column. Count connected coordinate roots afterward.
- **Depth-first search:** Build row and column adjacency and count graph components. It is correct, but naive pairwise adjacency construction still costs `O(n^2)`.
- **Single stone:** No pair or successful union exists, so zero stones can be removed.
- **All stones in one row:** Each new stone joins the same component; exactly `n - 1` unions succeed and all but one stone are removable.
- **No shared row or column:** Every stone remains isolated, no union succeeds, and the answer is zero.
- **Redundant cycles:** Extra edges within a component return false and do not inflate the answer.
- **Transitive connection:** Stones need not directly share coordinates with every component member; a path of row and column relationships is enough.
- **Unique coordinates:** No two stones occupy the same point, though sharing one coordinate is precisely what creates edges.
- **Boolean addition:** The code relies on Python treating true as one and false as zero. An explicit conditional would be needed in languages without that behavior.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\alpha(n))$. Let `n` be the number of stones.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
