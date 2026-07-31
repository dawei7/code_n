## General

Let `dp[r]` be the minimum cost for the prefix `nums[0:r]`, with `dp[0] = 0`. If the final part of that prefix begins at `left`, the candidate cost is `dp[left] + k + trimmed_length(nums[left:r])`. Taking the minimum over every possible `left` considers every valid final cut, while `dp[left]` already represents an optimal split of everything before it.

**Update the trimmed length without rescanning**

For each right endpoint, extend the prospective final part backward and maintain the frequency of every value. Adding a value for the first time contributes nothing because it would be removed by trimming. Its second occurrence makes both copies survive, increasing the trimmed length by 2. Every later occurrence adds one more surviving element. This makes each transition constant time after its frequency update.

The recurrence is correct by the last-part decomposition. Every complete split has a unique start `left` for its final part, so it appears among the candidates. Conversely, each candidate joins an optimal split of the preceding prefix to one valid non-empty final part. The minimum therefore equals the optimum for the larger prefix.

## Complexity detail

There are $O(n^2)$ pairs of left and right endpoints. Frequencies and the trimmed length update in $O(1)$ time per pair because every value lies in `[0, n)`, giving $O(n^2)$ time. The DP table and one frequency array each use $O(n)$ auxiliary space; the frequency array is reused for successive right endpoints.

## Alternatives and edge cases

- **Recompute every trimmed subarray:** Counting a candidate part from scratch for each DP transition takes $O(n^3)$ time.
- **Precompute all part costs:** A two-dimensional table supports constant-time transitions but uses $O(n^2)$ space; updating costs during each right-endpoint scan retains only $O(n)$ space.
- **Greedy cutting at duplicates:** Whether a duplicate justifies a cut depends on both the base cost `k` and later repetitions, so a locally attractive cut need not be globally optimal.
- **First occurrence:** A value seen once in the current part contributes zero to its trimmed length.
- **Second versus later occurrences:** The second copy contributes 2 at once; the third and every later copy contribute only 1 each.
- **All values distinct:** One part costs exactly `k`, which cannot be improved by paying the base cost more than once.
- **Single element:** The only valid split contains one part and costs `k`.
- **Large base cost:** The answer can exceed 32-bit intermediate ranges in other languages, so implementations should use a sufficiently wide numeric type.
