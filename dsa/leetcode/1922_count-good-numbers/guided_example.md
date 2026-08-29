# Guided Example: Count Good Numbers

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 10000}`
- **Required output:** `325891746`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A digit string is **good** if the digits **(0-indexed)** at **even** indices are **even** and the digits at **odd** indices are **prime** (`2`, `3`, `5`, or `7`).

The objective is to compute `325891746` from `{"n": 10000}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Count choices by position type

A good digit string has one rule for even indices and another for odd indices. At an even index, the digit must be even, so the choices are `0`, `2`, `4`, `6`, and `8`: five possibilities. At an odd index, the digit must be prime, so the choices are `2`, `3`, `5`, and `7`: four possibilities.

These choices are independent. Selecting a digit for one position does not restrict any other position, and repeated digits are allowed. Therefore the multiplication principle applies: multiply the number of choices for every position.

Because indexing begins at zero, the even indices are $0,2,4,\ldots$. When $n$ is even, exactly half the positions are even-indexed and half are odd-indexed. When $n$ is odd, the extra position is index $n-1$, which is even. Consequently,

$$
\text{even positions}=\left\lceil\frac n2\right\rceil
=\left\lfloor\frac{n+1}{2}\right\rfloor
$$

and

$$
\text{odd positions}=\left\lfloor\frac n2\right\rfloor.
$$

The total before applying the modulus is therefore

$$
5^{\lceil n/2\rceil}\cdot4^{\lfloor n/2\rfloor}.
$$

Leading zeroes are explicitly allowed because the objects being counted are digit strings, not ordinary decimal integer representations. Thus `0` really is one of the five choices at index $0$. Excluding it would incorrectly reduce the answer.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 10000}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Read the exact bit operations

The solution computes the two position counts as `(n + 1) >> 1` and `n >> 1`. For a nonnegative integer, shifting right by one bit is integer division by two. Thus `n >> 1` equals $\lfloor n/2\rfloor$, while `(n + 1) >> 1` equals $\lfloor(n+1)/2\rfloor=\lceil n/2\rceil$.

It then calls Python's three-argument power function:

`pow(5, (n + 1) >> 1, mod)`

and

`pow(4, n >> 1, mod)`.

The three-argument form computes a power modulo `mod` without first constructing the enormous full power. Internally, modular exponentiation uses repeated squaring. Writing an exponent in binary lets the algorithm build the answer from only the powers corresponding to set bits. Each squaring or selected multiplication is immediately reduced modulo $10^9+7$, so intermediate modular values remain bounded.

Finally, the two modular powers are multiplied and reduced once more:

`power_of_five * power_of_four % mod`.

This is valid because modular arithmetic preserves multiplication:

$$
(a\bmod M)(b\bmod M)\bmod M=(ab)\bmod M.
$$

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: A small derivation

For $n=4$, indices $0$ and $2$ are even, while indices $1$ and $3$ are odd. There are $5^2$ ways to fill the even positions and $4^2$ ways to fill the odd positions, giving $25\cdot16=400$ good strings.

For $n=5$, there are three even indices, $0,2,4$, and two odd indices, $1,3$. The count becomes $5^3\cdot4^2$. This example shows why simply using $n/2$ for both exponents would lose the final even-indexed position when the length is odd.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `325891746` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 10000}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `325891746` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Manual binary exponentiation:** A loop can square the base, multiply it into an accumulator when the current exponent bit is one, and halve the exponent each round. This has the same $O(\log n)$ time and $O(1)$ space, but Python's three-argument `pow` is shorter and highly optimized.
- **Linear repeated multiplication:** Multiplying by five and four once per position is conceptually simple but takes $O(n)$ time, which is impossible for $n$ up to $10^{15}$.
- **Constructing or enumerating strings:** There are exponentially many valid strings. Generation is unnecessary because independent choices give the count directly.
- **Using floating-point powers:** Floating-point numbers cannot represent such enormous exact counts and do not preserve the required modular value. Modular integer exponentiation is the correct tool.
- **Odd length:** There is one more even-indexed position than odd-indexed positions. The `(n + 1) >> 1` exponent accounts for it.
- **Even length:** Both position types occur exactly $n/2$ times, so the two shift expressions produce equal exponents.
- **Length one:** Only index $0$ exists. It is even-indexed and has five valid digits, while the odd-position exponent is zero. Because any nonzero base to exponent zero is one, the formula returns $5\cdot1=5$.
- **Leading zero:** The string `"0"` and longer strings beginning with zero are valid candidates. Treating the result as a number and disallowing leading zeroes would violate the contract.
- **Modulo placement:** Reducing each power and reducing the final product is mathematically exact. Omitting the final remainder could return a product larger than the requested range even though each factor was already reduced.
- **Prime-index misconception:** The word prime describes the digit placed at an odd index, not the index itself. Odd positions use digits `2`, `3`, `5`, or `7`; even positions use even digits.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log n)$. Let $n$ be the requested string length. Repeated squaring needs one iteration per binary digit of an exponent. Both exponents are at most $\lceil n/2\rceil$, so each `pow` call takes $O(\log n)$ modular-arithmetic steps. Two such calls plus one final multiplication remain $O(\log n)$ time.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
