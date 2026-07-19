## General
Synonym pairs define an undirected graph, and interchangeable words are exactly its connected components. Build those components with union-find: create a parent entry for every word and union the endpoints of each pair. Here, $\alpha$ denotes the inverse Ackermann function from amortized union-find analysis.

**Build sorted choices for each component**

After all unions, group every synonym word by its representative and sort each component's words. For a text word present in the structure, its available replacements are that sorted component; for any other word, its only choice is itself.

**Generate sentences directly in lexical order**

Process text positions from left to right and enumerate each position's choices in ascending order. Depth-first Cartesian-product traversal then emits complete token sequences lexicographically: every sentence under an earlier word choice precedes all sentences under a later choice at the first differing position. Join each completed sequence with single spaces.

Union-find supplies transitive equivalence, and the Cartesian product makes one independent choice at every position, so every valid sentence is produced. Each token sequence is unique because component word lists contain distinct words.

## Complexity detail
The $P$ unions take $O(P\alpha(V))$ amortized time. Producing $K$ sentences of $W$ words requires $O(KW)$ output work, which dominates component sorting under the small vocabulary limits. Including the returned strings and traversal state, space is $O(V+KW)$.

## Alternatives and edge cases
- **Graph search for each text word:** Repeated BFS or DFS finds the same components but revisits synonym edges for repeated words.
- **Generate then globally sort:** It is correct but adds $O(K\log K)$ sentence comparisons after output generation.
- **Only direct pairs:** Ignoring transitivity misses valid replacements connected through intermediate synonyms.
- **No synonym pairs:** The only result is the unchanged input sentence.
- **Repeated text word:** Each occurrence is replaced independently, so one component may contribute choices at several positions.
- **Words outside the graph:** Preserve them exactly as written with one available choice.
