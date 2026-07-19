## General
**Store two different counts at every node**

Each node keeps a terminal count for words ending there and a prefix count for word occurrences passing through it. These quantities answer different questions: the node for `"app"` may have terminal count zero while still having a positive prefix count because `"apple"` is stored.

**Update the whole path for insert and erase**

Insertion follows or creates one child per character and increments each reached node's prefix count, then increments the final terminal count. Erasure follows the guaranteed-existing path, decrements every reached prefix count, and decrements the final terminal count exactly once.

**Read the count at the completed path**

An exact query traverses the requested word and returns its final terminal count. A prefix query traverses the prefix and returns its final prefix count. If a required child is absent, the answer is zero.

After every update, a node's prefix count equals the number of current word occurrences containing that path, while its terminal count equals occurrences ending there. This invariant is initially true and each insert or erase changes exactly the affected path by one, proving all query results are correct.

## Complexity detail
Every method traverses at most the $L$ characters in its argument, so it takes $O(L)$ time. The trie creates at most one node per distinct stored prefix and therefore uses $O(S)$ space. Nodes whose count becomes zero may be retained without changing this bound over the operation history.

## Alternatives and edge cases
- **Hash map of complete words:** Exact counts are constant-time, but a prefix query must scan every distinct word and can become quadratic over a long operation sequence.
- **Boolean terminal markers:** They cannot represent repeated insertions or erase exactly one occurrence.
- **Duplicate insertion:** Increment all path counts and the terminal count for every occurrence.
- **Erase one duplicate:** Decrement counts by one, leaving other occurrences present.
- **Word that is another word's prefix:** Terminal and prefix counts must remain independent at the shared node.
- **Missing query path:** Return zero without creating nodes.
- **Zero-count retained nodes:** Queries remain correct because their stored counts are zero; physical pruning is optional.
