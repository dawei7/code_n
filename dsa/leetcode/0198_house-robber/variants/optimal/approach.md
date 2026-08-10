## General

**Define one smaller problem for every starting index**

Let `dfs(i)` mean the maximum money obtainable from houses at indices `i`
through the end, assuming no earlier decision prevents choosing house `i`.
This state contains all information the future needs. Earlier robbed houses do
not need to be remembered because the recursive jump itself enforces adjacency.

The desired answer is `dfs(0)`, which considers the entire street.

**Recognize the only two choices at a house**

At index `i`, a legal optimal plan either robs the current house or does not.
These cases are mutually exclusive and collectively cover every valid set of
houses.

If the plan robs house `i`, it gains `nums[i]` and may not rob adjacent house
`i + 1`. The next independent subproblem therefore starts at `i + 2`, giving
candidate `nums[i] + dfs(i + 2)`.

If the plan skips house `i`, it receives nothing there and may consider the
next house normally, giving candidate `dfs(i + 1)`. Taking the maximum chooses
the better legal continuation:

`dfs(i) = max(nums[i] + dfs(i + 2), dfs(i + 1))`

**Why skipping must remain an option**

A locally large house can make an adjacent choice unavailable, and that tradeoff
may interact with later houses. There is no safe rule such as always choosing
the larger of two neighbors. The skip branch allows the algorithm to compare
complete future consequences rather than make an irreversible local guess.

The input values are nonnegative, but that does not mean every house should be
robbed. Adjacency, not negative value, creates the conflict.

**Stop beyond the street**

When `i >= len(nums)`, there are no houses left, so the best additional amount
is zero. This single base case handles both `i == n` from skipping near the end
and `i == n + 1` from robbing the final house and jumping two positions.

It also makes the recurrence safe for a one-house array: robbing produces that
house's value plus zero, while skipping produces zero, and the nonnegative
house value is selected.

**Trace the first example**

For `[1,2,3,1]`, consider the meaningful suffix results from right to left.
Starting at the last house gives 1. Starting at value 3 compares robbing it for
3 with skipping to obtain 1, so the result is 3. Starting at value 2 compares
`2 + 1 = 3` with the suffix result 3. Starting at value 1 compares
`1 + 3 = 4` with 3, returning 4.

The chosen set is indices 0 and 2. The recurrence never explicitly stores that
set because the contract needs only its maximum sum.

**Why the recurrence is exact**

Assume `dfs(i + 1)` and `dfs(i + 2)` correctly solve their shorter suffixes.
Every legal plan for suffix `i` either includes house `i` or excludes it. An
including plan must exclude `i + 1`, so its best possible value is exactly
`nums[i] + dfs(i + 2)`. An excluding plan's best value is exactly
`dfs(i + 1)`.

The maximum of those two quantities is therefore the best among all legal
plans for suffix `i`. The base case is exact for an empty suffix, so the
argument applies backward to `dfs(0)`.

**Memoize overlapping suffixes**

Without caching, the two branches repeatedly solve the same indices. For
example, `dfs(i + 2)` is reached directly from `dfs(i)` and indirectly through
`dfs(i + 1)`. That recursive tree grows exponentially.

`@cache` stores the answer associated with each integer index. The first call
computes it; later calls return the saved value. There are only about $n$ useful
indices, so memoization reduces the total work to linear time.

**Exact source does not use constant space**

The manifest summary and space bound describe the two-variable optimized DP,
but the exact optimal file uses a cache entry for each suffix and a recursive
call stack. Its auxiliary space grows with the number of houses and is
$O(n)$, not $O(1)$. The competitive variant is the file that actually carries
only two running totals.

Documentation must distinguish the algorithm present from the algorithm the
manifest appears to describe. Both are correct, but their memory profiles are
different.

**Standalone import requirements**

The exact file uses `List` in its annotation and `@cache` as a decorator without
showing imports. Outside a harness that supplies these names, it needs
`from typing import List` and `from functools import cache`. Otherwise class
definition or method execution fails despite the recurrence being correct.

The maximum input length is 100, so recursion depth is modest under the stated
constraints. A generalized much longer street could hit Python's recursion
limit, another reason to prefer iteration.

## Complexity detail

There is one cached state per starting index, plus constant many beyond-end
base indices. Each state performs constant arithmetic and two cached lookups,
so time is $O(n)$.

The memoization table contains $O(n)$ results, and the deepest recursive path
uses $O(n)$ stack frames. Thus exact auxiliary space is $O(n)$. This contradicts
the manifest's $O(1)$ claim for this file; $O(1)$ is achievable with the
iterative two-total recurrence.

## Alternatives and edge cases

- **Two-variable forward DP:** Track best totals for prefixes ending before the current and one house earlier; $O(n)$ time and $O(1)$ space.
- **Bottom-up table:** Store every prefix or suffix optimum; avoids recursion but uses $O(n)$ memory.
- **Unmemoized recursion:** Mirrors the choice tree clearly but repeats subproblems and takes exponential time.
- **Greedy neighbor comparison:** Not generally correct because local choices can block a better combination farther away.
- **One house:** Return its nonnegative value.
- **Two houses:** Return the larger value because both cannot be selected.
- **All zeros:** Every legal selection totals zero.
- **Empty array:** Outside the Reference, but the exact recurrence would return zero.
- **Long generalized input:** Iteration avoids recursion-limit risk.
- **Missing imports:** `List` and `cache` must exist in the runtime namespace.
