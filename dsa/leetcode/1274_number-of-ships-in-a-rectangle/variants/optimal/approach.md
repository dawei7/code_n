## General
**Use the oracle to prune empty water**

For a rectangle with valid corner order, first ask `sea.hasShips` whether it contains anything. A negative answer proves that the entire region contributes zero, regardless of its area. If a positive rectangle has shrunk to one coordinate, that point contains exactly one ship.

**Split occupied rectangles without overlap**

Otherwise choose the midpoint of each coordinate range and partition the rectangle into four disjoint quadrants. The left quadrants end at `mid_x`, while the right quadrants begin at `mid_x + 1`; similarly, the lower quadrants end at `mid_y` and the upper ones begin at `mid_y + 1`. Skip any quadrant whose corners are inverted. Recursively count the remaining quadrants and add their results.

Every ship belongs to exactly one child because the four coordinate ranges neither overlap nor leave gaps. Empty children return zero after one oracle query. Repeated halving eventually reduces every occupied path to a single point, which contributes one. Therefore the sum counts every ship in the original rectangle exactly once. Because only branches whose rectangles still contain ships continue splitting, the sparse search stays within the interface's $400$-query budget for the legal grid and ship limits.

## Complexity detail
At each of $O(\log C)$ levels, only rectangles associated with the at most $s$ ships can remain active; each active rectangle creates at most four constant-time oracle queries. The work is therefore $O(s \log C)$. Depth-first recursion stores one path plus constant local state per level, requiring $O(\log C)$ auxiliary space.

The legal values satisfy $s \le 10$ and $C \le 1001$. Those fixed limits, together with the explicit $400$-query contract, make honest runtime scaling unsuitable; the package uses bounded-domain proof and boundary-property regression instead.

## Alternatives and edge cases
- **Query every coordinate:** It is simple but can make more than one million calls and violates the $400$-query limit.
- **Split along only one axis:** It can work, but four-way subdivision reduces both coordinate ranges together and gives the required shallow search on a two-dimensional grid.
- **Overlapping midpoint quadrants:** Including the midpoint in both sides double-counts ships and can prevent progress; one side must start at the midpoint plus one.
- **Empty target rectangle:** The initial oracle call returns false, so the answer is `0` immediately.
- **Single coordinate:** A positive oracle result means that exact point holds one ship.
- **Ships on boundaries:** The oracle is inclusive, and the non-overlapping quadrant boundaries assign each such ship to exactly one child.
- **Narrow rectangles:** Invalid quadrants created when one dimension has length one must be skipped rather than queried.
