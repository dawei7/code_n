# Guided Example: Minimum Number of Swaps to Make the String Balanced

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"s": "][]["}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a **0-indexed** string `s` of **even** length `n`. The string consists of **exactly** $n / 2$ opening brackets `'['` and $n / 2$ closing brackets `']'`.

The objective is to compute `1` from `{"s": "][]["}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Greedily cancel bracket pairs

Scan from left to right while `x` counts opening brackets that have not yet been matched.

When the current character is `"["`, increment `x`. When it is `"]"` and `x` is positive, match it with one earlier opening bracket and decrement `x`. When it is `"]"` and `x` is zero, it cannot be matched with anything to its left, so the code leaves `x` unchanged.

This is equivalent to removing every balanced `[]` relationship possible while preserving order, but it needs only one counter rather than a stack.

After the scan, `x` is the number of unmatched opening brackets. Because the original string contains equal numbers of opening and closing brackets, the number of earlier unmatched closing brackets is also `x`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"s": "][]["}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Understand the unmatched residual shape

Once all possible ordered matches are removed, unmatched closing brackets conceptually appear before unmatched opening brackets:

`]]]...[[[`.

If an unmatched opening had appeared before an unmatched closing, the greedy scan would have paired them. The task is therefore to repair two equal groups of size `x` using arbitrary-index swaps.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Once all possible ordered matches are removed, unmatched clo... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: How one swap repairs up to two unmatched pairs

Swap an early unmatched closing bracket with a suitably late unmatched opening bracket. Placing an opening near the front fixes a prefix deficit, while placing the closing near the back supplies a closing endpoint. In the residual arrangement, one swap can reduce the unmatched count `x` by two in the typical case.

Therefore the number of swaps is the ceiling of $x/2$:

$$
\left\lceil\frac x2\right\rceil
=\left\lfloor\frac{x+1}{2}\right\rfloor.
$$

The source writes this as `(x + 1) >> 1`. For nonnegative integers, right shift by one is floor division by two.

If `x` is even, every swap repairs two units. If it is odd, the final swap repairs the remaining one unit along with bracket structure already repositioned, giving the ceiling.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"s": "][]["}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Explicit stack:** Push unmatched openings and :** - **Explicit stack:** Push unmatched openings and pop on closings. It derives the same `x` but uses $O(N)$ space.
- **Track minimum prefix balance:** Treat `"["` as plus one and `"]"` as minus one; the deepest negative deficit leads to an equivalent ceiling formula.
- **Greedy matching interpretation:** Ignoring a closing only when no opening is available isolates exactly the brackets whose order must be repaired.
- **Simulate swaps:** Finding actual indices and rebuilding the string is unnecessary when only the minimum count is requested.
- **Already balanced:** No unmatched openings remain and the answer is zero.
- **Single pair `"[]"`:** The counter rises then falls to zero.
- **Reversed pair `"]["`:** One unmatched opening remains after cancellation, requiring one swap.
- **All closings then openings:** This maximizes imbalance and illustrates the ceiling formula.
- **Odd `x`:** Adding one before shifting implements ceiling rather than floor.
- **Even `x`:** Every swap can repair two units, so the result is exactly `x // 2`.
- **Equal bracket totals:** The proof relies on unmatched opening and closing counts being equal, guaranteed by the contract.
- **Arbitrary-index swaps:** One operation may exchange distant brackets; an adjacent-swap problem would require a different cost analysis.
- **Final balance:** Equal total bracket counts guarantee the completed string can reach balance zero after prefix deficits are fixed.
- **No mutation:** The scan calculates the count without changing `s`.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the string length.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
