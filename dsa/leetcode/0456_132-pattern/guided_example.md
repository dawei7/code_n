# Guided Example: 132 Pattern

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nums": [1, 2, 3, 4]}`
- **Required output:** `false`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

Given an array of `n` integers `nums`, a **132 pattern** is a subsequence of three integers $\text{nums}[i]$, $\text{nums}[j]$ and $\text{nums}[k]$ such that `i < j < k` and $\text{nums}[i] < \text{nums}[k] < \text{nums}[j]$.

The objective is to compute `false` from `{"nums": [1, 2, 3, 4]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Meaning of the stack and `vk`

`stk` contains unresolved suffix values that may serve as the “3” of a future pattern. From bottom to top it is monotonically nonincreasing: larger values are below, and smaller or equal values are above.

`vk` starts at negative infinity. Once a stack value is popped by a larger value `x`, that popped value is certified as a possible “2”: `x` occurs to its left in the original array and is strictly larger, so together they satisfy

$$
\text{popped value} < x.
$$

Here `x` can play the “3” and the popped value can play the “2.” `vk` stores the strongest such “2” established so far. If a still-earlier value is smaller than `vk`, the three values and their scan order form the required 132 pattern.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nums": [1, 2, 3, 4]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Why the check happens before stack updates

For each reverse-scanned value `x`, the first operation is `if x < vk`. At that moment, `vk` came from a `(3, 2)` pair located entirely to the right of `x` in the original array. Therefore using `x` as the “1” automatically gives the correct index order $i<j<k$. The strict inequality supplies the remaining value relation.

Only after this check does the code let `x` act as a possible “3.” Checking afterward could incorrectly try to use the same array position as two roles.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | Evaluate transition invariant | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: Why popping smaller values finds a `(3, 2)` pair

While the stack top is strictly smaller than `x`, the code pops it and assigns it to `vk`. The current `x` appears earlier in the original array than every stack element because of the reverse scan. Thus each pop proves a pair with `x` as `nums[j]` and the popped value as `nums[k]`, satisfying both $j<k$ and `nums[k] < nums[j]`.

Because the stack is decreasing from bottom to top, popped values come off in nondecreasing order. The last popped value is the largest one below `x`, making it the easiest certified “2” for an earlier number to fall below. The stack structure also prevents a previously stronger certified value from being lost: either a later `x` cannot cross the larger barrier that certified it, or it crosses that barrier and establishes an even larger candidate.

After all smaller tops are removed, `x` is appended. The remaining top, if any, is greater than or equal to `x`, so appending preserves the monotonic order. Equal values are not popped because the pattern requires a strict `nums[k] < nums[j]` relation.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `false` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nums": [1, 2, 3, 4]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `false` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **Check every triple:** It directly follows the definition but takes $O(n^3)$ time.
- **Prefix minimum plus suffix scan:** Fix the “3,” use the minimum value to its left, and scan its right side for a middle value. This improves to $O(n^2)$ but repeats suffix work.
- **Prefix minima plus a monotonic stack:** Another linear method explicitly stores the best “1” for every position and searches right-side “2” candidates. It uses $O(n)$ space but more state than the exact reverse-stack solution.
- **Balanced search structure:** Scanning possible middle indices while querying a suffix set can take $O(n\log n)$ time.
- **Fewer than three values:** No triple exists. The loop performs harmless stack operations and returns `false`.
- **Strict inequalities:** Equal values never form either `<` relation. The stack pops only with `<`, and detection also uses `<`.
- **Strictly increasing input:** Reverse scanning keeps popping, but no earlier value is smaller than the certified middle in the needed index arrangement, so no pattern is reported.
- **Strictly decreasing input:** Nothing is popped because reverse-scanned values keep getting smaller; `vk` remains negative infinity.
- **Negative values:** Starting `vk` at `-inf` works below every legal integer, and comparisons are otherwise unchanged.
- **Reversed-copy cost:** The exact syntax duplicates the array. An iterator can remove that copy if constant factors matter.
- **Off-by-one errors:** verify loop termination conditions and inclusive/exclusive interval bounds.
- **Degenerate inputs:** handle minimum-sized inputs without null references or out-of-bounds access.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(n)$. Let $n$ be the array length. Each value is pushed onto `stk` once. A value can be popped at most once, so all executions of the inner `while` loop across the entire scan total at most $n$. The monotonic-stack work is therefore $O(n)$ time.
- **Auxiliary Space Complexity:** $O(n)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
