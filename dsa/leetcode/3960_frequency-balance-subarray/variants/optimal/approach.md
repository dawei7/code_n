## General

Fix a left endpoint and extend the right endpoint one position at a time. The map `counts[value]` stores each value's current occurrence count. A second map, `frequencyCounts[c]`, stores how many distinct values currently occur exactly $c$ times.

When a value whose old count is $c$ is appended, remove one value from bucket $c$ (deleting the bucket if it becomes empty), increment the value's count, and add it to bucket $c+1$. Each extension therefore updates the complete frequency distribution in expected constant time.

The current subarray is valid in exactly two situations:

1. `counts` has one key, which implements the special single-distinct-value rule.
2. `frequencyCounts` has exactly two keys `low` and `high`, and `high == 2 * low`. Because both keys are present, both required frequency levels occur.

Checking every right endpoint for every left endpoint considers every nonempty subarray. The maintained maps equal the true counts by induction over extensions, and the two tests are a direct translation of the definition, so the greatest recorded length is the requested answer.

The initial whole-array distinct-count checks return immediately for the all-equal and all-distinct extremes. They do not change the worst-case bound.

## Complexity detail

There are $O(n^2)$ left-right endpoint pairs. Hash-map updates and the validity test use expected $O(1)$ time per pair, giving $O(n^2)$ expected time. At most $n$ distinct values and $n$ frequency buckets can be stored, so auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Recompute every subarray:** Building a fresh frequency map for each endpoint pair takes $O(n^3)$ total time.
- **Scan all value counts after each extension:** Keeping `counts` but rebuilding the set of frequency levels costs another $O(n)$ per extension; the frequency histogram avoids that scan.
- **All frequencies equal:** Multiple distinct values that all occur $f$ times are invalid because the required $2f$ level is absent.
- **One distinct value:** Any positive count is valid under the separate first rule, even though only one frequency level exists.
- **Arbitrary value magnitudes:** Values can reach $10^9$, so an array indexed by value is inappropriate; use a hash map.
