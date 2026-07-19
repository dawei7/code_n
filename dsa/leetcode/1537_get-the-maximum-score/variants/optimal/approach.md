## General
**Shared values divide every path into independent segments**

Between two consecutive values that occur in both arrays, switching is impossible. A path must take the whole intervening segment from exactly one array. At the next shared value, both choices meet at the same state again, so only the larger accumulated score can matter to any continuation.

Scan the sorted arrays with one pointer per array while maintaining `score1` and `score2`, the best scores reaching the current positions along their respective arrays. When `nums1[i]` is smaller, only the first path can consume it; add it to `score1` and advance `i`. Handle a smaller `nums2[j]` symmetrically.

**Merge the two states at an intersection**

If the pointed values are equal, either incoming path may reach that shared value and may leave through either array. Set both scores to `max(score1, score2) + nums1[i]`, then advance both pointers. Adding the shared value once preserves the path rule even though it appears in both inputs.

After one array ends, no further intersection exists. Add each remaining suffix to its corresponding score and return the larger total modulo $10^9 + 7$. The modulo is postponed until the end so comparisons always use the true path totals.

**Why discarding the smaller prefix is safe**

At a shared value, the possible future values depend only on the chosen outgoing array, not on how that intersection was reached. Any continuation available after the smaller prefix is also available after the larger prefix. Replacing both states with the larger incoming score plus the shared value therefore cannot remove an optimal path. Repeating this argument at every intersection proves that the final larger state is the maximum valid score.

## Complexity detail
Each pointer advances monotonically and visits its array once, so the running time is $O(n + m)$. Apart from the pointers and two score accumulators, the scan uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Hash shared values, then process segments:** can also obtain the right score, but storing intersections uses $O(\min(n,m))$ extra space instead of exploiting the sorted order directly.
- **Search for every value in the other array:** repeated linear membership checks can take $O(nm)$ time; repeated binary searches improve this to $O((n+m)\log\max(n,m))$ but remain unnecessary.
- If the arrays have no common values, the answer is simply the larger complete-array sum.
- If every value is shared, each value is still counted exactly once and both running scores remain equal.
- A path may benefit from switching at several intersections; choosing the better prefix independently at each shared value captures all such combinations.
- Compute with unrestricted or sufficiently wide integers, and apply the modulus only to the final maximum so modular wraparound cannot reverse a score comparison.
