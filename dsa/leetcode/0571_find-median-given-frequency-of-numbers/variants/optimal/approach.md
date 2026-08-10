## General

The table is a compressed sorted multiset: row `(num, frequency)` means `num` appears that many times. The query locates the middle position or positions without physically expanding those copies.

CTE `t` attaches three cumulative quantities to each distinct number row.

**Count copies at or below the current number.** The ascending window:

`SUM(frequency) OVER (ORDER BY num ASC) AS rk1`

adds frequencies from the smallest number through the current `num`. Thus `rk1` is the final one-based decompressed position occupied by this number when counting from the low end.

**Count copies at or above the current number.** The descending window:

`SUM(frequency) OVER (ORDER BY num DESC) AS rk2`

adds frequencies from the largest number down through the current value. It is the number of decompressed elements greater than or equal to this `num`.

**Attach total sample size.** `SUM(frequency) OVER () AS s` has no partition or order, so every row receives total decompressed count `T`.

The outer filter keeps rows satisfying:

`rk1 >= s / 2 AND rk2 >= s / 2`.

Intuitively, a median value must reach at least halfway into the sample when counted from the bottom and also reach at least halfway when counted from the top.

For odd total `T = 2q + 1`, only the number whose frequency block contains position `q + 1` can satisfy both sides. Values completely below it have too few copies at or above; values completely above have too few at or below.

For even total `T = 2q`, the middle decompressed positions are `q` and `q + 1`. If they contain different values, each corresponding number row passes the two-sided condition. If both positions fall inside the same frequency block, only that one row passes, which is sufficient because averaging the same value twice would give the same result.

In the example, zero occupies decompressed positions one through seven of twelve. Ascending cumulative count is seven and descending count including zero is twelve, both at least six. Number one has only five copies at or above it, so it fails. The selected set contains zero and its average is 0.0.

**Why averaging selected rows gives the median.** With odd `T`, one row is selected and `AVG(num)` returns the central value. With even `T` and different middle values, exactly those two rows are selected and their average is the conventional median. With equal middle values, one compressed row represents both and returns that value.

The query uses `ROUND(AVG(num), 1)` to produce one decimal place and aliases the aggregate `median`.

**Why no frequency weighting appears inside AVG.** The selected rows identify the middle value blocks, not the full sample. For an even sample with two different middle values, each middle position contributes once regardless of how large the surrounding blocks are. When one block covers both positions, averaging one copy yields the identical result.

**Why unique `num` values matter.** The primary key guarantees one frequency block per value. Ordered cumulative sums therefore have a clear block boundary and the outer AVG cannot receive duplicate rows for the same numeric value.

The CTE logically computes windows across all Numbers rows before filtering. Filtering earlier would change totals and cumulative positions.

The final aggregate always returns one row. The source assumes a nonempty decompressed sample so a median exists.

For a concrete even case, suppose values two and ten each have frequency one. At two, `rk1 = 1` and `rk2 = 2`; at ten, `rk1 = 2` and `rk2 = 1`. With `s / 2 = 1`, both pass and `AVG` returns six. For frequencies two: two and ten: one, total three makes the two block cross the center from both directions, so only two passes.

The two cumulative ranks can be viewed as coverage intervals. A number with ascending cumulative end `rk1` and descending count `rk2` occupies decompressed positions from `s - rk2 + 1` through `rk1`. The filter asks whether that block touches the central position region. This is why one compressed row can represent both even middle copies.

## Complexity detail

Let $R$ be the number of compressed rows. A typical engine sorts rows by `num` for ordered windows, requiring $O(R\log R)$ time without a supporting index. Computing cumulative sums and filtering adds $O(R)$ work.

The intermediate CTE contains $R$ rows and may require $O(R)$ memory or temporary storage, matching the manifest. A primary-key order on `num` may let the optimizer reduce sorting cost.

The algorithm depends on compressed row count rather than total frequency `T`, which can be much larger.

## Alternatives and edge cases

- **Expand every occurrence:** It makes median positions obvious but costs $O(T)$ time and space rather than working with $R$ compressed rows.
- **Compute cumulative ascending positions only:** It can locate explicit middle ranks, but the two-sided condition elegantly handles odd and even totals.
- **Odd total:** Exactly one value block contains the middle.
- **Even total, distinct middle values:** Two rows are averaged.
- **Even total, same middle value:** One compressed row is sufficient.
- **One distinct number:** It is the median regardless of frequency.
- **Large frequency:** Window sums handle it without row expansion.
- **Negative numbers:** Numeric ordering and averaging work unchanged.
- **Rounding:** Applied after the median average, to one decimal place.
- **Supporting index:** It may improve physical execution without changing query semantics.
