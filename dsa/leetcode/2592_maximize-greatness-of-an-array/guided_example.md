# Guided Example: Maximize Greatness of an Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 3, 5, 2, 1, 3, 1]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a 0-indexed integer array `nums`. You are allowed to permute `nums` into a new array `perm` of your choosing.

The objective is to compute `4` from `{"nums": [1, 3, 5, 2, 1, 3, 1]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Treat the permutation as a one-to-one matching

Every original occurrence `nums[i]` is a target that would like to receive a strictly larger occurrence from the same multiset. Each value used in `perm` can occupy only one index, so the problem is to form as many disjoint pairs

$$
(\textit{target},\textit{replacement})
$$

as possible with `replacement > target`.

Original index order does not constrain which occurrence may replace which, so sorting the values exposes a standard greedy matching problem.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 3, 5, 2, 1, 3, 1]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Meaning of the pointer

After `nums.sort()`, pointer `i` identifies the smallest target value that has not yet been successfully matched. The loop visits every sorted value `x` as a possible replacement, also from smallest to largest.

If `x > nums[i]`, this replacement beats the current smallest unmatched target. The algorithm forms that pair and increments `i`.

If `x <= nums[i]`, `x` cannot beat the smallest unmatched target. Since all other unmatched targets are at least as large, it cannot beat any of them. The candidate is skipped as a replacement.

At the end, `i` equals the number of successful pairs and therefore the maximum number of indices where `perm[i] > nums[i]` can hold.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why using the smallest feasible replacement is safe

Suppose candidate $x$ is the first scanned value large enough to beat smallest unmatched target $a$. Matching them uses the weakest currently feasible replacement.

If an optimal matching leaves $x$ unused but matches $a$ with a later value $y\ge x$, replace $y$ by $x$ for target $a$. The pair remains valid and the number of matches is unchanged, while $y$ becomes available.

If the optimal matching uses $x$ for a larger target $b\ge a$, while $a$ is matched by $y\ge x$ or left unmatched, swap so $x$ matches $a$. If $b$ was also matched, give it $y$; the ordered structure preserves feasibility whenever that original larger replacement existed. This exchange produces an equally large matching agreeing with greedy.

Repeating the argument at each successful scan proves immediate matching cannot reduce the final cardinality.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 3, 5, 2, 1, 3, 1]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Maximum-frequency formula:** Count occurrences and return $n-\text{maxFrequency}$ in expected $O(n)$ time and $O(n)$ space, matching the manifest summary.
- **Two explicit pointers:** Scan a small-target pointer and a large-candidate pointer over the sorted array; it is equivalent to the compact loop.
- **Try permutations:** There are $n!$ arrangements, far beyond feasible.
- **All values equal:** No strict comparison can succeed, and the answer is zero.
- **Strictly increasing values:** Every value except the largest can be matched with its successor, giving $n-1$.
- **Duplicates:** Occurrences remain distinct pairing resources even though their values compare equal.
- **Strict inequality:** Equal candidates must be skipped; using `>=` would solve a different problem.
- **Single element:** It cannot be greater than itself after permutation, so the result is zero.
- **Input mutation:** `nums.sort()` destroys original ordering.
- **Manifest distinction:** The code is sorting-based $O(n\log n)$ matching, not linear frequency counting.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length. Sorting takes $O(n\log n)$ time, and the scan takes $O(n)$. The exact total is $O(n\log n)$, not the manifest's $O(n)$ frequency-based bound.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
