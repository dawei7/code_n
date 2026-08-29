# Guided Example: Missing Number In Arithmetic Progression

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [5, 7, 11, 13]}`
- **Required output:** `9`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

In some array `arr`, the values were in arithmetic progression: the values $arr[i + 1] - \text{arr}[i]$ are all equal for every $0 \le i < \text{arr.length} - 1$.

The objective is to compute `9` from `{"arr": [5, 7, 11, 13]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Recover the missing value from a sum identity

The original array was an arithmetic progression with \(n+1\) values, where \(n\) is the length of the remaining `arr`. Exactly one interior value was removed. Because neither endpoint was removed, `arr[0]` and `arr[-1]` are still the first and last terms of the original progression.

An arithmetic progression has a useful sum formula:

\[
\text{sum}
=\frac{(\text{first term}+\text{last term})\cdot
\text{number of terms}}{2}.
\]

The original progression therefore had total

\[
T=\frac{(\texttt{arr[0]}+\texttt{arr[-1]})\cdot(n+1)}{2}.
\]

The current array contains every original term except the missing value \(x\), so

\[
\sum \texttt{arr}=T-x.
\]

Rearranging gives

\[
x=T-\sum \texttt{arr}.
\]

The exact solution is this formula written as one return expression.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [5, 7, 11, 13]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the arithmetic-progression sum formula works

Pair the first original term with the last, the second with the second-to-last, and so on. Every pair has the same sum, first plus last, because moving one step forward adds the common difference while moving one step backward subtracts that same difference.

If the number of terms is even, there are half as many pairs. If it is odd, the middle term is exactly half of first plus last, so the same formula still applies. This proof works for increasing, decreasing, and constant progressions.

The method never needs to calculate the common difference or locate the gap. It uses the fact that the missing term is exactly the difference between the complete total and the observed total.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Following the first example

For `arr = [5, 7, 11, 13]`, the remaining length is four, so the original length was five. The complete progression’s sum must be

\[
\frac{(5+13)\cdot5}{2}=45.
\]

The observed sum is \(5+7+11+13=36\). Their difference is \(45-36=9\), which is the removed term.

For the decreasing example `[15, 13, 12]`, the original length was four. The complete sum is

\[
\frac{(15+12)\cdot4}{2}=54.
\]

The observed sum is 40, so the missing value is 14. Nothing in the formula assumes a positive common difference.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `9` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [5, 7, 11, 13]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `9` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Binary search for the first shifted index:** Derive the common difference from the preserved endpoints, compare `arr[mid]` with its expected value, and find the first mismatch in \(O(\log n)\) time and \(O(1)\) space. This matches the manifest but is more complex.
- **Linear difference scan:** Derive the common difference and return the first expected value that does not match. It has the same \(O(n)\) time as the sum formula with more branching.
- **Increasing progression:** The complete-total formula works without locating the unusually large adjacent gap.
- **Decreasing progression:** Endpoint order and negative difference do not affect the sum identity.
- **Constant progression:** Every term is equal, and subtracting totals returns that repeated value.
- **Missing value repeated elsewhere:** In a constant progression, the numerical value is not unique to one position, but the requested number is still unambiguous.
- **Preserved endpoints:** The method depends critically on this guarantee. Allowing an endpoint deletion would invalidate the complete-sum calculation.
- **Exact integer arithmetic:** The numerator is always even for a valid integer progression, so floor division does not lose information.
- **Overflow in other languages:** Endpoint values and lengths should be promoted before multiplication. Python’s arbitrary-precision integers avoid this issue.
- **Input validity:** The code does not verify that the remaining values came from a valid progression with one interior deletion; it relies on the contract.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(\log n)$. Let \(n=\lvert\texttt{arr}\rvert\). Computing `sum(arr)` scans all \(n\) values, so the exact implementation takes \(O(n)\) time. Endpoint access, length, arithmetic, and subtraction take \(O(1)\) additional operations.
- **Auxiliary Space Complexity:** $O(1)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
