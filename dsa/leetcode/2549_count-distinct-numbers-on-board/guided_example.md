# Guided Example: Count Distinct Numbers on Board

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 5}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a positive integer `n`, that is initially placed on a board. Every day, for $10^{9}$ days, you perform the following procedure:

The objective is to compute `4` from `{"n": 5}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: For `n>1`, every number from 2 through `n` eventually appears

Start with `n` on the board. For any current number `x>=3`, choose:

$$
i=x-1.
$$

Then:

$$
x\bmod(x-1)=1,
$$

because $x=1\cdot(x-1)+1$.

Therefore, presence of `x` causes `x-1` to be added on the next day. Beginning from `n`, this creates the descending chain:

$$
n,\ n-1,\ n-2,\ldots,2.
$$

So all `n-1` integers in interval `[2,n]` appear after at most `n-2` days.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 5}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why one never appears

For every integer `x`:

$$
x\bmod1=0,
$$

not one. The procedure can never add `i=1` from any board value.

When `n>1`, the final board therefore contains exactly 2 through `n` and excludes one.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For every integer `x`:

$$
x\bmod1=0,
$$

not one.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why no value above `n` can appear

The rule considers candidate `i` only in range `1<=i<=n`, where `n` is the original input bound. No operation can place a number outside that range.

Combined with the descending-chain inclusion and exclusion of one, this proves the final set exactly.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 5}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Board simulation:** It would eventually stabil:** - **Board simulation:** It would eventually stabilize for `n<=100` but is unnecessary and obscures the invariant.
- **`n=1`:** Initial one remains, so return one.
- **`n=2`:** Only two remains, also giving one.
- **`n>2`:** Final set is exactly `\{2,\ldots,n\}`.
- **Candidate one:** It never satisfies remainder one.
- **Candidate above `n`:** The rule never considers it.
- **Multiple additions per day:** They can accelerate stabilization but not change the final set.
- **Persistence:** Previously placed values are never removed.
- **Billion-day count:** It has no effect after early stabilization.
- **Closed form:** `max(1,n-1)` unifies both input regimes.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The method evaluates one subtraction and one maximum operation, independent of `n` and day count. Time is $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
