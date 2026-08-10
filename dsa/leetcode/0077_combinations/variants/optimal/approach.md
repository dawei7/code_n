## General

**Make one include-or-exclude decision per number**

The recursive function `dfs(i)` considers the next available number `i`. The list `t` contains the increasing combination prefix chosen from numbers smaller than `i`. At each ordinary state, the source explores two exhaustive possibilities:

- Include `i`: append it, recurse on `i + 1`, then remove it.
- Exclude `i`: recurse on `i + 1` without it.

Every size-`k` subset of `[1, n]` makes exactly one such yes-or-no decision for each relevant number. Following those decisions reaches its unique recursive path. This binary decision view is easy to derive even without thinking about permutations or nested loops.

**Why combinations are increasing and unique**

Numbers are considered strictly in order: every recursive call advances from `i` to `i + 1`. Once a number has been skipped or selected, the recursion never returns to a smaller value within the same path. Consequently `t` is always strictly increasing.

The increasing representation removes permutation duplicates. The subset containing 1 and 3 can appear only as `[1, 3]`; no path can produce `[3, 1]` because 1 is no longer available after the recursion reaches 3. Distinct decision paths choose distinct sets, so the same increasing combination is never emitted twice.

**Copy a complete combination before backtracking**

When `len(t) == k`, the current prefix is a complete answer. The source appends `t[:]`, a shallow copy, and returns immediately. The copy is essential because `t` is the single mutable working list shared by all recursive calls. Appending `t` itself would make every result entry refer to that same list, which is later popped and reused.

Returning at size `k` is also safe. Adding more numbers would create an oversized selection, and excluding future numbers would only lead to the same already-recorded combination. One output is produced at the first moment the path reaches the required size.

**Restore shared state after the include branch**

The sequence `t.append(i)`, recursive call, and `t.pop()` is the backtracking pattern. Before the include call, `t` represents the parent choice plus `i`. After the call explores every completion containing `i`, `pop()` restores exactly the parent's prefix. The exclude call can then explore completions that do not contain `i`.

Without the pop, choices made for one branch would leak into its sibling. Popping after rather than before recursion ensures descendants actually see the included value.

**Understand both stopping conditions**

The success condition is checked first. If `t` has size `k`, it is recorded even if `i` has advanced beyond `n`; all selected values are already legal.

If the combination is still too short and `i > n`, no legal number remains, so the path cannot succeed and returns without output. This failure condition is necessary for exclude-heavy paths such as choosing nothing.

The source does not check whether the number of remaining values is smaller than the number still needed. For example, if two more elements are needed but only one value remains, it continues exploring include and exclude calls until `i > n`, even though failure is already certain. This omission affects efficiency but not correctness.

**A recursive invariant and completeness proof**

On entry to `dfs(i)`, `t` is a strictly increasing subset of `[1, i - 1]`, and the call is responsible for generating every size-`k` combination whose intersection with `[1, i - 1]` is exactly `t`.

If `t` is complete, copying it fulfills that responsibility. If `i > n` while it is incomplete, no completion exists. Otherwise every responsible combination either contains `i` or does not. The include call generates exactly the first category after appending `i`, and the exclude call generates exactly the second after state restoration. The categories are disjoint and exhaustive.

Starting with `dfs(1)` and empty `t` assigns responsibility for every size-`k` subset of `[1, n]`. The invariant therefore proves that the returned list contains all and only the requested combinations.

**Trace `n = 4`, `k = 2`**

The first path includes 1 and then 2, records `[1, 2]`, and backtracks. It then excludes 2, includes 3, and records `[1, 3]`; similarly it reaches `[1, 4]`. After every completion beginning with 1 has been explored, the root-level pop removes 1 and the exclude branch generates `[2, 3]`, `[2, 4]`, and `[3, 4]`.

The order is a depth-first decision order. The contract allows any output order, so no sorting step is needed.

**The missing feasibility pruning is material**

A common optimization returns when `len(t) + (n - i + 1) < k`, because even selecting every remaining number cannot complete the prefix. This source lacks that test.

For `k == n`, only one answer exists, yet the recursion explores essentially the full include/exclude tree of incomplete subsets before proving that most branches cannot reach size `n`. Thus the exact source cannot be described solely by output-sensitive `O(k * C(n,k))` time. Similarly, long chains of exclusions make recursion depth depend on `n`, not only on the current combination size.

## Complexity detail

Copying all outputs necessarily costs $\Theta(k\binom{n}{k})$. Beyond that output work, the unpruned search visits states for incomplete selections across growing prefixes. A useful bound is $O(\sum_{q=1}^{k}\binom{n+1}{q})$ recursive states; in the worst case, such as `k = n`, this is $O(2^n)$. Exact time is therefore safely described as $O(2^n+k\binom{n}{k})$ in the worst case, not the manifest's $O(k\binom{n}{k})$ for this source.

The working list holds at most `k` values, but the recursive call stack can follow exclusions until `i == n + 1`, giving $O(n)$ auxiliary space. This does not match the manifest's $O(k)$ claim when `k` is small. The returned answer itself occupies $\Theta(k\binom{n}{k})$ space and is conventionally excluded from the auxiliary bound.

## Alternatives and edge cases

- **Feasibility-pruned backtracking:** Stop when remaining values cannot fill the needed slots, or limit the choice loop to legal starts. This removes dead subtrees and supports the output-sensitive manifest time more closely.
- **Increasing-choice DFS:** Loop from the next minimum value through the last feasible choice rather than creating an explicit exclude branch. Its stack depth is bounded by `k`.
- **Lexicographic index successor:** Start with `[1, ..., k]` and repeatedly advance the rightmost movable index. It is iterative and output-sensitive.
- **Bitmask enumeration:** Test all $2^n$ subsets and output masks with `k` bits. It is simple for small `n` but explicitly exponential regardless of output count.
- **`k == 1`:** The include branch emits each singleton, while exclusion chains still reach depth proportional to `n`.
- **`k == n`:** Only one output exists, but missing feasibility pruning causes extensive dead exploration.
- **`n == 1`, `k == 1`:** The first include immediately records `[1]`.
- **Copy requirement:** `t[:]` prevents later pops from changing stored answers.
- **Any output order:** Depth-first order is acceptable without post-sorting.
- **No duplicate combinations:** Strictly increasing decisions create one representation per subset.
- **Contract excludes `k > n`:** If it occurred, the source would eventually return an empty answer after exploring failure paths.
- **Manifest discrepancy:** Both time and stack-space declarations require a pruned or different generator, not this exact unpruned binary recursion.
