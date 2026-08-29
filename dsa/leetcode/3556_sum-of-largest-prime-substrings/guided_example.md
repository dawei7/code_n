# Guided Example: Sum of Largest Prime Substrings

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "12234"}`
- **Required output:** `1469`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s`, find the sum of the **3 largest unique prime numbers** that can be formed using any of its** substrings**.

The objective is to compute `1469` from `{"s": "12234"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Enumerating every substring exactly once

The outer index `i` chooses the substring’s starting position. The inner index `j` moves from `i` to the final position, so it visits:

`s[i:i+1]`, `s[i:i+2]`, ..., `s[i:n]`.

Across all starts, this produces every nonempty contiguous substring exactly once as a position interval. There are

$$
\frac{n(n+1)}{2}
$$

such intervals.

Different intervals may represent the same integer. For example, repeated digits can create identical substrings, and leading zeros can make `"011"` and `"11"` both represent `11`. Enumeration is by substring occurrence; uniqueness is handled later by the set.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "12234"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Building values without substring conversion

At the beginning of each outer iteration, `x = 0`. Extending the current substring by digit `s[j]` uses

`x = x * 10 + int(s[j])`.

Multiplying by ten shifts the existing decimal representation one place to the left, and adding the new digit fills that last place. If the digits from `i` through `j - 1` represented `x` before the update, the new `x` is exactly the integer represented by digits `i` through `j`.

For start `i` in the string `"12234"`, the values grow as `1`, `12`, `122`, `1223`, and `12234`. The earlier digits are reused arithmetically rather than reparsed for each longer substring.

This update also implements the leading-zero rule automatically. Starting from the first character of `"011"` gives `0`, then `1`, then `11`. Decimal arithmetic naturally ignores leading zeros, just as required.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Testing primality

`is_prime(x)` first rejects every `x < 2`. This correctly excludes zero and one, neither of which is prime.

For `x \ge 2`, it checks possible divisors from `2` through `\lfloor\sqrt{x}\rfloor`. If `x` is composite, it can be written as `a \cdot b`. Both factors cannot exceed `\sqrt{x}`, because then their product would exceed `x`. Therefore every composite number has at least one divisor no larger than its square root.

Conversely, if no integer in that range divides `x`, no nontrivial factorization exists and `x` is prime.

The expression

`all(x % i for i in range(2, int(sqrt(x)) + 1))`

uses remainders as truth values. A nonzero remainder is truthy and means `i` is not a divisor. A zero remainder is false and makes `all` stop immediately, rejecting the number. When `x` is `2` or `3`, the range is empty; `all` of an empty iterable is true, correctly classifying both as prime.

The source tests every integer divisor, including even divisors after two. This is simple and correct, though not the most optimized trial-division loop.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1469` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "12234"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1469` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Parse every substring slice:** Using `int(s[i:j+1])` is straightforward and also ignores leading zeros, but it repeatedly creates and parses strings, adding an extra length factor across all substrings. Incremental decimal construction reuses the prior prefix value.
- **Check the set before primality:** Tracking every previously tested numeric value could avoid repeated primality tests for duplicate substrings. It needs an additional set or a combined cache and may improve repeated inputs, but the exact source tests first and stores only primes.
- **Keep a three-element min-heap:** A heap can retain only the three largest unique primes after deduplication, avoiding a full final sort. With at most 55 substrings under `n \le 10`, sorting the set is simpler and easily fast enough.
- **Sieve of Eratosthenes:** Sieving through `M` would make primality lookups fast but could require memory proportional to a number near `10^{10}`, which is completely impractical. Trial division is appropriate for few candidates in a huge numeric range.
- **Faster primality testing:** Deterministic Miller–Rabin for the bounded integer range or optimized trial division skipping even candidates can be much faster. They add complexity unnecessary for the ten-character limit.
- **Zero and one:** `is_prime` rejects both explicitly through `x < 2`.
- **Two and three:** Their divisor ranges are empty, and the mathematical convention `all(empty) == true` correctly accepts them.
- **Leading zeros:** Incremental arithmetic turns `"007"` into values `0`, `0`, and `7`; the prime `7` is counted once by value.
- **Repeated prime occurrences:** A prime is inserted into `st` many times harmlessly, but contributes once to the final sum.
- **Fewer than three unique primes:** The negative slice returns every available element, so their complete sum is returned.
- **No primes:** Sorting an empty set, slicing it, and summing it naturally returns zero.
- **A one-character string:** The only substring is tested normally, so a one-digit prime is returned and any other digit yields zero.
- **Floating square root:** `sqrt(x)` is converted to an integer to obtain the trial bound. Values are at most ten decimal digits here, well within the range where the computed square root is sufficiently represented; for far larger integers, an exact integer square root would be safer.
- **Uniqueness by integer, not text:** `"02"` and `"2"` both represent prime `2` and must count only once; the integer set enforces exactly that interpretation.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\sqrt{x})$. Let `n` be the string length and `M` the largest numeric value represented by any substring. There are `O(n^2)` substrings. Extending a value is constant-time under the usual bounded-integer model, while a worst-case primality test tries `O(\sqrt{x})` divisors and is bounded by `O(\sqrt{M})`.
- **Auxiliary Space Complexity:** $O(n^2)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
