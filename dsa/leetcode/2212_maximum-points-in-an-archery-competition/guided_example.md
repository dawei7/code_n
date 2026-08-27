# Guided Example: Maximum Points in an Archery Competition

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"numArrows": 9, "aliceArrows": [1, 1, 0, 1, 0, 0, 2, 1, 0, 1, 2, 0]}`
- **Required output:** `47`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Alice and Bob are opponents in an archery competition. The competition has set the following rules:

The objective is to compute `47` from `{"numArrows": 9, "aliceArrows": [1, 1, 0, 1, 0, 0, 2, 1, 0, 1, 2, 0]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn each scoring section into one yes-or-no choice

Bob does not receive more points for placing more arrows into a section after he has already beaten Alice there. For section `i`, Alice has `aliceArrows[i]` arrows. Bob loses or ties that section when he uses at most that many arrows, and he wins it only when he uses at least one more. Therefore, if Bob decides to win section `i`, the cheapest useful allocation is exactly `aliceArrows[i] + 1` arrows. That decision costs that many arrows and earns exactly `i` points.

This observation removes an enormous number of meaningless allocations. Instead of asking how many arrows to place in every section, the solution first asks only which sections Bob should win. Every section has two relevant states:

- do not deliberately win it, spending no arrows on it during the search and gaining no points from it; or
- win it with the minimum required number of arrows, spending `aliceArrows[i] + 1` and gaining `i` points.

There are `s = len(aliceArrows)` sections. A bitmask from `0` through `2^s - 1` can represent every possible subset of sections. Bit `i` is `1` precisely when the subset proposes winning section `i`. Enumerating masks is practical because this problem always has only twelve scoring sections, even though the explanation keeps `s` as a useful general symbol.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"numArrows": 9, "aliceArrows": [1, 1, 0, 1, 0, 0, 2, 1, 0, 1, 2, 0]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Evaluate one mask

For every nonempty `mask`, the inner loop visits all entries of `aliceArrows`. When `mask >> i & 1` is true, section `i` belongs to the proposed winning set. The solution then adds `i` to `s`, the score of this proposal, and adds `x + 1` to `cnt`, where `x` is `aliceArrows[i]`. Thus, `cnt` is not an arbitrary allocation: it is the smallest total number of arrows that can win exactly all selected sections.

The mask is feasible when `cnt <= numArrows`. If its score `s` is strictly larger than the best score `mx` found so far, the code remembers both the score and the mask by assigning `mx = s` and `st = mask`. The strict comparison is intentional. The problem permits any maximum-scoring allocation, so there is no need to replace an earlier best subset with a later subset that has the same score.

The code uses the name `s` both conceptually for the number of sections in the complexity discussion and locally for the score accumulated for one mask. In the Python function, `m = len(aliceArrows)` is the actual section count, while the local `s` is reset to zero for each mask. Keeping those roles separate makes the loops easier to understand.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For every nonempty `mask`, the inner loop visits all entries... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why minimum winning costs are sufficient

Suppose an allocation wins section `i` using more than `aliceArrows[i] + 1` arrows. Removing the excess arrows does not change whether Bob wins the section and does not change its point value. Those arrows can therefore be left unused until the final construction step. Consequently, every optimal score has at least one representation among the masks using the minimum winning cost for each selected section.

Conversely, every mask with `cnt <= numArrows` can be turned into a legal allocation. Give each selected section its recorded minimum winning amount. This wins every selected section and consumes `cnt` arrows. The remaining `numArrows - cnt` arrows can be placed somewhere without undoing any victory. This establishes a direct connection between feasible masks and achievable scores: no achievable optimal score is omitted, and every score considered feasible can actually be produced.

Since the loop examines all subsets, it eventually examines a mask corresponding to an optimal set of scoring sections. The stored value `mx` can never exceed the true optimum because it comes only from a feasible allocation. It also cannot finish below the optimum because the optimal subset is among the enumerated masks and would update `mx` unless an equally good subset was already stored. Therefore, `st` identifies a maximum-scoring choice of sections.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `47` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"numArrows": 9, "aliceArrows": [1, 1, 0, 1, 0, 0, 2, 1, 0, 1, 2, 0]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `47` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Backtracking over win-or-skip choices:** A dep:** - **Backtracking over win-or-skip choices:** A depth-first search can make the same two decisions for each section and track arrows and score along the recursion. It has the same exponential worst-case work, and pruning unaffordable branches can reduce practical work, but the bitmask version is shorter and makes exhaustive coverage especially explicit.
- **Zero-one knapsack by arrow budget:** Treat each section as an item with weight `aliceArrows[i] + 1` and value `i`. A budget-indexed dynamic program can find the maximum score, but its cost depends on `numArrows` and reconstruction needs additional state. With only twelve sections, enumerating `2^12` subsets is simpler and independent of a potentially larger arrow budget.
- **Greedily choosing the best score-to-arrow ratio:** Ranking sections by `i / (aliceArrows[i] + 1)` is not reliable for a zero-one choice problem. A locally attractive ratio can consume arrows that would enable a better combination of other sections, so only a method that considers combinations can guarantee the optimum.
- **Spending extra arrows while evaluating a subset:** Excess arrows never increase a section's points. Using the minimum winning cost during comparison is essential because it gives every proposed subset its fairest feasibility test; leftovers are handled only after the best subset is known.
- **No affordable positive-scoring section:** The initialized empty choice remains optimal. The result places all arrows in section `0` and returns a valid allocation whose score is zero.
- **Armor-like “at most” reasoning does not apply here:** Bob must allocate exactly all `numArrows`, not merely at most that number. The reconstruction's final addition to `ans[0]` is what turns the minimum-cost winning plan into an exact-total allocation.
- **Ties do not score:** Bob needs strictly more arrows than Alice in a section. This is why the cost is `aliceArrows[i] + 1`, not `aliceArrows[i]`.
- **Several optimal answers:** The strict `s > mx` update preserves the first maximum-scoring mask encountered. The problem explicitly accepts any maximum-scoring allocation, so no tie-breaking rule is required.
- **All arrows left after reconstruction:** Assigning them to index `0` may change the outcome of the zero-point section, but it cannot change the numeric score and cannot invalidate any selected victory.
- **Fixed twelve-section domain:** The exponential algorithm is appropriate because the number of sections is tiny and fixed. It would not scale to an input with hundreds of independently selectable sections; a different constraint structure would then demand dynamic programming, meet-in-the-middle search, or another optimization method.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(2^s s)$. Let `s` be the number of scoring sections. There are `2^s` possible masks. The code skips the empty mask but still examines `2^s - 1` masks, which has the same asymptotic size. For each mask, it scans all `s` sections to compute the required arrows and score. The search therefore takes `O(2^s \cdot s)` time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
