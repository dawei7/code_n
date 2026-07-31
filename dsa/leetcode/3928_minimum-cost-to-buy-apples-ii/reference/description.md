## Description

There are `n` shops numbered from `0` through `n - 1`. Shop `i` sells apples for `prices[i]`. Bidirectional roads connect some pairs of shops; a road described by `[u, v, cost, tax]` has two travel prices. Crossing it while empty costs `cost`, whereas crossing it while carrying apples costs `cost * tax`.

For every possible starting shop `i`, choose between buying there immediately and making a round trip to buy at some shop `j`. On such a trip, travel from `i` to `j` without apples, pay `prices[j]`, and return to `i` while carrying the purchase. Either leg may use any number of roads, and the outward and return routes do not have to coincide.

Compute the least total cost independently for each starting shop and return those `n` costs in shop order.
