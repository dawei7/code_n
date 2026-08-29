# Guided Example: Bag of Tokens

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"tokens": [100], "power": 50}`
- **Required output:** `0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You start with an initial **power** of `power`, an initial **score** of `0`, and a bag of tokens given as an integer array `tokens`, where each $\text{tokens}[i]$ denotes the value of token*_i*.

The objective is to compute `0` from `{"tokens": [100], "power": 50}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Two resources move in opposite directions

Playing a token face-up spends power and gains score. Playing one face-down spends score and gains power. The objective is the largest score reached at any time; not every token must be played.

After sorting, the smallest remaining token is the cheapest possible way to buy one score, and the largest remaining token is the most power obtainable by selling one score. This leads to a two-pointer greedy strategy.

Pointer `i` identifies the smallest unplayed token and `j` the largest. Tokens outside `[i, j]` have already been consumed.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"tokens": [100], "power": 50}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: When enough power is available

If `power >= tokens[i]`, the solution plays the smallest token face-up:

- subtract `tokens[i]` from power;
- add one to `score`;
- move `i` right.

Any face-up move always gains exactly one score. Choosing a larger affordable token would gain the same score while leaving less power for later moves. Therefore, the smallest remaining token is never worse and can only be better.

After gaining score, the code updates `ans = max(ans, score)`. This records the best score ever achieved, even if a later face-down move temporarily reduces the current score.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: When the cheapest token is unaffordable

Because tokens are sorted, if the smallest remaining token cannot be bought, no other remaining token can be bought face-up.

If `score > 0`, the only way to make progress is to spend one score on a face-down token. Every such move loses exactly one score, so the best choice is the largest remaining token `tokens[j]` because it gives the most power for the same cost.

The code adds that value to power, subtracts one from score, and moves `j` left.

Selling a smaller token would leave no more score and strictly less or equal power, so it could not enable any sequence that selling the largest token cannot also enable.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"tokens": [100], "power": 50}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Try every play sequence:** Each token has multiple choices, producing exponential search. Sorting exposes exchange-dominant choices.
- **Always play face-up only:** This misses beneficial score-for-power trades that can unlock several later purchases.
- **Sell the smallest token:** It sacrifices the same one score but gains less power than selling the largest remaining token.
- **Return final score:** A late trade can make final score smaller than an earlier maximum, so `ans` is necessary.
- **Empty token list:** `j = -1`, the loop never runs, and zero is returned.
- **Zero-valued tokens:** They are bought face-up for no power and increase score, so sorting places them in the best possible position.
- **One remaining token:** If affordable, buy it. If unaffordable but score is positive, the code may sell it, but `ans` preserves the previous maximum.
- **Already enough power for all tokens:** Every token is bought from smallest to largest and the answer is `n`.
- **Input mutation:** `tokens.sort()` changes token order. Use a sorted copy if the caller needs the original order.
- **Equal token values:** Their identities do not matter; every token is still consumed at most once.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n log n)$. Let `n` be the number of tokens.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
