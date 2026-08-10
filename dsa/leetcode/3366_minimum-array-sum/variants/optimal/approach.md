## General

**Track how many limited operations have been assigned.** Choices on one element affect the global budgets available for later elements, so optimizing each value independently is unsafe. The source uses

`f[i][j][k]`

for the minimum sum of the first `i` elements after using exactly `j` divide-by-two operations and exactly `k` subtraction operations.

Every state begins at infinity except `f[0][0][0] = 0`. Infinity prevents an unreachable operation-count combination from becoming a false minimum.

The source parameter `d` is the quantity named `k` in the description. Renaming it locally avoids colliding with the DP loop variable `k`, but the operation still means subtract `d`.

**Leave the current value unchanged.** From a reachable state for the first `i-1` elements, doing nothing to current `x` adds its original value:

`f[i-1][j][k] + x`.

This transition is always legal and is important because both operations are optional and bounded by “at most,” not required exactly.

**Apply only the halving operation.** When `j > 0`, the predecessor used one fewer operation 1. Integer ceiling division is

$$
\left\lceil\frac{x}{2}\right\rceil
=\frac{x+1}{2}\text{ with floor integer division},
$$

implemented as `(x + 1) // 2`.

**Apply only subtraction.** When `k > 0` and original `x >= d`, the predecessor uses one fewer operation 2 and current contribution is `x - d`. The value check enforces the operation's legality.

**Apply both operations in either order.** Order can change the result and even legality.

If halving happens first, `y = (x + 1) // 2`. Subtraction may follow only when `y >= d`, producing `y - d`.

If subtraction happens first, it requires `x >= d` and leaves `x-d`. Halving that value produces `(x - d + 1) // 2`.

The DP tests both expressions and takes the smaller legal total. This is essential: subtraction before halving often gives a smaller number, but it is not universally interchangeable with halving before subtraction.

Both transitions come from `f[i-1][j-1][k-1]` because each operation is used once on the current index. No transition applies the same operation twice to one element.

**Why prefix DP prevents index reuse.** Every transition moves from layer `i-1` to layer `i` and makes one complete choice for element `i-1`. Once the next layer begins, that element is never revisited. The “at most once per index” rule is therefore built into the layer structure.

**Convert exact-use states to at-most budgets.** The final answer takes the minimum of `f[n][j][k]` over every `0 <= j <= op1` and `0 <= k <= op2`. This permits unused operations. Reading only `f[n][op1][op2]` would incorrectly force both budgets to be exhausted.

**Why all valid operation plans appear.** For each element, a valid plan chooses exactly one of four categories: neither operation, only operation 1, only operation 2, or both in one of two orders. The recurrence contains every legal category and combines it with every feasible budget allocation for the preceding prefix. Conversely, every transition respects eligibility and per-index limits. Induction over `i` makes each state the minimum for its exact counts.

**Trace an order-sensitive value.** If `x=10` and `d=6`, halving first gives five, after which subtraction is illegal. Subtracting first gives four and then halving gives two. The two-order checks retain the legal result two rather than assuming both operations commute.

**The source stores all prefix layers.** Although each transition reads only layer `i-1`, `f` is allocated for all `n+1` layers. This is simpler to index but materially affects the space bound.

## Complexity detail

There are $(n+1)(\texttt{op1}+1)(\texttt{op2}+1)$ states. Each performs constant transition work, so time is

$$
O(n\cdot\texttt{op1}\cdot\texttt{op2}).
$$

The exact three-dimensional table occupies the same asymptotic number of entries:

$$
O(n\cdot\texttt{op1}\cdot\texttt{op2})
$$

space. This contradicts the manifest's $O(\texttt{op1}\cdot\texttt{op2})$ space claim, which would require rolling two prefix layers. With both budgets as large as $n$, the exact allocation can be cubic and may be impractical.

## Alternatives and edge cases

- **Rolling two DP layers:** It preserves all transitions and reduces space to the manifest's $O(\texttt{op1}\cdot\texttt{op2})$.
- **Greedy largest reduction:** It can spend an operation needed for a better combined choice elsewhere and ignores order effects.
- **Top-down memoization:** It explores the same state space recursively and can skip unreachable states, but adds recursion overhead.
- **No operations available:** Only unchanged transitions survive, returning the original sum.
- **`x < d`:** Subtraction cannot be the first or only operation.
- **Halving drops below `d`:** The halve-then-subtract order becomes illegal even when subtract-then-halve is legal.
- **`d = 0`:** Subtraction changes nothing and may always be omitted; the final minimum over unused budgets handles this.
- **`x = 0`:** Halving leaves zero, and subtraction is legal only when `d=0`.
- **Odd value:** `(x+1)//2` implements required upward rounding.
- **Both orders equal:** Testing both is harmless; the minimum simply sees duplicate costs.
- **At-most budgets:** Final minimization over all `j,k` is necessary.
- **Infinity states:** Arithmetic with `inf` remains infinite and cannot create a false finite optimum.
- **Parameter naming:** Source `d` corresponds to statement parameter `k`.
- **Manifest mismatch:** Exact source retains $n+1$ layers rather than rolling them.
- **Memory risk:** At maximum budgets, Python's nested cubic table can exceed practical memory despite the correct recurrence.
- **Input preservation:** The DP computes contributions without changing `nums`.
