## General

Operations on different intervals cannot partially overlap, so a legal
transformation partitions the string into unchanged characters and converted
blocks. Repeated operations on one block are allowed only with the same
endpoints, meaning every intermediate rule string for that block has the same
length.

**Close the rule graph under indirect conversions.** Assign an ID to every
distinct string appearing in `original` or `changed`. Directed rule costs form
a graph on those IDs. Keep the cheapest duplicate edge, then use
Floyd–Warshall to compute the minimum cost between every pair. Edges already
preserve length, so reachable paths automatically represent legal repeated
operations on one identical interval.

**Recognize candidate blocks without slicing.** Insert every identified rule
string into a trie. At a reachable prefix boundary `start`, walk `source` and
`target` through the same trie in parallel. Whenever both walks end at known
rule strings and their all-pairs cost is finite, the interval can extend the
prefix dynamic program. If either trie walk fails, no longer rule string can
begin at that position, so scanning that start can stop.

Also advance one character for zero cost whenever the aligned characters are
already equal. Each dynamic-programming transition appends either one unchanged
position or one converted interval, so transitions never overlap. Conversely,
every legal operation collection has these prefix boundaries and is considered
by the recurrence.

## Complexity detail

Let $N$ be the string length, $M$ the number of distinct rule strings, and $S$
their total distinct length. Floyd–Warshall costs $O(M^3)$, trie construction
costs $O(S)$, and simultaneous matching across all prefix starts costs at most
$O(N^2)$. Total time is $O(M^3+N^2+S)$. The distance matrix, dynamic program,
and trie use $O(M^2+N+S)$ space.

## Alternatives and edge cases

- **Slice every candidate interval:** Hash lookup on materialized substrings is conceptually simple, but copying characters across all intervals can raise the work to $O(N^3)$.
- **Shortest path during every DP transition:** Repeating graph searches discards the benefit of the small shared rule graph and adds substantial redundant work.
- **Identical interval chain:** Multiple conversions may reuse exactly the same endpoints, enabling indirect rule paths.
- **Partial overlap:** Two otherwise useful conversions are illegal if their intervals intersect without being identical.
- **Matching character:** It advances for zero cost without requiring any rule string.
- **Duplicate rules:** Only the cheapest direct cost for an ordered string pair matters.
- **Different rule lengths:** They belong to disconnected graph components because every individual rule preserves length.
- **Unreachable suffix:** Return `-1` if the final prefix state remains infinite.
