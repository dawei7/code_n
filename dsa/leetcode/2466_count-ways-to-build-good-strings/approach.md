## General

**A state needs only the current length**

Every operation appends a fixed block: `zero` copies of `'0'` or `one` copies of `'1'`. Whether future construction can reach a good length depends only on the current length, not on the exact characters already written.

The cached function `dfs(i)` counts good strings that can be obtained starting from any construction whose current length is `i`, including the current string itself when its length is already in the good interval.

The initial state is the empty string at length zero.

**Stop after the maximum allowed length**

Both append lengths are positive. Once `i>high`, every future operation makes the string even longer, so no good string can be reached. The method returns zero.

For `i<=high`, `ans` starts at one when `low<=i<=high`. This counts stopping construction at the current string. A good string may also be extended and yield additional good strings of greater allowed lengths, so counting the current string does not end recursion.

The two recursive branches append a zero block or a one block:

`dfs(i+zero) + dfs(i+one)`.

The result is reduced modulo $10^9+7$ before caching.

**Why construction paths represent different strings**

Choosing the zero operation appends only zero characters; choosing the one operation appends only ones. A final binary string determines its operation sequence by splitting each maximal zero run into blocks of size `zero` and each maximal one run into blocks of size `one`. If a string is constructible, those block counts are fixed.

Thus two different operation sequences cannot generate the same final string. Counting recursive construction paths counts distinct strings, not merely histories with duplicates.

When `zero==one`, the two branches reach the same length state, but they prepend different blocks to their continuations. Adding both cached counts is correct because one branch's strings begin at that step with zeros and the other's with ones.

**Trace the first example**

With `zero=one=1` and `low=high=3`, each of the three operations independently appends 0 or 1. There are $2^3=8$ sequences and hence all eight binary strings of length three.

For `low=2`, `high=3`, `zero=1`, and `one=2`:

- At length 2, strings `"00"` and `"11"` qualify.
- At length 3, `"000"`, `"011"`, and `"110"` qualify.

The recurrence counts the current string at each good length and continues until exceeding three, totaling five.


From a construction at length `i`, every possible final good string falls into exactly one category:

- stop now, possible only inside `[low,high]`;
- perform a zero-block append first;
- perform a one-block append first.

These categories are disjoint because stopping adds no characters and the two non-stopping choices append different characters. The recursive states count all continuations in their categories. Their sum is therefore exact, and memoization changes only repeated computation, not the recurrence.

**The exact operational form**

The manifest describes a one-dimensional recurrence, which is mathematically accurate, but the source implements it top-down with recursion and `@cache` rather than an iterative array.

For small append lengths and `high=100000`, recursion depth can approach 100,000 and exceed Python's default recursion limit. An iterative DP is much safer for the full constraint even though asymptotic bounds are the same.

## Complexity detail

At most $O(H)$ length states are reachable up to and slightly beyond `high=H`. Each cached state performs constant work and two cache lookups, so time is $O(H)$.

The cache stores $O(H)$ results. Recursion depth can be $O(H/\min(zero,one))$, which is $O(H)$ in the worst case. Total auxiliary space is $O(H)$.

Modulo reduction at every state keeps cached results bounded. The base cases slightly above `high` are also cached, but their count is bounded by the append lengths and remains $O(H)$ because both are at most `low<=H`.

## Alternatives and edge cases

- **Bottom-up length DP:** Set ways at length zero to one, propagate to lengths plus `zero` and `one`, and sum good-length states. It preserves $O(H)$ bounds and avoids recursion overflow.
- **Breadth-first enumeration of strings:** Explicit strings grow exponentially and are unnecessary because length DP aggregates them.
- **`zero==one`:** Both append choices reach the same next length but create different characters, so both contributions must remain.
- **`low==high`:** Only constructions of one exact length are counted.
- **Overshooting high:** Positive append lengths mean an overshot state can terminate immediately.
- **Current good string can extend:** Counting it does not prevent recursive branches from producing longer good strings.
- **Empty string:** `low>=1`, so length zero is never counted as good; it is only the construction start.
- **Modulo placement:** Reducing cached state totals preserves the requested final remainder under addition.
- **Unreachable lengths:** They are never called and need no cache entry.
- **Recursion limit:** The exact code may fail for long chains even though the DP complexity is linear; iterative tabulation is operationally robust.
