# Guided Example: Binary Watch

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"turnedOn": 0}`
- **Required output:** `["0:00"]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A binary watch has 4 LEDs on the top to represent the hours (0-11), and 6 LEDs on the bottom to represent the minutes (0-59). Each LED represents a zero or one, with the least significant bit on the right.

The objective is to compute `["0:00"]` from `{"turnedOn": 0}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Enumerate the complete legal watch domain

The watch does not describe an unbounded search problem. A displayed hour can only be `0` through `11`, and a displayed minute can only be `0` through `59`. There are exactly

$$
12\cdot60=720
$$

legal time values.

The exact solution checks every one of those 720 pairs. For each hour `i` and minute `j`, it counts the lit bits in their binary representations. If the combined count equals `turnedOn`, it formats and includes the time.

Because the domain size is fixed by the physical watch rather than by a growing input, exhaustive enumeration is both simple and optimal for this contract.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"turnedOn": 0}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why binary one-bits correspond to lit LEDs

The four hour LEDs represent binary place values, and the six minute LEDs do the same. A bit equal to one means its LED is on. Therefore the number of lit hour LEDs is the population count—the number of one bits—of the hour value. The minute count is calculated identically.

For example, hour `4` is binary `0100`, so one hour LED is on. Minute `51` is binary `110011`, so four minute LEDs are on. Time `4:51` uses five lit LEDs in total.

Leading zero bits do not need to be written by `bin`. Omitting them does not change the one-bit count because every omitted bit is zero.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The four hour LEDs represent binary place values, and the si... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How the exact one-bit expression works

The filter is



`bin(i)` and `bin(j)` produce strings such as `"0b100"` and `"0b110011"`. Concatenating them joins the two representations. Counting character `'1'` in the combined string equals the sum of the separate one-bit counts.

The `0b` prefixes contain no digit `1`, so they do not affect the count. Mathematically,

$$
\operatorname{ones}(i)+\operatorname{ones}(j)
=
\operatorname{count}_{\texttt{'1'}}(\texttt{bin}(i)+\texttt{bin}(j)).
$$

Calling `i.bit_count() + j.bit_count()` would express the same calculation without strings, but the exact source’s expression is correct over these bounded values.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `["0:00"]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"turnedOn": 0}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `["0:00"]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate all 1024 LED masks:** Split each ten:** - **Enumerate all 1024 LED masks:** Split each ten-bit mask into four hour bits and six minute bits, reject hour values at least 12 or minute values at least 60, and keep masks with the requested population count. This is also constant time but requires explicit validity checks.
- **- **Generate combinations of lit LEDs:** Choose ex:** - **Generate combinations of lit LEDs:** Choose exactly `turnedOn` positions among ten LEDs, convert them to hour/minute values, and reject invalid displays. It may examine fewer states for some counts but is more complicated than 720 direct checks.
- **- **Use `int.bit_count`:** `i.bit_count() + j.bit_:** - **Use `int.bit_count`:** `i.bit_count() + j.bit_count()` avoids binary strings and states the population-count operation directly. It is an equivalent implementation detail.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The nested loops always examine exactly 720 pairs. Binary representations contain at most four hour bits and six minute bits, so their conversion and counting take bounded constant time. Runtime is therefore $O(1)$ with respect to `turnedOn`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
