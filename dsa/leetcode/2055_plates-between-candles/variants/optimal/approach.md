## General

**A query needs its first and last internal candles**

For query interval `[l,r]`, a plate counts only if some candle lies to its left and another lies to its right inside the same interval.

Let `i` be the first candle at or after `l`, and `j` the last candle at or before `r`. Every qualifying plate is exactly a plate strictly between `i` and `j`.

Plates outside those boundary candles lack one required side within the query and must be ignored.

**Build a prefix count of plates**

`presum[p]` stores the number of `*` characters in indices zero through `p-1`. It begins with zero and updates as

`presum[i + 1] = presum[i] + (c == '*')`.

The Boolean contributes one for a plate and zero for a candle.

With this half-open convention, the number of plates from index `a` through `b-1` is `presum[b] - presum[a]`.

**Precompute the nearest candle on the left**

The forward scan keeps `l` as the latest candle index seen, initially negative one.

When `s[i]` is a candle, `l=i`. Then `left[i]=l`. Thus `left[i]` is the nearest candle at or before index `i`, or negative one when none exists.

For a query's right endpoint `r`, `left[r]` is therefore the last candle inside the interval, provided it is not left of the query's start.

**Precompute the nearest candle on the right**

The backward scan similarly keeps `r` as the nearest candle seen from the right. `right[i]` becomes the nearest candle at or after index `i`, or negative one when none exists.

For query left endpoint `l`, `right[l]` is the first candle that can serve as the left boundary.

**Answer one query in constant time**

The source assigns

`i, j = right[l], left[r]`.

It requires both indices to exist and `i < j`. Strict inequality means two distinct candle positions enclose a nonnegative interior interval. If the only candle is the same on both sides, no plate can be between two candles.

When valid, the exact count is

`presum[j] - presum[i + 1]`.

This subtracts prefix counts to cover indices `i+1` through `j-1`, excluding both candles. Since candles contribute zero, other equivalent prefix boundaries exist, but this formula directly expresses the strict interior.

**Why the chosen candles capture all qualifying plates**

Any plate before the first query candle `i` has no candle to its left within the query. Any plate after the last query candle `j` has no candle to its right.

Every plate strictly between `i` and `j` has candle `i` on its left and candle `j` on its right. Therefore the qualifying set is exactly that interior.

**Trace the first query**

For `s = "**|**|***|"` and query `[2,5]`, `right[2]=2` and `left[5]=5`. The interior indices three and four are both plates.

`presum[5] - presum[3]` equals two, matching the source's `presum[j] - presum[i+1]`.

For query `[5,9]`, the boundary candles are at five and nine, enclosing three plates.

**Why preprocessing is worthwhile**

Scanning every query substring could take $O(N)$ per query and $O(NQ)$ overall. The prefix and nearest-candle arrays summarize all needed information once.

Each query then uses a fixed number of array lookups, comparisons, and one subtraction.


The forward and backward invariants prove `left[r]` and `right[l]` are the extreme candles inside the query whenever they exist. The boundary argument proves exactly the plates between those extremes satisfy the definition.

The prefix difference counts each such plate once and no outside character. Invalid or non-distinct candle boundaries leave the initialized answer zero, which is required.

## Complexity detail

Let $N=len(s)$ and $Q=len(queries)$. Building the plate prefix, left-nearest array, and right-nearest array takes three linear scans, or $O(N)$ time. Each query is answered in $O(1)$, for total time $O(N+Q)$.

The three preprocessing arrays use $O(N)$ space. The returned answer uses $O(Q)$ required output space. Excluding output, auxiliary space is $O(N)$.

## Alternatives and edge cases

- **Store candle indices only:** Binary-search the first and last candle for each query, giving $O(\log N)$ per query with less preprocessing state.
- **Scan every substring:** Correct but can degrade to $O(NQ)$.
- **No candle in query:** Both or one boundary lookup fails, so answer is zero.
- **Exactly one candle:** `i==j` and no plate is enclosed.
- **Adjacent candles:** `i<j` but the prefix difference is zero.
- **Plates outside boundary candles:** Correctly excluded because they lack a candle on one query side.
- **Query endpoints are candles:** Nearest arrays may choose the endpoints themselves.
- **All plates:** Nearest candles remain negative one and every answer is zero.
- **All candles:** Every answer is zero because there are no plates.
- **Inclusive query bounds:** `right[l]` and `left[r]` search inside those inclusive endpoints.
- **Boolean prefix increment:** `c == '*'` contributes zero or one in Python.
- **Input preservation:** The string and queries are only read.
