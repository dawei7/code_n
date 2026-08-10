## General

**Translate every two-letter word into an ordering edge.** If word `"uv"` must be a subsequence, some occurrence of `u` must appear before some occurrence of `v` in the common supersequence. The source collects the at most $16$ distinct letters, maps them to compact vertices, and records edge $u\to v$ in the bit mask `outgoing[u]`.

Every used letter must appear at least once. Some letters may need a second occurrence to satisfy cyclic ordering requirements. A frequency vector is therefore determined by the subset of letters used twice: ordinary vertices have frequency one, doubled vertices frequency two, and unused alphabet letters frequency zero.

**Why cycles force doubled letters.** Suppose a set of letters each appears only once. Their positions in any string define a strict linear order. All graph edges between those single-occurrence letters must point forward in that order, so their induced directed graph must be acyclic.

If a directed cycle remains among single-occurrence letters, no ordering can satisfy every edge. At least one vertex of each cycle must be doubled. Equivalently, after removing all doubled vertices, the remaining graph must be a DAG. The doubled subset is a feedback vertex set.

This condition is also sufficient. Place one copy of every doubled letter first, then place all remaining letters in a topological order, then place the second copy of every doubled letter. An edge from a doubled source can use its early copy; an edge to a doubled target can use its late copy; and an edge between two remaining vertices is satisfied by topological order. Edges between doubled vertices are also satisfied by an early source and late target. A self-loop such as `"aa"` forces `a` to be doubled because its loop prevents a topological ordering when it remains.

**Enumerate doubled subsets in increasing size.** The total supersequence length is

$$
m+\lvert D\rvert,
$$

where $m$ is the number of distinct letters and $D$ the doubled subset. The source tries `doubled_count` from zero upward and enumerates every subset of that size with `combinations`.

For one subset, `remaining = full ^ doubled` gives the single-occurrence vertices. The code builds indegrees only for edges whose source and target both remain. It then runs Kahn's topological-sort algorithm with bit masks.

`ready` contains every remaining vertex with indegree zero. The loop removes one ready bit, marks it visited, and decreases indegrees of its remaining outgoing neighbors. A neighbor enters `ready` when its indegree reaches zero.

If `visited != remaining` after the loop, some directed cycle prevented all vertices from being processed, so the doubled subset is invalid. If every remaining vertex is visited, the subset yields a feasible shortest-supersequence frequency pattern.

**Construct one canonical frequency vector per permutation class.** The result does not ask for the strings themselves. Strings with the same letter frequencies are permutations of each other and should appear only once. Each valid doubled subset uniquely determines its frequency vector: participating letters receive `1 + doubled_bit` and all other alphabet letters remain zero.

Different doubled subsets produce different positions containing frequency two, so they cannot duplicate a frequency vector. The source appends all valid vectors at the first subset size that has any answer, then returns immediately. Because sizes were tried increasingly, these and only these vectors have minimum total length.

For `["ab","ba"]`, the graph is the two-cycle $a\leftrightarrow b$. Removing either $a$ or $b$ makes the remainder acyclic. Those two minimum doubled subsets produce frequencies $(2,1)$ and $(1,2)$.

For `["aa","ac"]`, the self-loop forces $a$ to be doubled. Removing it leaves $c$ acyclic, producing the single vector with two $a$s and one $c$.

**Why bit masks fit well.** With at most $16$ vertices, one integer can represent a subset, outgoing neighbors, ready vertices, or visited vertices. `targets & -targets` extracts the least significant set bit, and `bit_length() - 1` converts it back to a vertex index. These are implementation details of ordinary set and topological operations.

## Complexity detail

Let $C\le16$ be the number of distinct letters and $W$ the total input characters. Building letters and edges costs $O(W)$. Across all subset sizes, at most $2^C$ doubled subsets are tested. Rebuilding indegrees and performing topological processing costs $O(C^2)$ per subset in the dense worst case. Total time is $O(W+2^C C^2)$.

Outgoing masks, indegrees, index maps, and topological masks use $O(C)$ auxiliary storage. The returned answer can itself contain up to exponentially many $26$-entry vectors; excluding required output, space matches the manifest's $O(C)$ characterization.

## Alternatives and edge cases

- **Enumerate supersequence strings:** Even at small alphabet size, ordering and repeated-letter choices create enormous duplication. Frequency subsets avoid permutations entirely.
- **Topological sort without doubling:** It works only when the original graph is already acyclic. Cycles require repeated letters.
- **Double every cycle vertex:** That is sufficient but not shortest. The enumeration finds minimum feedback vertex sets.
- **Self-loop:** A word with two equal letters requires two copies, and its graph self-loop forces that vertex into every valid doubled subset.
- **Acyclic graph:** The empty doubled subset succeeds first, so every used letter receives frequency one.
- **Multiple edges:** Bitwise OR deduplicates identical ordering edges without changing feasibility.
- **Disconnected components:** Kahn's algorithm processes all zero-indegree components; doubled choices are needed only to hit cycles.
- **Several minimum subsets:** All are collected before returning, producing all non-permutation-equivalent shortest frequencies.
- **Alphabet letters absent from words:** Their frequency remains zero in every length-26 result.
- **Construction sufficiency:** Early and late copies of doubled letters satisfy edges crossing the removed set, while the remaining DAG's topological order satisfies every single-to-single edge.
