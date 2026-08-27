# Guided Example: Smallest Absent Positive Greater Than Average

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [3, 5]}`
- **Required output:** `6`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given an integer array `nums`.

The objective is to compute `6` from `{"nums": [3, 5]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Finding the first integer strictly above the average

Let

$$
S = \sum_{x \in \texttt{nums}} x
$$

and let $n$ be the number of elements. The exact average is $S/n$. We need the smallest integer $k$ for which

$$
k > \frac{S}{n}.
$$

For any real number $a$, the smallest integer strictly greater than $a$ is

$$
\lfloor a \rfloor + 1.
$$

This formula also handles an average that is already an integer. For example, if the average is exactly $4$, the answer must start at $5$, not $4$, because the comparison is strict. If the average is $4.7$, its floor is $4$, so the first integer above it is again $5$.

The implementation computes this value as:

`sum(nums) // len(nums) + 1`

Python's `//` operator performs floor division when the divisor is positive, and `len(nums)` is always positive because the array is nonempty. That detail matters for negative sums. For instance, $-3/2=-1.5$, and `-3 // 2` is $-2$, the mathematical floor, so adding one gives $-1$, the smallest integer strictly greater than $-1.5$. No floating-point calculation is needed, so there is no danger of rounding an average such as $2/3$ incorrectly.

The requested result must also be positive. Therefore, if the first integer above the average is zero or negative, the search should begin at $1$. The line

`ans = max(1, sum(nums) // len(nums) + 1)`

combines both lower bounds. After this line, `ans` is exactly the smallest positive integer that is strictly greater than the average. It is not merely a convenient starting point: every smaller integer violates at least one of the two numerical requirements.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [3, 5]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Making absence checks fast

The remaining question is whether the candidate occurs in `nums`. Repeatedly searching the original list would cost linear time per candidate. Instead, the solution creates

`s = set(nums)`

so membership checks are expected constant-time operations. Duplicates do not need special handling because the question only asks whether a value appears at least once.

If `ans` is in the set, it cannot be returned, so the only possible next candidate is `ans + 1`. The loop keeps increasing the candidate by one:

`while ans in s:`

`    ans += 1`

When the loop stops, `ans` is absent. Increasing an integer preserves both positivity and the property of being strictly greater than the average, so no numerical condition needs to be checked again.

Consider `nums = [3, 5]`. Its average is $4$, so the initial candidate is $5$. Because $5$ is present, the loop advances to $6$. Six is absent, and it is returned. This also explains why simply returning the first integer above the average would be insufficient.

As another example, take `nums = [-4, -2, 1]`. The average is $-5/3$, and its floor is $-2$. Adding one gives $-1$, but the result must be positive, so `max` changes the starting candidate to $1$. Since $1$ is present, the loop advances to $2$, which is the answer.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The remaining question is whether the candidate occurs in `n... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why stopping at the first missing candidate gives the minimum

At initialization, every positive integer smaller than `ans` is disqualified because it is not strictly above the average. During the loop, each value that the algorithm passes over is disqualified because the set confirms that it is present in `nums`. Consequently, when the loop reaches its first absent value, every smaller positive integer has a known reason that it cannot be returned. The current value satisfies every requirement, so it is the smallest valid result.

The answer is guaranteed to be found. The array contains only finitely many distinct values, while the positive integers continue forever. Even if several consecutive values beginning at the threshold are present, eventually the loop reaches one that is not in the finite set.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `6` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [3, 5]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `6` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Sorting first:** Sorting the distinct values w:** - **Sorting first:** Sorting the distinct values would also make it possible to walk upward from the threshold, but sorting costs $O(n \log n)$ time. The hash set preserves linear expected time and expresses the only needed operation—membership—directly.
- **Repeated list membership checks:** Testing `ans in nums` without building a set can scan the whole array for every candidate. With up to $n$ consecutive candidates present, that approach can take $O(n^2)$ time.
- **Floating-point average:** Computing `sum(nums) / len(nums)` and then rounding introduces unnecessary floating-point behavior. Exact floor division gives the correct strict integer threshold for positive, zero, and negative sums.
- **An integral average:** If the average is exactly $a$, the search must begin at $a+1$, because “strictly greater” excludes $a$. The added one after floor division handles this automatically.
- **A negative average:** Positivity becomes the stronger lower bound, so the search begins at $1$. The `max(1, ...)` operation is essential here.
- **The initial candidate is present:** The loop skips it and every immediately following present value. For `[3, 5]`, it skips $5$ and returns $6$.
- **Duplicates:** Multiple copies of a number have the same effect as one copy: that number is present and must be skipped. Converting to a set intentionally removes multiplicity.
- **Values below the threshold:** Their presence is irrelevant because none can satisfy the strict-average requirement. The algorithm never wastes time searching downward.
- **A long consecutive run:** Even if all of the next several integers occur in the array, each successful loop iteration skips a distinct set member, so the scan remains linear overall.
- **Off-by-one errors: verify loop termination conditi:** Off-by-one errors: verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs: handle minimum-sized inputs wit:** Degenerate inputs: handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n + k)$. Let $n$ be `len(nums)`, and let $k$ be the number of consecutive present integers beginning with the initial candidate.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
