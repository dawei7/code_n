# Guided Example: Percentage of Letter in String

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "foobar", "letter": "o"}`
- **Required output:** `33`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a string `s` and a character `letter`, return* the **percentage** of characters in *`s`* that equal *`letter`* **rounded down** to the nearest whole percent.*

The objective is to compute `33` from `{"s": "foobar", "letter": "o"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Translate the percentage definition directly

Let `m` be the number of characters in `s` equal to `letter`, and let `n = len(s)`. The exact percentage before rounding is

$$
\frac{m}{n}\cdot 100.
$$

The problem asks for this value rounded down to a whole percent, so the desired integer is

$$
\left\lfloor\frac{100m}{n}\right\rfloor.
$$

The return expression implements this formula as `s.count(letter) * 100 // len(s)`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "foobar", "letter": "o"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Count every matching position

`s.count(letter)` scans the string and returns how many occurrences of the one-character string `letter` it contains. Since `letter` is guaranteed to be one lowercase English character, this is exactly the number of positions satisfying the condition.

Repeated matches are all counted. Their positions and whether they are adjacent do not matter because a percentage depends only on the total number of matching characters.

The method needs no frequency table for other letters. Every nonmatching position contributes only to the denominator `len(s)`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Multiply before applying integer division

The operation order is essential. `m * 100 // n` first scales the fraction into percent units and then floors the result.

If the code instead performed `m // n * 100`, integer division would happen too early. For every case with `0 < m < n`, `m // n` would be zero, incorrectly reporting zero percent. Keeping multiplication first preserves the fractional information until the final required rounding.

For `s = "foobar"` and `letter = "o"`, `m = 2` and `n = 6`. The code calculates `200 // 6 = 33`, which is the floor of approximately 33.333 percent.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `33` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "foobar", "letter": "o"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `33` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Manual counting loop:** Increment a counter for each matching character, then use the same formula. It has identical complexity but is more verbose than `str.count`.
- **Frequency dictionary:** It computes counts for every character even though only one letter is queried, adding unnecessary state.
- **Floating-point division:** It is avoidable and may introduce rounding ambiguity; exact integer arithmetic already matches the contract.
- **Round to nearest:** Python `round` would implement a different rule. The result must always be rounded down.
- **Divide before multiplying:** `m // n * 100` loses every proper fraction and is incorrect for mixed strings.
- **No matches:** The numerator is zero and the method returns zero.
- **Every character matches:** Numerator equals denominator times 100, so the method returns 100.
- **Single-character string:** The result is either zero or 100, and division is safe.
- **Non-divisible percentage:** Floor division discards the remainder, such as 200 divided by six producing 33.
- **Exact whole percentage:** When `100m` is divisible by `n`, `//` returns that exact percentage.
- **Nonempty guarantee:** `len(s)` is at least one, so division by zero cannot occur.
- **One-character target:** The source guarantee makes `count` count positions rather than longer substring matches.
- **Lowercase constraint:** Character encoding and case normalization require no special handling.
- **Result bound:** The formula cannot produce less than zero or more than 100.
- **Input preservation:** No mutation or reconstructed string is involved.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let `n` be the length of `s`. `s.count(letter)` examines the string in `O(n)` time. `len(s)` is `O(1)` for a Python string, and the remaining arithmetic is constant time for the bounded values. Total time is `O(n)`.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
