## General

**Reduce gap-closing deletions to original intervals.** Suppose a later deletion spans gaps created by earlier operations. Combine the elements deleted by that later operation with every previously deleted interval inside its original endpoints. Their union is one contiguous interval of the original array. Every component sum is divisible by `k`, so the union's sum is also divisible. Repeating this merge shows that any deletion sequence is equivalent to deleting disjoint divisible-sum intervals from the original array. The reverse direction is immediate: disjoint original intervals can be deleted one by one.

**Dynamic programming over prefixes.** Let `dp[i]` be the minimum retained sum after processing the first `i` original elements. One option keeps `nums[i - 1]`, giving `dp[i - 1] + nums[i - 1]`. Alternatively, delete an interval `[j, i)` when the original prefix sums at `j` and `i` have the same remainder modulo `k`; this leaves cost `dp[j]`.

Maintain, for every remainder seen so far, the smallest `dp[j]` attached to a prefix with that remainder. At each new prefix, compare the keep cost with the stored deletion cost for its remainder, then update that remainder's minimum. This summarizes all possible interval starts in constant expected time.

## Complexity detail

The algorithm performs one expected-constant-time hash lookup and update per element, taking expected $O(n)$ time. At most one entry is stored per encountered remainder, bounded by both $n+1$ and $k$, so auxiliary space is $O(\min(n,k))$.

The benchmark sets size $N=n$, fixes a nontrivial modulus, and uses tiers 32, 128, and 512 for a 16x span. The accepted remainder map takes expected $O(N)$ time. A correct interval DP that checks every earlier prefix remainder for every endpoint takes $O(N^2)$ time and must finish all tiers but fail scaling.

## Alternatives and edge cases

- **Quadratic interval DP:** Testing all starts for each endpoint follows the recurrence directly but repeats remainder comparisons.
- **Simulate deletion states:** Enumerating arrays produced by different deletion orders is exponential and obscures the interval-merging equivalence.
- **Whole sum divisible:** Equal initial and final prefix remainders allow deleting the complete array and returning `0`.
- **No divisible interval:** Every element must remain, so the answer is the original sum.
- **Modulus one:** Every subarray sum is divisible and the entire array can be removed.
- **Positive values:** Keeping an element always increases the retained sum, which makes the minimum-prefix summary sufficient.
