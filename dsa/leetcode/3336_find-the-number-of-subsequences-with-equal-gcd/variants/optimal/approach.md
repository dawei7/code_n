## General

**Assign each index to one of three destinations.** Two subsequences are disjoint exactly when every array index is used by at most one of them. For each value, there are three mutually exclusive choices: ignore it, place it in `seq1`, or place it in `seq2`. The source's three recursive branches encode this ternary assignment directly, so disjointness needs no later check.

State `dfs(i, j, k)` counts valid assignments of indices zero through $i$ when the GCD already accumulated from later-decided elements of the first subsequence is $j$, and that of the second is $k$. Processing backward rather than forward does not change which subsets can be selected.

GCD zero represents an empty subsequence. This works because `gcd(value, 0) = value`, so the first selected element initializes the subsequence GCD naturally.

**Three exact transitions.** For `nums[i]`:

- `dfs(i - 1, j, k)` ignores the index;
- `dfs(i - 1, gcd(nums[i], j), k)` assigns it to the first subsequence;
- `dfs(i - 1, j, gcd(nums[i], k))` assigns it to the second.

No branch assigns the same index to both. Ordered pairs matter: swapping which subsequence receives an index generally follows a different branch and counts a different pair, as the examples do.

**Base equality and the empty-empty correction.** When `i < 0`, every index has been assigned. The state contributes one exactly when `j == k`. Positive equal values mean both subsequences are nonempty and have equal GCD.

Equality also accepts `j == k == 0`, corresponding only to ignoring every index and leaving both subsequences empty. Because all input values are positive, no nonempty subsequence can have GCD zero. Subtracting one from the initial result removes precisely this one forbidden assignment.

It is impossible for only one subsequence to be empty and still pass equality: its GCD would be zero while the nonempty one's is positive.

**Memoization collapses repeated suffix decisions.** Many ternary assignment paths reach the same triple $(i,j,k)$. `@cache` stores its count. Possible positive GCDs are bounded by $V=\max(nums)$, plus zero, so each `i` layer has at most $(V+1)^2$ GCD pairs.

All branch sums are reduced modulo $10^9+7$. The final subtraction also uses modulo, returning the standard nonnegative residue.
At state $(i,j,k)$, every disjoint assignment of current index $i$ belongs to exactly one of the three branches. Each branch updates the corresponding GCD using its defining operation and leaves the other unchanged. By induction, recursive results count all completions of that choice, and summing counts every disjoint ordered pair once. The base accepts exactly equal GCDs, with the explicit subtraction enforcing non-emptiness.

**Actual cache includes the index dimension.** The manifest's $O(V^2)$ space describes a rolling iterative DP. This top-down source may retain a result for every reachable $(i,j,k)$ and therefore uses up to $O(nV^2)$ cache entries, not $O(V^2)$. With $n,V\le200$, reachability may be smaller in practice, but the structural bound must follow the code.

GCD calculations also take logarithmic arithmetic time. The manifest's $O(nV^2)$ time treats them as constant under the small bounded domain; a more explicit bound includes $O(\log V)$ per nontrivial transition.

## Complexity detail

There are at most $O(nV^2)$ memo states, and each performs three recursive lookups plus two GCD computations. The conventional bound is $O(nV^2\log V)$ time, or $O(nV^2)$ under a unit-cost bounded-integer model.

The memo cache can use $O(nV^2)$ space, and recursion depth is $O(n)$. This contradicts the manifest's $O(V^2)$ rolling-space claim. The nested function and cache become unreachable after the method returns, but peak memory remains index-dimensional.

## Alternatives and edge cases

- **Rolling $V\times V$ table:** Distribute each state to three destinations for every input value. It achieves $O(V^2)$ space and matches the manifest.
- **Sparse dictionary DP:** Store only reachable GCD pairs, which can reduce practical work when few divisors occur.
- **Enumerate two subsequences directly:** There are $3^n$ index assignments and exponential work without memoization.
- **Both subsequences empty:** The base counts it once and the final subtraction removes it.
- **Only one empty:** GCD zero cannot equal a positive GCD, so it is automatically excluded.
- **Ordered pair:** `(seq1,seq2)` and `(seq2,seq1)` are different unless the index selections somehow coincide, which disjoint nonempty sequences cannot do.
- **Duplicate values:** Indices remain distinct choices even when values match; recursive assignment counts them separately.
- **Value one:** Once a subsequence GCD reaches one, adding more values leaves it one, causing many paths to share cached states.
- **Modulo subtraction:** `(... - 1) % mod` safely handles the residue.
- **Positive-input assumption:** It makes zero an unambiguous empty-subsequence sentinel.
- **Recursion depth:** Maximum depth 200 is normally safe in Python.
- **Manifest discrepancy:** Exact memo space is $O(nV^2)$ rather than $O(V^2)$.
- **State direction:** Processing indices backward changes only recursion order, not subsequence order; selected indices still define their natural increasing-index subsequences.
