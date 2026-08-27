# Guided Example: Broken Calculator

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"startValue": 2, "target": 3}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a broken calculator that has the integer `startValue` on its display initially. In one operation, you can:

The objective is to compute `2` from `{"startValue": 2, "target": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reverse the problem so that multiplication becomes division

Working forward from `startValue` gives two choices: double the display or subtract one. A locally attractive choice can be misleading because an optimal route may deliberately overshoot the target and then subtract.

Working backward from `target` makes the structure much clearer. The inverse operations are:

- if the current target is even, divide it by two to undo a forward doubling;
- add one to undo a forward subtraction.

The reverse operations have the same cost as their forward counterparts, and reversing an operation sequence preserves its length. Therefore, the minimum number of forward operations equals the minimum number of reverse operations needed to reach `startValue`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"startValue": 2, "target": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Odd targets force the next reverse move

If the current reverse target is odd, it cannot have been produced by doubling an integer: twice any integer is even. Therefore, the final forward operation leading to this odd value must have been subtraction from the next larger even value.

The only useful reverse step is consequently

`target += 1`.

The bit test `target & 1` is nonzero exactly when `target` is odd. Adding one makes it even, allowing a division on a later iteration.

For example, to reason backward from five, the algorithm must first go to six. In forward order, this corresponds to reaching six and then subtracting one to obtain five.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | If the current reverse target is odd, it cannot have been pr... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Even targets should be halved immediately

When the reverse target is even and still greater than `startValue`, halving makes the largest possible useful reduction in one operation:

`target >>= 1`

is integer division by two for these positive values.

Why is adding one first not better? Starting from an even value `y`, additions must occur in pairs before another division is possible: one addition makes `y + 1` odd, and a second makes `y + 2` even. Two additions followed by division reach

`(y + 2) / 2 = y / 2 + 1`

in three operations. Halving immediately reaches `y / 2` in one operation; if the extra one is genuinely useful, one later addition reaches `y / 2 + 1` in a total of two operations. Thus postponing the division cannot improve the route.

More generally, additions before an available halving can be moved after that halving with no worse destination and fewer or equal operations. An optimal reverse path therefore always halves an even target while it remains above the start.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"startValue": 2, "target": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Forward breadth-first search:** It can find a :** - **Forward breadth-first search:** It can find a shortest sequence but explores many display values and needs a safe search bound, making it far less efficient.
- **Forward greedy doubling:** Doubling whenever below the target fails when decrementing first enables an exact or cheaper later doubling, as in five to eight.
- **Recursive reverse solution:** Apply the same odd/even recurrence recursively. It is concise but uses `O(\log T)` call-stack space instead of constant space.
- **Target already equal to start:** The loop is skipped, the difference is zero, and the answer is zero.
- **Target below start:** Only forward decrements are useful; the method returns `startValue - target` directly.
- **Odd target above start:** The increment is mandatory because no integer doubling can produce an odd result.
- **Power-of-two relationship:** Repeated halving reaches the start with no odd corrections when the target is the start multiplied by a power of two.
- **Temporary increase:** Adding one to an odd reverse target may exceed the original target by one, but it enables the forced halving and guarantees progress over the pair of steps.
- **Positive-value guarantee:** Bit shifting and parity reasoning use positive integers throughout; the stated constraints ensure this.
- **Large final difference:** It is counted with one subtraction expression rather than simulated, so a large `startValue - target` does not increase runtime.
- **Bit operations:** `target & 1` and `target >>= 1` are exact integer parity and division operations here; they introduce no rounding.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log T)$. Let `T` be the original target value.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
