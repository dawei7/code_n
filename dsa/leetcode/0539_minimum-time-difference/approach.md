## General

Clock times wrap after midnight, so they are points on a circle of 1440 minutes rather than ordinary unbounded numbers. The solution converts each `"HH:MM"` time into minutes after midnight, sorts those positions, checks neighboring positions, and adds one artificial neighbor to represent the midnight wrap.

**Use the fixed clock domain first.** A day contains only:

$$
24\cdot 60=1440
$$

distinct minute values. If `len(timePoints) > 1440`, at least two entries must represent the same minute by the pigeonhole principle. Their difference is zero, the smallest possible answer, so the method returns zero immediately.

This early test is more than a performance shortcut. It proves the answer without parsing any strings whenever the number of inputs exceeds the number of available minute positions.

**Convert each time to one integer.** For a string `x`:

- `int(x[:2])` reads the hour;
- `int(x[3:])` reads the minute after the colon;
- multiplying the hour by 60 and adding the minute yields minutes since midnight.

Thus `"00:00"` becomes zero, `"01:30"` becomes 90, and `"23:59"` becomes 1439.

Integer positions make differences easy to calculate. The expression is supplied to `sorted` through a generator, producing list `nums` in ascending minute order.

**Why only sorted neighbors matter.** On a line, consider sorted positions `a <= b <= c`. The difference `c - a` contains both smaller gaps `b - a` and `c - b`, so it cannot be smaller than both. More generally, any nonadjacent difference is a sum of adjacent nonnegative gaps. Therefore the smallest ordinary difference occurs between adjacent sorted entries.

If two equal times appear, they become adjacent and contribute gap zero, so duplicate handling needs no separate branch when the input count is at most 1440.

**Turn the circular wrap into one more adjacent pair.** Sorting places the earliest time at `nums[0]` and latest at `nums[-1]`. Their short clock distance may cross midnight rather than travel backward along the same day.

The clockwise gap from the latest time to the earliest time on the next day is:

$$
1440-\texttt{nums[-1]}+\texttt{nums[0]}.
$$

The code represents that by appending `nums[0] + 1440`. The final adjacent difference then becomes:

`(nums[0] + 1440) - nums[-1]`,

exactly the wraparound gap.

For `["23:59", "00:00"]`, the sorted positions are zero and 1439. Appending 1440 produces `[0, 1439, 1440]`. The ordinary gap is 1439, while the final wrap gap is one, so the answer is one.

For `["00:00", "23:59", "00:00"]`, sorting produces zero, zero, and 1439. The first adjacent gap is zero, which the minimum correctly returns.

**Use `pairwise` to examine every needed edge.** After the append, `pairwise(nums)` yields consecutive tuples:

`(nums[0], nums[1]), (nums[1], nums[2]), ...`.

The generator expression computes `b - a` for each tuple, and `min` returns the smallest gap.

There were at least two original time points, so after appending the wrap point there are at least three values and `min` always receives candidates.

**Why this covers the complete clock circle.** The sorted distinct-or-duplicate positions divide the 24-hour circle into arcs: every adjacent ordinary gap plus the one last-to-first midnight gap. Any route between two non-neighboring time points is the sum of at least two of these nonnegative arcs in one direction. A globally smallest pair must therefore be endpoints of one arc examined by the algorithm.

The appended value is not a real extra input and cannot create a false answer. It is a shifted copy of the earliest time used only to calculate the one missing circular adjacency.

The input list is not modified. `sorted` constructs a new numeric list, and only that list receives the appended value.

## Complexity detail

Let $n$ be the number of time points. When $n>1440$, the early return takes $O(1)$ time before parsing. Otherwise conversion costs $O(n)$, sorting costs $O(n\log n)$, and the adjacent scan costs $O(n)$. The exact source therefore has $O(n\log n)$ time and $O(n)$ auxiliary space under an input-sensitive analysis.

This differs from the manifest's $O(n)$ time and $O(1)$ space, which correspond to using a fixed 1440-entry presence array and scanning the bounded minute domain. Because 1440 is a fixed constant, one may describe all work after the pigeonhole bound as domain-bounded, but the actual implementation still allocates and sorts `n` converted values.

## Alternatives and edge cases

- **1440-entry presence array:** Detect duplicates while marking minutes, then scan occupied buckets. It achieves the manifest's $O(n)$ time and $O(1)$ domain-fixed space.
- **Compare every pair:** It handles wraparound but costs $O(n^2)$ time.
- **Omit the wrap gap:** This fails for times near opposite ends of the textual day, such as `"23:59"` and `"00:00"`.
- **More than 1440 entries:** A duplicate minute is guaranteed, so zero is returned.
- **Exactly duplicate strings:** Sorting places equal minute values together and yields gap zero.
- **Earliest and latest are closest across midnight:** The appended first value exposes that gap.
- **Two inputs:** The scan compares their direct sorted gap and their complementary wrap gap.
- **Midday-adjacent times:** They appear next to each other after sorting and are checked normally.
- **`"00:00"`:** It maps to zero.
- **`"23:59"`:** It maps to 1439, the largest legal minute.
- **Input immutability:** Only a newly created numeric list is sorted and extended.
