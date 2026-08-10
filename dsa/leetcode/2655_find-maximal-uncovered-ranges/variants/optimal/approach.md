## General

**Work with intervals rather than an array of size $n$**

$n$ can be as large as $10^9$, so marking each covered index in a Boolean array is impossible.

Only the covered interval endpoints matter. By sorting covered ranges and sweeping their union, the solution identifies gaps without touching individual cells.

Variable `last` represents the greatest array index known to be covered by the union of all ranges processed so far.

**Sort by starting point**

`ranges.sort()` orders pairs lexicographically:

- increasing left endpoint;
- increasing right endpoint when starts tie.

After sorting, when processing interval $[l,r]$, no future interval begins before $l$. Therefore, any gap between the previous covered union and $l$ is final and can be emitted immediately.

The sort mutates the input interval list.

**Use `last = -1` as a virtual boundary**

The real array begins at index zero. Initializing:

`last = -1`

pretends that coverage before the first interval ends immediately before the array.

Then the first possible uncovered index is always `last + 1`:

- initially zero;
- later, one position after the merged covered prefix.

This removes the need for a separate “gap before the first interval” branch.

**Detect a nonempty gap**

For sorted covered interval $[l,r]$, the condition is:

`last + 1 < l`.

If true, at least one integer lies strictly after prior coverage and strictly before this new interval. The maximal uncovered gap is:

$$
[\texttt{last}+1,l-1].
$$

The code appends exactly those inclusive endpoints.

If `last + 1 == l`, coverage is adjacent with no missing cell. If `last >= l`, the ranges overlap or the current one begins inside prior coverage. Neither case creates a gap.

**Merge coverage with a maximum**

After considering the possible gap:

`last = max(last, r)`.

Taking the maximum is essential for nested and overlapping intervals.

Suppose prior coverage reaches ten and current interval is $[3,5]$. Assigning `last = 5` would move the frontier backward and later invent an uncovered gap inside already covered cells. `max` keeps it at ten.

For an interval extending farther right, the frontier advances to its endpoint.

**Why one frontier summarizes the processed union**

Because ranges are sorted by start, once sweep coverage has reached `last`, every processed covered cell relevant to future gaps lies at or before that frontier.

Any separated components encountered earlier already caused their intervening gap to be emitted. The latest component's rightmost endpoint is all the state needed to compare with the next interval.

Thus overlapping ranges are merged implicitly rather than stored in a separate union list.

**Emit the final suffix**

After all covered ranges, positions beyond `last` have no future interval that could cover them.

If:

`last + 1 < n`,

the nonempty tail gap is:

$$
[\texttt{last}+1,n-1].
$$

If `last >= n-1`, the covered union reaches the array end and no tail exists.

**Trace the first example**

For $n=10$ and sorted ranges `[[3,5],[7,8]]`:

- start with `last=-1`;
- interval $[3,5]$ leaves gap $[0,2]$, then `last=5`;
- interval $[7,8]$ leaves gap $[6,6]$, then `last=8`;
- after the loop, tail $[9,9]$ remains.

The returned ranges are already sorted by start because the sweep discovers them left to right.

**Trace overlapping ranges**

For `[[2,4],[0,3]]`, sorting yields `[[0,3],[2,4]]`.

- first interval begins at zero, so there is no leading gap; `last=3`;
- second begins inside coverage and extends it to four;
- final tail is `[5,n-1]`.

No false gap appears between overlapping intervals.

**Empty interval list**

With no covered ranges, the loop does nothing and `last` remains negative one. The tail condition is true for $n\ge1$, producing:

$$
[0,n-1].
$$

The whole array is correctly reported as one maximal uncovered range.

**Why emitted gaps are maximal**

Each emitted range starts immediately after covered index `last` or at array start, and ends immediately before the next covered start or at array end.

It cannot be extended left or right without including a covered cell or leaving array bounds. Adjacent uncovered gaps can never be emitted separately because no covered interval would separate them.

Every uncovered cell lies between consecutive portions of the covered union or outside its ends, so it belongs to exactly one emitted gap.


Before each sorted interval:

- `last` is the farthest covered endpoint of the most recent merged coverage component;
- every index before or at the current sweep position has been classified;
- all completed uncovered components have been appended in order.

The gap check classifies positions before the new interval, and the maximum update merges its coverage. After the loop, the suffix check classifies all remaining positions.

This proves completeness, disjointness, sorted order, and maximality.

## Complexity detail

Let $m=\texttt{len(ranges)}$. Sorting costs $O(m\log m)$. The sweep visits every range once in $O(m)$ time, so total time is $O(m\log m)$.

Python sorting may use $O(m)$ auxiliary memory. The returned answer can also contain $O(m+1)$ gaps, so total extra space including output is $O(m)$.

The algorithm's memory is independent of potentially enormous $n$.

## Alternatives and edge cases

- **Boolean coverage array:** Requires $O(n)$ time and space and is impossible for $n$ up to $10^9$.
- **Explicitly merge ranges first:** Correct but unnecessary; the gap sweep merges coverage implicitly.
- **Difference map of endpoints:** Can avoid cell storage but still needs sorted events and more bookkeeping.
- **No covered ranges:** Return the single full interval `[0,n-1]`.
- **Whole array covered:** No leading, internal, or trailing gap is emitted.
- **Overlapping intervals:** `max(last,r)` merges them.
- **Nested interval:** It must not move `last` backward.
- **Adjacent covered intervals:** They leave no uncovered integer between them.
- **Single-cell gap:** Strict condition detects and emits equal endpoints.
- **Input mutation:** `ranges.sort()` changes the caller-visible order.
