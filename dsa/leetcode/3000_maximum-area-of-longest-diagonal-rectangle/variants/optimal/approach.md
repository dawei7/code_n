## General

**Compare squared diagonals.** The diagonal of a rectangle with side lengths
$a$ and $b$ is $\sqrt{a^2+b^2}$. Because square root is strictly increasing,
comparing $a^2+b^2$ gives exactly the same order without floating-point
rounding.

Scan every rectangle while storing the largest squared diagonal seen and the
area selected for it. A strictly larger squared diagonal replaces both stored
values. An equal squared diagonal replaces the stored area only when its area
is greater. Thus the stored pair is the required lexicographic maximum after
each prefix of the input, and the final stored area is the answer.

## Complexity detail

The algorithm performs constant work for each of the $N$ rectangles, so it
uses $O(N)$ time and $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Square-root comparison:** It is mathematically equivalent but introduces unnecessary floating-point arithmetic.
- **Sort by diagonal and area:** Sorting the rectangles by the same pair costs $O(N\log N)$ time and extra storage.
- **Pairwise dominance checks:** Comparing each rectangle with every other rectangle is correct but costs $O(N^2)$ time.
- **Equal diagonals:** Area, not input position, determines the winner.
- **Single rectangle:** Its area is returned directly.
