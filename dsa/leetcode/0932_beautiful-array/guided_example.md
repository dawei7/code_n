# Guided Example: Beautiful Array

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"n": 4}`
- **Required output:** `[2, 1, 4, 3]`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

An array `nums` of length `n` is **beautiful** if:

The objective is to compute `[2, 1, 4, 3]` from `{"n": 4}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: What must be prevented

A beautiful array is a permutation of the integers from `1` through `n` in which no three positions `i < k < j` satisfy `2 * nums[k] = nums[i] + nums[j]`. In other words, the value at a position strictly between two other positions must never be the arithmetic mean of the two endpoint values.

Trying to place the numbers one at a time and testing every earlier pair creates a difficult global search. A choice that appears harmless now can form a forbidden triple after more values are appended. The optimal construction avoids backtracking by exploiting two facts:

- the beautiful property survives a suitable linear transformation of every value;
- an odd number plus an even number can never equal twice an integer.

Those facts let the solution construct the answer recursively from two smaller beautiful arrays.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"n": 4}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why transforming a beautiful array preserves beauty

Suppose an array `a` is already beautiful. Transform each value with `b[x] = p * a[x] + q` for some positive integer `p` and constant `q`. Imagine that three transformed entries at positions `i < k < j` violated the rule:

`2 * b[k] = b[i] + b[j]`.

Substituting the transformation gives `2 * (p * a[k] + q) = (p * a[i] + q) + (p * a[j] + q)`. The two copies of `q` cancel, and dividing by positive `p` leaves `2 * a[k] = a[i] + a[j]`. That would already be a forbidden triple in `a`, contradicting that `a` was beautiful.

The code uses exactly two such transformations:

- `2 * x - 1` turns the integers `1, 2, ..., ceil(n / 2)` into every odd integer from `1` through `n`;
- `2 * x` turns the integers `1, 2, ..., floor(n / 2)` into every even integer from `1` through `n`.

Therefore, if the recursive arrays are beautiful before the transformation, the odd group and the even group remain beautiful internally afterward.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why odd values and even values are separated

The result places all transformed odd values first and all transformed even values second. Consider any possible forbidden triple in the concatenated result.

If both endpoints lie in the odd group, then the middle position also lies inside that earlier group because its index is between them. The transformed odd array is already beautiful, so this case is impossible. The same reasoning applies when both endpoints lie in the even group.

The remaining possibility has the left endpoint in the odd group and the right endpoint in the even group. Their values have different parity, so their sum is odd. However, `2 * nums[k]` is always even for every integer `nums[k]`. An even number cannot equal an odd number, so a triple crossing the boundary is also impossible. This parity argument works regardless of whether the middle position belongs to the odd group or the even group.

Separating by parity is therefore more than an ordering preference: it makes every cross-group endpoint pair automatically safe.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `[2, 1, 4, 3]` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"n": 4}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `[2, 1, 4, 3]` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Memoizing results by size:** Repeated subproblem sizes can occur, so caching may avoid reconstructing identical beautiful arrays. It uses additional retained memory and is unnecessary for the given direct construction, but it can reduce repeated recursive work if the same helper is reused across calls.
- **Iterative doubling construction:** Start with `[1]` and repeatedly form valid odd and even transformations, filtering out values greater than `n`. This uses the same mathematical idea without recursion and can reach `O(n)` generated output work with careful implementation.
- **Backtracking over permutations:** It can test the definition directly, but the search space grows factorially and ignores the parity structure that makes a deterministic construction possible.
- **Random shuffling:** A random permutation might be beautiful, but repeated guessing provides no useful worst-case guarantee and still requires expensive validation.
- **Keeping natural sorted order:** `[1, 2, ..., n]` fails once `n >= 3` because consecutive values form arithmetic progressions; for example, the middle of `1, 2, 3` is exactly their average.
- **The cases `n = 1` and `n = 2`:** No three indices exist, so every permutation is automatically beautiful. The recursion returns valid arrays without special handling for `n = 2`.
- **Odd `n`:** The odd group contains one more value than the even group. Using `(n + 1) >> 1` is what preserves the largest odd value instead of accidentally omitting it.
- **Ordering the two groups:** Placing evens before odds would also support the same parity proof if both transformed groups remained internally beautiful. The code consistently returns odds first.
- **Do not confuse positions with values:** The restriction requires `i < k < j` for positions, then compares the values stored there. The construction controls position ranges by concatenating groups and controls value equality through affine preservation and parity.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. At a call of size `n`, the two recursive subproblems have total size `n`. After they return, the two list comprehensions transform `n` values in total, and concatenating the lists copies `n` references into a new result. Thus the recurrence is `T(n) = T(ceil(n / 2)) + T(floor(n / 2)) + O(n)`. There are `O(log n)` levels, and each level processes `O(n)` total values, giving `O(n log n)` time for this exact implementation.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
