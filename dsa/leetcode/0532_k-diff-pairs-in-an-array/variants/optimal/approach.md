## General
**Count values rather than index pairs**

Build a frequency map for the array. The answer concerns distinct value pairs, so repeated occurrences should establish availability without multiplying the result.

**Handle positive differences in one direction**

When $k > 0$, iterate over distinct values `value` and test whether `value + k` exists. This canonical lower-to-higher direction finds every valid unordered pair once and avoids both reversed duplicates and repeated-index combinations.

**Treat zero difference as a duplicate test**

When $k = 0$, a pair requires two separate occurrences of the same value. Count exactly those frequency-map entries whose frequency is at least two. Presence alone is insufficient in this case.

**Why the count is exact**

Every positive-`k` pair has a unique smaller member, and the lookup performed for that member finds its larger partner exactly once. Every zero-`k` pair corresponds to one value with at least two occurrences, which contributes once regardless of its exact frequency. Thus no valid value pair is omitted or duplicated.

## Complexity detail
Building the frequency map and scanning its at most `n` keys take expected $O(n)$ time. The map stores at most `n` distinct values, so space is $O(n)$.

## Alternatives and edge cases
- **Sort plus two pointers:** uses $O(n \log n)$ time and can use less auxiliary space, but duplicates require careful skipping.
- **Seen set plus result-pair set:** supports expected $O(n)$ time in one pass, though storing canonical result tuples is more machinery than frequency counting.
- **Enumerate every index pair:** can deduplicate answers with a set but takes $O(n^2)$ time.
- **$k = 0$:** only values occurring at least twice contribute.
- **Many duplicates:** each distinct value pair is counted once, not once per index combination.
- **Negative values:** the `value + k` lookup works without special handling.
- **No matching pair:** returns zero after all distinct values are checked.
