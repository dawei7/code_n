# Guided Example: Distribute Candies to People

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"candies": 7, "num_people": 4}`
- **Required output:** `[1, 2, 3, 1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

We distribute some number of `candies`, to a row of **$n = \text{num}_{people}$** people in the following way:

The objective is to compute `[1, 2, 3, 1]` from `{"candies": 7, "num_people": 4}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Simulate gifts in their natural order

Gift number `i + 1` is intended for person `i % num_people` when turns are zero-indexed. The modulo operation wraps from the last person back to the first without needing a separate round counter.

`ans` starts with one zero per person, and `i` starts at zero. During each loop, the current person receives `min(candies, i + 1)`. If enough candies remain, this is the full scheduled gift. Otherwise it is every remaining candy, which implements the special final partial gift.

The same amount is subtracted from `candies`, then `i` advances. Because at least one candy is removed whenever the loop runs, the remaining amount strictly decreases and the loop terminates at zero.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"candies": 7, "num_people": 4}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why modulo assigns the right person

For turns zero through `num_people - 1`, the remainder equals the turn index, so people receive gifts one through `num_people` in order. On the next turn, the remainder returns to zero and the scheduled amount is `num_people + 1`. Every later block behaves the same way.

Thus the expression simultaneously represents row position and repeated rounds. A person may receive several gifts, and `+=` accumulates them in that person’s final total.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For turns zero through `num_people - 1`, the remainder equal... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Handle the last gift without a special branch

Suppose the next scheduled amount is seven but only three candies remain. `min` returns three, adds all three to the correct person, and subtraction makes `candies` zero. The loop then ends. No following person receives anything, exactly matching the statement.

Calling `min` twice produces the same amount because `candies` is not changed between the addition and subtraction. Storing it in a local variable would avoid repeated evaluation but would not change behavior.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 2, 3, 1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"candies": 7, "num_people": 4}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 2, 3, 1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Closed-form complete rounds:** Solve the trian:** - **Closed-form complete rounds:** Solve the triangular-number inequality to find how many gifts are fully paid, then use arithmetic-series formulas for each person and distribute the remaining candies. This can achieve the manifest’s $O(P)$ time.
- **Binary-search the number of full gifts:** Find the greatest $T$ with $T(T+1)/2 \le C$, compute per-person progressions, and place the remainder. This avoids floating-point square-root concerns.
- **Round-by-round nested loops:** Iterate people inside rounds and stop on exhaustion. It is equivalent but requires more bookkeeping than a single turn index with modulo.
- **Fewer candies than people:** The first few people receive increasing gifts until a partial gift consumes the remainder; later entries stay zero.
- **Exactly a triangular number:** The final full scheduled gift consumes the last candies, and no partial gift occurs.
- **One person:** Every gift wraps to index zero, so the sole answer entry becomes the entire original candy count.
- **Partial final gift:** `min` ensures it never exceeds the scheduled amount or remaining supply.
- **Large candy count:** The simulation is far smaller than $C$ iterations because gifts increase, but it is still not strictly $O(P)$.
- **Answer sum:** Each subtraction has an equal addition to one slot, preserving the total until the remainder reaches zero.
- **Positive inputs:** Both candy count and people count are at least one, so modulo is valid and the loop initially runs.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(P+\sqrt{C})$. Let $C$ be the initial candy count and $P$ the number of people. If $T$ full or partial gifts are made, the loop takes $O(T)$ time. Scheduled full gifts grow as one, two, three, and so on, whose first $T$ terms total $T(T+1)/2$. Therefore $T = O(\sqrt{C})$, and the exact protected simulation takes $O(\sqrt{C})$ time.
- **Auxiliary Space Complexity:** $O(P)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
