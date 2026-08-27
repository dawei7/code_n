# Guided Example: Integer to Roman

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"num": 3749}`
- **Required output:** `"MMMDCCXLIX"`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Seven different symbols represent Roman numerals with the following values:

The objective is to compute `"MMMDCCXLIX"` from `{"num": 3749}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Treat subtractive pairs as complete Roman tokens

Canonical Roman notation uses seven one-character symbols plus six allowed subtractive pairs. The solution places all thirteen tokens in descending numerical order:

| Value | Token | Value | Token |
|---:|:---:|---:|:---:|
| `1000` | `M` | `900` | `CM` |
| `500` | `D` | `400` | `CD` |
| `100` | `C` | `90` | `XC` |
| `50` | `L` | `40` | `XL` |
| `10` | `X` | `9` | `IX` |
| `5` | `V` | `4` | `IV` |
| `1` | `I` |  |  |

The two tuples `cs` and `vs` store these tokens and values at matching positions. `zip(cs, vs)` therefore yields pairs such as `('M', 1000)`, then `('CM', 900)`, down through `('I', 1)`.

Including `900`, `400`, `90`, `40`, `9`, and `4` directly is the key simplification. The main loop does not need separate logic for numbers whose decimal place begins with four or nine; it selects `CM`, `CD`, `XC`, `XL`, `IX`, or `IV` just like any other largest fitting token.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"num": 3749}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Choose the largest token that fits the remaining value

For each descending pair `(c, v)`, the loop appends the token while its value can still be subtracted:



At every append:

- `c` represents exactly `v`;
- subtracting `v` maintains the unrepresented remainder;
- appending tokens in descending scan order keeps the Roman numeral in canonical high-to-low order.

If `v` is too large, the loop performs zero iterations and the scan moves to the next smaller token. If it fits several times, the method uses it repeatedly before considering anything smaller. Under the range up to `3999`, `M`, `C`, `X`, and `I` can each appear at most three times in their additive role. Five-unit symbols do not repeat because the next lower tokens consume the remainder according to the canonical table.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | For each descending pair `(c, v)`, the loop appends the toke... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why greedy selection creates the required decimal-place forms

The token list encodes every special boundary at which ordinary repetition would become noncanonical.

- A remainder from `1` through `3` uses one to three `I` tokens; `4` selects `IV`; `5` selects `V`; `6` through `8` select `V` followed by `I` tokens; `9` selects `IX`.
- The same structure is scaled by ten for `X`, `XL`, `L`, and `XC` in the tens place.
- It is scaled by one hundred for `C`, `CD`, `D`, and `CM` in the hundreds place.
- The thousands place uses up to three `M` tokens because `num <= 3999`.

Since tokens are processed from largest to smallest, a lower decimal place cannot be used prematurely to replace an available canonical higher-place form. For example, remainder `49` does not become `IL`: `40` is selected as `XL`, leaving `9`, which is selected as `IX`. The result is `XLIX`, respecting the rule that conversion is based on decimal places.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `"MMMDCCXLIX"` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"num": 3749}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `"MMMDCCXLIX"` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Use `divmod` per token:** Compute `count, num :** - **Use `divmod` per token:** Compute `count, num = divmod(num, v)` and append `c * count`. This reduces each table entry to one division and makes the number of outer iterations visibly fixed; it produces the same canonical sequence.
- **Hardcode each decimal digit:** Use lookup arrays for thousands, hundreds, tens, and ones, then concatenate four entries. This is also constant time but less flexible if the symbol system or supported range changes.
- **Handle 4 and 9 with branches:** One can convert each decimal place using separate cases. Treating subtractive pairs as tokens produces simpler uniform greedy code.
- **Omit subtractive tokens:** A greedy scan of only `I,V,X,L,C,D,M` would generate noncanonical forms such as `IIII` and `VIIII`. The six pairs are required.
- **Minimum input `1`:** Every larger token is skipped and one `I` is appended.
- **Maximum input `3999`:** Produces `MMMCMXCIX` without requiring a symbol above `M`.
- **Pure additive digit:** `8` becomes `VIII`: one `V` and three `I` tokens.
- **Subtractive boundary:** `4`, `9`, `40`, `90`, `400`, and `900` are each consumed by one explicit pair token.
- **Mixed decimal places:** `49` becomes `XLIX`, not `IL`, because the descending table respects independent tens and ones forms.
- **No zero input:** The contract starts at `1`, so the method never needs to define a Roman representation for zero.
- **Input preservation:** The local integer variable `num` is reduced, but integers are immutable and the caller's value is unaffected.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(1)$. Under the stated range `1 <= num <= 3999`:
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
