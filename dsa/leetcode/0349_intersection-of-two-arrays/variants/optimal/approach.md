## General
**Reduce both requirements to set membership**

Fast membership testing is the only information needed. Build a set from the shorter array so its duplicate values collapse and its elements can be queried in average constant time. Scan the longer array and add every value found in that set to a result set; the result set prevents repeated matches from appearing more than once.

**Why the result contains exactly the shared values**

For any returned value, membership in the shorter-array set and its occurrence during the longer-array scan prove that it belongs to both inputs. Conversely, every value shared by the arrays is present in the membership set and encountered in the scan, so it is added. Set uniqueness gives exactly one copy, establishing both directions of the required result.

**Trace duplicate input values**

With `[1, 2, 2, 1]` and `[2, 2]`, the shorter side becomes `{2}`. Both scanned occurrences match, but inserting them into the result set still produces only `{2}`.

## Complexity detail
Let the input lengths be $n$ and $m$. Building the smaller set and scanning the other array take $O(n + m)$ expected time. The membership set and unique result each contain at most $\min(n,m)$ values, so space is $O(\min(n, m))$, including the returned collection.

## Alternatives and edge cases
- **Sort both arrays and use two pointers:** takes $O(n \log n + m \log m)$ time but can avoid hash storage when mutating the inputs is acceptable.
- **Linear membership for every candidate:** can degrade to $O(nm)$, especially when the arrays are disjoint.
- If either input is empty, the intersection is empty.
- Negative values and zero are ordinary set keys.
- Duplicates on either or both sides never create duplicate output values.
