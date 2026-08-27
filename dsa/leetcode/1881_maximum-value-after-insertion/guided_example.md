# Guided Example: Maximum Value after Insertion

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": "99", "x": 9}`
- **Required output:** `"999"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a very large integer `n`, represented as a string,​​​​​​ and an integer digit `x`. The digits in `n` and the digit `x` are in the **inclusive** range `[1, 9]`, and `n` may represent a **negative** number.

The objective is to compute `"999"` from `{"n": "99", "x": 9}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**Maximizing depends on the sign.** Inserting one digit makes every candidate have the same final number of digits, so the first position at which two candidates differ determines which numerical value is larger. For a positive number, the goal is the lexicographically largest digit sequence: place `x` before the first existing digit smaller than `x`. For a negative number, a numerically larger result has a smaller absolute magnitude, so the goal reverses: place `x` before the first magnitude digit larger than `x`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": "99", "x": 9}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

**Handle the minus sign before scanning digits.** Variable `i` begins at zero. If `n[0] == "-"`, the code increments `i` to one so insertion can never occur to the left of the sign. The remaining characters are all digits. For a positive number, scanning naturally begins at zero. This single boundary difference lets the returned slices preserve the sign without treating it as a numeric digit.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | **Handle the minus sign before scanning digits.** Variable `... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

**Positive-number rule.** The loop continues while `int(n[i]) >= x`. Every digit greater than `x` should remain before `x` because moving `x` ahead of it would make the first differing digit smaller and therefore reduce the result. Equal digits can also be passed: inserting before or after an equal digit produces the same complete digit sequence. The first digit below `x` is the first position where inserting `x` improves the most significant available place. The loop stops there, and insertion occurs before that smaller digit.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"999"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": "99", "x": 9}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"999"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Generate every insertion candidate:** Construc:** - **Generate every insertion candidate:** Constructing $O(N)$ strings of length $O(N)$ and comparing them costs $O(N^2)$ time and space traffic. The first-difference rule identifies the winner in one scan.
- **Parse into an integer:** The input can be vastly larger than fixed-width numeric types, and converting plus multiplying by powers of ten is unnecessary. String order contains all information needed.
- **Use character comparisons:** Because digits `'1'` through `'9'` have the same lexicographic and numeric order, comparing characters with `str(x)` could avoid repeated `int` calls. The exact source uses integer comparison explicitly.
- **All digits equal to `x`:** The scan passes every equal digit and appends `x`. Inserting anywhere produces the same final string, so this tie choice is valid.
- **Positive number with every digit smaller than `x`:** The scan stops immediately and inserts `x` at the front, the most significant possible position.
- **Negative number with every digit larger than `x`:** The scan stops just after the minus sign, placing the smaller digit at the front of the magnitude and maximizing the negative value.
- **Insertion beside the sign:** For a negative input, starting at index one permits insertion immediately after `'-'` but never before it, exactly matching the rule.
- **No zero digits:** The contract restricts all digits and `x` to one through nine. If zeros were allowed, the same comparison proof would still work, but representation rules around leading zeros might need separate clarification.
- **Input preservation:** Python strings are immutable. The source returns a newly assembled string and cannot modify `n` in place.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the length of the input string, including a possible minus sign. The scan advances `i` monotonically and inspects at most every digit once, costing $O(N)$ time. Constructing the prefix slice, digit string, suffix slice, and concatenated result also copies $O(N)$ characters. Total time is $O(N)$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
