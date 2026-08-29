# Guided Example: Bulb Switcher II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 1, "presses": 1}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

There is a room with `n` bulbs labeled from `1` to `n` that all are turned on initially, and **four buttons** on the wall. Each of the four buttons has a different functionality where:

The objective is to compute `2` from `{"n": 1, "presses": 1}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Only the parity of each button count matters

Pressing a button flips a fixed set of bulbs. Pressing the same button twice returns every affected bulb to its previous state. Therefore, for each of the four buttons, the final effect depends only on whether it was pressed an odd or even number of times.

The order of button presses also does not matter. Flipping bulb states is XOR, and XOR operations commute.

Every possibly long sequence can therefore be summarized by a four-bit `mask`:

- bit zero says whether button one was pressed an odd number of times;
- bit one does the same for button two;
- bit two for button three;
- bit three for button four.

There are only `2 ** 4 = 16` parity masks to examine.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 1, "presses": 1}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Not every parity mask is reachable with exactly `presses`

Let `cnt = mask.bit_count()`, the number of buttons that must be pressed an odd number of times.

At least `cnt` presses are required: press each odd-parity button once. Any additional presses must preserve all four parities, so they must be added in pairs. Pressing any one button twice supplies such a pair.

Thus a mask is reachable exactly when:

- `cnt <= presses`;
- `cnt` and `presses` have the same parity.

The code checks `cnt % 2 == presses % 2`. If both conditions hold, the difference `presses - cnt` is a nonnegative even number and can be filled with canceling pairs.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why six bulbs are enough

The four button patterns depend on:

- whether a label is even or odd, which repeats every two;
- whether it is congruent to one modulo three, which repeats every three;
- the all-bulbs operation, which is constant.

The combined pattern repeats every least common multiple of two and three, which is six. Bulb `j` and bulb `j + 6` are affected identically by every button.

Therefore, for `n > 6`, the first six bulb effects determine all later bulbs. Replacing `n` with `min(n, 6)` loses no information about distinct statuses.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 1, "presses": 1}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Closed-form case analysis:** The first three bulbs actually determine all states, allowing a small formula based on capped `n` and whether presses is zero, one, two, or at least three. It is faster only by a constant and less directly connected to the operations.
- **Breadth-first simulation by press count:** Repeatedly apply four buttons to every current state. Capping to six bulbs keeps the state universe small, but parity enumeration reaches the answer more directly.
- **Enumerate all operation sequences:** There are `4 ** presses` sequences, which is impossible for large `presses` and repeats many equivalent parities.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The algorithm examines exactly 16 masks. For each, it performs constant-time tests and at most four XOR operations. Its running time is `O(1)`, independent of `n` and `presses`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
