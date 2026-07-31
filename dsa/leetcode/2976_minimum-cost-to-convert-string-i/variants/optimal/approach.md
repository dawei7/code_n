## General

Treat the 26 lowercase letters as vertices of a directed weighted graph. Every
conversion rule is an edge; when duplicate rules share endpoints, only their
minimum cost can matter. Converting one string position is then a shortest-path
query between its source and target letters.

**Precompute every letter-to-letter cost.** Initialize a $26\times26$ distance
matrix with zero on its diagonal, direct rule minima on edges, and infinity
elsewhere. Floyd–Warshall considers each letter as an allowed intermediate and
relaxes every ordered pair through it. After all 26 intermediates, each matrix
entry is the minimum cost of any rule sequence between those letters.

**Add independent position costs.** Operations affect one chosen character, so
choices at different indices neither constrain nor discount one another. Scan
the aligned characters and sum their precomputed shortest-path costs. A
matching pair contributes zero. If any matrix entry remains infinite, that
position can never reach its target and the whole conversion is impossible.

## Complexity detail

Let $N$ be the string length, $K$ the number of rules, and $A=26$ the alphabet
size. Loading edges, computing all-pairs paths, and scanning the strings take
$O(K+A^3+N)$ time. The distance matrix uses $O(A^2)$ space.

## Alternatives and edge cases

- **Dijkstra from every letter:** With positive edge costs, 26 Dijkstra runs are correct and have comparable practical cost; Floyd–Warshall is simpler for this dense, fixed-size alphabet.
- **Shortest path per string position:** Repeating a graph search for every index needlessly recomputes the same letter-pair costs and can take $O(NK)$ or worse.
- **Duplicate directed rules:** Retain the cheapest direct edge before computing transitive paths.
- **Indirect conversion:** A multi-rule path may be cheaper than a direct rule or may be the only route.
- **Matching characters:** They require no operation and cost zero even without an explicit self-rule.
- **One unreachable position:** Return `-1` immediately because every position must match.
- **Large total:** Repeated costs across $10^5$ positions may exceed 32-bit signed range.
