## Description

The rows describe a landscape of adjacent vertical bars. Sequential `id`
values give the bars' left-to-right order, each bar is one unit wide, and
`height` gives its elevation.

After rain, water above a bar is bounded by the tallest bar at or to its left
and the tallest bar at or to its right. Calculate the total number of water
units held across the complete landscape. Boundary bars and positions without
a taller boundary on both sides contribute zero. Return one value named
`total_trapped_water`; row order is irrelevant.
