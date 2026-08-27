# Guided Example: Maximum Star Sum of a Graph

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"vals": [-5], "edges": [], "k": 0}`
- **Required output:** `-5`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is an undirected graph consisting of `n` nodes numbered from `0` to $n - 1$. You are given a **0-indexed** integer array `vals` of length `n` where $\text{vals}[i]$ denotes the value of the $$i^{\text{th}}$$ node.

The objective is to compute `-5` from `{"vals": [-5], "edges": [], "k": 0}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Choose a center, then choose only helpful neighbors

A star consists of one center and at most `k` of its adjacent nodes. The center is always present, so its value must be included even when negative. Neighbor participation is optional because the limit is “at most” `k` rather than “exactly” `k`.

For a fixed center, a neighbor with a negative value can only decrease the star sum. A zero-valued neighbor leaves the sum unchanged and is never needed to improve it. Therefore, an optimal star uses only positive neighbors, selecting up to the `k` largest positive values adjacent to its center.

The problem can consequently be solved independently for every possible center.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"vals": [-5], "edges": [], "k": 0}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Build lists of positive neighbor values

The graph is undirected. For each edge `[a,b]`:

- if `vals[b]>0`, append `vals[b]` to `g[a]` because node `b` is a useful candidate neighbor for center `a`;
- if `vals[a]>0`, append `vals[a]` to `g[b]` for the reverse center-neighbor relationship.

The conditions depend on the neighbor's value, not the center's. A negative-valued node can still be a center, and it may become the best center if its positive neighbors compensate for it. Its negative value merely means it should not be included as an optional neighbor of another center.

Both edge directions are considered even though only positive endpoint values are stored. If both endpoints are positive, each endpoint appears in the other's list. If only one is positive, it appears only as a candidate for the other center.

`defaultdict(list)` makes an absent center behave as if it had an empty neighbor list.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The graph is undirected.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Sort each center's candidates from best to worst

Every stored list `bs` is sorted in descending order. Then `g[i][:k]` contains exactly the first `k` entries, or the whole list if it has fewer than `k`.

Because every stored value is positive, taking more entries until the limit is reached always increases the sum. Thus the best choice for center `i` is:

$$
\texttt{vals}[i]
+
\text{sum of its largest }\min(k,p_i)\text{ positive neighbor values},
$$

where $p_i$ is its number of positive neighbors.

An exchange argument proves the top-choice rule. Suppose a selected neighbor has value $x$ while an unselected eligible neighbor has a larger value $y$. Replacing $x$ with $y$ preserves the edge limit and increases the star sum by $y-x$. Therefore, no optimal selection can omit a larger positive value in favor of a smaller one.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `-5` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"vals": [-5], "edges": [], "k": 0}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `-5` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Size-`k` min-heaps:** Keep only the best `k` p:** - **Size-`k` min-heaps:** Keep only the best `k` positive neighbors per center for $O(m\log(k+1))$ time; this matches the manifest summary but not the exact source.
- **Select then partition:** A linear-time selection algorithm can avoid fully sorting large neighbor lists, though it is more complex.
- **Negative center:** It must still be included, but sufficiently valuable positive neighbors may make its star optimal.
- **Negative neighbor:** Never include it because using fewer than `k` edges is allowed.
- **Zero neighbor:** It cannot improve the sum and may safely be omitted.
- **`k=0`:** Choose the maximum single node.
- **Isolated node:** Its only possible star contains itself.
- **Fewer than `k` positive neighbors:** Use all available positive ones.
- **Multiple edges:** The constraints describe graph edges; the algorithm assumes each edge represents one neighbor relationship.
- **Manifest mismatch:** Complexity analysis must account for sorting complete lists in the protected implementation.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n+m)$. Let $n$ be the number of nodes and $m$ the number of edges. Graph construction processes each edge once and stores at most two positive-neighbor entries, using $O(n+m)$ time and $O(n+m)$ space including dictionary lists.
- **Auxiliary Space Complexity:** $O(n + m)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
