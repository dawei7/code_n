# Guided Example: Similar RGB Color

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"color": "#09f166"}`
- **Required output:** `"#11ee66"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

The red-green-blue color `"#AABBCC"` can be written as `"#ABC"` in shorthand.

The objective is to compute `"#11ee66"` from `{"color": "#09f166"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Optimize the three color channels independently

The similarity is the negative sum of three squared channel differences:

$$
-(R-R')^2-(G-G')^2-(B-B')^2.
$$

The chosen red byte affects only the first term, the green byte only the second, and the blue byte only the third. There is no constraint coupling their hexadecimal digits.

Maximizing the total similarity is therefore equivalent to minimizing each channel's squared difference independently and concatenating the three best channel choices.

This removes any need to try all $16^3$ shorthand colors.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"color": "#09f166"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Characterize every shorthand-expressible channel

A shorthand digit `x` expands to a two-digit hexadecimal channel `xx`.

If hexadecimal digit `x` has numeric value from zero through 15, then:

$$
(xx)_{16}=16x+x=17x.
$$

Thus the only allowed numeric channel values are:

`0, 17, 34, ..., 255`.

For an original channel value `q`, the best shorthand channel is the nearest multiple of 17.

Because squaring preserves the ordering of nonnegative absolute differences, minimizing `(q-17x)^2` is the same as minimizing `abs(q-17x)`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Parse one channel

Helper `f(x)` receives a two-character hexadecimal string such as `"09"` or `"f1"`.

`int(x, 16)` converts it to an integer `q` from zero through 255.

The method then calculates:

`y, z = divmod(q, 17)`.

This means:

$$
q=17y+z,\qquad 0\le z<17.
$$

`17y` is the allowed shorthand value immediately at or below `q`, and `17(y+1)` is the next allowed value above it when that value exists.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"#11ee66"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"color": "#09f166"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"#11ee66"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Try all shorthand colors:** Testing $16^3=4096$ complete colors is still constant under fixed RGB width, but it ignores channel independence.
- **Try 16 values per channel:** Check every `00,11,...,ff` candidate independently. This is simple and also constant-time, with 48 comparisons.
- **Floating-point rounding:** Computing `round(q/17)` is concise, but explicit quotient and remainder make the tie rule and boundary behavior unambiguous.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The input always contains exactly three two-digit channels. Each helper call performs constant-size parsing, division, comparison, and formatting. Total time is $O(1)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
