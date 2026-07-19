## General
**Unweighted transformation edges make BFS the shortest-path method**

Treat each legal one-character transformation as an unweighted graph edge. Start a queue with `begin_word` at sequence length one because the return value counts words, not edges. FIFO order processes all shorter sequences before any longer one.

**Generate neighbors without building the full quadratic graph**

For each dequeued word, replace each of its `L` positions with each of `A` alphabet characters and test set membership. This generates only potential outgoing neighbors on demand rather than comparing every pair of dictionary words.

If `end_word` is absent from the dictionary, return zero immediately under the contract that every post-start word must be listed.

**First discovery fixes a word's minimum distance**

Delete a candidate from the unvisited set as soon as it is enqueued. BFS guarantees this first discovery uses the minimum number of edges. A later route to the same word is no shorter and is irrelevant when only the final minimum length—not every path—is requested.

**Every queued length is already optimal**

Every queued pair stores the minimum sequence length from the start to that word. No word outside the unvisited set has an undiscovered shorter route.

**First BFS arrival fixes the shortest transformation length**

Each generated neighbor differs in exactly one character and belongs to the allowed dictionary, so every queue edge is a legal transformation. Breadth-first layers contain words reachable with equal sequence length and are processed in increasing length order.

The first discovery of `endWord` therefore supplies a shortest ladder; no later layer can improve it. Marking words visited after discovery prevents redundant longer routes without losing a shorter one. If the queue empties, every reachable dictionary word has been explored and no ladder exists.

## Complexity detail
For at most `N` visited words, `L` positions and alphabet size `A` generate $O(NLA)$ candidates. Stored words and the queue use $O(NL)$ space.

## Alternatives and edge cases
- **Depth-first search:** may explore many long ladders before finding the shortest.
- **Store complete paths:** duplicates prefixes when only the minimum length is required.
- **Bidirectional BFS:** can reduce practical frontier size but is more intricate; asymptotic candidate generation remains bounded by the dictionary.
- The returned length includes both endpoints, so a direct one-edge transformation has length two.
- Removing words at enqueue time is correct here but would lose alternate parents in Word Ladder II, whose output requires all shortest paths.
