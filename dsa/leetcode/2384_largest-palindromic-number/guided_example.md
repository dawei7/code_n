# Guided Example: Largest Palindromic Number

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"num": "444947137"}`
- **Required output:** `"7449447"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a string `num` consisting of digits only.

The objective is to compute `"7449447"` from `{"num": "444947137"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: A palindrome consumes digits in pairs plus at most one center

Every position left of a palindrome's center must match a symmetric position on the right. Therefore, digit `d` can contribute `cnt[d] // 2` pairs. If any digit has an odd count, one leftover occurrence may occupy the center.

To maximize the resulting integer, the most significant left-side digits should be as large as possible. The palindrome should also use every available pair that can be placed without creating an invalid leading zero: adding a pair increases length, and a longer positive integer with a nonzero first digit is larger than a shorter one.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"num": "444947137"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Choose the largest possible center

The first loop scans digits from nine down to zero and selects the first digit whose count is odd. It stores that character in `ans` and decrements its count by one.

Choosing a center from an odd count does not reduce how many pairs that digit can supply:

$$
\left\lfloor\frac{c-1}{2}\right\rfloor=\left\lfloor\frac{c}{2}\right\rfloor
$$

when $c$ is odd. Thus, all choices of an odd-count center leave the same multiset of usable pairs. The largest odd digit is therefore always the best center.

Only one center is possible. Other leftover single digits cannot be included without breaking symmetry, and the problem permits unused digits.

If every count is even, `ans` remains the empty string. The eventual palindrome then has even length unless zero cleanup reduces it.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The first loop scans digits from nine down to zero and selec... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Build from the inside outward

The second loop scans digits from zero upward. For digit `v`, it halves the remaining count and creates a string `s` containing that many copies. It wraps the current palindrome:



Because low digits are processed first, they occupy inner layers. Later, higher digits wrap around them and become more significant. After the final iteration, the left half is in descending digit order and the right half mirrors it.

For example, suppose pairs are available for digits `4` and `7` and the center is `9`. Digit four first creates `"494"`. Digit seven then wraps it to `"7449447"`. Placing sevens outside fours makes the number larger than the reverse arrangement.

The code uses all pairs for a digit at once. Repeating the same digit in one block preserves the palindrome and places equal digits contiguously at the appropriate significance level.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"7449447"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"num": "444947137"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"7449447"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Build a left-half list then mirror it:** Appen:** - **Build a left-half list then mirror it:** Append pair digits from nine down to zero, choose a center, and concatenate left, center, and reversed left. This avoids repeated wrapping and is often easier to reason about.
- **Sort all input digits:** Sorting costs $O(n\log n)$ and still requires pair counting; the ten-value Counter is more efficient.
- **All digits zero:** Outer-zero removal empties the temporary string, and the fallback returns `"0"`.
- **Only one nonzero digit:** It becomes the center if its count is odd; unused zeros cannot surround it as leading digits.
- **Even counts only:** There is no center, and the palindrome is formed entirely from pairs.
- **Several odd counts:** Only the largest leftover digit is used as center; the rest may contribute their available pairs.
- **Zero pair plus nonzero pair:** The nonzero pair wraps outside, so zeros remain valid internal digits.
- **Unused digits:** Leftover singles beyond the center are intentionally discarded, as permitted.
- **Leading-zero cleanup:** `strip('0')` is safe because symmetry makes every stripped trailing zero the mirror of a forbidden leading zero.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the length of `num`. Building the Counter takes $O(n)$ time and at most ten key entries. The two digit loops have fixed length ten.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
