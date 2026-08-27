# Guided Example: Fraction Addition and Subtraction

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"expression": "-1/2+1/2"}`
- **Required output:** `"0/1"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `expression` representing an expression of fraction addition and subtraction, return the calculation result in string format.

The objective is to compute `"0/1"` from `{"expression": "-1/2+1/2"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Normalizing the first sign

Every later fraction begins with `+` or `-` because operators separate terms. A positive first fraction may omit its plus sign. The source makes all terms follow one parsing pattern:



After this normalization, index `i` always points to a term’s sign at the top of the loop. A leading negative expression already has a sign and is left unchanged.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"expression": "-1/2+1/2"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Extracting one term

The sign becomes `-1` for `-` and `1` otherwise. The parser advances past it, then moves `j` until the next plus/minus sign or the end:



The substring `expression[i:j]` therefore contains exactly one unsigned fraction such as `"10/7"`. Splitting at `/` yields numerator text `a` and denominator text `b`.

The input grammar guarantees a valid sequence, positive raw numerators and denominators, and no embedded signs inside a fraction. The parser can consequently treat every plus or minus as a term boundary without needing a more general expression tokenizer.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The sign becomes `-1` for `-` and `1` otherwise.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Converting into fixed-denominator units

For signed fraction

$$
\text{sign}\cdot\frac{a}{b},
$$

the equivalent numerator over $y$ is

$$
\text{sign}\cdot a\cdot\frac{y}{b}.
$$

The update is:



Integer division is exact because every legal $b\in[1,10]$ divides 30240. No remainder is discarded. This is the critical reason the fixed denominator works; choosing an arbitrary large number that was not divisible by every denominator would silently corrupt fractions.

The parser repeats until every term has contributed its signed count of $1/y$ units. For `"1/3-1/2"`, the contributions are $10080$ and $-15120$, so `x = -5040` over 30240, equal to $-1/6$.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"0/1"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"expression": "-1/2+1/2"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"0/1"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Running cross multiplication:** Maintain `num/:** - **Running cross multiplication:** Maintain `num/den` and combine `a/b` as `(num*b + sign*a*den)/(den*b)`, reducing along the way or at the end. It works for arbitrary denominators but can grow intermediates.
- **Running LCM:** Use `lcm(den,b)` as the smallest next common denominator. It limits intermediate size and generalizes beyond denominators 1–10.
- **Regular-expression tokenization:** Extract signed numerator/denominator pairs directly. Concise, but manual scanning is easier to derive and avoids regex-specific knowledge.
- **Hard-coded 30240:** Correct only because every denominator is in $[1,10]$. If that contract changes, the constant must not be reused blindly.
- **First positive fraction:** The source prepends `+` so every loop starts at a sign.
- **First negative fraction:** Its existing sign is parsed directly.
- **Zero total:** GCD reduction produces exactly `"0/1"`.
- **Integer total:** Complete cancellation produces denominator 1, as required.
- **Negative result:** `gcd` is nonnegative, so the sign remains on the numerator rather than moving to the denominator.
- **Denominator 10:** It divides 30240 exactly; the fixed-denominator update remains integral.
- **One fraction:** It is converted to the common denominator and reduced back to its already irreducible value.
- **No intermediate reduction:** Safe under the small bounded term count and final 32-bit guarantee, though other languages might need wider intermediate integers.
- **Space fidelity:** Prepending to an immutable Python string is an actual $O(n)$ allocation; the manifest’s $O(1)$ target belongs to a parser that avoids copying the input.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n \log V)$. Let $n$ be the expression length and let $V$ bound the magnitude of the final accumulator values. The two indices move forward across the expression, so parsing takes $O(n)$ character work. Each legal fraction has very short bounded numeric fields under the given constraints. One Euclidean GCD costs $O(\log V)$ arithmetic iterations. A precise high-level bound is $O(n+\log V)$, which is safely covered by the manifest’s coarser $O(n\log V)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
