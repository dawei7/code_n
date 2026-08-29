# Guided Example: Find Closest Person

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"x": 2, "y": 7, "z": 4}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given three integers `x`, `y`, and `z`, representing the positions of three people on a number line:

The objective is to compute `1` from `{"x": 2, "y": 7, "z": 4}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Arrival time is determined only by distance

Person 1 starts at coordinate `x`, Person 2 starts at coordinate `y`, and the stationary Person 3 is at coordinate `z`. The first two people move toward `z` at the same speed.

For motion at constant positive speed `v`, travel time is:

`time = distance / v`.

Both arrival times have the same positive denominator `v`. Dividing two nonnegative distances by the same positive number preserves their order. Therefore:

- the smaller distance means the earlier arrival;
- equal distances mean equal arrival times.

The actual speed never needs to be known. The problem reduces to computing two number-line distances and comparing them.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"x": 2, "y": 7, "z": 4}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Distance on a number line requires an absolute value

The distance between coordinates `p` and `q` is `abs(p - q)`. The absolute value matters because a person may begin on either side of `z`:

- if `p < z`, the movement distance is `z - p`;
- if `p > z`, the movement distance is `p - z`;
- if `p = z`, the movement distance is zero.

All three cases are captured by `abs(p - z)` without branching on direction.

The protected source computes:

`a = abs(x - z)`

`b = abs(y - z)`.

Here `a` is Person 1's distance and `b` is Person 2's distance. These short variable names are not positions or times; they are nonnegative travel distances.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Map the comparison to the required return codes

The return expression is a nested conditional:

`return 0 if a == b else (1 if a < b else 2)`.

It should be read from left to right:

1. If `a == b`, both travel the same distance at the same speed, so return `0`.
2. Otherwise the distances are unequal. If `a < b`, Person 1 is closer, so return `1`.
3. The only remaining possibility is `a > b`, so Person 2 is closer and the source returns `2`.

These cases are mutually exclusive and exhaustive for two integers. Exactly one required result is returned.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"x": 2, "y": 7, "z": 4}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Step-by-step movement simulation:** Moving both people toward `z` until one arrives is intuitive but unnecessary. Absolute distance summarizes the number of equal-speed steps immediately.
- **Compare `x - z` with `y - z` without absolute values:** Signed differences encode direction as well as distance and can rank a farther person as “smaller” merely for being left of `z`.
- **Compare x directly with y:** Their closeness to each other says nothing about their separate distances to `z`.
- **Square the distances:** Comparing `(x-z)^2` and `(y-z)^2` would give the same ordering for nonnegative distances, but absolute values are simpler and avoid needless multiplication.
- **Compute explicit arrival times:** Dividing both distances by a shared speed cannot change their order. The speed is not provided because it cancels.
- **People on opposite sides of z:** Direction differs, but `abs` produces comparable route lengths.
- **People on the same side of z:** The nearer coordinate to `z` has the smaller absolute difference, exactly as required.
- **Person 1 already at z:** `a = 0`. The source returns one unless `b` is also zero.
- **Person 2 already at z:** `b = 0`. The source returns two unless `a` is also zero.
- **Both people at z:** Both distances are zero, so the equality branch returns zero.
- **x equals y:** Their distances to every `z` are identical, so the answer is always zero.
- **Symmetric positions around z:** If `x = z-d` and `y = z+d`, both distances are `d` and the result is zero.
- **Nested conditional readability:** Expanding the expression into `if`, `elif`, and `else` branches would be equivalent. The protected one-line return evaluates equality first and then resolves the only two unequal cases.
- **Equal speed assumption:** If speeds differed, distance comparison alone would be insufficient; one would need compare `distance/speed`. The problem explicitly guarantees equal speed.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The method performs two subtractions, two absolute-value operations, at most two comparisons, and one return. The number of operations does not depend on the coordinate magnitudes or on any input collection size. Time complexity is `O(1)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
