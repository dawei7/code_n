## General

**Use a suffix state for every possible next start**

A split partitions the array into consecutive subarrays. Once the first subarray ending at `j` is chosen, the remaining decision depends only on suffix `j+1` onward.

The cached function `dfs(i)` means the minimum number of valid subarrays needed to cover `nums[i:]`. If `i>=n`, no elements remain and zero more subarrays are needed.

For a nonempty suffix, the method tries every possible endpoint `j` from `i` through `n-1`. The candidate first part `nums[i:j+1]` is valid exactly when

`gcd(nums[i], nums[j]) > 1`.

Only the first and last elements matter; interior values do not participate in this condition.

For a valid endpoint, one subarray is used now and the best continuation is `dfs(j+1)`. The transition is `1+dfs(j+1)`, and the minimum over all valid endpoints gives `dfs(i)`.

**Singleton subarrays**

When `j==i`, the first and last element are the same. Its GCD with itself is `nums[i]`. A singleton is therefore valid exactly when that value is greater than one.

This explains why `[3,5]` can be split into two valid singletons, while any occurrence of 1 is more difficult: `gcd(1,1)=1`, so a singleton containing 1 is invalid, and 1 cannot share a GCD greater than one with any endpoint.

Interior ones can still occur in a valid longer subarray because only endpoints are tested.

**Impossible states**

`ans` begins at infinity. If no endpoint produces a valid first subarray leading to a finite continuation, the state remains infinite.

The initial result is converted to -1 only after `dfs(0)` finishes. Intermediate infinity values are useful because adding one to infinity remains infinity and cannot accidentally win a minimum.

For `nums=[1,2,1]`, every possible first subarray begins with 1, and its last endpoint has GCD 1 with that start. No transition exists, so the result is -1.

**Why the recurrence covers every valid split**

Take an optimal split of suffix `i`. Its first subarray must end at some `j>=i`, and validity requires the exact GCD test used by the loop. The remainder of that split is a valid split of suffix `j+1`, whose minimum size is `dfs(j+1)`. Therefore the recurrence includes a transition no worse than the optimum.

Conversely, every transition joins one valid first subarray with a recursively valid partition of the remaining suffix. It covers every element once and preserves contiguity. Thus no transition represents an invalid split.

Taking the minimum gives exactly the optimal number.

**Memoization turns a branching search into dynamic programming**

Different choices can reach the same suffix index. `@cache` computes each `dfs(i)` only once. The explicit `dfs.cache_clear()` releases cached entries before the method returns.

For `[2,6,3,4,3]`, one transition from index 0 can end at index 1 because `gcd(2,6)=2`. From index 2, ending at index 4 is valid because `gcd(3,3)=3`. This produces two parts. The recurrence also explores other endpoints and verifies none yields one complete valid part.

**The exact implementation differs from the manifest**

The summary describes indexing best prefix splits by shared prime factors in near-linear time. The protected source does no factorization or prime-indexed optimization. It checks every possible suffix endpoint from every cached start and computes a GCD for each.

Its exact worst-case time is quadratic in array length, with a logarithmic numeric factor, and recursive execution can reach depth $n$.

## Complexity detail

There are $n+1$ cached suffix states. State `i` loops over $n-i$ endpoints, for

$$
\sum_{i=0}^{n-1}(n-i)=O(n^2)
$$

GCD tests. Each Euclidean GCD costs $O(\log V)$ for maximum value $V$, so time is $O(n^2\log V)$.

The cache stores $O(n)$ results, and recursion depth can reach $O(n)$ through repeated singleton choices. Total auxiliary space is $O(n)$. This is much smaller than the manifest's sieve-domain array in one dimension but accompanies a slower runtime.

At $n=1000$, recursion depth can approach Python's default limit and may be fragile. A bottom-up version avoids that operational risk.

## Alternatives and edge cases

- **Prime-factor indexed DP:** Factor endpoints and remember the best split count associated with each prime. This matches the manifest and can reduce transition work dramatically.
- **Bottom-up quadratic DP:** Compute minimum parts for prefixes or suffixes iteratively. It preserves the exact recurrence and complexity while avoiding recursion depth.
- **Greedy longest valid prefix:** It is not generally safe because a farther valid endpoint can leave an impossible suffix, while an earlier split may enable completion.
- **Value one at a required endpoint:** Its GCD with every number is one, so no subarray starting or ending there is valid.
- **Interior ones:** They do not affect the endpoint-only GCD condition.
- **One element greater than one:** The singleton is valid and answer is one.
- **One element equal to one:** No valid split exists and -1 is returned.
- **No valid continuation:** Infinity propagates through the minimum until final conversion to -1.
- **Cache clearing:** It frees memoized state after the answer is obtained and does not change the returned value.
- **Metadata mismatch:** The source is cached quadratic endpoint enumeration, not a prime-factor-indexed near-linear DP.
