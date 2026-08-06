## Description

There are `n` cities numbered from $0$ through $n-1$. Each entry
`[a, b, toll]` in `highways` describes one undirected highway between distinct
cities `a` and `b`; crossing it in either direction adds `toll` to the trip's
cost. No city pair has more than one highway.

Choose any starting city and make a trip that crosses exactly `k` highways.
Every city may be visited at most once, including the starting city, so the
trip must be a simple path of `k + 1` cities. Return the greatest total toll
among all such trips, or `-1` if no qualifying path exists.
