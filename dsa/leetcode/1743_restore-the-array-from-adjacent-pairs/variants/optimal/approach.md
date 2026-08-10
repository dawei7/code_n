## General

**View every pair as an undirected edge**

Each distinct value in the forgotten array can be treated as a graph vertex. A pair `[a, b]` says that `a` and `b` were next to each other, but the pair may be written in either direction. The exact solution therefore creates an undirected edge by appending `b` to `g[a]` and `a` to `g[b]`.

Because the original array has unique elements, every interior value has exactly two neighbors: the values immediately before and after it. Each endpoint has exactly one neighbor. The supplied pairs include every original adjacency and are guaranteed to describe a valid array, so the resulting graph is not a branching general graph. It is one connected path containing all $n$ values.

This structural observation is the key. Restoring the array does not require trying permutations. Walking from either endpoint of the path to the other lists the values in a valid order. Starting at the opposite endpoint merely produces the reversed array, which is also accepted.

**Build the adjacency lists**

`g` is a `defaultdict(list)`. For every input pair, the source appends both directions. A list is appropriate because valid degrees are only one or two. There is no need for a set, sorting, or duplicate removal under the problem guarantees.

The array length is recovered as `n = len(adjacentPairs) + 1`. A path with $n$ vertices always has exactly $n-1$ edges, and the input contains one pair per adjacency. The answer list is preallocated as `[0] * n`. These zeros are placeholders only; actual values may also be zero, but positions are overwritten according to the traversal rather than tested for emptiness.

**Choose one endpoint and establish the direction**

The loop over `g.items()` searches for the first vertex whose neighbor list has length one. Such a vertex must be an endpoint. It writes that endpoint into `ans[0]` and its only neighbor into `ans[1]`, then stops searching.

There are exactly two endpoints, and dictionary iteration may encounter either one first. That nondeterminism is harmless. If one endpoint generates the original order, the other generates its reverse, and both contain every required adjacent pair.

Seeding two values is particularly useful because it establishes a travel direction without needing a visited set. Once `ans[0]` and `ans[1]` are known, the algorithm can always distinguish the neighbor it came from from the neighbor it should visit next.

**Choose the next neighbor without revisiting**

For each position `i` from two through `n - 1`, let the current path vertex be `ans[i - 1]` and the previous vertex be `ans[i - 2]`. The current vertex is still an interior point at every iteration where another value must be chosen, so its adjacency list `v` has exactly two elements.

One element of `v` is the previous value and the other is the next value. The source uses:

`ans[i] = v[0] if v[1] == ans[i - 2] else v[1]`.

If `v[1]` is the previous value, then `v[0]` must be the unvisited forward neighbor. Otherwise `v[1]` must be the forward neighbor. This also covers the case where `v[0]` is the previous value. Uniqueness of the original values makes equality testing sufficient to identify which neighbor is which.

The traversal never explicitly marks a vertex as visited. A path has no branch or cycle, and refusing to move back to the immediately previous vertex forces the walk forward. Thus the two most recent answer values contain all the state needed for navigation.

**Trace a representative reconstruction**

For pairs `[[2,1],[3,4],[3,2]]`, the graph has endpoint vertices one and four. Suppose dictionary order selects one. The first two answer entries become one and two.

At vertex two, the neighbors are one and three. One is the previous answer value, so three is selected next. At vertex three, the neighbors are four and two. Two is the previous value, so four is selected. The result is `[1,2,3,4]`.

Had the endpoint search selected four, the same rule would produce `[4,3,2,1]`. Its adjacent unordered pairs are identical, so it is equally valid.

**Why every written position is correct**

The first two values form a supplied adjacency because the second is the endpoint's sole graph neighbor. Assume the answer prefix through position `i - 1` follows the path without repetition. At its current final vertex, one neighbor is the preceding answer value. Because the graph is a path and more positions remain, the other neighbor is exactly the next unvisited path vertex. The conditional writes that other neighbor at position `i`.

By induction, every consecutive output pair is an input adjacency and the traversal never turns backward. It writes exactly $n$ positions in a graph containing exactly $n$ vertices, so it reaches every value once. The returned list is therefore one of the two valid orientations of the forgotten array.

## Complexity detail

Let $n$ be the number of values in the original array. The input contains $n-1$ pairs. Building both directions takes $O(n)$ time. Scanning dictionary entries to find an endpoint takes at most $O(n)$ time. The reconstruction loop writes the remaining values once, and inspecting a valid adjacency list costs $O(1)$ because its degree is at most two. Total time is $O(n)$.

The graph stores $n$ keys and $2(n-1)$ neighbor entries, so it uses $O(n)$ space. The returned answer uses another $O(n)$ space. Other variables are constant-sized. Thus total additional storage, including the required output, is $O(n)$, matching the manifest.

The iterative traversal uses no recursive call stack. That distinction is useful at the maximum $n=100000$, where a recursive path walk could exceed Python's recursion limit even though it has the same asymptotic space bound.

## Alternatives and edge cases

- **Recursive DFS:** Start at an endpoint and pass the previous vertex through recursion. It is logically equivalent but risks stack overflow on a path of length 100000.
- **Visited set:** A normal graph traversal can mark every visited value, but a path needs only the immediately previous value, so the set adds unnecessary $O(n)$ storage.
- **Degree map plus neighbor map:** Degrees can be counted separately, but adjacency lists already reveal endpoint degrees and are needed for traversal.
- **Try to order the input pairs directly:** Pair order and orientation are arbitrary, so sorting or chaining raw rows without a graph is unreliable.
- **Two possible answers:** Starting from either endpoint returns opposite orientations; the contract accepts both.
- **Exactly two values:** There is one pair, the endpoint seed fills both answer positions, and the reconstruction loop is empty.
- **Negative values:** Dictionary keys and equality comparisons handle them without any index conversion.
- **Zero as a real value:** Preallocated zeros are overwritten; the algorithm never interprets zero as an unused marker.
- **Large magnitudes:** Values up to the stated limits affect neither graph shape nor complexity.
- **Unique elements:** This guarantee is essential because the algorithm represents each numeric value as one graph vertex.
- **Endpoint degree:** A valid nontrivial path has exactly two vertices with degree one, guaranteeing that the seed loop finds one.
- **Interior degree:** Whenever the main loop needs a next value, the current vertex has two neighbors, making `v[1]` safe to access.
- **No cycle handling:** The code intentionally has no visited set because the valid-input guarantee says the graph is a path, not a cycle.
- **Dictionary order:** It influences only which accepted orientation is returned, not correctness.
- **Input preservation:** The pair list is read to build `g` and is never reordered or modified.
