# Guided Example: Find the Longest Balanced Substring of a Binary String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "01000111"}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a binary string `s` consisting only of zeroes and ones.

The objective is to compute `6` from `{"s": "01000111"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Translate “balanced” into two exact tests

A nonempty balanced substring must have the form

$$
0^q1^q
$$

for some positive integer $q$. In plain language, it contains one consecutive block of zeroes, followed by one consecutive block of ones, and the two block lengths are equal.

That definition has two independent requirements:

1. order: once a one has appeared, no later zero is allowed;
2. count: exactly half the characters must be ones, which then also means exactly half are zeroes.

The helper `check(i, j)` tests these requirements for the candidate substring from index $i$ through index $j$, inclusive.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "01000111"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: How the helper recognizes the required order

The local variable `cnt` counts ones seen in the candidate. The loop visits every position from `i` to `j`.

- If the current character is `'1'`, it increments `cnt`.
- If the character is `'0'` and `cnt` is already positive, the helper immediately returns `false`.

That early return detects exactly the forbidden pattern: a zero occurring after at least one one. If no such position exists, all zeroes in the range precede all ones. The candidate may so far be all zeroes, all ones, or a correctly ordered zero-block followed by a one-block; the count test distinguishes these cases.

After the scan, the substring length is `j - i + 1`. The condition

`cnt * 2 == j - i + 1`

says that ones occupy exactly half of the positions. Because every other character is guaranteed to be zero, the number of zeroes is the same. Combining this equality with the ordering check proves that the candidate is balanced.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Enumerate every possible nonempty candidate of useful length

The outer loop chooses each starting index `i`. The inner loop chooses every ending index `j` strictly greater than `i`. Therefore, the solution checks every substring of length at least two.

A nonempty balanced substring cannot have length one: equal positive counts of zeroes and ones require an even length of at least two. Excluding `j == i` loses no valid nonempty answer.

For each candidate accepted by `check`, the solution updates `ans` with its length. The initial value is zero, which represents the empty balanced substring explicitly allowed by the contract. Thus no separate “not found” branch is needed.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "01000111"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **One-pass run tracking:** Count a zero-run and the immediately following one-run, then maximize `2 * min(zeroes, ones)`. This is the true $O(n)$ optimal method summarized by the manifest.
- **Regular-expression-shaped thinking:** Looking for blocks matching `0+1+` captures order, but run lengths must still be compared and a regex is unnecessary.
- **Equal counts alone:** A range such as `"0110"` has equal counts but is not balanced because a zero follows a one.
- **Correct order but unequal counts:** `"00111"` is not itself balanced, although its prefix `"0011"` is.
- **All zeroes:** No nonempty range contains equal positive counts, so the answer is zero.
- **All ones:** The final equality rejects every nonempty candidate, leaving zero.
- **Alternating characters:** Each `"01"` boundary can contribute length two, but a `"10"` transition prevents a larger balanced block across it.
- **Length one:** Only the empty substring is balanced, and `ans` remains zero.
- **Odd candidate length:** The equality `cnt * 2 == length` automatically rejects it.
- **No substring allocation:** Index-based checking avoids hidden $O(n)$ copies and keeps extra space constant.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n=|s|$. There are $\Theta(n^2)$ pairs $(i,j)$ with $i<j$. A call to `check(i, j)` can inspect $\Theta(n)$ characters in the worst case. The exact implementation consequently has $O(n^3)$ worst-case time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
