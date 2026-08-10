## General

There is no cost for switching a bulb between time units and no requirement at inactive times. Therefore the spatial bulb-placement problem and the temporal interval-union problem can be solved independently:

1. determine the minimum number of bulbs that must be on during one active time;
2. determine how many distinct integer time units are active;
3. multiply the two values.

The source carries out this multiplication separately for every merged interval, which is equivalent to multiplying once by the total union length.

**Minimum bulbs for one time unit**

One bulb illuminates at most three positions: its own position and its immediate neighbors. Hence $q$ active bulbs can illuminate at most $3q$ distinct positions. To illuminate at least `brightness` positions, every solution needs at least

$$
\left\lceil\frac{\texttt{brightness}}{3}\right\rceil
$$

bulbs.

For integers, the source computes this ceiling as:

`(brightness + 2) // 3`.

The lower bound is achievable on a line. Place bulbs with enough spacing that their three-position neighborhoods cover consecutive groups, adjusting the first or final placement near a boundary. With

$$
q=\left\lceil\frac{\texttt{brightness}}{3}\right\rceil,
$$

the line contains at least `brightness` positions because `brightness <= n`, and $q$ bulbs can cover at least that many distinct positions. Boundary bulbs may cover only two positions, but placements can be shifted inward; the familiar minimum dominating placement for all $n$ path positions uses $\lceil n/3\rceil$ bulbs, and covering only a requested prefix of at most $n$ positions is no harder.

For small lines the same formula remains exact:

- with $n=1$, one bulb covers the one required position;
- with $n=2$, one bulb covers both positions;
- with $n=3$, the middle bulb covers all three.

Thus the per-active-time minimum is precisely the ceiling, independent of which time is being considered.

**Why the same spatial minimum can be repeated**

At every active integer time, bulbs may be chosen independently. There is no startup cost, switching penalty, persistence rule, or limit on how often a bulb is toggled.

The same optimal placement can simply be used at every active time, consuming the minimum number of energy units each time. Inactive times use zero bulbs.

Consequently, if $T$ distinct time units are covered by at least one interval, total minimum energy is:

$$
\left\lceil\frac{\texttt{brightness}}{3}\right\rceil T.
$$

Overlapping interval requirements do not add together. A time covered by several intervals still asks for the same brightness once and consumes one time unit's energy.

**Sort intervals before forming their union**

The source sorts `intervals` lexicographically, which orders them by start time and then by end time. It initializes `merged` with the first sorted interval.

For each later interval `x`:

- if the previous merged end is strictly less than `x[0]`, the intervals do not overlap, so `x` starts a new merged component;
- otherwise, they overlap at one or more inclusive integer times, and the previous end is extended to the larger endpoint.

An interval contained completely inside the previous component changes nothing because `max` keeps the existing farther end.

The condition uses `merged[-1][1] < x[0]`. Thus intervals `[1,3]` and `[3,5]` merge because they share time 3. Intervals `[1,2]` and `[3,5]` remain separate. They are adjacent on the integer timeline but share no active time; keeping them separate or combining their lengths would give the same total count.

**Inclusive interval length**

A merged interval from `start` through `end` contains:

$$
\texttt{end}-\texttt{start}+1
$$

integer time units. The added one includes both endpoints.

For each component, the source multiplies this length by the per-time bulb count and adds it to `ans`. Merged components are disjoint, so their lengths sum to the size of the interval union. No active time is counted twice.

**Input mutation**

`intervals.sort()` rearranges the caller-supplied outer list in place. In addition, `merged` stores references to original interval rows, and extending `merged[-1][1]` can modify those rows. This side effect does not change the returned minimum, but it is exact source behavior that callers retaining `intervals` can observe.

## Complexity detail

Let $m$ be the number of intervals. Sorting takes $O(m\log m)$ time. The merge scan and energy sum are each $O(m)$, so total time is $O(m\log m)$.

The `merged` list may contain all $m$ intervals when they are disjoint, using $O(m)$ additional reference storage. Python's in-place sort also uses implementation-dependent temporary storage bounded within the same asymptotic scale. The manifest's $O(m)$ space bound is appropriate.

All endpoint and energy arithmetic uses Python integers, so time endpoints up to $10^9$ and large accumulated energy do not overflow.

## Alternatives and edge cases

- **Iterate every active time unit:** Endpoints reach $10^9$, so expanding intervals into individual times is infeasible. Union lengths summarize them.
- **Add every interval length independently:** Overlapping time units would be charged more than once even though brightness is one shared requirement.
- **Use `brightness // 3` bulbs:** This rounds down and fails whenever brightness is not a multiple of three. Ceiling division is required.
- **Assume boundary bulbs always cover three:** A boundary placement covers fewer positions, but optimal bulbs can be shifted inward; the global ceiling remains achievable.
- **Optimize bulb positions separately for every interval:** The per-time minimum is identical, and overlap is handled through union length. Actual position identities do not affect energy.
- **Single-position line:** One bulb is necessary and sufficient for the only possible brightness.
- **Brightness equals `n`:** The formula becomes the domination number $\lceil n/3\rceil$ for the whole path.
- **One-point interval:** Inclusive length is one, so it consumes exactly one active time's bulb count.
- **Nested intervals:** The smaller interval adds no new active time and is absorbed by the larger merged component.
- **Touching at one endpoint:** They overlap at that integer time and are merged.
- **Adjacent but non-overlapping intervals:** `[a,b]` and `[b+1,c]` remain separate, but their summed inclusive lengths still equal the contiguous union size.
- **Caller-visible changes:** Sorting and endpoint extension mutate `intervals` and some of its row lists.
- **Large overlapping collection:** Sorting dominates; the linear merge prevents duplicate energy charges.
