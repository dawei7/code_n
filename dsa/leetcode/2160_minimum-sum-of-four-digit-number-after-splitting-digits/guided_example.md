# Guided Example: Minimum Sum of Four Digit Number After Splitting Digits

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"num": 2932}`
- **Required output:** `52`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **positive** integer `num` consisting of exactly four digits. Split `num` into two new integers `new1` and `new2` by using the **digits** found in `num`. **Leading zeros** are allowed in `new1` and `new2`, and **all** the digits found in `num` must be used.

The objective is to compute `52` from `{"num": 2932}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why two two-digit numbers are sufficient

Using one three-digit number and one one-digit number creates positional coefficients $100,10,1,1$. Using two two-digit numbers creates coefficients $10,10,1,1$. Every digit is nonnegative, so replacing the coefficient 100 with 10 can never increase the sum. Therefore an optimum always exists in the two-by-two form, even when a leading zero makes one displayed number shorter.

The problem reduces to assigning four digits to two tens positions and two units positions.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"num": 2932}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Extract every digit

The loop repeatedly appends `num % 10` and performs `num //= 10`. Remainder modulo ten extracts the current last digit, while integer division removes it.

Although the loop condition is `while num`, the input is guaranteed to be a four-digit integer. It therefore performs exactly four iterations. Zero digits inside the number are preserved: for `4009`, extraction produces `[9,0,0,4]` before sorting.

The extracted order does not matter because the digits may be rearranged arbitrarily.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The loop repeatedly appends `num % 10` and performs `num //=... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Assign small digits to expensive positions

After `nums.sort()`, write the digits as

$$
d_0\le d_1\le d_2\le d_3.
$$

The tens positions have coefficient ten, which is larger than the units coefficient one. To minimize a weighted sum, the two smallest digits must receive the two larger coefficients.

An exchange proves this. Suppose a larger digit $b$ occupies a tens position while a smaller digit $a$ occupies a units position. Their contribution is $10b+a$. Swapping them gives $10a+b$, reducing the sum by $9(b-a)\ge0$. Repeating such exchanges places $d_0$ and $d_1$ in the tens positions.

The remaining digits $d_2$ and $d_3$ occupy units positions. It does not matter which of the two numbers receives which tens or units digit because only their total sum is requested.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `52` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"num": 2932}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `52` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Enumerate all assignments:** Four digits have :** - **Enumerate all assignments:** Four digits have only a constant number of permutations and split points, so brute force can work, but it obscures the positional-weight proof.
- **Convert through a string:** Sorting `str(num)` is concise but still needs converting digit characters back to integers. Arithmetic extraction follows the exact source.
- **Three-digit plus one-digit split:** Its hundreds coefficient cannot improve on two tens coefficients for nonnegative digits.
- **Repeated digits:** Sorting retains all copies, and the same weighted argument applies.
- **One zero:** The zero should occupy a tens position because that removes the greatest possible place-value cost.
- **Two zeros:** Both tens positions become zero, leaving the two nonzero digits as the effective numbers.
- **Three zeros:** The minimum sum is the sole nonzero digit.
- **No zeros:** The two smallest digits become tens digits and the two largest become units digits.
- **Already sorted decimal digits:** Arithmetic extraction reverses them initially, but sorting restores the required value order.
- **Leading zeros:** They affect digit placement but not the numeric value of the constructed integers, exactly as permitted.
- **Equal choice of pairings:** Once tens digits are fixed, pairing either units digit with either tens digit leaves the sum unchanged.
- **Four-digit guarantee:** It ensures `nums[0]` through `nums[3]` always exist after the loop.
- **Pair labels:** Swapping `new1` and `new2` changes neither legality nor their sum, so no tie-breaking rule is needed.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. The input always contains exactly four digits. Extraction runs four times, sorting handles four values, and the return uses a fixed number of arithmetic operations. Time is $O(1)$ with respect to the problem’s input size.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
