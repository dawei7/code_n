## General

Consider the array from right to left. Maintain `merged`, the value of the mergeable block that begins at the current suffix boundary. Initially the last element is the only such block.

For an element `nums[index]`, there are two cases. If `nums[index] <= merged`, it can legally merge into the block on its right, producing `nums[index] + merged`. Taking this merge is always beneficial: all values are positive, so the receiver grows and becomes at least as easy for an even earlier element to merge into.

If `nums[index] > merged`, the current right-hand block cannot absorb it. Absorbing additional elements from the left would only make `nums[index]` larger, so this boundary can never be crossed from left to right. Start a new block by assigning `merged = nums[index]`.

**Why the final block value is the answer**

Every time a merge succeeds, `merged` increases. Every time a boundary forces a reset, the new value is strictly larger than the preceding block's value. Thus `merged` never decreases during the reverse scan and always equals the largest completed or active block seen so far. After the leftmost element is processed, it is therefore the greatest value attainable in any final array.

## Complexity detail

Let $n$ be the length of `nums`. The reverse scan examines each element once, so it takes $O(n)$ time. Apart from the accumulator and loop index, it uses $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Forward simulation:** Repeatedly search for a legal adjacent pair, replace it with its sum, and restart. This can be correct, but array rebuilding and repeated scans may require $O(n^2)$ time.
- **Explicit stack of blocks:** Scan from right to left while storing mergeable aggregates. It can express the same greedy decisions, but the single accumulator is sufficient and avoids $O(n)$ storage.
- **Single element:** No operation is possible, so that element is already the answer.
- **Strictly decreasing values:** No adjacent pair initially satisfies the rule, and the first element is the largest attainable value.
- **Equal neighbors:** Equality is allowed by the `<=` condition, so equal adjacent values can merge.
- **Values beyond 32-bit range:** Up to $10^5$ values of $10^6$ may combine, so implementations need an integer type capable of representing sums up to $10^{11}$.
