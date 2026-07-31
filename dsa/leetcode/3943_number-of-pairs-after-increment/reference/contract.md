## Function Contract

**Inputs**

- `nums1`: A nonempty fixed array of positive integers.
- `nums2`: A nonempty array of positive integers whose current values are changed by type-1 queries.
- `queries`: A nonempty sequence containing inclusive range additions `[1, x, y, val]` and pair-count requests `[2, tot]`.

Queries are processed from left to right. A type-2 query observes every type-1 update that precedes it and none that follows it. Pair counts use indices, not merely distinct values.

**Return value**

Return one integer for every type-2 query, in query order. Each integer is the number of index pairs `(j, k)` for which the current sum `nums1[j] + nums2[k]` equals that query's target.
