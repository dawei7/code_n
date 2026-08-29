# Guided Example: Permutations IV

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 4, "k": 6}`
- **Required output:** `[3, 4, 1, 2]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given two integers, `n` and `k`, an **alternating permutation** is a permutation of the first `n` positive integers such that no **two** adjacent elements are both odd or both even.

The objective is to compute `[3, 4, 1, 2]` from `{"n": 4, "k": 6}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Core Step 1

**Alternation fixes the parity of every remaining position.** An alternating permutation must switch parity at each adjacent position. If $n$ is odd, there is one more odd number than even number among $1$ through $n$, so every valid permutation must start and end odd. If $n$ is even, the parity counts are equal and a valid permutation may start with either parity.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 4, "k": 6}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Core Step 2

Once a prefix ends with an odd value, the next position must be even, then odd, and so on. The values within the odd slots may be permuted freely among themselves, as may the even values. This makes it possible to count all completions of a candidate prefix without generating them.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Core Step 3

The source precomputes `factorial[r] = r!` for every $r$ through $n$. It stores all unused values in ascending list `available`, tracks their counts with `odd_left` and `even_left`, converts the one-based input `k` to zero-based `rank = k - 1`, and constructs `answer` from left to right.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[3, 4, 1, 2]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 4, "k": 6}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[3, 4, 1, 2]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Generate all permutations and filter:** There are $n!$ permutations, making enumeration impossible even for moderate $n$.
- **Generate only alternating permutations:** Their count is still the product of odd and even factorials, which is enormous.
- **Use a generic permutation factorial number system:** It ignores forced parity slots; each prefix block here has `odd! * even!` completions rather than simply `remaining!`.
- **Cap factorials at \(10^{15}+1\):** This would reduce big-integer work because larger exact counts are indistinguishable for the allowed rank, but the protected source stores exact factorials.
- **Odd \(n\):** Only an odd first value can use the one extra odd number without breaking alternation.
- **Even \(n\):** Odd-starting and even-starting permutations are both valid and appear interleaved by their actual first values in lexicographic order.
- **\(n=1\):** The sole valid permutation is `[1]`; larger `k` values return an empty list.
- **Rank exactly at a block boundary:** The `rank >= block` comparison skips the entire earlier block, correctly selecting the first permutation of the next block.
- **One-based input rank:** Subtracting one at initialization is essential; `k=1` must select the first feasible candidate at every position.
- **Unavailable parity:** The remaining-count test prevents selecting a value that would strand too many numbers of one parity.
- **List mutation:** The chosen value is popped only after its block is selected, and the candidate loop ends immediately afterward.
- **Out-of-range \(k\):** Failure to select at any position returns `[]` as required.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n^2)$. Factorial precomputation costs $O(n)$ conventional arithmetic operations. At each of $n$ positions, the algorithm may scan $O(n)$ available candidates. Removing a selected list element can also shift $O(n)$ references. Total conventional time is $O(n^2)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
