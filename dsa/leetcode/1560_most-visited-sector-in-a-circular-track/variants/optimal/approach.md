## General

**Collapse the whole marathon into its start and finish**

Movement always follows increasing sector labels, wrapping from sector `n` back to sector one. The round boundaries do not change that direction; they merely identify checkpoints along one continuous traversal.

Imagine writing the entire visited sequence from `rounds[0]` to `rounds[-1]`. Every complete lap visits every sector exactly once. Complete laps therefore add the same count to all sectors and cannot affect which sectors are most visited.

After removing all complete laps, only the final partial traversal matters. It starts at the marathon's first sector and ends at its final sector, including both endpoints.

The exact source consequently reads only `rounds[0]` and `rounds[-1]`. Intermediate round endpoints determine how many full laps occurred, but those equal contributions do not change the winners.

**Why the residual arc receives one extra visit**

The starting sector is visited before any movement. As the runner proceeds, each crossed sector is visited in ascending circular order.

Whenever a full lap is completed, every sector gains one visit. At the end, sectors along the residual arc from the initial sector through the final sector have been encountered one additional time compared with sectors outside that arc.

Those residual-arc sectors are therefore exactly the most visited sectors.

This conclusion remains true when several rounds stop and restart conceptually at the same checkpoint: the marathon's path is continuous, so a round endpoint that is also the next round's start represents the same visit rather than an extra stationary visit.

**Case one: the residual arc does not wrap**

If `rounds[0] <= rounds[-1]`, the final partial traversal runs directly through:

`rounds[0], rounds[0] + 1, ..., rounds[-1]`.

The source returns `list(range(rounds[0], rounds[-1] + 1))`. Python's range excludes its upper endpoint, so adding one includes the final sector.

This list is already in ascending numeric order, exactly as required.

If start and finish are equal, this branch returns just that one sector. It has one extra visit after an integer number of complete laps.

**Case two: the residual arc wraps around n**

If the start label is greater than the finish label, the traversal first covers:

`rounds[0], rounds[0] + 1, ..., n`,

then wraps and covers:

`1, 2, ..., rounds[-1]`.

Traversal order would place the high-label portion first. The required output order is numeric ascending, so the source deliberately returns the two pieces in the opposite concatenation order:

`list(range(1, rounds[-1] + 1)) + list(range(rounds[0], n + 1))`.

Every selected residual sector appears exactly once in the output, and low labels precede high labels.

**Tracing the first example**

With four sectors and round checkpoints one, three, one, and two, the continuous sequence is one, two, three, four, one, two.

Sectors one and two occur twice. Sectors three and four occur once. The marathon starts at one and finishes at two without wrapping in the residual part, so the first branch returns one and two.

Intermediate checkpoints explain the route but are unnecessary after recognizing the full-lap symmetry.

**Tracing a wrapped residual arc**

Suppose the marathon starts at sector five and finishes at sector two on a seven-sector track after any number of rounds.

The residual arc contains five, six, seven, one, and two. These sectors have one more visit than three and four.

Ascending output must be one, two, five, six, seven. The second branch constructs precisely that list.

**A counting argument**

Let $L$ be the number of completed full laps after the starting visit is aligned. Every sector receives the same baseline of $L$ visits.

Each sector on the inclusive residual arc receives one additional visit, while every sector outside it receives none. Therefore maximum count is $L+1$, and the maximizing set is exactly that arc.

The two source branches enumerate that set for the nonwrapped and wrapped cases. This proves both membership and ordering correctness.

**Why simulating rounds is unnecessary**

A literal simulation could increment visit counts sector by sector for every round. Although constraints here are small, the work would depend on total traveled distance and obscure the invariant.

The endpoint method gives the result directly because only a difference of at most one visit can remain after canceling full laps.

## Complexity detail

Let $K$ be the number of returned sectors. Creating the output lists takes $O(K)$ time and $O(K)$ output space. Since $K \le N$, the manifest summarizes time as $O(N)$.

Apart from the returned lists and temporary range objects, the algorithm uses $O(1)$ auxiliary state. Python range objects themselves are constant-size; converting them to lists accounts for output allocation.

The number of round checkpoints does not enter the running time because the exact source accesses only the first and last elements.

## Alternatives and edge cases

- **Visit-count simulation:** Follow every round and count sectors. It is correct but does unnecessary work compared with the endpoint invariant.
- **Difference array on the circle:** It can count interval coverage efficiently for more general movement, but is excessive here.
- **Start below finish:** Return one contiguous inclusive numeric interval.
- **Start above finish:** Return the low-label interval followed by the high-label interval to preserve ascending output.
- **Start equals finish:** Exactly that sector has the residual extra visit.
- **Many complete laps:** They add equally to every sector and do not change the answer.
- **All sectors most visited:** This occurs when the residual arc covers the entire circle, as in a start of one and finish of `n`.
- **Two-sector track:** The same endpoint branches remain valid.
- **Round endpoints:** Intermediate values affect total laps but not which sectors receive the final extra visit.
- **Inclusive finish:** The upper range bound adds one so the ending sector is present.
- **Traversal order versus output order:** Wrapped traversal starts with high labels, but output must be numerically ascending.
- **Output space:** The returned list can contain all $N$ sectors even though auxiliary computation is constant.
