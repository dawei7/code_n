# Guided Example: Total Distance Traveled

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"mainTank": 5, "additionalTank": 10}`
- **Required output:** `60`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A truck has two fuel tanks. You are given two integers, `mainTank` representing the fuel present in the main tank in liters and `additionalTank` representing the fuel present in the additional tank in liters.

The objective is to compute `60` from `{"mainTank": 5, "additionalTank": 10}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Simulate consumption one liter at a time

The transfer rule triggers after every fifth liter consumed from the main tank, including liters that were previously transferred into it. The exact implementation models this directly.

`mainTank` is the amount currently available to burn. `additionalTank` is the reserve. `cur` counts total liters burned so far, and `ans` stores distance traveled.

The loop continues while `mainTank` is positive, because every available main-tank liter can propel the truck another ten kilometers.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"mainTank": 5, "additionalTank": 10}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Process one liter

On each iteration:

- increment `cur` by one;
- add ten to `ans`;
- subtract one from `mainTank`.

This represents consuming exactly one liter and traveling the fixed mileage. The order places the transfer check after consumption, matching “whenever five liters get used up.”

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | On each iteration:

- increment `cur` by one;
- add ten to `... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Transfer only at consumption multiples of five

After burning a liter, `cur % 5 == 0` precisely means total consumption has reached 5, 10, 15, and so on.

If the reserve is nonempty at such a moment, the code subtracts one from `additionalTank` and adds one to `mainTank`. That liter can be consumed by a future iteration.

If the reserve is empty, no transfer occurs. A later multiple of five cannot restore reserve fuel, so all remaining driving comes only from whatever is already in the main tank.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `60` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"mainTank": 5, "additionalTank": 10}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `60` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Closed-form transfer count:** Compute the thre:** - **Closed-form transfer count:** Compute the threshold formula and return ten times initial fuel plus transfers; this truly uses $O(1)$ operations.
- **Simulate five-liter chunks:** Can reduce iterations while preserving trigger semantics, but must handle the last partial chunk carefully.
- **Initial main tank below five:** No transfer trigger is reached, so distance is ten times `mainTank`.
- **Reserve empty:** The source constraints make it positive, but with zero reserve no transfer would occur.
- **Exactly five main liters:** One reserve liter is transferred if available, yielding six consumed liters total.
- **Transferred fuel reaches another multiple:** It is counted by `cur` and can trigger another transfer.
- **Large unused reserve:** Reserve fuel that never receives a trigger remains unusable.
- **Immediate trigger timing:** Transfer occurs after the fifth liter is consumed, even if the main tank just became empty.
- **No strategic choices:** Consuming every available liter is always optimal.
- **Manifest mismatch:** The exact code is a per-liter simulation, not a closed-form computation.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(M+T)$. Let $M$ be the initial main-tank fuel, $A$ the reserve, and $T$ the number of successful transfers. The loop runs once for each consumed liter, exactly $M+T$ times. Its time is $O(M+T)$, with:
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
