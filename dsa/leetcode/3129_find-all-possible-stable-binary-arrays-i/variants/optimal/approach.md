## General

**Translate the subarray rule into a run-length rule**

A binary array violates the condition precisely when it contains more than `limit` consecutive equal bits. If there is a run of `limit + 1` zeros, that run itself is a subarray longer than `limit` containing no 1. The same holds for ones. Conversely, if every run has length at most `limit`, then every subarray longer than `limit` must cross a change of bit and therefore contains both 0 and 1.

So the task is to count arrangements using exactly `zero` zeros and `one` ones in which no zero-run and no one-run is too long.

**Define a state by counts and the final bit**

The memoized function `dfs(i, j, k)` counts valid arrays containing exactly $i$ zeros and $j$ ones whose last bit is $k$:

- $k=0$ means the array ends in 0;
- $k=1$ means the array ends in 1.

The last bit is enough information because the recurrence counts all ways to append that bit and subtracts exactly the ways whose new trailing run would be too long. The cache ensures that every triple `(i, j, k)` is evaluated at most once.

**Boundary states with only one kind of bit**

If $i=0$, the only possible nonempty array is a run of $j$ ones. It is valid only if the requested last bit is 1 and $j \le \texttt{limit}$. That is exactly:

`return int(k == 1 and j <= limit)`.

The $j=0$ case is symmetric: the all-zero array is valid only for $k=0$ and $i \le \texttt{limit}$.

The public inputs are positive, so the final call never asks for an empty completed array. Some recurrence paths can reach an axis state, and these two rules terminate them correctly.

**Derive the recurrence for arrays ending in zero**

Assume $i>0$, $j>0$, and we want `dfs(i, j, 0)`. Remove the final zero. The remaining valid prefix uses $i-1$ zeros and $j$ ones, and it may end in either 0 or 1. This initially gives

$$
\operatorname{dfs}(i-1,j,0)+\operatorname{dfs}(i-1,j,1).
$$

Most of these prefixes remain valid after appending zero. The only bad ones are those that already end in exactly `limit` zeros, because the append creates `limit + 1` consecutive zeros.

What lies immediately before those `limit` trailing zeros? It must be a 1 because $j>0$ and the prefix was valid. Removing the newly appended zero plus those `limit` old trailing zeros leaves a valid array using $i-\texttt{limit}-1$ zeros and $j$ ones and ending in 1. Therefore, when that zero count is nonnegative, the number of newly invalid extensions is

$$
\operatorname{dfs}(i-\texttt{limit}-1,j,1).
$$

Subtracting it gives the exact code recurrence. If $i-\texttt{limit}-1<0$, it is impossible to have an overlong zero suffix, so the code subtracts zero.

**The recurrence for arrays ending in one**

By symmetry,

$$
\operatorname{dfs}(i,j,1)
=\operatorname{dfs}(i,j-1,0)+\operatorname{dfs}(i,j-1,1)
-\operatorname{dfs}(i,j-\texttt{limit}-1,0),
$$

with the last term included only when its one count is nonnegative.

The two final-bit classes are disjoint and cover every nonempty binary array, so the requested answer is their sum at `(zero, one)`. The code takes that sum modulo $10^9+7$.

**Why delayed modulo still gives the correct residue**

Individual cached values are not reduced modulo $10^9+7$ inside `dfs`. Python integers are exact, so additions and subtractions do not overflow. The recurrence therefore computes the exact mathematical count, and reducing the final sum yields the correct residue. This differs from the usual implementation that reduces every state; it is correct but can create extremely large intermediate integers and consume substantially more time and memory than modular state values.

After obtaining the answer, `dfs.cache_clear()` releases the memoized states before the method returns.

## Complexity detail

Let $z=\texttt{zero}$ and $o=\texttt{one}$.

There are at most $2(z+1)(o+1)$ states because $i$ has $z+1$ possibilities, $j$ has $o+1$, and $k$ has two. Each state performs a constant number of cache lookups, additions, a comparison, and possibly one subtraction. Under the standard unit-cost model for modular-sized integers, this is $O(zo)$ time.

The cache stores $O(zo)$ states. The recursive call chain can decrease $i$ and $j$ across many levels, so stack depth can reach $O(z+o)$. The total auxiliary space is therefore $O(zo)$, with the cache dominating for nontrivial two-dimensional inputs.

There is an exact-code qualification: cached values are arbitrary-precision exact counts rather than residues. Arithmetic cost is not truly constant when those integers become very large. Their bit lengths can grow with the number of arrangements, so practical time and memory can exceed the clean $O(zo)$ unit-cost estimate. Applying modulo inside each state would preserve the recurrence while keeping numbers bounded.

For ID 3129, $z,o\le200$. Even so, a top-down path may be several hundred calls deep. The method depends on the runtime's recursion limit being high enough. The manifest's $O(zo)$ time and $O(zo)$ space match the usual DP state-count analysis, but the recursion-stack and unbounded-intermediate details belong to the exact implementation.

## Alternatives and edge cases

- **Bottom-up two-table DP:** Fill counts for arrays ending in 0 and 1 iteratively using the same add-and-subtract recurrence. It avoids recursion depth and can reduce every state modulo $10^9+7$ immediately.
- **Choose alternating runs:** Represent an array as alternating zero-runs and one-runs, then count bounded positive compositions. This is mathematically elegant but requires summing over possible run counts and careful combinatorics.
- **Track current run length:** A state `(i,j,last,length)` is easier to invent because it directly forbids an excessive append, but it adds a factor of `limit` and is slower.
- **Brute-force permutations:** Trying all binary strings or all placements of zeros takes exponential or combinatorial time and ignores the repeated-subproblem structure.
- **`limit = 1`:** Equal adjacent bits are forbidden, so only alternating arrays qualify. The recurrence's subtraction removes every attempted second equal bit.
- **`limit` at least both counts:** No run can exceed the limit, so every placement of the required zeros among all positions is valid. The recurrence never needs a feasible subtraction term.
- **One count reaches zero:** The remaining array is one monochromatic run, valid exactly when its length is at most `limit` and its requested final bit matches.
- **Subtraction can look negative:** It is inclusion-exclusion, not a negative number of arrays. Exact DP identities guarantee a nonnegative true count even though modular implementations may temporarily need normalization.
- **Final-bit double counting:** An array cannot end in both 0 and 1, so adding the two terminal states does not duplicate anything.
- **Modulo placement:** Final-only reduction is mathematically valid in Python, but per-state reduction is safer and faster in practice and is necessary in fixed-width languages.
- **Cache cleanup:** Clearing after the result is computed does not change the answer; it only releases references held by the decorated local function.
