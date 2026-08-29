# Guided Example: Separate the Digits in an Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [13, 25, 83, 77]}`
- **Required output:** `[1, 3, 2, 5, 8, 3, 7, 7]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of positive integers `nums`, return *an array *`answer`* that consists of the digits of each integer in *`nums`* after separating them in **the same order** they appear in *`nums`.

The objective is to compute `[1, 3, 2, 5, 8, 3, 7, 7]` from `{"nums": [13, 25, 83, 77]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Extracting one decimal digit at a time

For every positive integer in `nums`, the output must contain its decimal digits from most significant to least significant. The integers themselves must also be processed in their original array order. The solution handles these two ordering requirements separately: the outer loop preserves the order of the integers, while a temporary list repairs the order in which arithmetic digit extraction discovers the digits.

For a positive integer $x$, the remainder $x\bmod 10$ is its last decimal digit. Integer division by $10$ then removes that digit:

$$
x\leftarrow\left\lfloor\frac{x}{10}\right\rfloor.
$$

For example, begin with $x=10921$. The first remainder is $1$, and division changes $x$ to $1092$. Repeating the operations produces $2$, $9$, $0$, and $1$. These are exactly the original digits, but they arrive from right to left as `[1, 2, 9, 0, 1]`.

That reversal is unavoidable when repeatedly looking at the units place. The solution therefore appends the extracted digits to a temporary list `t` and, after the number has become zero, extends the answer with `t[::-1]`. Reversing the temporary sequence changes the example back to `[1, 0, 9, 2, 1]`, the required left-to-right order.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [13, 25, 83, 77]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the loop stops at the right moment

At the start of each pass through `while x`, the current $x$ consists precisely of the digits not yet extracted. The remainder operation moves its final remaining digit into `t`, and floor division removes that digit from $x$. Because $x$ is a nonnegative integer and becomes at least ten times smaller after each pass, it must eventually reach zero.

When it reaches zero, there are no digits left to process. If the original value contains $d$ decimal digits, the loop runs exactly $d$ times. A zero inside the number is not lost. For instance, processing $10$ first extracts $0$ and changes $x$ to $1$; the next pass extracts $1$. Both digits are stored in `t`. The truth test only ends the loop when the whole remaining number is zero, not when one extracted digit happens to be zero.

The constraints say every input integer is at least $1$. This matters because the representation of the number zero contains one digit, but `while x` would perform no iteration for an initial zero. No special case is needed under the stated contract.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Preserving order across the whole array

After one number has been completely extracted, `ans.extend(t[::-1])` appends all of its corrected digits to the end of the shared answer. It does not sort them or insert them ahead of digits from earlier numbers. The temporary list is recreated on the next outer-loop iteration, so digits from neighboring values never become mixed before reversal.

For `nums = [13, 25, 83, 77]`, the steps are:

- extracting `13` creates temporary `[3, 1]` and appends `[1, 3]`;
- extracting `25` creates temporary `[5, 2]` and appends `[2, 5]`;
- extracting `83` creates temporary `[3, 8]` and appends `[8, 3]`;
- extracting `77` creates temporary `[7, 7]` and appends `[7, 7]`.

The accumulated result is `[1, 3, 2, 5, 8, 3, 7, 7]`. The process is a flattening operation: each integer becomes its ordered digit sequence, and those sequences are concatenated in input order.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[1, 3, 2, 5, 8, 3, 7, 7]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [13, 25, 83, 77]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[1, 3, 2, 5, 8, 3, 7, 7]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Convert each number to a string:** Iterating through `str(x)` is concise and also takes $O(D)$ time, but the checked-in solution demonstrates the arithmetic representation directly and avoids character-to-integer conversion.
- **Traverse input backward and reverse once:** Processing `nums` from right to left, appending units digits immediately, and reversing the complete answer at the end avoids a separate temporary list per number. It has the same $O(D)$ time and still stores the output.
- **Place-value divisor:** One can first find the largest power of ten not exceeding $x$ and then read digits from left to right. This avoids reversing a temporary list but requires careful divisor updates and leading-zero reasoning.
- **Single-digit values:** One remainder extracts the value, one division reaches zero, and reversing a one-element list changes nothing.
- **Internal zeros:** Values such as `1005` work correctly because `x % 10` can append zero. A zero digit must not be confused with termination of the entire number.
- **Maximum value:** `100000` has six digits, including five trailing zeros. Each zero is extracted on a separate iteration before the leading one.
- **Initial zero outside the contract:** If zero were allowed, the current loop would append nothing for it. Supporting that altered contract would require an explicit `if x == 0` case.
- **Input preservation:** Reassigning the local name `x` is safe because integers are immutable and the code never assigns through an index of `nums`.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(D)$. Let $D$ be the total number of decimal digits across every value in `nums`. Every execution of the inner loop extracts one digit, so all inner loops together execute exactly $D$ times. Reversing and extending each temporary list also touches each extracted digit once. The total time is consequently $O(D)$.
- **Auxiliary Space Complexity:** $O(D)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
