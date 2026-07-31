## General

**Make every part as long as possible**

Scan `s` from left to right while maintaining the decimal value of the current part. Appending a digit changes that value to `value * 10 + digit`. Keep the digit in the current part when the extended value is at most `k`; otherwise, close the current part and begin a new one with that digit.

If a single digit exceeds `k`, no partition can make it smaller, so the answer is immediately `-1`.

**Why the greedy cut is optimal**

At any starting position, the algorithm chooses the longest feasible prefix. Any good partition must place its first cut no later: extending beyond the greedy prefix would exceed `k`. If another optimal partition cuts earlier, moving its first cut right to the greedy boundary consumes at least as many digits without increasing the number of remaining parts. Applying the same argument after each cut proves that no good partition uses fewer parts than the greedy scan.

## Complexity detail

Each of the $n$ digits is processed once. The time complexity is $O(n)$, and the algorithm stores only the current value and part count, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Dynamic programming over cut positions:** It can compute the minimum number of parts, but considering every earlier cut takes $O(n^2)$ time and is unnecessary because longer feasible prefixes are always safe.
- **Parse candidate substrings:** Repeated slicing and integer conversion creates extra allocations; incremental arithmetic avoids them.
- If any digit is greater than `k`, return `-1` before starting an invalid one-digit part.
- The final open part must be counted after the scan, including when the entire string fits in one part.
