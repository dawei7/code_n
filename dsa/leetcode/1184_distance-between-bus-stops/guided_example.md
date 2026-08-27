# Guided Example: Distance Between Bus Stops

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"distance": [1, 2, 3, 4], "start": 0, "destination": 1}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A bus has `n` stops numbered from `0` to $n - 1$ that form a circle. We know the distance between all pairs of neighboring stops where $\text{distance}[i]$ is the distance between the stops number `i` and $(i + 1) \% n$.

The objective is to compute `1` from `{"distance": [1, 2, 3, 4], "start": 0, "destination": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Measure the whole circumference first

The solution computes `s = sum(distance)`. This is the total length of every segment in the circle, or the circle’s circumference. Once one directional route has length `t`, the other route must contain exactly the segments not used by the first route, so its length is `s - t`.

This complementary-sum idea avoids running a second traversal in the opposite direction. It is valid even when some segments have length zero because the two routes still partition the segment positions, and subtraction still gives the other total.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"distance": [1, 2, 3, 4], "start": 0, "destination": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Walk one direction from start to destination

The variable `t` begins at zero. While `start != destination`, the current `start` identifies the next clockwise segment to cross. The code adds `distance[start]` and advances the stop with

`start = (start + 1) % n`.

If `start` is not the final stop, this simply moves to the next number. If it is `n - 1`, adding one gives `n` and taking modulo `n` wraps the value to zero. The loop ends immediately upon arriving at `destination`, so the segment leaving the destination is not included.

Although the function parameter named `start` is updated, the original value is no longer needed after traversal begins. The mutation changes only the local parameter binding; it does not alter the caller’s integer.

Because the stops form a cycle and the destination is a valid stop, repeatedly moving forward must reach it. If the stops differ, this takes between one and `n - 1` segment crossings. If they are equal, the loop performs no work and `t` remains zero.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The variable `t` begins at zero.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How the two routes partition the circle

The walked route begins at the original start, follows consecutive forward segments, and ends at the destination. The reverse-direction route from the same start to the same destination uses every other segment. No segment belongs to both route interiors, and together the routes cover the full cycle once. Their lengths add to `s`, so the unwalked route has length `s - t`.

The return expression `min(t, s - t)` selects the shorter direction. If both routes have equal length, either one is shortest and their common value is returned.

For `distance = [1, 2, 3, 4]`, start zero, and destination two, the forward traversal adds the segment from zero to one and then the segment from one to two. Thus `t = 1 + 2 = 3`. The circumference is ten, so the other direction has length seven. The answer is three.

For the same array with destination three, the forward route adds `1 + 2 + 3 = 6`. The complement is `10 - 6 = 4`, corresponding to traveling from zero backward across the segment that connects stop three to stop zero. Taking the minimum correctly returns four even though the explicitly traversed direction was longer.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"distance": [1, 2, 3, 4], "start": 0, "destination": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Sum a normalized index interval:** Swap `start:** - **Sum a normalized index interval:** Swap `start` and `destination` so the first is smaller, sum the direct array slice between them, and compare it with the circumference complement. This avoids modulo traversal but may allocate a temporary slice in Python if written carelessly.
- **Traverse both directions separately:** Walking clockwise and counterclockwise gives the same two totals, but the second walk is unnecessary after the circumference is known.
- **General shortest-path algorithm:** Modeling stops as a weighted graph and running Dijkstra’s algorithm would work for nonnegative edges, but it ignores the special cycle structure and adds needless complexity.
- **Start equals destination:** The empty route has distance zero. The loop does not execute, and `min(0, s)` returns zero.
- **One-stop circle:** Both valid indices are zero, so this reduces to the equal-endpoint case and returns zero.
- **Wraparound route is shorter:** The explicit traversal may take the long arc. The complementary value `s - t` still captures the shorter wraparound direction.
- **Zero-length segments:** They are valid and do not disrupt the partition argument. Multiple stops can be separated by total distance zero.
- **Equal route lengths:** `min` returns their shared length, and no tie-breaking direction is required.
- **Final segment indexing:** `distance[n - 1]` connects stop `n - 1` back to zero. The modulo update is necessary to cross that boundary correctly.
- **Nonnegative-distance guarantee:** The claim that repeated travel cannot improve a route relies on segment lengths being nonnegative, which the constraints guarantee.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of stops, which is also the length of `distance`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
