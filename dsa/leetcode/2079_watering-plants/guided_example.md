# Guided Example: Watering Plants

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"plants": [2, 2, 3, 3], "capacity": 5}`
- **Required output:** `14`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You want to water `n` plants in your garden with a watering can. The plants are arranged in a row and are labeled from `0` to $n - 1$ from left to right where the $i^{\text{th}}$ plant is located at $x = i$. There is a river at $x = -1$ that you can refill your watering can at.

The objective is to compute `14` from `{"plants": [2, 2, 3, 3], "capacity": 5}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Track only the water currently in the can

Plants must be watered from left to right, and the gardener's location before each plant is completely determined. Before watering plant 0, the gardener is at the river at coordinate $-1$. Before every later plant `i`, plant `i - 1` has just been watered, so the gardener is at coordinate $i-1$.

The variable `water` records how much water remains. It starts at `capacity` because the can is full at the river. The variable `ans` accumulates movement steps; watering itself does not cost a movement step.

For each pair `i, p` from `enumerate(plants)`, `p` is the exact amount needed by plant `i`. The algorithm has only two possible actions, matching the rules.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"plants": [2, 2, 3, 3], "capacity": 5}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Move forward one step when enough water remains

If `water >= p`, the current supply can completely water plant `i`. The gardener moves from the previous position to `i`, which costs exactly one step, waters the plant, and retains `water - p` units.

The code performs

`water -= p`

and

`ans += 1`.

Equality belongs in this branch. When `water == p`, the current plant can be watered completely, leaving zero water. The gardener must not refill before watering it because early refills are forbidden.

If a next plant exists, its own iteration will observe the zero remainder, find it insufficient for that positive demand, and account for the required refill then.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: When water is insufficient, count the round trip directly

If `water < p`, the gardener cannot partially water the current plant. From the position immediately before it, coordinate $i-1$, the gardener must return to the river at coordinate $-1$.

That return distance is

$$
(i-1)-(-1)=i.
$$

After refilling, walking from the river to plant `i` costs

$$
i-(-1)=i+1.
$$

The combined movement is therefore

$$
i+(i+1)=2i+1.
$$

This is exactly the source expression `i * 2 + 1`.

The gardener arrives with a full can and immediately waters the plant. The remaining amount becomes `capacity - p`, which the source assigns directly to `water`. There is no need to first assign `capacity` and then subtract `p` as two separate operations.

The input guarantees `p <= capacity` for every plant, so a full refill is always sufficient to water the current plant completely.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `14` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"plants": [2, 2, 3, 3], "capacity": 5}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `14` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Step-by-step movement simulation:** Moving a coordinate one unit at a time would reproduce the story but spend work proportional to the potentially large answer. The formula `2 * i + 1` compresses each forced refill trip into constant time.
- **Refilling whenever the can is not full:** This violates the rule forbidding early refills and can change the total route. A refill occurs only when the remaining water cannot completely satisfy the current next plant.
- **Prefix-sum grouping:** One can divide plants into maximal segments watered by each full can using cumulative sums. The direct state loop is simpler and already linear.
- **Exact equality:** If `water == p`, water the plant immediately without refilling. The `>=` condition correctly leaves zero afterward.
- **First plant:** Capacity is guaranteed to cover every single demand, so plant 0 normally takes the enough-water branch and costs one step from the river. Even the refill formula at `i = 0` would equal one, but no refill is required.
- **One plant:** The method adds one step from coordinate $-1$ to 0, waters it, and returns 1. There is no need to walk back after the final plant.
- **Refill before every later plant:** When each remaining amount is too small for the next demand, every iteration adds its full $2i+1$ trip. The formula handles this worst travel pattern without extra loops.
- **Water left after the last plant:** It is irrelevant. The gardener is not required to return to the river, and the solution adds no final return trip.
- **Demand equal to capacity:** After a refill, `capacity - p` becomes zero. The next positive-demand plant then correctly forces another refill.
- **Large capacity:** If the can covers all demands, every plant costs one forward step and the answer is $n$.
- **Capacity guarantee:** Because every `plants[i] <= capacity`, one refill always suffices. Without this guarantee, the branch would need to handle an impossible-to-water plant.
- **No array mutation:** The source records only the remaining total in `water`; plant demands remain intact throughout the traversal.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of plants.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
