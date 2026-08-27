# Guided Example: Implement Rand10() Using Rand7()

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"rand7_values": [1, 1], "draws": 3}`
- **Required output:** `[1, 1, 1]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given the **API** `rand7()` that generates a uniform random integer in the range `[1, 7]`, write a function `rand10()` that generates a uniform random integer in the range `[1, 10]`. You can only call the API `rand7()`, and you shouldn't call any other API. Please **do not** use a language's built-in random API.

The objective is to compute `[1, 1, 1]` from `{"rand7_values": [1, 1], "draws": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Create 49 equiprobable cells

The first call is converted from `1..7` to `0..6`:

`i = rand7() - 1`.

The second call remains `j` in `1..7`. The expression

$$
x=7i+j
$$

maps each ordered pair uniquely to an integer in `1..49`.

For `i = 0`, results are `1..7`; for `i = 1`, they are `8..14`; and so on through `43..49` for `i = 6`. Because the two `rand7()` calls are independent and uniform, every pair has probability $1/49$, and therefore every `x` is equally likely.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"rand7_values": [1, 1], "draws": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why only 1 through 40 are accepted

Ten output values need equal-sized groups. Forty is the largest multiple of 10 not exceeding 49. Accepting `x <= 40` gives exactly 40 equiprobable cells, which can be divided into ten groups of four.

Values `41..49` cannot be distributed equally among ten outputs. Returning something for them would make some outputs more likely than others, so the loop rejects those nine cells and draws a fresh independent pair.

Conditioning on acceptance preserves equality: each accepted cell originally had the same probability, so after ignoring rejected trials each still has probability $1/40$ within the accepted trial.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Ten output values need equal-sized groups.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Map accepted cells to 1 through 10

The code returns

`x % 10 + 1`.

Across `x = 1..40`, each remainder from zero through nine occurs exactly four times. Remainder zero comes from `10,20,30,40` and maps to output one. Remainder one comes from `1,11,21,31` and maps to output two. Continuing this pattern, every output from 1 through 10 receives four cells and therefore probability $4/40=1/10$.

The mapping is rotated compared with the common formula `(x - 1) % 10 + 1`, but rotation does not affect uniformity.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 1, 1]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"rand7_values": [1, 1], "draws": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 1, 1]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Modulo a single `rand7` result:** Seven source:** - **Modulo a single `rand7` result:** Seven source outcomes cannot produce ten values at all.
- **Use two draws and take modulo 10 without rejection:** Forty-nine is not divisible by ten, so nine outputs would create uneven remainder frequencies and bias the result.
- **Reuse rejected entropy:** Values `41..49` form nine uniform states that can be combined with another `rand7()` call, then further leftovers can be reused. This lowers the expected call count to about 2.193, but the exact source uses simpler two-draw rejection.
- **Built-in random API:** Forbidden by the contract; all entropy must come from `rand7()`.
- **Long rejection streak:** Valid and possible, so worst-case time is not finite even though expected time is constant.
- **Deterministic adapter stream:** It must eventually enter `1..40` pairs, as the local contract states.
- **Endpoint `x = 40`:** Accepted because it completes the fourth cell for one output class.
- **Endpoint `x = 41`:** Rejected because accepting any of `41..49` would make equal ten-way grouping impossible.
- **Independence assumption:** Correlated `rand7()` results would invalidate the 49-cell uniformity proof; the provided API guarantees independent uniform draws.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. For one native `rand10()` call, expected time is $O(1)$ because the expected attempt count is $49/40$. The worst-case running time is unbounded: random draws may reject any finite number of times, although the probability of infinite rejection is zero. Auxiliary space is $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
