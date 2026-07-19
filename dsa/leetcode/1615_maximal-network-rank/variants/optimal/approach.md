## General
**Separate incident counts from shared-road detection.** Process every road once. Increment the degree of each endpoint, and mark the two cities as directly connected in a symmetric Boolean matrix. The degree array then counts every road touching each city, while the matrix answers whether a particular pair shares one road in constant time.

**Evaluate each unordered city pair once.** For cities `first < second`, adding their degrees counts all roads incident to either city. Every road other than `[first, second]` touches at most one selected endpoint and is counted once. If the selected cities are adjacent, their shared road appears in both degrees, so subtract one Boolean connection indicator. Thus `degree[first] + degree[second] - connected[first][second]` is exactly that pair's network rank.

Taking the maximum across all $n(n-1)/2$ unordered pairs considers every legal choice of two different cities. Since each pair formula counts precisely the union of its incident roads, the largest computed value is the infrastructure's maximal network rank.

## Complexity detail
Building degrees and connections takes $O(m)$ time. Inspecting every unordered city pair takes $O(n^2)$ time, for $O(n^2+m)$ overall. The Boolean connection matrix uses $O(n^2)$ space and the degree array uses $O(n)$ more.

## Alternatives and edge cases
- **Adjacency sets:** Store each city's neighbors in a set instead of a matrix. Membership remains expected $O(1)$ and space falls to $O(n+m)$, with the same expected time bound.
- **Rescan roads for every pair:** Building the union of incident roads separately for each city pair is correct but can require $O(n^2m)$ time.
- With no roads, every pair has rank zero.
- Isolated cities remain valid pair members, although pairing two isolated cities contributes no roads.
- If the chosen cities are directly connected, their shared road must be subtracted exactly once.
- Disconnected components do not restrict the choice; cities from different components can form the best pair.
- In a complete graph, any pair has rank $2n-3$, not $2n-2$, because its connecting road is shared.
