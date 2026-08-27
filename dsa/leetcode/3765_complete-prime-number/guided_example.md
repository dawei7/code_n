# Guided Example: Complete Prime Number

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"num": 23}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer `num`.

The objective is to compute `true` from `{"num": 23}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Translate decimal pieces into an incremental scan

If `num` has $D$ decimal digits, the required prefixes are the first 1, 2, through $D$ digits, and the required suffixes are the last 1, 2, through $D$ digits. The whole number appears in both families.

The source converts `num` to its decimal string `s` so it can visit the digits in their written order. It does not repeatedly slice and parse every prefix and suffix. Instead, it builds each next value from the previous one, checks it immediately, and stops on the first failure.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"num": 23}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Test primality by searching only through the square root

The nested `is_prime(x)` helper first rejects every `x < 2`. This handles zero and one explicitly because neither is prime.

For `x >= 2`, it evaluates

`all(x % i for i in range(2, int(sqrt(x)) + 1))`.

For each candidate divisor `i`, `x % i` is zero exactly when `i` divides `x`. Zero is false in a Boolean context, while a nonzero remainder is true. Therefore `all(...)` returns true only when every tested divisor leaves a remainder.

Testing stops at $\lfloor\sqrt{x}\rfloor$. If a composite number can be written as $x=ab$ and both factors were greater than $\sqrt{x}$, then their product would be greater than $x$, which is impossible. Consequently every composite `x` has at least one factor no larger than its square root. Finding no divisor in this range is enough to establish primality.

For 2 and 3, the divisor range is empty. Python's `all` of an empty sequence is true, which is correct after the earlier `x < 2` rejection.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The nested `is_prime(x)` helper first rejects every `x < 2`.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Build prefixes from left to right

The prefix accumulator starts at zero. For each character `c` in `s`, the update

`x = x * 10 + int(c)`

shifts the existing decimal digits one place left and appends the new digit. After processing the first $k$ characters, `x` is exactly the integer represented by the first $k$ digits.

For `num = 317`, the accumulator visits 3, then 31, then 317. Each value is passed to `is_prime` as soon as it is complete. If any prefix is nonprime, returning `false` is final: the definition requires every prefix and suffix to be prime, so no later check could repair the failed condition.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"num": 23}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Repeated decimal slicing:** Testing `int(s[:k]:** - **Repeated decimal slicing:** Testing `int(s[:k])` and `int(s[-k:])` is straightforward, but repeatedly reparses digit sequences. The accumulators express the same values incrementally.
- **Sieve of Eratosthenes:** A sieve up to `num` would answer primality queries quickly after preprocessing but uses $O(n)$ time and space, excessive for only a few tested values.
- **Probabilistic or deterministic Miller–Rabin:** This is valuable for much larger integers, but trial division is simple and sufficient for `num <= 10^9`.
- **Check only the whole number:** A prime full number can still contain a composite shorter prefix or suffix; every length is required.
- **Check only prefixes:** Passing prefixes says nothing about the shorter suffixes, and conversely.
- **One-digit input:** The same value is checked in both loops and returns true exactly for 2, 3, 5, or 7.
- **A piece equal to zero or one:** `is_prime` rejects it before attempting division.
- **Even multi-digit piece:** Trial division finds divisor 2 immediately and short-circuits.
- **Perfect square:** Including `int(sqrt(x))` in the range is essential because the square root itself is a divisor.
- **Suffix containing a leading zero:** It is interpreted numerically, so `"03"` becomes 3.
- **Early failure:** Returning immediately is safe because the requirement is a conjunction of all prefix and suffix conditions.
- **Full-number duplicate test:** The source tests it as both a prefix and suffix. Skipping the second test would be a possible micro-optimization, not the current behavior.
- **Floating square root:** The constrained values are small enough for `sqrt` and integer conversion to identify the required trial bound reliably.
- **Input preservation:** Only local strings and integers are created; `num` is not modified.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\sqrt n)$. Let $n$ denote the numeric value `num` and let $D=\lfloor\log_{10}n\rfloor+1$ be its decimal digit count.
- **Auxiliary Space Complexity:** $O(D)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
