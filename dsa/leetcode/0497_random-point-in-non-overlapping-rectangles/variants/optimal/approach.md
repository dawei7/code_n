## General

Uniformly choosing a rectangle first would be wrong because the rectangles can contain different numbers of integer points. A rectangle with one hundred lattice points should be selected one hundred times as often as a rectangle with one lattice point. The solution handles this with a prefix sum of integer-point counts.

For an inclusive rectangle `[x1, y1, x2, y2]`, the possible integer `x` coordinates are

`x1, x1 + 1, ..., x2`,

so there are `x2 - x1 + 1` choices. The same reasoning gives `y2 - y1 + 1` possible `y` coordinates. Because every horizontal choice can be combined with every vertical choice, the rectangle contains

`(x2 - x1 + 1) * (y2 - y1 + 1)`

integer points.

The two `+ 1` terms are essential. The geometric width `x2 - x1` measures continuous distance, but both endpoints are legal integer coordinates. A rectangle from coordinate two through coordinate four has the three integer positions two, three, and four.

**Build cumulative point counts.** `self.s[i]` stores the total number of integer points in rectangles `0` through `i`. For each rectangle, the code adds its point count to `self.s[i - 1]`.

At `i = 0`, `self.s[i - 1]` means `self.s[-1]`. Python's negative index refers to the last array element, and the entire prefix array was initialized with zeros, so that value is zero during the first iteration. This makes the same assignment work for every index, although an explicit running total would be more language-independent.

If rectangle point counts are `4, 6, 3`, the prefix array becomes `[4, 10, 13]`. It partitions ticket numbers `1` through `13` into intervals:

- tickets `1` through `4` select rectangle zero;
- tickets `5` through `10` select rectangle one;
- tickets `11` through `13` select rectangle two.

The length of each ticket interval equals that rectangle's number of integer points.

**Select a weighted rectangle with one random ticket.** `random.randint(1, self.s[-1])` chooses every integer ticket in the complete range uniformly and includes both endpoints. `bisect_left(self.s, v)` returns the first prefix total at least `v`. That index is exactly the rectangle whose ticket interval contains `v`.

Using `bisect_left` matters at boundaries. If `v` equals a prefix total, that ticket belongs to the rectangle ending at that prefix, not the following rectangle. For prefixes `[4, 10, 13]`, ticket four maps to index zero and ticket five maps to index one.

**Choose one point inside the selected rectangle.** Once rectangle `idx` is known, the code independently samples `x` uniformly from `[x1, x2]` and `y` uniformly from `[y1, y2]`. There are exactly the product number of coordinate pairs, and independent uniform choices give every pair probability

$$
\frac{1}{x_2-x_1+1}\cdot\frac{1}{y_2-y_1+1}
=
\frac{1}{A_i},
$$

where `A_i` is the integer-point count of rectangle `i`.

Let `S` be the total number of covered integer points. Rectangle `i` is selected with probability `A_i / S` because it owns `A_i` of the `S` tickets. Conditional on selecting it, each of its points has probability `1 / A_i`. Multiplying gives

$$
\frac{A_i}{S}\cdot\frac{1}{A_i}=\frac{1}{S}.
$$

Thus every covered integer point has exactly the same final probability, regardless of rectangle size.

The non-overlap guarantee is important because it makes every covered point belong to one rectangle. If rectangles shared an integer point, that point could be reached through multiple rectangle choices and would receive excess probability unless overlaps were explicitly corrected.

Coordinates may be negative, but `randint` works on any inclusive integer interval where the lower endpoint does not exceed the upper endpoint. Only rectangle widths and heights determine weights, so translating a rectangle does not affect its probability.

The constructor performs all weighting work once. Up to ten thousand later calls can reuse the same prefix array, making each pick logarithmic in the number of rectangles rather than recounting all points.

## Complexity detail

Let $r$ be the number of rectangles and $d$ the number of calls to `pick`. Construction visits each rectangle once, taking $O(r)$ time. Each pick uses binary search on the prefix array in $O(\log r)$ time and constant-time random coordinate generation. Across all calls, time is $O(r+d\log r)$.

The object stores the rectangle reference and an $r$-element prefix array, so its additional persistent space is $O(r)$. Each pick uses $O(1)$ temporary space and returns one two-integer list. The manifest's $O(r+d)$ space can include all outputs retained by an external caller; the solution object itself does not accumulate one result per call.

## Alternatives and edge cases

- **Choose rectangles uniformly:** This biases points in smaller rectangles because every rectangle gets equal probability despite unequal point counts.
- **Flatten every point explicitly:** It makes uniform choice trivial but can store millions of coordinate pairs unnecessarily. Prefix weights represent the same distribution compactly.
- **Linear weighted selection:** Scan prefix totals until finding the ticket. It is correct but costs $O(r)$ per pick instead of $O(\log r)$.
- **Alias table:** More preprocessing can support expected $O(1)$ weighted rectangle selection, but the small rectangle count makes prefix sums and binary search simpler.
- **Inclusive boundaries:** Both coordinate endpoints are valid, so each dimension count and each `randint` call must be inclusive.
- **One rectangle:** Its prefix owns every ticket, and sampling coordinates uniformly already produces the required distribution.
- **Negative coordinates:** They do not change widths, point counts, binary search, or uniform integer sampling.
- **Prefix boundary ticket:** `bisect_left` assigns a ticket equal to `self.s[i]` to rectangle `i`, which owns that final ticket.
- **First prefix construction:** `self.s[-1]` is safe only because the zero-filled list's last cell is still zero at `i = 0`. A running total is clearer in languages without Python negative indexing.
