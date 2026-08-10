## General

Each query needs the true mode of a subarray: highest frequency, with smallest value breaking ties. Only after finding that mode does the threshold decide whether to return it or `-1`.

The source uses square-root decomposition:

- precompute the mode of every interval made of complete blocks;
- inspect the at-most-two partial boundary fragments per query;
- obtain exact candidate frequencies with binary search in position lists.

**Coordinate compression**

`values=sorted(set(nums))` stores distinct values in ascending order. Each original value maps to its index, called its rank.

Smaller numeric values receive smaller ranks. Therefore, tie-breaking by smallest rank is exactly tie-breaking by smallest original value.

`ranked` replaces each array value with its rank for compact frequency arrays.

**Position lists**

`positions[rank]` stores every array index containing that rank, in increasing order because indices are appended during a left-to-right scan.

To count rank r in inclusive range `[left,right]`:

`bisect_right(indices,right)-bisect_left(indices,left)`.

The first binary search finds how many positions are at most right; the second removes positions below left. This gives exact frequency in `O(\log n)`.

**Block layout**

`block_size=isqrt(n)+1` is approximately `\sqrt n`. The array is divided into consecutive blocks of that many positions, with a possibly shorter final block.

There are also approximately `\sqrt n` blocks. This balances preprocessing and per-query boundary work.

**Precomputing modes of complete-block intervals**

`block_modes[start_block][end_block]` stores the best rank in the array interval beginning at the first index of `start_block` and ending at the final index of `end_block`.

For each start block, the source creates a fresh frequency array and scans from that block's first index to the end of nums. It updates:

- `best_frequency` when a rank becomes more frequent;
- `best_rank` when frequency is larger or ties with a smaller rank.

At every block boundary, it records the current mode.

One forward scan therefore fills all end-block entries for a fixed start block without recomputing frequencies from scratch for each end.

**Small queries**

If a query lies within one block or spans only two adjacent blocks, its length is at most about `2*block_size`. The source directly scans every element in the range using a temporary dictionary.

This finds exact frequencies and applies the same frequency-then-rank comparison. For a short range, direct work is cheaper and simpler than combining an empty middle with boundaries.

**Large-query decomposition**

When at least one whole block lies strictly between the endpoint blocks:

- `middle_start=left_block+1`;
- `middle_end=right_block-1`.

The middle consists entirely of complete blocks. Its mode is retrieved in constant time from `block_modes`.

The source computes that middle mode's exact frequency across the full query using `range_frequency`, because boundary fragments may contain additional occurrences.

It then scans values in:

- the left fragment from `left` to the next block boundary;
- the right fragment from the first index after `middle_end` through `right`.

For each distinct boundary rank not already checked, it obtains the exact whole-query frequency from its position list and compares it with the current best.

`seen` prevents repeated binary searches when a value appears several times in boundary fragments or is already the middle mode.

**Why these candidates are sufficient**

Consider a value x that does not appear in either boundary fragment. Its full-query frequency equals its middle frequency.

Let y be the precomputed middle mode. In the middle, y has frequency at least x's, with smaller rank if tied. In the full query, y can only gain additional boundary occurrences; x gains none.

Therefore, x cannot beat y in the complete query. Any value that displaces the middle mode must gain something from a boundary and must therefore appear in a scanned boundary fragment.

This proves that the candidate set—middle mode plus distinct boundary values—contains the true full-range mode.

**Tie-breaking correctness**

Every update uses:

`frequency > best_frequency or frequency == best_frequency and rank < best_rank`.

Because rank order matches numeric value order, the selected candidate is the smallest value among those with maximum frequency.

Parentheses are omitted in source, but Python evaluates `and` before `or`, giving the intended grouping.

**Threshold handling**

After finding the true mode and its exact frequency, the source returns:

`values[best_rank]`

only if `best_frequency>=threshold`.

If the mode fails the threshold, every other value has frequency no larger, so no qualifying element exists and `-1` is correct.

It would be wrong to stop at the first value meeting threshold because another may have higher frequency or win the tie rule.

**Following a conceptual query**

Suppose a query has a large complete middle plus short edge fragments. The middle mode starts as best. A boundary value that occurs many times inside the middle may overtake it once its full frequency is counted. A value occurring only in the middle but not at either boundary cannot overtake the middle mode by the sufficiency proof.

This is how a small amount of boundary scanning recovers the exact answer for a much larger range.

**Precomputation correctness**

For one start block, the running frequencies exactly describe the interval from that block start through current index. At each complete block end, `best_rank` is maintained as its exact mode.

Thus every stored `block_modes[a][b]` is correct. Query logic then combines that correct middle candidate with all possible boundary challengers, proving every answer.

## Complexity detail

Let `B≈\sqrt n` be block size and number of blocks.

For each of `O(\sqrt n)` start blocks, preprocessing scans up to n positions and initializes a frequency array of up to n ranks. Time is `O(n\sqrt n)`.

The block-mode table has `O((n/B)^2)=O(n)` entries. Ranked data, position lists, and transient frequency arrays also use `O(n)` space.

A short query scans `O(B)` elements. A large query scans `O(B)` boundary positions, and each distinct candidate uses two binary searches costing `O(\log n)`. Worst-case query time is `O(\sqrt n\log n)`.

For q queries, total time is:

$$
O(n\sqrt n+q\sqrt n\log n),
$$

and auxiliary space is `O(n)`, matching the manifest.

## Alternatives and edge cases

- **Mo's algorithm:** Reorder offline queries and maintain frequencies; tie-aware mode maintenance is more complex, and answers must be restored to original order.
- **Segment tree of candidates:** A majority-style candidate is insufficient because queries request the true mode for arbitrary thresholds.
- **Scan every query:** It can cost `O(nq)`.
- **Precompute every subarray mode:** It needs `O(n^2)` space.
- **Query within one block:** Direct dictionary counting handles it exactly.
- **Query across two blocks:** Still short enough for direct scanning.
- **No complete middle block:** The source deliberately uses the small-query branch.
- **Threshold one:** The mode always qualifies in a nonempty range.
- **Threshold above mode frequency:** Return `-1` because no other value can qualify.
- **Frequency tie:** Smaller compressed rank means smaller original value.
- **Large numeric values:** Compression removes dependence on their magnitude.
- **Repeated boundary value:** `seen` avoids duplicate frequency searches.
- **Middle mode also on boundary:** Its full frequency is computed before boundary scans and it is already in `seen`.
- **Single-element range:** Direct scan returns that value when threshold is one.
- **Position lists:** Their sorted order follows construction and makes bisect counts valid.
- **Input preservation:** The source builds compressed structures without modifying `nums` or `queries`.
