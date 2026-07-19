## General
**Make the global comparisons constant-time.** Build
`suffix_minimum[i]`, the minimum value from index `i` through the end. During a
left-to-right scan, maintain `prefix_maximum`, the maximum strictly before the
current index. The score-$2$ condition becomes
`prefix_maximum < nums[i] < suffix_minimum[i + 1]`.

**Apply the higher score before the fallback.** If the global condition holds,
add $2$. Otherwise test the two immediate neighbors and add $1$ only when
`nums[i - 1] < nums[i] < nums[i + 1]`. Update the prefix maximum after scoring
the current index so it still describes only earlier positions.

The stored extrema summarize all values on their respective sides. Therefore,
the first test is equivalent to both universal comparisons in the definition,
not merely a necessary approximation. When it fails, the second test exactly
matches the stated fallback. Every interior index receives its prescribed
exclusive score once, so their accumulated total is correct.

## Complexity detail
Here $N$ is the length of `nums`. Constructing suffix minima and scanning the
interior indices each take $O(N)$ time. The suffix array uses $O(N)$ space,
while the prefix side needs one scalar.

## Alternatives and edge cases
- **Rescan both sides per index:** Computing a fresh left maximum and right
  minimum for every position is correct but takes $O(N^2)$ time.
- **Prefix and suffix arrays:** Storing both extrema arrays is also linear in
  time and space, but the prefix maximum can be maintained incrementally.
- All comparisons are strict; an equal value anywhere on the relevant side
  prevents beauty $2$, and an equal neighbor prevents beauty $1$.
- An array of length three has exactly one scored index.
- A locally increasing triple can earn $1$ even when a distant earlier maximum
  or later minimum invalidates the global condition.
