## General

Existing bulbs may have different illumination radii, while every newly installed bulb has radius exactly one. The first step is to forget which existing bulb covers a position and record only whether that position is already visible. Once that visibility pattern is known, the remaining work consists of covering the invisible positions with length-three intervals.

The source performs these two stages in linear time:

1. combine all existing illumination intervals with a difference array;
2. count each consecutive run of invisible positions and add `\lceil L/3\rceil` bulbs for a run of length `L`.

**Representing existing coverage as interval updates**

For an existing bulb at position `i` with positive radius `v`, the covered interval is

$$
\left[\max(0,i-v),\min(n-1,i+v)\right].
$$

Marking every position of every interval separately could take quadratic time when many bulbs have large radii. A difference array records an entire inclusive interval using only two constant-time changes.

The source creates `d` with `n` zeros. For interval `[l,r]`, it performs:

```python
d[l] += 1
if r + 1 < n:
    d[r + 1] -= 1
```

The positive change says that one more coverage interval begins at `l`. The negative change immediately after `r` says that this interval stops contributing. If `r=n-1`, there is no in-array position at which to subtract, so the second update is omitted.

Positions with `lights[i] == 0` contain no working bulb and create no interval.

**Recovering visibility with a prefix sum**

During the final left-to-right scan, `s` is the running prefix sum of `d`. At position `p`, `s` equals the number of existing illumination intervals containing `p`:

- if `s>0`, at least one existing bulb illuminates the position;
- if `s=0`, the position is currently invisible.

The exact count above zero is unimportant; overlapping bulbs do not make a position “more than visible.” Still, using counts rather than booleans allows interval starts and ends to combine correctly.

**Turning invisible positions into runs**

The variable `cnt` stores the length of the current consecutive invisible run. Whenever `s==0`, the source increments `cnt`. When a visible position is reached, the current run has ended, so its required bulbs are added to `ans` and `cnt` is reset.

After the loop, a final addition handles an invisible run that reaches the road's last position.

This delayed processing is useful because a new radius-one bulb can cover neighboring invisible positions together. Counting each invisible position independently would overestimate the answer.

**Why a run of length `L` needs `\lceil L/3\rceil` bulbs**

A new bulb placed at `j` illuminates at most

$$
j-1,\ j,\ j+1,
$$

after clipping at the road boundaries. Thus one added bulb can cover no more than three previously invisible positions. Covering `L` invisible positions requires at least

$$
\left\lceil\frac{L}{3}\right\rceil
$$

bulbs.

That lower bound is attainable. Starting from the leftmost invisible position, place a bulb one step to its right whenever that position exists within the run. It covers the first three run positions. Repeat from the next uncovered position. The final group contains one, two, or three positions and can be covered by one appropriately placed bulb, possibly at the boundary of the run.

For example:

- a run of length one needs one bulb;
- lengths two and three also need one bulb;
- length four needs two bulbs;
- lengths five and six need two bulbs.

The integer expression

```python
(cnt + 2) // 3
```

computes `\lceil cnt/3\rceil` without floating-point arithmetic. Adding two before floor division makes every positive remainder round upward.

**Why separate invisible runs can be counted independently**

At first glance, a new bulb placed in an already visible position might cover invisible positions on both sides and make summing runs incorrect. The structure of existing coverage prevents that situation.

Two distinct invisible runs must be separated by a nonempty internal block of positions illuminated by existing bulbs. Every working existing bulb has radius `v>0`. If its center is internal to the road, its interval includes the center, its left neighbor, and its right neighbor, so it has length at least three. A covered component lying between two invisible runs cannot be clipped by a road boundary, and therefore that separating visible component has length at least three.

The closest invisible positions on opposite sides of such a separator are consequently at least four indices apart. A radius-one bulb covers positions whose leftmost and rightmost indices differ by at most two, so no new bulb can cover an invisible position from both runs.

An existing interval clipped to length one or two can occur only at a road boundary for very short roads or boundary-centered bulbs. Such a visible component cannot lie between two invisible runs because there is road on only one of its sides.

Therefore every newly installed bulb contributes to at most one invisible run, and the lower bounds for different runs add. Since the per-run constructions are also simultaneously feasible, the sum of `\lceil L/3\rceil` over all runs is the global minimum.

**A complete example**

Suppose the existing coverage scan yields

```text
invisible invisible invisible invisible | visible visible visible | invisible invisible
```

The first run has length four and needs `(4+2)//3=2` bulbs. The second has length two and needs one. The visible separator is already covered and is too wide for one radius-one bulb to reach invisible positions on both sides. The answer is therefore three.

The source never needs to store this boolean pattern explicitly. The prefix value `s` and current run length `cnt` are sufficient as positions stream from left to right.

## Complexity detail

Let `n` be the number of road positions. The first loop examines each entry of `lights` once and performs at most two constant-time difference-array updates. The second loop scans all `n` difference values once. Total time is `O(n)`.

The difference array contains `n` integers, so auxiliary space is `O(n)`. All remaining variables are scalar.

The algorithm does not modify `lights`. It creates its own coverage representation.

The `O(n)` time bound is asymptotically optimal because the input contains `n` radius values. Any correct method must, in the worst case, inspect all of them: a single unexamined positive radius could change which road positions are already visible and therefore change the answer.

Although existing bulbs can cover intervals of length `O(n)`, the difference-array method never loops across such an interval. Its cost depends on the number of bulbs and positions, not on the sum of their radii.

## Alternatives and edge cases

- **Mark every covered cell directly:** Looping through every existing interval is straightforward but can take `O(n^2)` time when many bulbs each illuminate most of the road. Difference updates reduce each interval to constant work.

- **Store merged intervals:** Sorting and merging existing coverage intervals can also reveal gaps, but bulb centers are already indexed along the road. The difference array obtains the same gap information in linear time without sorting.

- **Greedily place bulbs while scanning:** One can place a new bulb as far right as possible whenever the first uncovered position is encountered. That also leads to the same per-run count, but the source only needs the count and expresses it directly as `\lceil L/3\rceil`.

- **Count every invisible position separately:** This ignores that one radius-one bulb can illuminate as many as three consecutive invisible positions and can overcount by nearly a factor of three.

- **Combine arbitrary runs:** New bulbs cannot bridge the internal existing-coverage component between two invisible runs. Treating all invisible positions as one total count could underestimate the answer because their locations matter.

- **All positions already visible:** Every `cnt` remains zero, both ceiling additions contribute zero, and the returned answer is zero.

- **No existing bulbs:** The entire road is one invisible run of length `n`, so the answer is `\lceil n/3\rceil`.

- **One road position:** If an existing bulb is present, the answer is zero; otherwise one additional bulb is required. The difference and run logic handles both cases.

- **Intervals clipped at boundaries:** The `max` and `min` calculations keep every update within `[0,n-1]`. Omitting the end marker when `r=n-1` avoids an out-of-range access.

- **Overlapping existing bulbs:** Prefix coverage `s` may be greater than one, but any positive value still means visible. Start and end changes combine without special overlap logic.

- **Trailing invisible run:** No visible position arrives to flush a run ending at `n-1`, so the separate addition after the loop is necessary.

- **Runs of lengths divisible by three:** For `L=3q`, `(L+2)//3=q` exactly; the ceiling formula does not add an unnecessary bulb.

- **Installing on an already visible position:** This is allowed and can be useful near the edge of one invisible run, but it cannot serve two distinct runs separated by an internal existing-coverage component. The per-run count already allows any best center.
