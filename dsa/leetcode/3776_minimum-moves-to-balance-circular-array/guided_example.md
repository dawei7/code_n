# Guided Example: Minimum Moves to Balance Circular Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"balance": [5, 1, -4]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **circular** array `balance` of length `n`, where $\text{balance}[i]$ is the net balance of person `i`.

The objective is to compute `4` from `{"balance": [5, 1, -4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use conservation to detect impossibility

Each move transfers one unit between neighbors. It changes where balance is stored but does not change the total sum.

If `sum(balance) < 0`, making every entry nonnegative is impossible because nonnegative final entries would have a nonnegative total. The source returns `-1` immediately.

The statement guarantees at most one initially negative index. Under that guarantee, a nonnegative total is also sufficient: all other indices are nonnegative supplies whose total can fill the single deficit.

If `min(balance) >= 0`, the array already satisfies the goal and zero moves are optimal.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"balance": [5, 1, -4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Reduce the problem to supplying one deficit

Otherwise, `mn = min(balance)` is the unique negative value, `i = balance.index(mn)` is its index, and

`need = -mn`

is the number of units it must receive.

There is no reason to move surplus between nonnegative destinations. Every required unit ultimately travels from some nonnegative index to `i`. Moving one unit across one edge costs one move, so a unit originating at circular distance $d$ costs at least $d$ moves. Sending it along a shortest path attains that cost.

The optimization is therefore to consume available units in nondecreasing shortest circular distance from the deficit.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Expand simultaneously to the left and right

For distance counter `j=1,2,...,n-1`, the source reads

`a = balance[(i-j+n) % n]`

and

`b = balance[(i+j-n) % n]`.

Modulo `n` wraps indices around the circle. These expressions are the positions `j` steps counterclockwise and clockwise from `i`.

From side `a`, the source takes

`c1 = min(a, need)`,

decreases `need` by `c1`, and adds `c1*j` to `ans`. It repeats the same operation for `b`.

Because all non-deficit positions are nonnegative, `min(supply, need)` never transfers a negative amount. It consumes no more than the donor owns and no more than the deficit still requires.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"balance": [5, 1, -4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Sort donors by distance:** It is correct but unnecessary because the circle can be enumerated directly in increasing distance.
- **Breadth-first unit movement:** Simulating every individual transfer can take time proportional to the numeric balances rather than array length.
- **Use only one direction:** The closest supply may lie across the other circular edge, producing a nonminimal cost.
- **Use linear distance `abs(i-j)`:** Circular distance is `min(abs(i-j), n-abs(i-j))`.
- **Negative total:** Conservation makes the goal impossible, so return `-1`.
- **No negative entry:** The answer is zero even when the total is positive.
- **Exactly sufficient total:** All positive supply may be consumed, but every final value can still reach zero.
- **More supply than needed:** The final donor is used only partially through `min(supply, need)`.
- **Two equidistant donors:** Either order has the same cost; the source processes left then right.
- **Even-length opposite node:** It appears from both directions, but feasibility makes `need` zero after its first necessary use.
- **Later modular revisits:** They contribute zero because all distinct supplies have already sufficed.
- **Single-element array:** A negative value has negative total and returns `-1`; a nonnegative value returns zero.
- **At-most-one-negative guarantee:** The greedy single-destination reasoning depends on it. Multiple deficits would require a more general transport argument.
- **Input preservation:** Donor amounts are not decremented in the list; local `need` tracks total demand.
- **Source/manifest mismatch:** This exact solution is linear-time distance expansion, not sorting.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Summing the array, finding its minimum, and locating the negative index each take $O(N)$ time. The distance loop has $N-1$ iterations and constant work per side, so it is also $O(N)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
