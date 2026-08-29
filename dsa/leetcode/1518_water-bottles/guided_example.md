# Guided Example: Water Bottles

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"numBottles": 9, "numExchange": 3}`
- **Required output:** `13`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There are `numBottles` water bottles that are initially full of water. You can exchange `numExchange` empty water bottles from the market with one full water bottle.

The objective is to compute `13` from `{"numBottles": 9, "numExchange": 3}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: What one exchange-and-drink cycle changes

The source begins with `ans = numBottles` because every initially full bottle can certainly be drunk. After those drinks, the same number of empty bottles exists.

Whenever at least `numExchange` bottles are available for exchange, spending that many empties obtains one full bottle. Drinking that new bottle adds one to the answer and returns one empty bottle.

The net number of available bottles therefore decreases by

$$
numExchange - 1.
$$

That is exactly why each loop executes

`numBottles -= numExchange - 1`

and `ans += 1`.

Although the variable is still named `numBottles`, after initialization it is best understood as the current number of bottles available in the exchange cycle, effectively empties after all currently counted full bottles have been drunk.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"numBottles": 9, "numExchange": 3}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the loop condition is correct

An exchange is possible exactly when the current bottle count is at least `numExchange`. If fewer remain, no combination of waiting or rearranging can create another full bottle, because no new empty bottle appears without first obtaining and drinking a full one.

The loop stops at that point, and `ans` already includes every full bottle ever drunk.

The guarantee `numExchange >= 2` ensures each iteration reduces `numBottles` by at least one. The process must terminate. If the exchange cost were one, every empty could be exchanged for a full bottle that produces another empty, creating an infinite process.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: A trace for nine bottles and exchange cost three

Initially, `ans = 9` and nine empty bottles remain conceptually.

- Exchange three and drink the result: the usable count drops by two to seven, and answer becomes ten.
- Repeat until the counts move from seven to five, then three, then one.
- Four extra bottles have been drunk, so the result is thirteen.

This per-bottle loop differs from batching all possible simultaneous exchanges, but both simulate the same conservation rule.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `13` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"numBottles": 9, "numExchange": 3}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `13` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Closed-form calculation:** Return `B + (B - 1) // (E - 1)`. This achieves the manifest's true $O(1)$ time and $O(1)$ space.
- **Batch exchanges:** Compute quotient and remainder of current empties to process many exchanges at once. It takes logarithmic-like rounds and is easy to simulate explicitly.
- **Drink one full bottle at a time:** It is correct but performs more state updates than the net-change loop.
- **Fewer bottles than exchange cost:** The loop never runs, and the answer is the initial bottle count.
- **Exact exchange threshold:** One exchange produces exactly one additional drink and leaves one empty.
- **Exchange cost two:** Every extra drink reduces the pool by one, producing the most loop iterations.
- **One initial bottle:** No exchange is possible under the valid minimum cost two.
- **Exchange cost one:** It would imply infinitely many drinks, which is why the contract excludes it.
- **Unused final empties:** They cannot contribute to another exchange and correctly add no drinks.
- **At most maximum consumption:** There is no strategic reason to skip an available exchange.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(B/(E-1)$. Let $B$ be the initial full-bottle count and $E$ the exchange requirement. Every iteration decreases the current count by $E-1$. The number of iterations is
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
