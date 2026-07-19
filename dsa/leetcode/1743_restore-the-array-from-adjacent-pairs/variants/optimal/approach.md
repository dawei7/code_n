## General
**Interpret the pairs as an undirected path**

Create an adjacency list. For each pair `[u,v]`, add `v` to `u`'s neighbors and `u` to `v`'s neighbors. Because all original values are unique and every consecutive pair is present, this graph is exactly a path: its two endpoints have degree one and every interior value has degree two.

**Choose either endpoint**

Find any value with one neighbor and place it first. Choosing the other endpoint would simply reverse the reconstruction, which the contract also accepts.

**Walk without returning to the previous value**

At each interior value, one neighbor is the value just appended and the other is the only possible next value. Append the neighbor that differs from the previous value and continue until all $n$ vertices are present. Every supplied edge is traversed once, so the output contains all and only the required adjacencies.

## Complexity detail
Building the graph processes the $n-1$ pairs once, and the path walk visits each of the $n$ values once, for $O(n)$ time. The adjacency map contains $n$ vertices and $2(n-1)$ neighbor entries, while the output contains $n$ values, so auxiliary storage is $O(n)$.

## Alternatives and edge cases
- **Repeatedly scan all pairs:** Searching the raw pair list for the next neighbor avoids an adjacency map but can take $O(n^2)$ time.
- **Recursive depth-first search:** A DFS from an endpoint reconstructs the path, but a legal $10^5$-node path can exceed the language recursion limit.
- **Two values:** Either ordering of the only pair is valid.
- **Negative values:** Values are identifiers; their sign has no effect on adjacency.
- **Shuffled and reversed pairs:** Neither pair order nor orientation carries global left-to-right information.
- **Either endpoint first:** The two possible outputs are reversals and must both be accepted.
- **Unique values:** Remembering only the previous value is sufficient because a path has no repeated vertex or branch.
