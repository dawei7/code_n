# Guided Example: Rotate String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "abcde", "goal": "cdeab"}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two strings `s` and `goal`, return `true` *if and only if* `s` *can become* `goal` *after some number of **shifts** on* `s`.

The objective is to compute `true` from `{"s": "abcde", "goal": "cdeab"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Describe a rotation as choosing a cut

After some number of left shifts, a prefix of `s` moves to the end while the remaining suffix moves to the front.

If:

$$
s = P + Q,
$$

where `P` is the shifted prefix and `Q` is the remaining suffix, the resulting rotation is:

$$
Q + P.
$$

Trying every cut and constructing every `Q + P` would work, but it repeats much of the same string data. Concatenating `s` with itself exposes every cut result inside one doubled string.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "abcde", "goal": "cdeab"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why doubling contains every rotation

Write the doubled string as:

$$
s+s=P+Q+P+Q.
$$

The length-`n` substring beginning immediately after prefix `P` is `Q + P`, exactly the rotation produced by moving `P` to the end.

As the cut moves from before index zero through before index `n - 1`, the corresponding length-`n` windows in `s + s` are all possible rotations.

For example, if `s = "abcde"`, then:

`s + s = "abcdeabcde"`.

The rotation `"cdeab"` begins at index two of the doubled string.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Write the doubled string as:

$$
s+s=P+Q+P+Q.
$$

The length... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why every relevant doubled substring is a rotation

The implication also works in reverse. Let a length-`n` match begin at index `r` within `s+s`, where `0 <= r < n`. Its characters are:

`s[r:] + s[:r]`,

which is the result of `r` left shifts.

A length-`n` pattern can also begin at index `n`, but that window is simply the second copy of `s`, identical to the zero-shift rotation. There is no other possible starting index because a length-`n` match must fit inside the length-`2n` doubled text.

Thus, among equal-length strings, substring membership in `s+s` is equivalent to being a rotation.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "abcde", "goal": "cdeab"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Explicit KMP search:** Search `goal` in `s+s` :** - **Explicit KMP search:** Search `goal` in `s+s` with a longest-prefix-suffix table, guaranteeing $O(n)$ time and using $O(n)$ table space without relying on library search behavior.
- **- **Two-Way string matching:** It can provide line:** - **Two-Way string matching:** It can provide linear worst-case search with constant auxiliary matching state, though implementation is more involved.
- **- **Simulate every shift:** Construct and compare :** - **Simulate every shift:** Construct and compare up to `n` rotations, costing $O(n^2)$ time for immutable strings.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the common length after the initial check. Creating `s+s` writes $2n$ characters, taking $O(n)$ time and $O(n)$ temporary space.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
