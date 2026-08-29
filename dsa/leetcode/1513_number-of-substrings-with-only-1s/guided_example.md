# Guided Example: Number of Substrings With Only 1s

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "0110111"}`
- **Required output:** `9`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given a binary string `s`, return *the number of substrings with all characters* `1`*'s*. Since the answer may be too large, return it modulo $10^{9} + 7$.

The objective is to compute `9` from `{"s": "0110111"}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Count valid substrings by where they end

Every all-ones substring has a unique ending position. The stored solution tracks `cur`, the length of the current consecutive run of ones ending at the character being processed.

If the current character is zero, no all-ones substring can end there, and the run is broken, so `cur` becomes zero.

If the character is one, it extends the preceding run, so `cur` increases by one. Exactly `cur` valid substrings end at this position: the one-character suffix, the two-character suffix if available, and every longer suffix through the entire current run.

The source adds this `cur` contribution to `ans` immediately and reduces modulo $10^9+7$.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "0110111"}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: A direct example

For a run `111`:

- At the first one, `cur = 1`, counting `1`.
- At the second, `cur = 2`, counting the suffixes `1` and `11` ending there.
- At the third, `cur = 3`, counting `1`, `11`, and `111` ending there.

The run contributes one plus two plus three, which is six. When a zero follows, resetting `cur` prevents a later one from forming a substring across that zero.

For `0110111`, the first run has length two and contributes three. The second run has length three and contributes six. The total is nine.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: The invariant

After processing a prefix of `s`:

1. `cur` equals the number of consecutive ones at the end of that prefix.
2. `ans` equals the number of all-ones substrings contained in the prefix, modulo the required modulus.

The empty prefix has both values zero. If the next character is zero, the suffix run becomes empty and no new valid substring ends there. If it is one, every valid new substring must be a suffix consisting of that character plus zero or more of the immediately preceding consecutive ones. There are exactly the new `cur` of those.

Adding that amount preserves the answer invariant. Induction proves correctness for the full string.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `9` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "0110111"}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `9` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Run-at-a-time triangular formula:** Measure each maximal run and add `L * (L + 1) // 2` when it ends. It has the same bounds but needs a final post-loop addition.
- **Enumerate every substring:** Checking each candidate is quadratic or cubic and unnecessary.
- **Dynamic programming array:** Store the count of valid suffixes for every index. It reproduces `cur` but wastes $O(N)$ space because only the previous value matters.
- **All zeros:** `cur` repeatedly resets and the result is zero.
- **All ones:** Contributions one through N sum to $N(N+1)/2$ modulo the required value.
- **Alternating characters:** Every one contributes exactly one single-character substring.
- **One-character string:** One returns one, while zero returns zero.
- **Zero between runs:** Resetting prevents invalid substrings from crossing it.
- **Modulo placement:** Reducing the accumulated answer is safe; reducing or changing the run length would obscure its meaning.
- **Nonempty substrings:** Every contribution has an endpoint and positive length, so the empty string is never counted.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the string length. The loop visits each character once and performs constant work, so time is $O(N)$.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
