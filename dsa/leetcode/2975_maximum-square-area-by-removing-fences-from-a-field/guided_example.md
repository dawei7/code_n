# Guided Example: Maximum Square Area by Removing Fences From a Field

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"m": 4, "n": 3, "hFences": [2, 3], "vFences": [2]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a large $(m - 1) x (n - 1)$ rectangular field with corners at `(1, 1)` and `(m, n)` containing some horizontal and vertical fences given in arrays `hFences` and `vFences` respectively.

The objective is to compute `4` from `{"m": 4, "n": 3, "hFences": [2, 3], "vFences": [2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A square needs the same realizable span in both directions

The outer field boundaries are permanent fences at horizontal coordinates one and `m` and vertical coordinates one and `n`. An internal fence may be removed. Therefore, choosing any two horizontal fence lines can define the top and bottom of a remaining rectangular region: all horizontal fences between them can be removed. The vertical height is the difference of those two coordinates. The same argument applies to any two vertical fence lines and their horizontal width.

A square exists exactly when some positive distance can be realized between a pair of horizontal fences and also between a pair of vertical fences. Among all shared distances, the largest one gives the greatest square area because area is the square of side length.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"m": 4, "n": 3, "hFences": [2, 3], "vFences": [2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Generate every realizable distance

Nested helper `f(nums, k)` extends the supplied internal-fence list with boundary coordinates `1` and `k`, then sorts it. It uses `combinations(nums, 2)` to enumerate every unordered pair of fence coordinates `a, b`. Since the list is sorted and combinations preserve index order, `b - a` is positive.

The set comprehension stores every such distance:

`{b - a for a, b in combinations(nums, 2)}`.

A set is appropriate because the existence of a side length matters, not how many fence pairs realize it. Duplicate distances would not create a larger square or need separate counting.

Calling the helper for `hFences` with boundary `m` produces `hs`, every possible vertical side length. Calling it for `vFences` with boundary `n` produces `vs`, every possible horizontal side length.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Nested helper `f(nums, k)` extends the supplied internal-fen... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Intersect the possible side lengths

`hs & vs` contains exactly the lengths available in both orientations. The code takes `max(..., default=0)`. If the intersection is empty, `ans` becomes zero. All genuine coordinate differences are positive, so zero is an unambiguous sentinel rather than a realizable square side.

If `ans > 0`, the area is `ans ** 2`. The result is reduced modulo $10^9+7$ only after selecting the true largest side and squaring it. Comparing values after modular reduction would be wrong because residues do not preserve numeric order.

For example, with horizontal coordinates `[1, 2, 3, 4]` and vertical coordinates `[1, 2, 3]`, the horizontal-distance set includes one, two, and three, while the vertical-distance set includes one and two. Their largest shared distance is two, so the maximum area is four.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"m": 4, "n": 3, "hFences": [2, 3], "vFences": [2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Only adjacent-fence gaps:** This misses square:** - **Only adjacent-fence gaps:** This misses squares formed by removing one or more fences between nonadjacent retained boundaries.
- **Compare every horizontal pair with every vertical pair:** Direct cross-comparison can take $O(H^2V^2)$ time. Sets reduce shared-length lookup to expected linear work in the generated distances.
- **Store distances in lists:** Lists retain duplicates and make intersection slower; multiplicity has no meaning here.
- **No shared distance:** The intersection is empty, `default=0` supplies the sentinel, and the function returns `-1`.
- **Boundary-only square:** Adding coordinates one and `m` or `n` ensures the full field dimensions are considered even when no matching internal span exists.
- **Duplicate distances:** Many pairs may produce the same span, but one set entry is sufficient.
- **Modulo timing:** Select and square the actual maximum side first; never maximize modulo-reduced areas.
- **Large coordinates:** Python integers safely square side lengths up to the stated bounds before applying the modulus.
- **Input mutation:** Both fence arrays gain boundary values and are sorted in place; callers needing preservation must pass copies.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(H^2+V^2)$. Let $H$ and $V$ be the original counts of internal horizontal and vertical fences. After adding boundaries there are $H+2$ and $V+2$ coordinates. Pair enumeration generates $O(H^2)$ and $O(V^2)$ differences. Sorting costs $O(H\log H+V\log V)$, which is dominated by pair generation. Set intersection is linear in the smaller set on average. Total expected time is $O(H^2+V^2)$.
- **Auxiliary Space Complexity:** $O(H^2 + V^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
