# Guided Example: Pow(x, n)

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"x": 2.0, "n": 10}`
- **Required output:** `1024.0`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Implement <a href="http://www.cplusplus.com/reference/valarray/pow/" target="_blank">pow(x, n)</a>, which calculates `x` raised to the power `n` (i.e., $x^n$).

The objective is to compute `1024.0` from `{"x": 2.0, "n": 10}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why multiplying `x` exactly `n` times is unnecessary

The exponent may have magnitude near $2^{31}$, so a loop performing one multiplication per exponent unit is far too slow. Binary exponentiation uses the fact that repeated squaring creates large powers quickly:

$$
x,\quad x^2,\quad x^4,\quad x^8,\quad x^{16},\ldots
$$

Every nonnegative integer exponent is a sum of distinct powers of two. If the binary representation of $n$ has a 1 in a particular position, the corresponding squared power belongs in the result. The algorithm reads those binary bits from least significant to most significant.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"x": 2.0, "n": 10}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Meaning of the helper variables

`qpow(a, n)` is called only with a nonnegative exponent. `ans` accumulates the powers selected by bits already processed. `a` is the base raised to the power represented by the current bit position. The local `n` contains the remaining unprocessed bits.

Initially, `a` is the original base, corresponding to $x^{2^0}$, no bits have been processed, and `ans = 1` is the multiplicative identity. If the low bit of `n` is 1, the test `n & 1` succeeds and `ans *= a` includes that power.

Then `a *= a` advances from $x^{2^k}$ to $x^{2^{k+1}}$, and `n >>= 1` removes the bit just handled. Right shifting a nonnegative integer by one is integer division by two with the remainder discarded, exactly what is needed to expose the next binary bit.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: A concrete binary trace

For exponent 13, the binary representation is `1101`, meaning $13 = 8 + 4 + 1$. The first low bit is 1, so the algorithm includes $x$. It squares the base to $x^2$ and shifts. The next bit is 0, so $x^2$ is not included. Further squaring yields $x^4$, whose bit is 1, and then $x^8$, whose bit is also 1.

The accumulator becomes

$$
x \cdot x^4 \cdot x^8 = x^{13}.
$$

Only four iterations are needed because 13 has four binary positions, rather than thirteen direct multiplications.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1024.0` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"x": 2.0, "n": 10}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1024.0` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Recursive exponentiation by squaring:** Compute the half power once, square it, and multiply by `x` for an odd exponent. It has the same time bound but uses $O(\log |n|)$ call-stack space.
- **Naive repeated multiplication:** It is simple but takes $O(|n|)$ time, which is infeasible for the maximum exponent.
- **Built-in power operator:** `x ** n` is concise but bypasses the requested implementation exercise and hides the binary process.
- **Exponent zero:** The untouched multiplicative identity 1 is returned.
- **Negative exponent:** The source computes the positive magnitude first and takes exactly one reciprocal at the end.
- **Minimum 32-bit exponent:** Python safely evaluates `-n` beyond signed 32-bit range. A fixed-width implementation must widen before negation.
- **Base zero:** Valid inputs allow it only with positive `n`, for which repeated squaring correctly returns zero.
- **Base one or negative one:** Squaring quickly stabilizes at one, while selected odd bits preserve the appropriate sign.
- **Negative base:** The parity of selected exponent bits naturally determines the sign; no special branch is needed.
- **Floating-point precision:** The algorithm minimizes multiplication count asymptotically but cannot eliminate ordinary rounding in floating-point operations.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log |n|)$. Each loop iteration shifts the nonnegative exponent right by one, halving it. The number of iterations is the number of bits in $|n|$, which is $O(\log |n|)$ for nonzero `n`; the zero case is constant time. Every iteration performs only constant-time arithmetic at the algorithmic model used by the problem.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
