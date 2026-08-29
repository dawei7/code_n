## General

**Enumerate every root-to-leaf path, but compare it in reverse**

Every candidate answer corresponds to one leaf. Its characters are read from that leaf upward through its ancestors to the root. A depth-first traversal naturally travels in the opposite direction—from the root down to a leaf—so the algorithm records the current root-to-node path and reverses it only when it reaches a leaf.

It must examine every leaf. Choosing the smaller child value greedily is not sufficient because lexicographic order starts at the leaf, not at the current parent, and a deeper continuation can change which complete leaf-to-root string is smaller.

**Convert node values to letters**

A node value is between zero and twenty-five. The expression

`chr(ord('a') + root.val)`

maps zero to `'a'`, one to `'b'`, and so on through twenty-five to `'z'`. The current node's letter is appended to `path` as soon as DFS enters the node.

At that point, `path` contains letters in root-to-current-node order. For example, if the path from root to leaf contains values zero, one, and three, then `path` is `['a', 'b', 'd']`. The required leaf-to-root candidate is `"dba"`, obtained by `''.join(reversed(path))`.

**Recognize only genuine leaves as candidates**

A leaf has no left child and no right child. The condition

`root.left is None and root.right is None`

tests both sides. A node with only one missing child is not a leaf, so it must not create an incomplete candidate.

Null references are handled by the outer `if root` guard. The helper is called for both children even when one is null; a null call simply does nothing and returns.

**Keep the smallest complete candidate**

Variable `ans` holds the smallest leaf-to-root string seen so far. It starts as

`chr(ord('z') + 1)`,

which is the character `'{'` in the relevant character ordering. Every valid candidate begins with a lowercase letter from `'a'` through `'z'`, all of which compare smaller than `'{'`. Therefore, the first leaf candidate always replaces the sentinel without requiring a separate “no answer yet” Boolean.

At each leaf, the assignment

`ans = min(ans, ''.join(reversed(path)))`

uses Python's lexicographic string comparison. Characters are compared from left to right; at the first difference, the smaller letter wins. If all characters of the shorter string match the start of the longer string, the shorter string wins. This is exactly the ordering specified by the problem.

**Backtrack with one reusable path list**

After recording and possibly evaluating the current node, DFS explores the left subtree and then the right subtree. Finally, `path.pop()` removes the current node's letter.

The removal is essential. When a call returns to its parent, the list must again represent the path ending at that parent. The sibling traversal can then append its own letters without inheriting characters from the completed branch.

Only one list object is shared through the recursion. Each call follows the disciplined sequence append, explore, pop. This avoids copying an entire path for every child and avoids creating a new immutable string at every internal node.

**The path invariant**

Immediately after a non-null call appends its character, `path` contains exactly one letter for every node on the unique route from the original root to the current node, in that order.

The invariant holds for the root because the initially empty list receives only the root letter. If it holds at a parent, a child call appends exactly the child's letter, extending the route correctly. After that child finishes, its final pop restores the parent's route before any sibling is explored.

Consequently, reversing `path` at a leaf produces exactly that leaf's required string, with no missing, duplicated, or sibling characters.

**Trace the first example**

For the tree represented by `[0, 1, 2, 3, 4, 3, 4]`, the root letter is `a`.

- Reaching the left-left leaf with value three produces root-to-leaf path `['a', 'b', 'd']` and candidate `"dba"`.
- The left-right leaf with value four produces `"eba"`.
- The right-left leaf with value three produces `"dca"`.
- The right-right leaf with value four produces `"eca"`.

Comparing from the first character eliminates both strings beginning with `e`. Between `"dba"` and `"dca"`, the first letters tie and `b < c` at the next position, so `"dba"` is the answer.

This example also shows why comparing root-to-leaf strings would be wrong: all candidates share the root `a` first in that orientation, while the required comparison begins at each leaf.

**Why the final answer is globally smallest**

Every leaf is reached exactly once by DFS because a tree gives each node one unique route from the root. By the path invariant, the candidate constructed at that visit is exactly its leaf-to-root string. Thus the algorithm considers every legal candidate once.

After processing any number of leaves, `ans` is the minimum of the sentinel and all candidates seen so far. The next leaf replaces it only when the new candidate is smaller, preserving that statement. Once traversal ends, every leaf has been seen, so `ans` is the minimum over the complete candidate set.

**Why internal prefixes cannot safely prune the search**

The letters currently in `path` are stored root first, but final strings are compared leaf first. An apparently large letter near the root may appear late in a candidate and be outweighed by a small leaf letter. Likewise, two descendants can create candidates of different lengths where the shorter-prefix rule matters. The implementation therefore performs no speculative pruning and obtains correctness by exhaustive leaf coverage.

## Complexity detail

Let `N` be the number of nodes and `H` the tree height measured in nodes.

DFS visits each node once, so append, pop, and child-call overhead total `O(N)`. At a leaf of depth `d`, reversing and joining the path takes `O(d)` time, and comparing the candidate with `ans` can also inspect `O(d)` characters. Summed over all leaves, this is at most `O(NH)`, which is the variant's time bound. It is often smaller; for a balanced tree, depths are logarithmic.

The shared path contains at most `H` characters, the recursion stack has at most `H` active calls, and `ans` plus the temporary leaf candidate have length at most `H`. Auxiliary space is `O(H)`. The returned string is also at most `H` characters.

## Alternatives and edge cases

- **Copy a string into every recursive call:** Prepending the current letter makes each state self-contained, but immutable-string creation copies path content repeatedly and can increase both time and temporary memory.
- **Breadth-first search:** Store a candidate string with every queued node. It visits all leaves correctly but may retain many path strings simultaneously.
- **Greedy child selection:** Following the locally smaller node value can miss a smaller leaf-to-root string because the deciding character is often deeper in the tree.
- **Store integer paths and compare manually:** A custom reverse comparison can avoid some string creation, but it adds intricate prefix and tie handling for little benefit at these constraints.
- **Single-node tree:** The root is also a leaf. Its one letter replaces the sentinel and is returned.
- **One-child nodes:** Such nodes are not leaves; DFS continues through the existing child, while the null child call returns immediately.
- **Equal candidate strings:** `min` keeps an equal value, and either identical leaf path is acceptable because the returned string is the same.
- **Prefix relationship:** Python string comparison already treats a shorter matching prefix as smaller, exactly as required.
- **Deep skewed tree:** There is only one leaf candidate, but recursion and the shared path grow to `O(N)`. Python recursion depth may be an implementation concern for a very deep legal tree.
- **Sentinel safety:** `'{'` is greater than every permitted lowercase starting character. It is never returned for a valid nonempty tree because at least one leaf exists.
- **Input preservation:** The tree is read-only; only the separate path list and answer string are modified.
