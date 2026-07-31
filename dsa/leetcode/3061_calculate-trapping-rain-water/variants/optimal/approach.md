## General

**Find both boundaries at every position.** In increasing `id` order, a
running `MAX(height)` gives the tallest bar at or to the left of the current
bar. A second running maximum in decreasing `id` order gives the tallest bar at
or to its right. Window functions attach both values to every original row
without collapsing the landscape.

**Turn boundaries into water depth.** The water surface above one position can
rise only to the lower of those two maxima. Subtract the current `height` from
that lower boundary and sum the results. Because both running maxima include
the current bar, their minimum is never below its height, so every contribution
is automatically nonnegative and no separate clamp is required.

The left and right maxima are the highest available retaining walls on their
respective sides. Their lower value is therefore exactly the maximum stable
water level at the position, making the sum of the derived depths the requested
total volume for unit-width bars.

## Complexity detail

Let $n$ be the number of bars. General database execution may sort the rows for
the two ordered window directions, taking $O(n\log n)$ time. The final
aggregation is linear. Window and sort state use $O(n)$ space. An engine that
reuses the primary-key order may reduce constants or one sorting pass without
changing the stated general bound.

## Alternatives and edge cases

- **Correlated maximum per bar:** Looking left and right with two subqueries for every row is correct but can take $O(n^2)$ time.
- **Global maximum:** One landscape-wide maximum ignores whether a retaining wall exists on both sides of a position.
- **Adjacent heights only:** Water can be bounded by distant bars, so immediate neighbors are insufficient.
- A single bar or a monotone landscape returns zero.
- Equal-height boundary bars can retain water between them.
- Multiple basins are handled independently by the per-position depths and then combined by the final sum.
- Including the current row in both running maxima guarantees nonnegative contributions at boundary bars.
