# Guided Example: Can Make Arithmetic Progression From Sequence

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"arr": [3, 5, 1]}`
- **Required output:** `true`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

A sequence of numbers is called an **arithmetic progression** if the difference between any two consecutive elements is the same.

The objective is to compute `true` from `{"arr": [3, 5, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Why sorting reveals the only possible progression order

An arithmetic progression has one constant difference between every adjacent pair. If a collection of numbers can be rearranged into such a progression, arranging it in nondecreasing order must also form a progression. A positive-difference progression appears in ascending order, a negative-difference progression appears in descending order, and a zero-difference progression looks the same in every order.

The stored source sorts `arr` in place. It then defines `d = arr[1] - arr[0]` as the required adjacent gap and checks whether every remaining adjacent pair has that same gap.

The input length is at least two, so accessing positions zero and one is safe. Negative values and duplicate values require no special syntax: subtraction handles negatives, and all-equal input produces `d = 0`.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"arr": [3, 5, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: How pairwise drives the check

`pairwise(arr)` yields adjacent tuples:

`(arr[0], arr[1])`, `(arr[1], arr[2])`, and so forth.

For each tuple `a, b`, the generator tests `b - a == d`. `all` consumes those Boolean results lazily. It returns false as soon as one adjacent difference disagrees, or true if every pair agrees.

The first pair is tested again even though its difference defined `d`. That comparison is necessarily true, but keeping it in the generator makes the expression uniform. For a two-element array, `pairwise` yields exactly one pair and `all` returns true, as any two numbers can form an arithmetic progression.

The source assumes `pairwise` is available, normally from `itertools`. It was added to Python in version 3.10.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | `pairwise(arr)` yields adjacent tuples:

`(arr[0], arr[1])`,... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why equal sorted gaps are sufficient

If every adjacent sorted difference equals `d`, then

$$
arr[i] = arr[0] + i d
$$

for every index $i$. This follows by repeatedly adding the common adjacent difference. Therefore, the sorted array itself is a valid rearrangement into an arithmetic progression, proving sufficiency.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `true` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"arr": [3, 5, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `true` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Endpoint arithmetic plus set:** Compute minimu:** - **Endpoint arithmetic plus set:** Compute minimum, maximum, and the required gap, then verify every expected term exists with appropriate uniqueness handling. It achieves expected $O(N)$ time and $O(N)$ space.
- **In-place index placement:** Map each value to its required progression index and swap values into position. It can use $O(1)$ extra data but must handle zero difference, divisibility, and duplicates carefully.
- **Sort a copy:** `sorted(arr)` preserves the caller's list but allocates a new list.
- **Two elements:** They always form an arithmetic progression because there is only one adjacent difference.
- **All equal:** The common difference is zero and every comparison succeeds.
- **Duplicates mixed with distinct values:** Sorting exposes a zero gap next to a nonzero gap, so the method returns false.
- **Negative values:** Sorting and subtraction work without modification.
- **Descending valid order:** Sorting converts it to the corresponding ascending progression with the negated common difference.
- **Input mutation:** The exact source permanently sorts `arr`.
- **Early mismatch:** `all` stops checking when the first unequal gap is found, although sorting has already completed.
- **Missing import:** `pairwise` must be supplied from `itertools` in a standalone module.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N\log N)$. Let $N$ be the array length. Python sorting costs $O(N\log N)$ worst-case time. The adjacent-pair generator visits $N-1$ pairs in the worst case, adding $O(N)$. Total time is $O(N\log N)$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
