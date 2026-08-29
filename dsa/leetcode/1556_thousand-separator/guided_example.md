# Guided Example: Thousand Separator

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 1234}`
- **Required output:** `"1.234"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an integer `n`, add a dot (".") as the thousands separator and return it in string format.

The objective is to compute `"1.234"` from `{"n": 1234}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Read decimal digits from right to left

Thousands separators divide a decimal representation into groups of three digits counted from the right. The rightmost group always contains the units, tens, and hundreds digits; the next group contains thousands through hundred-thousands, and so on.

Repeated division by ten naturally exposes digits in exactly that right-to-left order. The source uses `divmod(n, 10)`, which returns both the quotient and remainder:

- The remainder `v` is the current last decimal digit.
- The quotient becomes the still-unprocessed prefix.

The digit is converted to a one-character string and appended to list `ans`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 1234}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count digits within the current group

Variable `cnt` records how many digits have been appended since the most recent separator. It increases after each extracted digit.

When all remaining digits have been consumed, `n == 0` and the loop stops. That check deliberately occurs before separator insertion.

Otherwise, if `cnt == 3`, the current right-to-left group is complete. The source appends a dot and resets `cnt` to zero so the next three extracted digits form the next group.

Because extraction proceeds backward, `ans` temporarily contains the entire formatted result in reverse order.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why the stopping check must precede the dot

Consider `n = 123`. After extracting three, two, and one, `cnt` equals three, but the quotient is now zero. The result should be `"123"`, not `".123"`.

The source tests `n == 0` first and breaks, so no separator is added beyond the most significant group.

For `n = 1234`, after extracting four, three, and two, unprocessed quotient one remains. The code appends a dot because another group truly exists. It then extracts one and stops, giving reversed pieces `["4","3","2",".","1"]`.

This ordering handles exact multiples of three digits without a special case.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"1.234"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 1234}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"1.234"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Built-in comma formatting:** Format with commas and replace commas by dots. It is concise but hides the grouping logic and still creates strings.
- **Convert first and slice groups:** Split the decimal string from the right into chunks of three and join them. It is also $O(D)$.
- **Repeated string prepending:** It is correct but can repeatedly copy the growing immutable result.
- **Zero:** The unconditional loop emits one zero digit rather than an empty string.
- **One to three digits:** No separator is added because no higher group remains.
- **Exactly four digits:** One dot separates the leading digit from the final three.
- **Exactly six digits:** Only one dot is needed; the quotient-zero check prevents a leading dot.
- **Internal zeros:** Values such as 1000 retain a full `000` group.
- **Maximum input:** The same loop handles 2147483647 with three separators.
- **Negative values:** They are outside the contract; the digit-extraction logic is designed for nonnegative integers.
- **Separator placement:** Counting starts at the right, which is why groups remain correct regardless of total digit count.
- **Output allocation:** Returning a string necessarily requires space proportional to its displayed length when the numeric domain is treated as variable.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(D)$. Let $D$ be the number of decimal digits. The loop runs once per digit, reversal processes $O(D)$ pieces, and joining copies the $D$ digits plus separators. Time is $O(D)$, equivalently $O(\log n)$ for positive numeric magnitude.
- **Auxiliary Space Complexity:** $O(D)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
