# Guided Example: Multiply Strings

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"num1": "2", "num2": "3"}`
- **Required output:** `"6"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two non-negative integers `num1` and `num2` represented as strings, return the product of `num1` and `num2`, also represented as a string.

The objective is to compute `"6"` from `{"num1": "2", "num2": "3"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Recreate multiplication without converting the whole inputs

The restriction forbids turning `num1` and `num2` into built-in integers and multiplying them directly. It does not forbid converting one digit character at a time. The solution therefore reproduces grade-school multiplication: multiply every digit of the first number by every digit of the second, place each partial product according to decimal position, and propagate carries.

Let $m$ and $n$ be the input lengths. The product of an $m$-digit number and an $n$-digit number has at most $m + n$ digits. It can have $m + n - 1$ digits, but allocating `m + n` slots covers both possibilities and leaves room for a leading carry.

`arr` stores digits in normal most-significant-to-least-significant order. During the first phase its entries are not yet restricted to 0 through 9; they are buckets accumulating all raw products that belong at the same decimal position.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"num1": "2", "num2": "3"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why a pair contributes to `i + j + 1`

Digit `num1[i]` is $m - 1 - i$ positions from the right, while `num2[j]` is $n - 1 - j$ positions from the right. Their product belongs

$$
(m - 1 - i) + (n - 1 - j)
$$

positions from the right of the answer. In a length-$(m+n)$ array, that decimal position corresponds to array index `i + j + 1`. The slot immediately to its left, `i + j`, is where a carry from that position will eventually go.

This explains the otherwise mysterious extra `+ 1`. For `123 * 456`, the product of the rightmost digits `3 * 6` goes to the final slot because `i = 2`, `j = 2`, and `i + j + 1 = 5` in a six-slot array. The product `1 * 4` goes to index 1, leaving index 0 available if carry makes the final answer six digits.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Accumulate before carrying

The nested loops run from right to left, although accumulation correctness would also hold in another order because addition is commutative. For each pair, the source converts the two characters separately and adds `a * b` to `arr[i + j + 1]`.

No carry is performed inside these loops. Several products may make a bucket much larger than 9, and that is intentional. Separating multiplication from carry propagation keeps each phase simple: first place every pairwise contribution at its correct power of ten, then normalize the entire representation.

For example, the tens-position bucket may receive contributions from the units digit of one input times the tens digit of the other and vice versa. Adding both before carrying is exactly what written multiplication does when its shifted partial rows are summed.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"6"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"num1": "2", "num2": "3"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"6"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Carry after every digit multiplication:** A destination slot can be normalized immediately and its carry added leftward. This uses the same array and bounds but intertwines accumulation with normalization, making ordering harder to reason about.
- **Reverse both input strings:** Reversed digits let index `i + j` directly represent the power of ten. The result must then be normalized and reversed back, which is equally valid but adds reversal steps.
- **Build shifted partial strings:** This mirrors paper multiplication visually, but storing and summing all partial rows uses more intermediate space and more complicated string addition.
- **Convert whole strings with `int`:** It is concise in Python but explicitly violates the problem's restriction and hides the intended arbitrary-precision arithmetic.
- **Either operand is `"0"`:** The early return supplies one canonical zero rather than an empty string or many leading zeros.
- **Single-digit operands:** The same bucket and carry logic works; for `9 * 9`, the two slots normalize to `"81"`.
- **Maximum carry chains:** Right-to-left normalization propagates carries through as many positions as necessary because each left bucket is processed only after all rightward carries have reached it.
- **No leading zeros in inputs:** This guarantee justifies removing at most one unused result slot after excluding zero operands.
- **Inputs remain unchanged:** Strings are immutable and the algorithm only reads their characters.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(mn + m + n)$. The nested loops execute once for every pair of input digits, for $mn$ single-digit multiplications and additions. The carry pass and final string construction each process at most $m+n$ slots. Total time is therefore $O(mn + m + n)$, customarily simplified to $O(mn)$ for positive lengths.
- **Auxiliary Space Complexity:** $O(m+n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
