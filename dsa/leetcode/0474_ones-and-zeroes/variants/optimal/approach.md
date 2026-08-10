## General

Each binary string is an item with two resource costs: its number of zeros and its number of ones. Selecting it contributes value one to the subset size. The two budgets are `m` zeros and `n` ones. This is a zero-one knapsack problem with two capacity dimensions.

The exact solution uses a three-dimensional dynamic-programming table so every input string is considered once, with an explicit layer for how many items have been processed.

**State definition**

Let `K = len(strs)`. The state

`f[i][j][k]`

is the maximum number of strings selectable from the first `i` input positions while using at most `j` zeros and at most `k` ones.

The words “at most” matter. Unused capacity is allowed, so a solution feasible for smaller consumption is also represented at larger budget coordinates. The objective counts strings, not characters; every selected string adds exactly one.

All states initially contain zero. With zero processed strings, the only subset is empty, whose cardinality is zero for every budget. This supplies the base layer `f[0]` automatically.

**Count the current item's two costs**

For each string `s`, `a = s.count("0")` and `b = s.count("1")`. Because the source guarantees binary strings, these counts cover every character and `a + b == len(s)`.

Input positions are separate selectable items. If identical string text appeared at two positions, each would be processed on its own layer and could be selected independently, as required by subset semantics.

**Exclude or include**

At layer `i`, every optimal subset has exactly two possibilities concerning current string `s`.

If it is excluded, the answer is whatever was possible from the first `i - 1` strings with unchanged budgets:

`f[i - 1][j][k]`.

The code assigns this value first.

If `j >= a` and `k >= b`, the string fits. Selecting it consumes `a` zeros and `b` ones, leaving capacities `j - a` and `k - b` for earlier strings. This candidate is

`f[i - 1][j - a][k - b] + 1`.

Taking the maximum chooses the better of excluding and including.

Both transitions read exclusively from layer `i - 1`. Therefore the current string cannot be selected twice, even though the budget loops run upward. This is the defining zero-one behavior.

**Why the recurrence is complete**

Use induction on `i`. Assume the previous layer correctly solves every budget pair using the first `i - 1` strings. Any feasible subset from the first `i` either omits the current string, in which case the exclude state covers it, or contains it, in which case removing that item leaves a feasible previous-layer subset under the reduced budgets. The include state covers that case.

Conversely, both constructed candidates are feasible: exclusion changes nothing, and inclusion adds an item only when both capacities suffice. Their maximum is therefore exactly optimal.

After all `K` strings, `f[K][m][n]` is the maximum cardinality under the full available budgets.

**Trace a small example**

For `strs = ["10", "0", "1"]`, `m = 1`, and `n = 1`:

- `"10"` costs one zero and one one, so it can create value one at state `(1,1)`.
- `"0"` costs one zero. The table can either keep `"10"` or select `"0"`; maximum remains one at full budgets.
- `"1"` costs one one. Including it on top of the previous state with one zero and zero ones selects `"0" + "1"`, producing value two.

The returned answer is two.

**Why forward capacity loops are safe here**

A common space-optimized zero-one knapsack must iterate capacities backward; forward loops would reuse an item updated earlier in the same table. This exact solution has a separate layer for every `i` and always reads from `f[i - 1]`, so no current-layer value feeds another current-layer update. Forward loops are safe, though they use more memory.

## Complexity detail

Let $K$ be the number of strings and let

$$
S=\sum_{s\in\texttt{strs}}\lvert s\rvert.
$$

Counting zeros and ones costs $O(S)$ total time. For each of `K` layers, the nested budget loops visit `(m + 1)(n + 1)` states and do constant work, costing $O(Kmn)$. Total time is $O(S+Kmn)$.

The allocated table has `(K + 1)(m + 1)(n + 1)` integers, so exact auxiliary space is $O(Kmn)$. This differs from the manifest's $O(mn)$ claim, which corresponds to a rolling or in-place two-dimensional DP, not this full three-dimensional source.

## Alternatives and edge cases

- **Two-dimensional reverse DP:** Keep only `dp[j][k]` and iterate both capacities downward for each string. It preserves zero-one use and reduces space to $O(mn)$, matching the manifest.
- **Memoized recursion:** State `(index, zeros_left, ones_left)` has the same $O(Kmn)$ state count and adds call-stack overhead.
- **Enumerate all subsets:** Takes $O(2^K)$ choices and is infeasible for up to 600 strings.
- **Treat total length as one budget:** Incorrect because zeros and ones have independent limits.
- **String exceeding one budget:** Its include condition fails for those states, but exclusion remains available.
- **Unused capacity:** Returning the full-budget state is correct because states mean “at most,” not “exactly.”
- **Duplicate strings:** Different positions remain separate items and may both be selected if budgets allow.
- **All-zero or all-one strings:** One resource cost is zero; the same recurrence handles it.
- **Forward loops:** Safe only because reads come from the previous item layer.
- **Manifest mismatch:** The exact table retains all layers and therefore does not have $O(mn)$ space.
