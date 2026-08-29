## General

**View the choice as a subsequence with four stages.** Array `a` always has four elements. The task is to choose four entries of `b` in increasing index order and pair them, in order, with `a[0]` through `a[3]`. The chosen values need not be adjacent, so at every position of `b` the algorithm faces the same decision: skip that value, or use it for the next still-unmatched multiplier.

The exact source models this decision with `dfs(i, j)`. Here `i` is the number of multipliers from `a` already handled, or equivalently the index of the next multiplier to use. The index `j` is the next position of `b` that may be considered. The function returns the maximum additional score obtainable from `a[i:]` and `b[j:]` while preserving order.

**Derive the two transitions.** At state `dfs(i, j)`, one legal choice is not to select `b[j]`. The state then becomes `dfs(i, j + 1)` because the same multiplier still needs a partner but this position of `b` is gone. The other legal choice selects `b[j]` for `a[i]`. That contributes `a[i] * b[j]` immediately, and both indices advance, producing `a[i] * b[j] + dfs(i + 1, j + 1)`. The better of those exhaustive choices is the recurrence:

$$
F(i,j)=\max\left(F(i,j+1),\ a[i]\cdot b[j]+F(i+1,j+1)\right).
$$

This handles negative values correctly. A locally positive product is not automatically best, and a locally negative product may be unavoidable or may enable better later pairings. The recursion compares complete future scores rather than making a short-sighted choice.

**Base cases distinguish completion from failure.** If `i >= len(a)`, all four multipliers have been paired, so no additional score is needed and the function returns zero. This remains true even if unused values remain in `b`. If `j >= len(b)` while `i` is still below four, there are not enough positions left to complete the selection. The source returns `-inf`, not zero, for that impossible state.

That negative infinity sentinel is crucial. Returning zero for an incomplete selection would allow the recurrence to pretend it can stop early, especially when the remaining products are negative. Because adding any finite product to negative infinity stays negative infinity, an incomplete branch can never defeat a real four-choice branch. The initial constraint `len(b) >= 4` guarantees at least one complete selection from `dfs(0, 0)`.

The order of the source's base tests is also sensible. When `j` reaches the end, it returns zero only if `i` has also reached the end; otherwise it returns negative infinity. The following `i` check covers completion that happens before `b` is exhausted.

**Memoization turns the branching tree into a state table.** Without `@cache`, skip/take choices repeatedly solve the same suffix problem and generate an exponential recursion tree. A state is fully determined by the pair $(i,j)$, so caching its result makes every reachable pair execute its body once. Later requests reuse the stored value.

There are only five meaningful `i` levels, from zero selected multipliers through four, and $n+1$ possible `j` positions. Thus the apparent binary recursion is a small-width dynamic program spread across `b`. The exact source uses top-down recursion, not the constant-space iterative update described by the manifest summary. Its mathematical recurrence is the same as a four-stage subsequence DP, but its storage and runtime behavior must be analyzed from the code that actually exists.

**Why the recurrence is exact.** Take an optimal completion for state $(i,j)$. It either excludes index $j$, in which case its score cannot exceed the optimal value $F(i,j+1)$, or includes index $j$ as the next selected index, in which case its remaining choices form a legal completion of $(i+1,j+1)$ and its score cannot exceed the second recurrence branch. Therefore the maximum of the branches is at least as good as every legal solution. Conversely, each finite branch represents a legal action followed by an optimal legal suffix, so the recurrence never invents a selection. Induction from the base cases proves that `dfs(0, 0)` is exactly the desired maximum score.

**A practical issue in the exact Python source.** Although the number of multiplier stages is only four, a long sequence of skip transitions can make recursion depth proportional to `len(b)`. With the allowed length up to $10^5$, ordinary CPython's default recursion limit is far smaller. The algorithmic recurrence is valid, but this exact recursive implementation can raise `RecursionError` on a sufficiently long input unless the execution environment raises the limit or the implementation is converted to an iterative four-state DP. The source also assumes `cache` and `inf`, as well as typing names, are supplied by imports or the harness.

## Complexity detail

Let $n=\lvert b\rvert$. There are at most $5(n+1)$ cached state pairs because `i` takes only the constant number of values from zero through four. Each uncached state performs $O(1)$ arithmetic and at most two cached calls. The total time is therefore $O(n)$.

The cache stores $O(n)$ results, and the active recursion stack can also grow to $O(n)$ along repeated skip calls. The actual auxiliary-space bound of this source is $O(n)$, not the $O(1)$ stated in `solution_variants.json`. A bottom-up implementation can compress the four multiplier states to constant space, but that is not the protected source being explained. Integer products can reach large magnitudes, but Python integers expand automatically.

## Alternatives and edge cases

- **Four-state iterative dynamic programming:** Maintain the best score after choosing one, two, three, and four values while scanning `b`. Update stages from four down to one so the same `b[j]` cannot fill multiple stages. This retains $O(n)$ time, truly uses $O(1)$ auxiliary space, and avoids the recursion-depth defect.
- **Two-dimensional bottom-up table:** Store the same $F(i,j)$ recurrence explicitly. It avoids recursion but uses $O(n)$ space because one dimension has constant size; it is useful when teaching the state transition.
- **Enumerating four indices:** Four nested loops are correct but cost $O(n^4)$ time and are impossible at the maximum input size.
- **Greedily taking the largest immediate product:** This fails because indices must remain ordered and using one position changes all later options. Negative multipliers make local comparisons even less reliable.
- **All products are negative:** The algorithm still must select exactly four entries. The negative-infinity failure sentinel prevents it from returning an illegal shorter selection with score zero.
- **`b` has exactly four values:** Skipping any value eventually reaches an impossible state, so the only finite path pairs the four entries in order. The recurrence naturally produces that sole score.
- **Large positive and negative products:** The method compares full integer totals; no special sign case is needed. Fixed-width-language translations should use a sufficiently wide integer type and a safe sentinel to avoid overflow when adding to negative infinity.
- **Many equivalent optimal selections:** Memoization stores only the best numeric score, which is sufficient because the problem does not request the chosen indices.
- **Recursion depth:** A path that skips many `b` entries can be tens of thousands of calls deep. This is a genuine engineering limitation of the exact Python source even though its abstract dynamic program is optimal in time.
- **Manifest discrepancy:** The manifest's $O(1)$ space and scanning-state summary describe the natural iterative optimization, not this cached DFS. Complexity documentation should follow the exact source and report $O(n)$ auxiliary space.
