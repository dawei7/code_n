## General

**A value count alone does not identify a unique frequency**

First count every distinct value in `nums`. This produces $F(x)$, but knowing that a value occurs, for example, three times is not enough: the decision also depends on whether some *other* value occurs three times. A second map therefore counts frequencies themselves. For every distinct value $x$, increment the entry for $F(x)$. When that pass ends, `frequency_counts[f]` equals the number of distinct values occurring exactly $f$ times.

**The final scan restores the contract's notion of first**

The maps deliberately discard positional order, so selecting a key while iterating either map cannot establish which qualifying value appears first in `nums`. Scan the original array once more. At a value $x$, the test `frequency_counts[frequencies[x]] == 1` is true exactly when no other distinct value shares $F(x)$. Returning at the first true test therefore selects the smallest qualifying array index.

If the scan finishes, every represented frequency belongs to at least two distinct values. No array element can then satisfy the condition, so returning `-1` is correct.

## Complexity detail

Let $N$ be the length of `nums` and $D$ the number of distinct values. The three passes visit $N$, $D$, and at most $N$ entries, respectively, for expected $O(N)$ time with hash maps. The two maps hold at most $D$ value entries and at most $D$ different frequency entries, so they use $O(D)$ auxiliary space.

The runtime benchmark defines size as $N$ and uses arrays of distinct values. Every value then has frequency one, so no candidate can return early during the final scan. The accepted implementation and an independent `Counter` formulation retain linear scaling, while a correct repeated full-array counting control must do quadratic work before reaching the same `-1` result.

## Alternatives and edge cases

- **Sort and group:** Sorting a copy makes equal values contiguous and exposes all frequencies, but preserving the original first-occurrence rule still needs additional bookkeeping or another scan; the time bound becomes $O(N\log N)$.
- **Fixed indexed arrays:** Because values and frequencies are at most $10^5$, two arrays can replace the maps. This is deterministic $O(N+V)$ time and $O(V)$ space for $V=10^5$, but it initializes the entire source range even for a small input.
- **Repeated counting:** Calling a whole-array count for every encountered value can obtain the correct frequencies, but it can require $O(N^2)$ time when many values are distinct.
- **One element:** Its frequency is one and no other distinct value exists, so that sole value must be returned.
- **All values distinct:** Every distinct value has frequency one; when there is more than one value, that frequency is shared and the answer is `-1`.
- **Several unique frequencies:** More than one value may have a unique frequency. The answer depends on the earliest occurrence in `nums`, not on the smallest value or smallest frequency.
- **Repeated positions of one qualifying value:** Once a value's frequency is unique, every occurrence of that value qualifies; the leftmost occurrence is the one selected by the final scan.
- **No qualifying frequency:** The sentinel is `-1`, which cannot collide with an input element because every `nums[i]` is positive.
- **Upper value boundary:** The value `100000` is legal and behaves like every other key; a fixed-array implementation must include that endpoint.
