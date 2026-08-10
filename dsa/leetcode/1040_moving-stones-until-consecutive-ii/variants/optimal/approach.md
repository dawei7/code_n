## General

**Sort positions and think in terms of holes**

After `stones.sort()`, the positions satisfy

$$
s_0<s_1<\cdots<s_{n-1}.
$$

The game ends when all `n` stones occupy an interval of exactly `n` consecutive integer positions. Equivalently, the final outer span has length `n` and contains no holes.

The minimum and maximum require different reasoning. The minimum asks how many existing stones can already be kept inside one possible final block. The maximum asks how many empty positions can be filled one at a time before the endpoint rule forces completion.

**Minimum moves as a densest window**

Any final configuration occupies some interval of `n` consecutive positions. If a group of existing stones already lies within an interval whose inclusive width is at most `n`, those stones can potentially stay. Every stone outside that interval must be moved into one of its empty positions.

For sorted indices `i` through `j`, the inclusive width is

`stones[j] - stones[i] + 1`.

The sliding window maintains this width at most `n`. The right endpoint `j` moves forward once. While the window is too wide, `i` moves right until it fits.

The number of stones already inside is `j - i + 1`. Ordinarily, the number that must move is

`n - (j - i + 1)`.

Taking the minimum over windows keeps the largest feasible group and minimizes moved stones.

**Why moving outside stones usually works**

Suppose a fitting interval contains `q` existing stones and therefore has at least `n - q` empty positions after being extended, if necessary, to a length-`n` final block. Stones outside the block are endpoints of the current configuration. They can be moved into appropriate internal holes one at a time while preserving stones on both sides of the landing position.

Each moved outside stone fills one required position, so `n - q` is both a lower bound and a constructive count in the ordinary case.

**The special one-outlier case**

There is one important exception. Suppose the window contains exactly `n - 1` stones and those stones are already consecutive:

- `j - i + 1 == n - 1`.
- `stones[j] - stones[i] == n - 2`.

The ordinary formula says one move because only one stone lies outside the run. But the only positions that would extend the consecutive run are immediately before or after it. Moving the distant outlier into either position would leave the moved stone as the new smallest or largest stone. That violates the rule that the moved endpoint must cease to be an endpoint.

For example, with `[1,2,3,4,10]`, moving ten to five would form consecutive stones, but ten's stone would still be the right endpoint at position five, so that move is illegal.

Two moves are a safe candidate. If a consecutive run is `r, r + 1, ..., r + n - 2` and a sufficiently distant outlier lies to the right, move left endpoint `r` to `r + n`, which lies between the remaining run and the outlier. Then move the right outlier to `r + n - 1`. The final block is `r + 1` through `r + n`, and both moved stones landed in the interior at the time of their moves. The left-side case is symmetric.

Therefore, this window contributes two rather than the naïve one, and the code uses `mi = min(mi, 2)`. This does not claim the whole configuration always needs two: if the outlier is close enough, a different shifted sliding window can produce a legal one-move candidate. The minimum over all windows resolves that case.

If a fitting window has `n - 1` stones but they are not consecutive, it contains an internal hole. The outside endpoint can move into that hole and become non-endpoint, so one move is valid. That is why both parts of the special condition are necessary.

**Why the sliding window considers enough candidates**

For each right index `j`, the loop keeps the smallest left index `i` whose span fits within `n` positions. This is the maximum number of stones in a fitting window ending at `j`. A later left index would contain fewer stones and normally require at least as many moves.

In the special consecutive-`n - 1` case, dropping another stone would produce an ordinary candidate requiring two moves, equal to the corrected special value. Therefore, keeping only the maximal window for each `j` cannot miss a smaller answer.

If all `n` stones are already consecutive, the window count is `n` and the ordinary candidate is zero.

**Maximum moves must sacrifice one outer gap**

Initially, the leftmost or rightmost stone must move. Whichever endpoint moves inward, the new outer span discards the gap between that endpoint and its nearest neighbor. All empty positions in that discarded outer gap disappear at once and cannot each generate a separate move.

There are two choices:

- Move the left endpoint first and retain the interval from `stones[1]` through `stones[-1]`.
- Move the right endpoint first and retain the interval from `stones[0]` through `stones[-2]`.

The maximum strategy chooses the retained interval containing more empty positions.

**Count holes in the two retained intervals**

The interval `stones[1]` through `stones[-1]` has inclusive length

`stones[-1] - stones[1] + 1`

and already contains `n - 1` stones. Its number of holes is

`stones[-1] - stones[1] + 1 - (n - 1)`.

The symmetric interval `stones[0]` through `stones[-2]` has

`stones[-2] - stones[0] + 1 - (n - 1)`

holes.

The exact assignment

`mx = max(stones[-1] - stones[1] + 1, stones[-2] - stones[0] + 1) - (n - 1)`

chooses the larger count.

**Why every retained hole can produce one move**

Choose one retained interval. Repeatedly move the endpoint outside or at the advancing side into an empty position strictly between the current endpoints, arranging that only one hole is filled per move. There are always stones on both sides of such an internal landing position, so the moved stone ceases to be an endpoint.

For `[1,2,5]`, retaining interval two through five gives two holes, positions three and four. Move endpoint one to three, producing `[2,3,5]`. Then move endpoint two to four, producing `[3,4,5]`. Both moved stones land between the other endpoints, and two moves are achieved.

Each move toward completion fills at least one relevant hole or shortens the retained span. No sequence can use more moves than the number of holes after the unavoidable first outer-gap sacrifice. Since the construction fills them one at a time, the larger hole count is the exact maximum.

**Trace `[7,4,9]`**

Sorting gives `[4,7,9]` with `n = 3`.

For the minimum, window `[7,9]` has two stones inside three positions and contains an internal hole at eight. The outside endpoint four can move to eight and become the middle stone, completing `[7,8,9]` in one move.

For the maximum, retaining interval seven through nine has one hole, while retaining four through seven has two holes at five and six. The larger value is two. One valid sequence is nine to five, producing `[4,5,7]`, then four to six, producing `[5,6,7]`.

**Why the final pair is correct**

The sliding window checks every possible right boundary for a length-at-most-`n` target span and counts the fewest stones that must move, with the only illegal one-move geometry corrected to two.

The maximum formula first accounts for the mandatory loss of one extreme gap, then counts the largest number of remaining holes that can be consumed individually. These arguments independently prove the smallest and largest possible legal move counts.

## Complexity detail

Let `N = len(stones)`. Sorting dominates with `O(N \log N)` time. The sliding window is linear because `j` advances `N` times and `i` only moves forward, at most `N` times total. The maximum formula is constant time. Overall time is `O(N \log N)`, matching the manifest.

Python's in-place Timsort can use `O(N)` temporary storage, which matches the manifest's `O(N)` space. The sliding-window variables themselves use `O(1)` additional space. The method mutates the order of `stones`.

## Alternatives and edge cases

- **Simulate all legal configurations:** A state-space search can find minimum moves for tiny inputs but is infeasible for up to `10^4` stones and coordinates near `10^9`.
- **Count total holes only:** This can describe a loose maximum but ignores the rule that the first moved endpoint forces one outer gap to disappear. One of the two extreme gaps must be excluded.
- **Use only the densest window formula:** It incorrectly returns one for the consecutive-`n - 1` plus distant-outlier case. The endpoint landing rule creates the explicit two-move exception.
- **Already consecutive:** A window contains all `n` stones in width `n`, so minimum is zero; both maximum retained intervals contain no holes, so maximum is zero.
- **One internal hole and one outside stone:** If the `n - 1` kept stones are not consecutive, the outlier can fill the internal hole legally in one move.
- **One distant outlier beside a consecutive run:** Filling the adjacent extension would keep the moved stone as an endpoint, so minimum is two.
- **Large coordinate gaps:** Runtime depends on stone count, not numeric distance. Gaps contribute arithmetically to `mx` without being iterated.
- **Three stones:** The same formulas apply, including tricky configurations where a nominal finishing endpoint move is illegal.
- **Symmetry:** Reversing the number line swaps the two maximum candidates and leaves both results unchanged.
- **Unique positions:** Window counts and hole formulas rely on no two stones sharing a coordinate, as guaranteed.
- **Inclusive width:** The `+1` in `stones[j] - stones[i] + 1` counts integer positions, not distances. Omitting it breaks the fit test.
- **Input mutation:** If original stone order matters to the caller, sort a copy instead of the provided list.
- **Moved stone must become interior:** Every constructive move in the proof lands with at least one stone on each side; merely reaching a consecutive layout is not enough if that rule is violated.
