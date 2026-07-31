## General

**Compute every candidate value first.** Root the tree at node `0` and record a parent array and traversal order. Processing that order backward accumulates each node's value into its parent, producing the sum of every rooted subtree without recursion.

**Let traversal order enforce non-overlap.** A subtree can overlap another only when one root is an ancestor of the other. During a second depth-first traversal, query a node's subtree sum when entering the node, but add that sum to the data structure only when exiting it. At entry, no ancestor is present because ancestors have not exited. Descendants are also absent because they have not yet been visited. Every stored sum therefore belongs to a branch that finished earlier and is disjoint from the current subtree.

When a node exits, its descendants may already be stored. Adding the node alongside them is safe: none of those overlapping sums are queried against each other. A later query can see them only from outside the entire completed branch, where all of them are disjoint from the new subtree.

**Maximize XOR with a binary trie.** Store each completed subtree sum bit by bit from the most significant relevant bit downward. For a queried sum, greedily follow the opposite bit whenever possible, because setting a higher XOR bit dominates every choice among lower bits. If the opposite branch is absent, follow the matching bit. This finds the maximum XOR with any eligible completed sum.

Thus every considered pair is non-overlapping. Conversely, for any two non-overlapping subtrees, whichever branch is traversed first is stored before the other root is entered, so their score is considered. Taking the best trie query therefore yields the global maximum.

## Complexity detail

Let $S$ be the total of all node values. Rooting the tree and computing sums take $O(n)$ time. Each subtree sum is inserted once and queried at most once across $O(\log S)$ bits, giving $O(n \log S)$ time. The graph, traversal arrays, event stack, and binary trie use $O(n \log S)$ auxiliary space in the worst case.

## Alternatives and edge cases

- **Compare every pair of subtree sums:** Euler entry/exit intervals can test non-overlap in constant time, but checking all node pairs costs $O(n^2)$ time.
- **Recursive depth-first search:** It can express both passes compactly, but a legal chain of $5 \cdot 10^4$ nodes can exceed Python's recursion limit.
- **Incorrect global trie:** Inserting every sum before querying allows ancestor-descendant pairs, which overlap and must not contribute to the answer.
- **Rooted chain:** Every subtree contains the next one, so no two are disjoint and the result is zero.
- **Large sums:** The total can exceed 32 bits; derive the trie width from the largest subtree sum instead of assuming a fixed signed-integer width.
- **Arbitrary edge order:** The first traversal determines parent-child direction from root `0`; input edge orientation is irrelevant.
