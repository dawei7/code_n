# Guided Example: Minimum Absolute Distance Between Mirror Pairs

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [12, 21, 45, 33, 54]}`
- **Required output:** `1`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `1` from `{"nums": [12, 21, 45, 33, 54]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Store what future value each earlier index needs

For an earlier index `j` to pair with a future value, that future value must equal `reverse(nums[j])`. The dictionary `pos` maps this required future value to the latest earlier index that produces it.

When current value `x=nums[i]` arrives, checking `x in pos` immediately finds an earlier `j` with

$$
\operatorname{reverse}(\texttt{nums}[j])=x.
$$

Then `i-j` is a valid mirror-pair distance.

After checking, the source computes `reverse(x)` and stores `pos[reverse(x)]=i` so the current index can serve as the left endpoint of a future pair.

The check happens before insertion, ensuring `i<j` direction and preventing an index from pairing with itself.

The dictionary keys deserve special attention. A key is not necessarily a value already seen in the array. It is the value that would complete a pair for some earlier index. For example, after reading 120, the map contains key 21 because a future 21 is wanted. This “store the future requirement” viewpoint allows the current lookup to use `x` directly.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [12, 21, 45, 33, 54]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Reverse digits arithmetically

The helper repeatedly takes `x%10` and appends it to `y` using `y=y*10+digit`. Integer division removes the processed digit.

Trailing zeros of the original become leading zeros of the reversed sequence and naturally disappear numerically. For 120, steps build zero, two, then 21, producing the required result.

This directionality matters: reversing 120 gives 21, but reversing 21 gives 12, not 120.

For a positive number with `D` decimal digits, the loop runs exactly `D` iterations. Each iteration transfers the current last digit into the result. When the original number ends in zero, that zero is transferred first while `y` is still zero, so it does not create a visible leading digit. No special trimming rule is needed.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why only the latest index per required value is needed

For a fixed current right endpoint `i` and required value `x`, the closest valid earlier index minimizes `i-j`. Among all earlier indices stored under key `x`, the largest `j` is therefore always best.

Overwriting `pos[reverse(x)]` with the current index discards older endpoints that can never beat it for any future right endpoint. If future index `t>i` needs the same key, `t-i<t-j` for every older `j`.

The global `ans` keeps the minimum across all current endpoints and required-value keys.

For `[12,21,45,33,54]`, processing 12 stores key 21 at index zero. Current 21 finds it and records distance one. Processing 45 later stores key 54, which current 54 finds at distance two; the global minimum remains one.

For `[21,120]`, processing 21 stores key 12. Current 120 does not find key 120, so no pair is reported, correctly respecting direction.

A short map trace for `[120,8,21]` makes the order concrete. At index zero, 120 is not found and the scan stores `pos[21]=0`. At index one, 8 is not found, then `pos[8]=1` is stored because 8 reverses to itself. At index two, current value 21 finds index zero, producing distance two. Only after that lookup does the scan store `pos[12]=2`.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `1` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [12, 21, 45, 33, 54]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `1` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Check all index pairs:** Reversing and comparing every pair costs $O(n^2D)$. Required-value hashing reduces the pair search.
- **Store the earliest index:** That maximizes rather than minimizes distance for a fixed future endpoint. Latest is required.
- **Reverse the current value and search original earlier values:** That changes the directional condition for trailing-zero cases and is not equivalent.
- **String reversal:** `int(str(x)[::-1])` is valid and has the same digit complexity; the exact source uses arithmetic.
- **Palindromic value:** It can pair with the same value at a later distinct index.
- **Trailing zeros:** Arithmetic reversal omits their new leading zeros automatically.
- **Single element:** No earlier endpoint exists, so answer is `-1`.
- **Multiple valid earlier endpoints:** Overwriting retains the closest one.
- **Repeated palindromes:** For values such as 7 or 121, each new copy first pairs with the previous copy and then replaces it as the nearest endpoint for the future.
- **Distance one:** It is the smallest possible and may be found for adjacent mirror values.
- **Hash collisions:** Python dictionary semantics provide expected constant-time lookup while preserving exact key equality.
- **Manifest time:** Linear time assumes the bounded digit width; generalized complexity is $O(nD)$.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(nD)$. Let `n` be the array length and `D` the maximum decimal digit count. Reversing one value takes $O(D)$ time, so total expected time is $O(nD)$ including hash operations.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
