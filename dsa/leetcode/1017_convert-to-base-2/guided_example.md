# Guided Example: Convert to Base -2

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 2}`
- **Required output:** `"110"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer `n`, return *a binary string representing its representation in base* `-2`.

The objective is to compute `"110"` from `{"n": 2}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why ordinary base conversion needs an adjustment

In an ordinary positive base, repeated division works because the remainder gives the next least-significant digit. Base `-2` still uses only the digits `0` and `1`, but its place values alternate in sign:

$$
1,-2,4,-8,16,\ldots
$$

Thus a digit string `d_k\ldots d_1d_0` represents

$$
\sum_{p=0}^{k} d_p(-2)^p.
$$

The alternating signs are what make a nonnegative integer representable without a separate minus sign. For example, `110` means `1 \cdot 4 + 1 \cdot (-2) + 0 \cdot 1 = 2`.

The optimal code extracts digits from right to left. Its unusual feature is that it divides the working value by positive two, not negative two, and separately stores the sign of the current place in `k`. Initially `k = 1` because the units place is `(-2)^0 = 1`. After each digit, `k *= -1` switches between `1` and `-1`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 2}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: The invariant behind `n` and `k`

Let `N` denote the original input, and suppose the loop is about to choose the digit at position `p`. The digits for positions below `p` have already been appended to `ans`. At that moment:

$$
k = (-1)^p
$$

and the remaining part of the original value is represented by `n \cdot 2^p`. More fully,

$$
N = \sum_{j=0}^{p-1} d_j(-2)^j + n \cdot 2^p.
$$

This invariant explains every update in the loop. The code is not guessing digits. It chooses the only digit that makes the remaining normalized value divisible by two, then advances to the next power.

Because the available digits are zero and one, parity decides the current digit. If `n` is even, the current digit must be `0`. Subtracting zero leaves an even remainder, so the code appends `'0'` and proceeds directly to `n //= 2`.

If `n` is odd, the current digit must be `1`. At position `p`, that digit contributes `(-2)^p = k \cdot 2^p`. Since `n` is the residual after factoring out `2^p`, removing the chosen digit means replacing `n` by `n - k`. This is the purpose of `n -= k`.

The result is always even. When `k = 1`, an odd `n` minus one is even. When `k = -1`, `n -= k` means `n += 1`, and an odd `n` plus one is even. Only after making that adjustment does `n //= 2` move from the normalized coefficient of `2^p` to the normalized coefficient of `2^{p+1}`. Finally, negating `k` records that the next base `-2` place has the opposite sign.

This separation is a clean alternative to repeatedly calling division by `-2` and repairing a negative remainder. Python's integer division rules for negative divisors can be easy to misunderstand. The exact implementation keeps `n` nonnegative for every valid input and handles the sign through one alternating variable.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Let `N` denote the original input, and suppose the loop is a... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: A complete trace for `n = 2`

At the start, `n = 2` and `k = 1`. Two is even, so the units digit is `0`. The code appends `0`, divides `n` to one, and changes `k` to `-1`.

Now `n = 1` is odd at the negative-two place. The digit must be `1`. Subtracting `k` means computing `1 - (-1) = 2`. Division gives `n = 1`, and `k` changes back to `1`.

The working value is still one, but this is not a loop error: the place has changed from `-2` to `4`. Since `n` is odd, the code appends another `1`, subtracts positive one, and divides zero by two. The collected digits are `['0', '1', '1']` from least significant to most significant. Reversing them gives `"110"`, whose value is four minus two, or two.

For `n = 3`, the first odd step chooses a units digit of one and reduces the working value to one. The following negative place chooses one and temporarily keeps the normalized value at one after adjustment and division. The positive-four place chooses the final one. Reversal produces `"111"`, equal to `4 - 2 + 1 = 3`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"110"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 2}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"110"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Repeated division by `-2`:** A conventional fo:** - **Repeated division by `-2`:** A conventional formulation uses `n, remainder = divmod(n, -2)` and repairs a negative remainder by adding two and increasing the quotient. It is correct when implemented carefully, but the repair rule is easy to get wrong. The chosen code avoids negative remainders by dividing by positive two and tracking the place sign separately.
- **Build powers first and use a greedy choice:** One could find the largest power of `-2` and decide digits from left to right. Alternating positive and negative place values make an ordinary largest-first greedy rule much harder to justify, because choosing a large positive contribution changes what negative lower places must compensate.
- **Convert to ordinary binary and edit bits:** Base two and base negative two share digit symbols but not positional values. Merely flipping selected bits or inserting a sign cannot generally transform one representation into the other without carrying information across positions.
- **Recursive digit generation:** The same recurrence can be written recursively and concatenate a final remainder digit. Its reasoning is similar, but it consumes `O(B)` call-stack frames and may perform costly repeated string concatenation unless designed carefully.
- **Input zero:** Zero must be represented by exactly `"0"`. Returning the empty join would violate the contract, which is why the final `or '0'` is essential.
- **Input one:** The loop appends one at the units place and immediately reaches zero, returning `"1"`.
- **The temporary non-decrease at a negative place:** With `n = 1` and `k = -1`, the update produces one again after division. This is expected because the algorithm has moved to a different place value. The following positive-place iteration terminates, so there is no infinite loop.
- **No leading zeroes:** Zero digits may be appended early because the list is built from right to left. They become trailing zeroes in the final string, not leading zeroes. The last generated digit for a positive input is always one.
- **Mutation of the parameter:** The method reuses `n` as its shrinking working residual. That is safe because the original value is not needed after conversion and integers are immutable values from the caller's perspective.
- **Values near `10^9`:** The number of iterations grows logarithmically, so the upper constraint needs only a few dozen digit steps rather than work proportional to the numeric value.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(B)$. Let `B` be the number of digits in the returned base `-2` representation. Each iteration determines exactly one digit, performs a constant number of arithmetic operations, appends one character, and advances one place. The loop therefore takes `O(B)` time.
- **Auxiliary Space Complexity:** $O(B)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
