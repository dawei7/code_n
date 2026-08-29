# Guided Example: Removing Minimum Number of Magic Beans

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"beans": [4, 1, 6, 5]}`
- **Required output:** `4`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of **positive** integers `beans`, where each integer represents the number of magic beans found in a particular magic bag.

The objective is to compute `4` from `{"beans": [4, 1, 6, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Turn minimization into retained-bean maximization

Let `s = sum(beans)` be the original total. If a plan retains $R$ beans, it removes exactly $s-R$. Because $s$ is fixed, minimizing removed beans is identical to maximizing retained beans.

For a chosen target $x$, every surviving bag contains exactly $x$. If $k$ bags survive, the retained total is $xk$. This means the algorithm only needs to determine which target values are worth considering and how many bags can support each one.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"beans": [4, 1, 6, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Sort to make eligible bags a suffix

After `beans.sort()`, the counts are in nondecreasing order. At index `i`, let `x = beans[i]`. Every bag before `i` has a count no greater than $x$, and every bag from `i` onward has at least $x$ beans.

Using $x$ as the common amount, the algorithm empties all bags before `i` and reduces all `n-i` bags in the suffix to exactly $x$. Those surviving bags retain

$$
x(n-i)
$$

beans in total. The number removed is consequently

$$
s-x(n-i).
$$

The generator expression computes this value for every pair `(i, x)` produced by `enumerate(beans)`, and `min` returns the smallest removal total.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why an optimal target is one of the original bag sizes

At first, it may appear necessary to try every positive integer up to the largest bag. That is not needed.

Consider any feasible target $t$ and the bags that remain nonempty. If every surviving bag originally contained strictly more than $t$, then $t$ can be increased until it reaches the smallest original count among those survivors. The same bags can still support the larger target, and increasing the retained amount in every survivor removes fewer beans. Therefore the smaller $t$ could not have been optimal.

So, in an optimal plan, the target equals the original size of at least one surviving bag—specifically, the smallest survivor. Every such value appears somewhere in the sorted array and is considered by the generator.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `4` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"beans": [4, 1, 6, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `4` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Prefix sums after sorting:** Explicit prefix sums can calculate removal from the emptied prefix and reduced suffix separately. They are correct but unnecessary because total original beans minus total retained beans gives the candidate in one formula.
- **Frequency counting by value:** Since bag sizes are bounded, a frequency array can aggregate equal counts and scan possible targets. This can avoid comparison sorting but uses space tied to the maximum value and is less direct than the stored solution.
- **Try every positive target:** Values between consecutive bag sizes cannot be better than raising the target to the next eligible bag size, so testing them wastes work.
- **Keep only the largest bag:** This is always legal and corresponds to the last sorted index, providing a fallback candidate.
- **One bag:** Choosing its existing size removes zero beans, and the only generator candidate returns zero.
- **All bags equal:** The first occurrence keeps all beans, so the answer is zero.
- **Highly uneven counts:** Emptying many small bags may be cheaper than reducing a very large bag to a tiny common amount; checking all targets captures this tradeoff.
- **Duplicate target values:** Later equal occurrences keep fewer bags and cannot improve on the first occurrence, but including them does not change the minimum.
- **Positive-input guarantee:** Every considered target is positive, so every suffix bag remains nonempty as required.
- **No bean transfers:** The retained-total formula never moves beans between bags; it only discards the difference between original and final totals.
- **All eligible bags should remain:** Once a bag has at least the target, keeping $x$ beans from it strictly increases retention and has no effect on other bags.
- **Input mutation:** `beans.sort()` permanently reorders the caller's list. The returned count is correct, but callers that need the original order must pass a copy or use `sorted(beans)` in a different implementation.
- **Generator memory:** `min` consumes candidate values lazily, so the formula does not allocate a separate length-$n$ list.
- **Large totals:** With up to $10^5$ bags and $10^5$ beans per bag, the total can reach $10^{10}$; Python handles this exactly.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the number of bags. Python's sort takes $O(n\log n)$ time. Computing the sum is $O(n)$, and the generator evaluates one constant-time arithmetic expression for each element, adding another $O(n)$. Sorting dominates, so total time is $O(n\log n)$.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
