## General

**Deleting digits means choosing a subsequence.** The digits that remain keep their original relative order. Therefore, every possible final representation corresponds to a subsequence of `num`, and the operation count is the number of skipped digits.

The final integer is special when its remainder modulo 25 is zero. Rather than focusing only on possible last two digits, the exact solution explores keep/delete decisions with dynamic programming over the current remainder.

**Define the recursive state.** `dfs(i, k)` is the minimum additional deletions needed after considering the first `i` digits, when the decimal number formed by kept digits so far has remainder `k` modulo 25.

Only the remainder matters for future divisibility. If two different kept prefixes have the same remainder, appending the same remaining digits produces the same future remainders. Their full numeric values need not be stored.

**Delete the current digit.** The first choice skips `num[i]`. It costs one operation and leaves the remainder unchanged:

`dfs(i + 1, k) + 1`.

**Keep the current digit.** Appending decimal digit `d = int(num[i])` to a prefix with remainder `k` produces remainder

`(k * 10 + d) % 25`.

Keeping costs no deletion, so the second candidate is that next state directly. The source takes the smaller of delete and keep.

These two choices are exhaustive for each digit. Recursion therefore considers every subsequence without generating it explicitly.

**Interpret the base case.** At `i == n`, no digits remain. If `k == 0`, the kept subsequence represents a multiple of 25 and needs no more deletions, so the return is zero.

Otherwise, the path is invalid. The source returns `n` as a finite penalty rather than infinity. Any invalid path already accumulated nonnegative deletions, so its total is at least `n`. Deleting every digit from the initial state costs exactly `n` and is valid because the statement defines the empty result as zero. Thus an invalid penalized path can never beat a valid optimum, and `n` is a safe sentinel.

**The empty subsequence is handled naturally.** Starting remainder is zero. If every digit is deleted, remainder stays zero and the base accepts the path at cost `n`. This models the special rule that deleting all digits produces integer zero, which is divisible by 25.

Keeping a single zero also leaves remainder zero and can produce a cheaper result. Leading zeros in a kept subsequence do not change numeric divisibility, and the problem permits deletion results interpreted as integers.

**Memoization collapses exponential choices.** A naive decision tree has two branches per digit. `@cache` stores the result for each pair `(i, k)`. There are only $n+1$ positions and 25 possible remainders, so each subproblem is solved once.
Any optimal subsequence either excludes current digit `i` or includes it. The delete branch accounts for exactly the former solutions and their one operation; the keep branch accounts for exactly the latter and updates the decimal remainder correctly. Taking their minimum yields the best continuation. The base accepts exactly remainder-zero results, including the empty-as-zero case. Induction backward over `i` proves `dfs(0, 0)` is the minimum deletion count.

**The exact source differs from the manifest.** The manifest describes greedily finding a suffix among 00, 25, 50, and 75 from right to left, which achieves $O(n)$ time and $O(1)$ space.

This source uses a cached remainder DP. Since 25 is constant, its time is still $O(n)$ asymptotically, but it stores $O(25n)=O(n)$ states and uses an $O(n)$ recursion stack. It should not be described as constant-space suffix matching.

**Recursion limit consideration.** Here `n <= 100`, so recursive depth is safely below Python's ordinary limit. The same pattern on much longer strings might require iterative DP.

## Complexity detail

There are at most $(n+1)\cdot25$ cache states. Each performs constant arithmetic and at most two cached recursive calls. Time is $O(25n)=O(n)$.

The cache stores $O(25n)=O(n)$ results. Recursion depth is at most $n$, so auxiliary space is $O(n)$. This contradicts the manifest's $O(1)$ space claim for the exact source.

Converting one digit character with `int` is constant work. Remainders stay between zero and 24.

The finite invalid penalty does not change complexity and avoids importing an infinity value.

## Alternatives and edge cases

- **Match terminal pairs 00, 25, 50, and 75:** Scan from the right for each pattern and count deletions around the selected digits. Also consider keeping one zero or deleting all digits. This gives $O(n)$ time and $O(1)$ space and matches the manifest.
- **Bottom-up remainder DP:** Maintain minimum deletions for 25 remainders while scanning digits, avoiding recursion with $O(25)$ rolling space.
- **Brute-force subsequences:** It takes $O(2^n)$ time and is infeasible even at length 100.
- **Already divisible by 25:** Keeping every digit reaches remainder zero with zero deletions.
- **Single zero:** It is already special and returns zero.
- **No useful digits:** Deleting all digits costs $n$ and yields zero.
- **Leading zeros after deletion:** They do not affect the remainder and are allowed by the numeric interpretation.
- **Remainder state:** Full kept-prefix values can be enormous, but modulo 25 contains all needed future information.
- **Invalid-path penalty:** Returning `n` is safe because delete-all provides a valid solution of cost exactly `n`.
- **Cached closure:** `num` and `n` remain fixed during the method call, so `(i,k)` is a complete key.
- **Manifest mismatch:** The exact algorithm is DP with linear storage, not greedy two-digit suffix matching.
