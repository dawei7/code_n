## General

**An exact cover must satisfy both measure and boundary structure**

The small rectangles form one perfect larger rectangle only if two independent kinds of evidence agree:

1. their total area equals the area of the smallest axis-aligned bounding rectangle;
2. their corners join exactly as a rectangular tiling’s corners must join.

Area alone is insufficient. An overlap adds area twice, while a gap adds no area; an overlap and gap of equal size could cancel numerically. Corner structure alone is also insufficient because it does not measure how much region is covered. The exact solution checks both.

It makes one pass through all rectangles, accumulating total area, expanding the bounding box, and counting every rectangle-corner coordinate.

**Find the only possible outer rectangle**

For a rectangle `[x, y, a, b]`, `(x, y)` is bottom-left and `(a, b)` is top-right. Across all inputs, the cover’s only possible outer bounds are:

```text
minX = minimum left x-coordinate
minY = minimum bottom y-coordinate
maxX = maximum right x-coordinate
maxY = maximum top y-coordinate
```

The code initializes these from the first rectangle, then updates them with `min` and `max` for each rectangle. If an exact rectangular cover exists, its four outer corners must be

$$
(\texttt{minX},\texttt{minY}),
(\texttt{minX},\texttt{maxY}),
(\texttt{maxX},\texttt{maxY}),
(\texttt{maxX},\texttt{minY}).
$$

There is no other candidate enclosing rectangle: any cover must reach every extreme coordinate present in its pieces.

**The area condition**

Each rectangle contributes

$$
(a-x)(b-y)
$$

to `area`. Coordinates may be negative, but widths and heights are positive by the contract, so every contribution is positive.

After the scan, the bounding rectangle has area

$$
(\texttt{maxX}-\texttt{minX})
(\texttt{maxY}-\texttt{minY}).
$$

For a perfect cover, interiors of the pieces do not overlap and their union fills the bounding rectangle. Areas are then additive, so the two totals must be equal. If the sum is smaller, some bounding area is missing overall. If it is larger, some area is covered more than once overall. A mismatch immediately proves failure.

The comparison uses integer arithmetic, so there is no floating-point rounding concern.

**Count how corners meet**

For every small rectangle, the solution increments the count of all four coordinates:

```text
(x, y)  bottom-left
(x, b)  top-left
(a, b)  top-right
(a, y)  bottom-right
```

The dictionary `cnt` maps each coordinate pair to the number of small-rectangle corners located there.

In a valid tiling, the four outermost corners are special. Each belongs to exactly one small rectangle, because there is rectangle area on only one inward quadrant and nothing outside the cover. Their counts must therefore be exactly one.

Every other corner coordinate must be internally or peripherally joined so that no boundary starts or stops unexpectedly. Its valid count is two or four:

- count two occurs when two rectangle corners meet along a straight continuation or at a T-shaped subdivision where another rectangle’s edge passes through without contributing a corner;
- count four occurs when four rectangle corners meet around an internal cross point.

A count of one at a non-outer coordinate exposes an unmatched corner, which creates a notch, gap boundary, or protruding boundary. A count of three likewise cannot pair all local corner turns into a seamless tiling. More than four would force multiple rectangles to occupy the same local quadrant and is incompatible with an exact non-overlapping cover. The exact implementation therefore requires every non-outer recorded count to be either two or four.

**Why the four bounding corners are checked before deletion**

The condition verifies all of the following at once:

- total small-rectangle area equals bounding area;
- each of the four bounding corners has count one.

If any test fails, the method returns `False` immediately.

When they all pass, the four outer-corner keys are deleted from `cnt`. This leaves only coordinates that must be internal joins or non-corner points along the bounding boundary. The final expression

```text
all(c == 2 or c == 4 for c in cnt.values())
```

checks their allowed multiplicities.

Deleting the four special keys makes the final rule simple. They are supposed to have count one, while no remaining key is allowed that count.

**How the tests work together**

Imagine a missing rectangular patch. Its boundary introduces corner turns that are not part of the bounding rectangle. Those turns leave non-outer corner multiplicities that cannot all pair as two or four in the required local configuration, or the total area becomes too small.

Imagine instead an overlap. The overlapped area makes the area sum too large unless some gap elsewhere compensates. If a gap does compensate by equal area, the overlap and gap introduce extra internal boundary endpoints and corner incidences. The corner-count test prevents those disconnected defects from masquerading as one clean outer rectangle.

The area equality establishes the correct total measure, while corner matching establishes the topology of one rectangular boundary with seamless internal joins. Neither is being used as a substitute for the other.

**A valid joining pattern**

Suppose two rectangles split a larger rectangle vertically:

```text
[0,0,1,2] and [1,0,2,2]
```

The outer corners `(0,0)`, `(0,2)`, `(2,2)`, and `(2,0)` each occur once. The two coordinates on the shared edge, `(1,0)` and `(1,2)`, each occur twice. The small areas sum to four, equal to the bounding area `2 * 2`. All checks pass.

If the right rectangle began at `x = 1.5`, there would be a gap. The bounding area would exceed the sum. The corners at the two sides of the gap would also remain unmatched. The method rejects the input without needing to inspect individual interior points.

**A correctness argument from the maintained evidence**

If the rectangles form an exact cover, additivity gives area equality. The four outer bounding corners are each contributed once. At every other coordinate where rectangle corners occur, the local regions meet without overlap or vacancy, producing exactly a paired or four-way corner incidence. Therefore every condition is necessary and a valid cover returns `True`.

Conversely, suppose all checks pass. The bounding extremes define one candidate rectangle, and its four corners are the only unpaired exterior corners. All other recorded corner incidences close in pairs or four-way joins, so the combined rectangle boundaries have no additional unmatched starts, ends, holes, or protrusions. The total piece area equals the area enclosed by the outer boundary. Any positive-area overlap would add excess multiplicity and would require an equal positive-area gap to preserve the total; such defect regions would introduce additional boundary corners that violate the matching condition. Hence there can be neither overlap nor gap, and the pieces cover the bounding rectangle exactly once.

## Complexity detail

Let $r$ be the number of input rectangles.

The algorithm performs constant work per rectangle: one area calculation, four bound updates, and four expected constant-time dictionary increments. The final scan visits at most four distinct corner entries per rectangle. Total expected time is $O(r)$.

The dictionary contains at most $4r$ distinct coordinate pairs, so auxiliary space is $O(r)$. Repeated corners share one dictionary entry and can reduce actual storage, but the worst case has no shared corners.

Dictionary operations have the usual expected constant-time hash-table qualification. Coordinate pairs and areas are integers. With coordinate magnitudes up to $10^5$ and up to $2\cdot 10^4$ rectangles, a fixed-width implementation should use a sufficiently wide integer type for summed area; Python integers expand automatically.

## Alternatives and edge cases

- **Corner parity set plus area:** Toggle each corner in a set: add it if absent and remove it if present. A perfect cover leaves exactly the four bounding corners. Together with area equality, this is the classic equivalent $O(r)$ approach. The exact source retains full counts and explicitly accepts only multiplicities two or four.

- **Sweep line:** Sort vertical events and maintain covered y-intervals while moving across x-coordinates. This can detect overlaps and gaps directly but is substantially more complex and usually costs $O(r\log r)$ time.

- **Grid marking:** Mark every unit cell or compressed coordinate region. Raw marking is impossible for large coordinate ranges, and coordinate compression still uses more machinery than the area-and-corner invariant.

- **One rectangle:** Its area equals its own bounding area, its four corners each have count one, and no counts remain after deletion. `all` over an empty collection is `True`, correctly accepting it.

- **A pure gap:** Total area is smaller than bounding area or unmatched internal corners remain, so the input is rejected.

- **A pure overlap:** Summed area is larger than union/bounding area, so area equality fails.

- **Equal-area overlap and gap:** Area alone could cancel, but their additional boundary structure prevents all non-outer corners from satisfying the required pairing.

- **Duplicate rectangle:** Its area is counted twice and each corner multiplicity increases; the bounding area does not double, so the input fails.

- **Rectangles touching only at an edge:** Shared edge endpoints receive paired corner counts. Touching is legal when the union remains one filled rectangle.

- **Rectangles touching only at one point:** A diagonal point contact cannot by itself connect two positive-area regions into one rectangular cover; the bounding-area or corner conditions reject the resulting gap structure.

- **T-junction:** One rectangle edge can pass through a coordinate where two other rectangle corners meet. Only actual corners are counted, so a valid T-junction commonly contributes count two and is accepted.

- **Negative coordinates:** Bounds use ordinary `min` and `max`, and widths are coordinate differences. Nothing assumes the rectangle lies in the positive quadrant.

- **Positive-area guarantee:** Every input satisfies `x < a` and `y < b`. Degenerate zero-width or zero-height pieces would complicate corner counts but are excluded by the contract.

- **Outer-corner identity:** Checking coordinate extrema separately is not enough; the four combined pairs must each occur exactly once. The dictionary lookups enforce those precise corners.
