## General

Every letter appearing in the input must occur at least once in a common supersequence. Because every word has length two, no letter ever needs more than two occurrences in a shortest solution: one occurrence can satisfy all constraints consistently placed on one side, while two occurrences can provide both an early and a late copy.

Represent each distinct letter as a vertex and every word `ab` as a directed precedence edge $a\to b$. If both letters occur once, that edge requires the single `a` to precede the single `b`. Thus the vertices assigned frequency one must induce a directed acyclic graph; a topological order then realizes all precedence constraints between them.

A letter assigned frequency two can place one copy before the singleton portion and one after it. Consequently, every edge incident to that doubled letter can be satisfied without imposing an ordering cycle on the singleton vertices. Choosing doubled letters is therefore exactly choosing a feedback vertex set: remove those vertices so the remaining induced graph is acyclic. A self-loop correctly forces its own vertex into that set.

Enumerate subsets of the at most 16 used letters in increasing order of cardinality. For each subset, run Kahn's topological test on the complementary induced graph using bitset adjacency. As soon as one cardinality layer contains acyclic complements, retain every valid subset in that layer and stop before exploring larger sets. Convert each retained mask into a 26-entry frequency array, assigning two to its doubled letters, one to every other used letter, and zero to absent letters. The first feasible doubled-set size is identical to minimum supersequence length, and its masks encode exactly the requested equivalence classes under permutation.

## Complexity detail

Let $C\le16$ be the number of distinct letters and $W$ the number of words. Building compressed adjacency costs $O(W)$. There are $2^C$ masks, and an acyclicity test examines at most $C^2$ possible directed edges, for $O(W+2^C C^2)$ time. Excluding the required output arrays, adjacency, indegrees, and bit masks use $O(C)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate supersequence strings:** The number of orderings grows factorially and repeats many strings that share the same requested frequency vector.
- **Use one copy of every letter:** This succeeds only when the full precedence graph is acyclic.
- **Double every cyclic vertex:** Cycles can overlap, so a smaller feedback vertex set may break several cycles simultaneously.
- **Self-loop word:** A word such as `aa` forces frequency two for `a`.
- **Acyclic constraints:** The empty doubled set is uniquely optimal, producing one frequency vector with one copy of each used letter.
- **Several minimum feedback sets:** Every distinct minimum mask must be returned, because it produces a different frequency array.
- **Absent alphabet letters:** Their entries remain zero in every 26-position result.
