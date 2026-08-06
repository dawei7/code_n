## Description

There are $n$ cities numbered from `0` through `n - 1`. Each highway `[city1, city2, toll]` is undirected and may be traveled in either direction by paying `toll`. No pair of cities has more than one highway.

You own a limited number of single-use discounts. Applying one discount to a highway traversal changes that traversal's cost to `toll // 2`, and at most one discount may be used on a traversal. Discounts are optional. Return the minimum cost of reaching city `n - 1` from city `0`, or `-1` if no route exists.
