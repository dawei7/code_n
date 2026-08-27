# Guided Example: Find Polygon With the Largest Perimeter

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [5, 5, 5]}`
- **Required output:** `15`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an array of **positive** integers `nums` of length `n`.

The objective is to compute `15` from `{"nums": [5, 5, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Use the complete polygon inequality

For positive side lengths sorted as $a_1 \le a_2 \le \cdots \le a_k$, they can form a nondegenerate polygon exactly when the longest side is strictly smaller than the sum of all other sides:

$$
a_k < a_1+a_2+\cdots+a_{k-1}.
$$

The implementation sorts `nums` and builds prefix sums `s` with `s[0] = 0`. Thus `s[k]` is the sum of the first $k$ sorted values. For the prefix of length $k$, `nums[k - 1]` is its longest side and `s[k - 1]` is the sum of its other sides. The exact validity check is therefore

`s[k - 1] > nums[k - 1]`.

The loop begins at `k = 3` because a polygon needs at least three sides.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [5, 5, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why only sorted prefixes need to be considered

Suppose a candidate polygon’s longest chosen side is `nums[t]`. Every positive value before it that was not selected can be added as another side. Adding a positive side increases the perimeter and increases the sum on the “other sides” side of the inequality, while the longest side does not increase. Therefore, adding an omitted smaller or equal value cannot destroy validity and strictly improves the perimeter.

Consequently, for a fixed longest chosen side, the best candidate includes every sorted value through that side: it is a prefix. There is no reason to search arbitrary subsets. Any optimal polygon can be expanded into the complete prefix ending at its longest side, unless it already is that prefix.

This positive-value argument is essential. If zero or negative side lengths were allowed, adding every earlier number would not necessarily increase the perimeter or preserve the geometric meaning. The source constraints guarantee positive integers.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Suppose a candidate polygon’s longest chosen side is `nums[t... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Evaluate every possible longest side

For each prefix length $k$ from three through $N$, the implementation tests the inequality. When it holds, `s[k]` is the perimeter of a valid polygon and is compared with `ans`.

The prefix length can alternate between invalid and valid as larger sides are considered. For example, a sudden very large value may exceed the sum accumulated before it. Additional later positive values might eventually make another prefix valid under a different longest side. Scanning all $k$ values is therefore the straightforward complete method.

`ans` begins at `-1`, the required result when no valid polygon exists. The code uses `max(ans, s[k])` rather than assuming the most recently seen valid prefix is always the answer. Since all values are positive, prefix sums do increase, so a later valid prefix has a larger perimeter, but the explicit maximum makes the intended optimization unambiguous.

For `nums = [1, 12, 1, 2, 5, 50, 3]`, sorting gives `[1, 1, 2, 3, 5, 12, 50]`. Prefixes through five satisfy the polygon condition when appropriate, and the length-five prefix has perimeter twelve because `1 + 1 + 2 + 3 > 5`. Adding side twelve fails because the preceding sum is exactly twelve, not strictly greater. Side fifty also fails. The best stored perimeter remains twelve.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `15` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [5, 5, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `15` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Try every subset:** There are exponentially ma:** - **Try every subset:** There are exponentially many subsets. Positivity proves that the best candidate for each longest side is its complete sorted prefix.
- **Running sum without a prefix list:** The editorial-style implementation can keep one scalar sum and achieve the same $O(N\log N)$ time with less explicit storage, but the exact solution materializes `s`.
- **Only test triples:** A valid polygon may need four or more smaller sides to outweigh a long side, so triangle-only logic misses answers such as the five-side optimum in the example.
- **Equality:** `sum(other sides) == longest` is degenerate and must be rejected; the comparison is strict.
- **Exactly three inputs:** The single prefix is tested as an ordinary triangle.
- **No valid prefix:** `ans` remains `-1`, matching the required failure value.
- **Duplicate lengths:** They are separate usable sides and all contribute to the prefix sum.
- **Large sums:** The perimeter can exceed 32-bit integer range; Python’s unbounded integers avoid overflow.
- **Input mutation:** The array remains sorted after the call.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N\log N)$. Let $N$ be the number of side lengths. Sorting costs $O(N\log N)$ time. Constructing the prefix sums and scanning all candidate prefix lengths each cost $O(N)$, so the total time is $O(N\log N)$.
- **Auxiliary Space Complexity:** $O(N)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
