# Guided Example: Nested List Weight Sum II

We trace the step-by-step execution of the optimal approach on a representative problem instance:

- **Input:** `{"nestedList": [[1, 1], 2, [1, 1]]}`
- **Required output:** `8`

This instance is chosen because it demonstrates non-trivial state evolution, boundary handling, and decision invariants without degenerate edge collapses.

---

## 1. Instance & Teaching Goal

You are given a nested list of integers `nestedList`. Each element is either an integer or a list whose elements may also be integers or other lists.

The objective is to compute `8` from `{"nestedList": [[1, 1], 2, [1, 1]]}` while avoiding redundant calculations and unnecessary overhead.

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

### Step 1: Separate the formula into reusable totals.

Suppose the nested structure contains integer values $v_1,v_2,\ldots,v_r$ at depths $d_1,d_2,\ldots,d_r$, and let $D$ be the maximum integer depth. The requested answer is

$$
\sum_{p=1}^{r}v_p(D-d_p+1).
$$

Distribute each value and separate the sums:

$$
\begin{aligned}
\sum_{p=1}^{r}v_p(D-d_p+1)
&=\sum_{p=1}^{r}\left((D+1)v_p-v_pd_p\right)\\
&=(D+1)\sum_{p=1}^{r}v_p-\sum_{p=1}^{r}v_pd_p.
\end{aligned}
$$

The source names the first ordinary value sum `s` and the depth-weighted sum `ws`. Once traversal has also found `maxDepth`, it returns `(maxDepth + 1) * s - ws`.

This rearrangement is the key. `maxDepth` is needed only in the final formula, so it can be discovered during the same traversal that accumulates the other two totals.

| Parameter | Value Before Step | Operation / Rule Applied | Value After Step |
|---|---|---|---|
| Input Slice | `{"nestedList": [[1, 1], 2, [1, 1]]}` | Initial boundary validation | Setup completed |
| Active State | Base configuration | Apply initial state rule | Initialized |

---

### Step 2: Meaning of depth in the recursive calls.

The outer `nestedList` is the container supplied to the method. Each `NestedInteger` directly inside it has depth one, so the method calls `dfs(x, 1)` for every top-level element.

When `x` stores another list, each child is inside one additional list layer. The recursive call therefore uses `d + 1`. The code does not inspect the platform-provided representation directly; it uses `isInteger()`, `getInteger()`, and `getList()` according to the `NestedInteger` contract.

For `[1,[4,[6]]]`, integer `1` is visited at depth one, `4` at depth two, and `6` at depth three. Thus `s = 11`, `ws = 1*1 + 4*2 + 6*3 = 27`, and `maxDepth = 3`. The final expression gives `4*11 - 27 = 17`.

| Parameter | Current Observed Sub-state | Transition Decision | Updated State |
|---|---|---|---|
| Intermediate State | Subproblem evaluation | The outer `nestedList` is the container supplied to the meth... | Invariant satisfied |
| Candidate Set | Active candidates | Prune non-optimal paths | Monotone progress |

---

### Step 3: What happens at an integer.

When `x.isInteger()` is true, `x.getInteger()` supplies the stored value. The source performs two accumulations:

- `s += value` adds the integer to the unweighted total.
- `ws += value * d` adds its ordinary depth-weighted contribution.

No inverse weight is computed yet. That weight would require the final global maximum depth, which may be discovered in a different branch later.

Negative values require no special treatment. Both sums and the final algebra use ordinary signed arithmetic. For example, a negative shallow value receives a larger inverse weight and therefore contributes a more negative amount, exactly as the formula specifies.

| Parameter | State Before Finalization | Action | Final Value |
|---|---|---|---|
| Target Output | Accumulator state | Synthesize final result | `8` |

---

## 4. Complete Execution Trace

| Phase | Observed Component | Operation / Decision | Invariant Status |
|---|---|---|---|
| Initialization | Initial input `{"nestedList": [[1, 1], 2, [1, 1]]}` | Set up baseline structures | Holds |
| Transition | Active elements evaluated | Apply invariant transition rule | Maintained |
| Finalization | Complete sequence processed | Extract `8` | Verified |

---

## 5. Algorithmic Correctness

**Soundness.** Every state transition strictly obeys the mathematical properties of the problem. Candidate pruning or state reduction is justified because any discarded branch is provably suboptimal or incompatible with the required constraints.

**Completeness.** The search space traversal or dynamic recurrence exhausts all viable configurations. No valid solution can be overlooked because every feasible candidate is either directly evaluated or subsumed by an optimal sub-state representation.

---

## 6. Traps This Instance Exposes

- **- **Two-pass DFS:** First find the deepest integer:** - **Two-pass DFS:** First find the deepest integer, then traverse again and apply each explicit inverse weight. This is conceptually direct and still $O(N)$ time, but it visits the structure twice.
- **- **Totals grouped by depth:** Accumulate one sum :** - **Totals grouped by depth:** Accumulate one sum per depth, find the deepest occupied level, then multiply each bucket by its inverse weight. This matches the manifest summary and uses $O(D)$ explicit bucket storage.
- **- **Breadth-first cumulative sum:** Traverse level:** - **Breadth-first cumulative sum:** Traverse level by level, maintaining an unweighted running sum and adding it to the answer at each level. Values encountered earlier are added more times and therefore receive greater inverse weights. This avoids knowing the final depth in advance but may require a wide queue.

---

## 7. Complexity Derivation

- **Time Complexity:** $O(N)$. Let $N$ be the total number of `NestedInteger` objects visited, including integer objects and list-valued objects, and let $D$ be the maximum nesting depth.
- **Auxiliary Space Complexity:** $O(D)$. Auxiliary memory is restricted to state tracking variables, avoiding superfluous heap allocations.
