## General
**Reserve the two extremes of the unused range.** Initially, every value from $0$ through $n$ is available. Track the smallest and largest unused values with `low` and `high`. When the next character is `"I"`, append `low` and increment `low`. Every value that remains is then strictly larger than the appended value, so whichever value is chosen next will satisfy the required increase. When the character is `"D"`, append `high` and decrement `high`; every remaining value is strictly smaller, so the required decrease is guaranteed.

**Why local choices remain globally compatible.** Each step removes exactly one previously unused endpoint. Therefore the unused values always form the entire integer interval from `low` through `high`, with no duplicates or gaps. The selected endpoint guarantees the current comparison without restricting how later signs are handled, because either endpoint of the smaller remaining interval is still available for the next step.

After all $n$ characters have been processed, exactly one value remains and `low == high`. Append that value. The construction has used every integer from $0$ through $n$ once, and the endpoint argument establishes every adjacent comparison, so the result is a valid permutation.

## Complexity detail
The algorithm processes each of the $n$ characters once and performs constant work per character, for $O(n)$ time. The returned permutation stores $n+1$ integers, so its space usage is $O(n)$; apart from that output, the two endpoint variables use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Reverse maximal decreasing runs:** Start with `[0, 1, ..., n]` and reverse the value segment corresponding to each maximal run of `"D"` characters. This is also $O(n)$ but requires careful run boundaries.
- **Stack and flush:** Push consecutive values and flush the stack whenever an `"I"` is reached, plus once at the end. Reversal by stack order satisfies each decreasing run in $O(n)$ time and space.
- **Backtracking over permutations:** Trying unused values until every sign matches is correct but can explore factorially many permutations and is unsuitable for $n$ as large as $10^5$.
- **All increases:** The construction repeatedly takes the low endpoint and returns `[0, 1, ..., n]`.
- **All decreases:** The construction repeatedly takes the high endpoint and returns `[n, n - 1, ..., 0]`.
- **Alternating signs:** The chosen values alternate between the low and high ends; every value remains unique despite the direction changes.
- **Non-unique output:** Correctness depends on the permutation and comparisons, not on matching one particular example list.
