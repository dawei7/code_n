## General
**Index dynamic-programming states by endpoint and difference**

Let `dp[i][difference]` count arithmetic subsequences of length at least two that end at index `i` with the given difference. Length-two pairs are retained as intermediate states even though they are not yet included in the answer.

**Extend every earlier endpoint into the current value**

For each pair `left < right`, compute `difference = nums[right] - nums[left]`. Every sequence counted by `dp[left][difference]` can append `nums[right]`, forming a valid sequence of length at least three. Add that count to the answer.

**Store both extensions and the new pair**

At `dp[right][difference]`, add the extended sequences plus one for the new two-element pair `(left, right)`. That pair may become a counted arithmetic subsequence when a later value with the same difference extends it.

**Why every arithmetic subsequence is counted once**

Any qualifying subsequence has a unique final two indices `left, right` and a unique common difference. Removing its final element leaves exactly one state counted at `dp[left][difference]`; processing that pair extends and counts it. Nonmatching differences never share a state, and length-two pairs enter the DP but not the answer.

## Complexity detail
There are $n(n - 1) / 2$ ordered index pairs, each with average constant-time hash-map work, so time is $O(n^2)$. Across all endpoints, the difference maps can contain $O(n^2)$ states.

## Alternatives and edge cases
- **Three-index predecessor scan:** store pair states but scan every still-earlier index to find matching differences; this is correct but takes $O(n^3)$ time.
- **Enumerate all subsequences:** tests the condition directly but takes exponential time.
- **Equal values:** difference zero is an ordinary map key and may create many valid subsequences.
- **Duplicate values at different indices:** form distinct subsequences and must retain multiplicity.
- **Fewer than three elements:** no qualifying subsequence exists.
- **Large differences:** use the language's full integer range rather than narrowing subtraction.
