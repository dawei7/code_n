# Guided Example: Reformat Phone Number

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"number": "1-23-45 6"}`
- **Required output:** `"123-456"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a phone number as a string `number`. `number` consists of digits, spaces `' '`, and/or dashes `'-'`.

The objective is to compute `"123-456"` from `{"number": "1-23-45 6"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Remove formatting before creating new formatting

The original spaces and dashes carry no grouping meaning. The chained replacements first remove every dash and then every space, leaving a string containing only digits:

`number = number.replace("-", "").replace(" ", "")`.

Digit order is unchanged. Starting from this clean sequence prevents old separators from interfering with index calculations.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"number": "1-23-45 6"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Create provisional blocks of three

Let `n` be the number of cleaned digits. The list comprehension creates `n // 3` slices:

`number[i * 3 : i * 3 + 3]`.

These are consecutive three-digit blocks beginning at positions zero, three, six, and so on. When `n` is divisible by three, they cover the entire string and already form the final grouping.

When a remainder exists, the final behavior depends on whether it is one or two.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Let `n` be the number of cleaned digits.... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Handle a remainder of two

If `n % 3 == 2`, the provisional blocks cover the first `n - 2` digits. `number[-2:]` is exactly the remaining pair, so the source appends it.

For eight digits, the initial list contains the first six as two blocks of three, and the last two become one final block. No block has length one.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"123-456"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"number": "1-23-45 6"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"123-456"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Character filtering:** Build the clean digits :** - **Character filtering:** Build the clean digits with a comprehension testing `c.isdigit()`. It is a single conceptual pass but still uses $O(N)$ output storage.
- **Manual scanner and block builder:** It can emit blocks as digits arrive, though recognizing the final four requires buffering or knowing the cleaned length.
- **Regular expression removal:** It works but is unnecessary for two literal separator characters.
- **Exactly two digits:** No provisional three-block exists; the remainder-two branch appends the full pair.
- **Exactly three digits:** One three-digit block is returned.
- **Exactly four digits:** One provisional block is shortened to two and the final two digits are appended.
- **Multiple spaces or dashes:** Every occurrence is removed by `replace`, regardless of adjacency.
- **Leading and trailing separators:** Cleaning removes them without affecting digit order.
- **Leading zero digit:** String slicing preserves it; integer parsing would not.
- **Remainder one:** It must never be emitted as a one-digit block, which is why the last provisional triple is rebalanced.
- **At most two two-blocks:** Only the final four digits create two such blocks, and earlier blocks remain length three.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let `N` be the original string length. Each `replace` scans and constructs a string, costing $O(N)$ time. The block slices collectively copy $O(N)$ digits, and joining also costs $O(N)$. Total time is $O(N)$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
