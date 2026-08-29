# Guided Example: Change Minimum Characters to Satisfy One of Three Conditions

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"a": "aba", "b": "caa"}`
- **Required output:** `2`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given two strings `a` and `b` that consist of lowercase letters. In one operation, you can change any character in `a` or `b` to **any lowercase letter**.

The objective is to compute `2` from `{"a": "aba", "b": "caa"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Reduce strings to 26 letter frequencies

Only the number of occurrences of each lowercase letter matters. Operations may change any character to any lowercase letter, so original positions have no effect on the three target conditions.

`cnt1[i]` counts letter index `i` in `a`, and `cnt2[i]` counts it in `b`, where zero represents `'a'` and 25 represents `'z'`.

The source fills these fixed arrays in one pass over each string.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"a": "aba", "b": "caa"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Condition three: make both strings one common letter

Choose a target letter at alphabet index `i`. Existing occurrences of that letter in both strings can remain. Every other character must change.

The operation count is

$$
m+n-\texttt{cnt1}[i]-\texttt{cnt2}[i].
$$

The loop over `zip(cnt1,cnt2)` evaluates this for all 26 possible common letters and updates `ans`.

`ans` begins at `m+n`, a valid loose upper bound obtained by changing every character.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Conditions one and two become alphabet-boundary choices

To make every letter in the first string strictly less than every letter in the second, choose a dividing index `i` from one through 25:

- First-string letters must lie in indices zero through `i-1`.
- Second-string letters must lie in indices `i` through 25.

This creates a strict boundary because the allowed sets do not overlap.

Every first-string occurrence at index `i` or above must change, contributing `sum(cnt1[i:])`. Every second-string occurrence below `i` must change, contributing `sum(cnt2[:i])`.

The helper computes their sum and minimizes `ans`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `2` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"a": "aba", "b": "caa"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `2` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Prefix counts across the alphabet:** Precompute cumulative frequencies so each boundary cost is constant even when alphabet size is treated as a variable.
- **Try all replacement strings:** Exponential and unnecessary because positions are independent once a condition is selected.
- **Both strings already one same letter:** Condition three costs zero.
- **Each string uniform but different letters:** One ordering condition may already hold with zero operations.
- **All `a` greater than all `b`:** The second helper call finds zero.
- **Equal boundary letters:** Strict inequality forbids the same letter on both sides, which the disjoint ranges enforce.
- **Single-character strings:** All conditions and boundary formulas remain valid.
- **Best common letter absent from one string:** That string's every character may need change, while preserved occurrences in the other still reduce cost.
- **Boundary at one:** The lower side may contain only `'a'`.
- **Boundary at 25:** The upper side may contain only `'z'`.
- **Fixed lowercase alphabet:** It makes frequency arrays and slice overhead constant.
- **Nonlocal result:** Both helper directions contribute to the same global minimum.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N=m+n$ be the combined string length. Counting characters costs $O(N)$. All later loops and slice sums operate on arrays of fixed length 26, so they take $O(1)$ with respect to input length. Total time is $O(N)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
