# Guided Example: Chalkboard XOR Game

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 1, 2]}`
- **Required output:** `false`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of integers `nums` represents the numbers written on a chalkboard.

The objective is to compute `false` from `{"nums": [1, 1, 2]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reduce the game to two facts

At first glance, this looks like a game that needs recursive search over every possible number Alice or Bob might erase. The decisive information is much smaller:

- the bitwise XOR `S` of all numbers currently on the board;
- whether the number of remaining elements is even or odd.

The exact solution returns

`len(nums) % 2 == 0 or reduce(xor, nums) == 0`.

In words, Alice wins if the initial number of elements is even or if the initial XOR is zero. Understanding why this one-line condition is correct requires carefully respecting the unusual losing rule.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 1, 2]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: An XOR of zero at the start is an immediate win

The statement says that a player who starts a turn while the board's XOR is zero wins. Therefore, if the initial XOR is zero, Alice wins before erasing anything. This includes arrays with nonzero values that cancel under XOR, such as `[1, 2, 3]` because `1 ^ 2 ^ 3 = 0`.

This starting-turn rule is different from the rule for making a move. If a player erases a number and that erasure makes the remaining XOR zero, the player who made the move loses immediately. Thus, when the current XOR is nonzero, a “safe” move is one whose resulting XOR is still nonzero.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The statement says that a player who starts a turn while the... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How removing one number changes the XOR

Let the current board contain `x_1, x_2, ..., x_k`, and let

$$
S=x_1\oplus x_2\oplus\cdots\oplus x_k.
$$

If the player erases `x_i`, the XOR of the remaining values is

$$
S\oplus x_i.
$$

This follows because XORing `S` with `x_i` cancels the erased value: `x_i \oplus x_i = 0`, and zero does not affect XOR.

The move loses immediately exactly when

$$
S\oplus x_i=0.
$$

When `S` is nonzero, this equation is equivalent to `x_i = S`. Consequently, a move is unsafe precisely when the erased value equals the current total XOR.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `false` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 1, 2]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `false` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Minimax over erased subsets:** A recursive gam:** - **Minimax over erased subsets:** A recursive game search can model the rules directly, but there are up to `2^n` subsets of remaining elements. With `n` as large as 1000, even memoization by subset is impossible. The XOR/parity theorem gives the same optimal-play result in linear time.
- **- **Searching for Alice's actual first move:** Whe:** - **Searching for Alice's actual first move:** When the length is even and XOR is nonzero, the proof guarantees a safe value exists. The function only needs a Boolean answer, so locating that value would add work without changing the result.
- **- **Using ordinary sum or parity of values:** Addi:** - **Using ordinary sum or parity of values:** Addition does not have XOR's cancellation property. Only the bitwise XOR aggregate determines whether an erasure immediately loses.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the number of elements in `nums`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
