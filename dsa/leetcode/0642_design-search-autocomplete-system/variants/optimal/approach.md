## General

**Separate persistent sentence data from the current query**

The system must remember all historical sentences and their hot degrees across calls. It must also remember the characters typed since the most recent terminator. The solution represents these two kinds of state separately:

- a trie stores sentences and accumulated frequencies permanently;
- the list `t` stores the current unfinished input one character at a time.

When an ordinary character arrives, it is appended to `t` and the whole current text becomes the prefix to search. When `#` arrives, the characters in `t` form a completed sentence. That sentence is inserted with an increment of one, `t` is reset to an empty list, and no suggestions are returned for the terminator.

Keeping `t` as a list makes appending one character efficient. The implementation joins it into a string when it needs to search or save the sentence.

**How the trie represents the alphabet**

Every trie node owns an array of 27 child references. Indices zero through twenty-five represent lowercase `a` through `z`. Index twenty-six represents a space. The conversion is:

- `ord(c) - ord("a")` for a lowercase letter;
- twenty-six for a space.

An array gives direct child lookup without hashing. It is appropriate because the reference alphabet is fixed and small. A node represents the prefix spelled by the path from the root to that node; the root represents the empty prefix.

Only terminal nodes need sentence information. At the end of an inserted sentence:

- `v` stores its hot degree;
- `w` stores the complete sentence text.

Intermediate prefix nodes normally retain `v = 0` and an empty `w`. This lets the search traversal distinguish a complete historical sentence from a prefix that merely leads to longer sentences.

**Insertion accumulates rather than replaces frequency**

To insert sentence `w` with amount `t`, the trie walks or creates one edge for each character. At the terminal node, it performs `node.v += t` and saves the full sentence.

The addition is essential. The initialization data could conceptually contain an existing sentence count, and each later completed user input must raise that same sentence's hot degree by one. Replacing `v` would lose history. If the sentence is new, the default zero plus the increment creates its first count.

Storing the full sentence at the terminal node means a later traversal does not have to rebuild it from the path. That costs references to sentence strings but makes collection simple.

**Find the node for the current prefix**

`Trie.search(pref)` begins at the root and follows the child corresponding to every prefix character. If any required child is absent, no stored sentence can begin with the prefix, so it returns `None` immediately. Otherwise, the node reached after the last character represents exactly that prefix.

The exact `input` implementation restarts this walk from the trie root on every ordinary character. It first joins all characters currently in `t`, then searches the resulting prefix. It does not retain a current trie-node pointer between calls.

If a prefix is absent, the method returns an empty list, but it keeps accumulating typed characters. Every longer string still has the absent prefix at its beginning, so it cannot match an existing sentence during that input session. When the user eventually types `#`, the complete text is inserted and will become searchable in later sessions.

**Collect every sentence below the prefix**

Reaching a prefix node proves only that at least one stored path has that prefix. The requested ranking depends on complete sentences anywhere in the node's subtree, so a depth-first traversal explores that whole subtree.

At each visited node, a positive `v` means a sentence ends there. The traversal appends the pair `(frequency, full_sentence)` to `res`. It then recursively visits every non-null descendant through the 27 child positions. Calling the helper on null children is harmless because its first action returns immediately.

This collection includes the prefix itself if it is already a complete historical sentence, as well as every longer sentence beginning with it.

**Apply both ranking rules in the correct order**

Suggestions are ordered first by descending hot degree. When two sentences have the same degree, they are ordered by ascending ASCII sentence order. The sort key `(-frequency, sentence)` expresses those rules:

- negating frequency makes a normal ascending sort place larger original frequencies first;
- the sentence itself breaks equal-frequency ties in Python's lexicographic string order.

The implementation then returns only the sentence component from the first three sorted pairs.

The order in which DFS visits trie children does not determine the final answer because all matches are sorted afterward. This is particularly important because the trie assigns space to index twenty-six, whereas ASCII places a space before lowercase letters. The final string tie-break restores the contract's ASCII order even though child-array order is different.

**Why the returned suggestions are correct**

For a successful prefix search, the reached trie node has exactly the prefix typed so far. A trie descendant adds zero or more characters after that prefix, so every terminal node found by DFS is a stored sentence beginning with the prefix. Conversely, every stored sentence beginning with the prefix follows the prefix path to that node and then continues somewhere inside its subtree, so DFS reaches its terminal node. Thus `res` contains every eligible sentence exactly once and no ineligible sentence.

Sorting by `(-v, w)` imposes exactly the requested primary and secondary order. Taking the first three therefore returns the correct top three, or all available sentences when fewer than three exist.

On `#`, insertion increases precisely the completed sentence's hot degree and resetting `t` separates the next session from the old prefix. Therefore, the persistent ranking data remains consistent after every call.

**A small state evolution**

Suppose `"i love you"` has frequency five and `"island"` has frequency three. Typing `i` stores `["i"]` in `t`, finds the `i` prefix node, collects both terminal descendants, and ranks them by frequency. Typing a space next stores `["i", " "]`, searches `"i "`, and excludes `"island"` because its trie path does not contain that space.

If later characters form `"i love you"` and `#` is entered, insertion follows the existing path and changes its terminal frequency from five to six. No duplicate terminal sentence is created; later searches see the updated count.

## Complexity detail

Let `C` be the total number of characters across the initial sentences. Building the trie follows or creates one node per character, so initialization takes `O(C)` time. In the worst case it creates `O(C)` trie nodes. Each node contains 27 child slots, a constant-sized array, so the structural space remains `O(C)` under a fixed alphabet. Full-sentence strings are also referenced at terminal nodes; the provided input strings supply those initial objects, while newly completed sentences add storage proportional to their lengths.

The exact query cost requires more detail than a single total-character term. For one ordinary-character call, let `P` be the current prefix length, `U` the number of trie nodes in the matching prefix subtree, and `H` the number of terminal sentences in that subtree.

Joining `t` and searching from the root cost `O(P)`. DFS visits `U` nodes; because each node checks a fixed 27 children, this is `O(U)`. Sorting the `H` collected sentences costs `O(H log H)`, and constructing up to three output references is constant beyond their returned text. The exact per-character time is therefore `O(P + U + H log H)`. If the prefix does not exist, the DFS and sorting terms vanish, leaving `O(P)`.

For `#`, joining the current input of length `P` and inserting it both take `O(P)` time.

The manifest's broad `O(C + Q)` description captures linear construction and accumulated stored/query characters only under an abstract implementation that maintains ranked prefix data or otherwise treats result lookup as already indexed. The exact source shown here scans the matching subtree and sorts all matches on every ordinary call, so its honest query bound is the more detailed one above; it can be much larger when a short prefix matches many sentences.

Persistent trie storage is `O(C + A)`, where `A` is the total number of characters in distinct new sentences added after initialization. During an ordinary query, `t` and its joined prefix use `O(P)`, DFS recursion can reach a depth bounded by the longest matching suffix, and `res` holds `O(H)` pairs. The working-space bound for that call is therefore `O(P + H + D)`, with `D` the maximum DFS depth, in addition to the persistent trie.

## Alternatives and edge cases

- **Store the top three at every trie node:** During insertion, update each prefix node's cached best sentences. A query can then return results after following the new character, avoiding subtree traversal and full sorting. This greatly improves frequent-query performance but makes insertions more complicated because a frequency change can alter rankings along every prefix.

- **Maintain a current trie pointer:** Ordinary calls can advance from the node reached by the previous character instead of joining and rescanning the whole prefix. Once a path becomes missing, a sentinel state can remain missing until `#`. This reduces prefix navigation to constant time per character, though it does not remove the subtree traversal and sorting cost.

- **Heap for the best three:** While traversing matches, a size-three heap can avoid sorting all `H` results, reducing ranking work toward `O(H log 3)`. Tie ordering and the “worst of the kept three” comparison must be implemented carefully.

- **Hash map from prefix to sentences:** Precomputing every prefix can make lookup direct, but each sentence appears in many prefix collections, causing substantial duplicated storage and expensive ranking updates when frequencies change.

- **Dictionary children instead of 27 slots:** A map stores only existing edges and can save memory in sparse tries or support a larger alphabet. Array indexing is simpler and predictably constant-time for the fixed lowercase-letter-and-space alphabet.

- **Prefix is itself a sentence:** Its terminal node has positive `v`, so DFS collects it before visiting longer descendants. It competes normally by frequency and ASCII order.

- **No matching prefix:** `search` returns `None` and the result is empty. Typed characters must still remain in `t` so the completed new sentence can be learned at `#`.

- **Fewer than three matches:** Slicing `res[:3]` safely returns one, two, or zero entries without padding.

- **Equal hot degrees:** The sentence string in the sort key is mandatory. Relying on DFS child order would not reproduce ASCII ordering because the space edge is stored after the letter edges.

- **Repeated completed sentence:** Insertion reaches the existing terminal node and increments its hot degree. It must not create a separate record, or the same sentence could appear more than once.

- **Space inside a sentence:** It is a normal searchable character mapped to child index twenty-six. The terminator is `#`, not space.

- **The terminator character:** It is never appended to `t` and never inserted into the trie. It acts only as a command to save and reset.

- **Long trie paths and recursion:** DFS recursion depth is proportional to the remaining sentence-path length. The reference sentence-length bound keeps it modest, but an unrestricted production system might prefer an explicit stack to avoid language recursion limits.

- **Empty current input followed by `#`:** Normal problem interactions finish a typed sentence. The exact implementation would otherwise insert an empty terminal at the root; if such calls were allowed, they should be rejected or specified explicitly.

- **Updates after a previous absent prefix:** A new sentence inserted at termination creates the missing path. A later session can then find it, proving why an empty result during one session should not discard the typed text.
