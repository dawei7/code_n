# Guided Example: Convert Integer to the Sum of Two No-Zero Integers

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 10000}`
- **Required output:** `[1, 9999]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

**No-Zero integer** is a positive integer that **does not contain any `0`** in its decimal representation.

The objective is to compute `[1, 9999]` from `{"n": 10000}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Generating candidates

`count(1)` yields $1,2,3,\ldots$ without a built-in stopping point. For each positive `a`, the code computes `b`.

The problem guarantees at least one valid answer. A valid pair has both numbers positive, so it must be found for some `a` from one through `n - 1`. Under that guarantee, the infinite iterator always returns before reaching candidates with nonpositive `b`.

Without the guarantee, using `count` would be unsafe. Once `a > n`, `b` becomes negative, and a negative decimal string without zero could accidentally pass even though positivity is required. A defensive implementation would use `range(1, n)` and handle failure after the loop.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 10000}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Checking both decimal representations at once

`f"{a}{b}"` converts both integers to decimal text and concatenates them. The condition

`"0" not in f"{a}{b}"`

is true exactly when neither representation contains a zero. If either number has a zero digit, that character appears somewhere in the combined string.

No separator is needed. The property being tested is simply whether zero occurs anywhere; joining the texts cannot remove or create a zero digit.

This equivalence can be stated in both directions. If `a` contains a zero, its characters appear unchanged at the beginning of the formatted result, so the combined membership test fails. If `b` contains a zero, its characters appear unchanged at the end and the same test fails. Conversely, if the combined text contains zero, that character must have come from one of the two decimal representations because formatting inserts no other characters between positive integers. Therefore, passing the one combined test proves that both numbers are No-Zero integers; it is not a shortcut that weakens either individual requirement.

For `n = 11`:

- `a = 1` gives `b = 10`, and `"110"` contains zero, so it is rejected;
- `a = 2` gives `b = 9`, and `"29"` contains no zero, so `[2, 9]` is returned.

The first valid pair is returned immediately. It does not need to minimize either number because any valid answer is accepted.

Increasing enumeration also makes termination easy to reason about under the promise. A valid pair `[a, b]` has some positive first component. The counter visits every positive integer in order without skipping that component. Earlier rejected candidates do not affect later ones because each `b` is recomputed directly from `n - a`. As soon as the promised component is reached, the exact sum relation and zero test both hold, so control leaves the otherwise unbounded iterator.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `f"{a}{b}"` converts both integers to decimal text and conca... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the returned pair is valid

`a` begins at one, and the solution guarantee ensures return before `a` reaches `n`, so both `a` and `b = n - a` are positive. Their sum is algebraically

$$
a+(n-a)=n.
$$

The string condition verifies that neither decimal representation includes digit zero. Therefore, every returned list satisfies all three requirements.

Conversely, because enumeration tries every positive `a < n` in order and derives its matching `b`, it eventually reaches the first component of at least one guaranteed valid pair. That iteration passes the digit test and terminates.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 9999]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 10000}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 9999]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Bounded enumeration:** `for a in range(1, n)` :** - **Bounded enumeration:** `for a in range(1, n)` enforces positivity of `b` even without the solution guarantee and is safer than an infinite counter.
- **Arithmetic digit test:** Repeatedly inspect `x % 10` and divide by ten. It avoids string allocation but still takes $O(\log n)$ time per candidate.
- **Construct digits without zero:** A direct carry-aware construction can avoid testing many candidates, but it is more complex than needed for `n <= 10000`.
- **`n = 2`:** The first candidate gives `[1,1]`, which is valid.
- **A candidate containing zero:** It is rejected even if only one of the two numbers has zero.
- **Concatenation boundary:** No separator is needed because the test asks only whether any zero exists.
- **Multiple answers:** Increasing enumeration returns the one with the smallest `a`; this is incidental, not a requirement.
- **Guaranteed existence:** The lack of loop bounds and fallback return relies on it. Removing that promise requires a bounded loop.
- **Negative string outside intended range:** A minus sign is not zero, so unbounded enumeration could accept a negative `b` if no valid positive pair existed.
- **Leading zeros:** Ordinary integer formatting never creates leading zeroes, so only actual digits of the number are examined.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n\log n)$. In the worst case, the method tests $O(n)$ candidate values before finding a pair. Each candidate has $O(\log n)$ decimal digits across `a` and `b`. Formatting, concatenating, and scanning the combined string therefore take $O(\log n)$ time.
- **Auxiliary Space Complexity:** $O(\log n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
