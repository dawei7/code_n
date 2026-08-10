## General

**A palindrome is governed by frequency parity.** A multiset of digits can be rearranged into a palindrome when at most one digit has an odd occurrence count. Every mirrored pair consumes two equal digits. For an even-length palindrome all counts must be even; for an odd-length palindrome exactly one central digit may have an odd count.

The path's exact counts are more information than needed. The algorithm stores only whether each digit's count is odd or even in an integer bit mask. Bit position `d` represents digit `d`. A zero bit means the count seen on the current root-to-node path is even, and a one bit means it is odd.

**Toggle one bit for each visited node.** `1 << root.val` creates an integer with only the current digit's bit set. XORing `mask` with that value flips the bit: zero becomes one on the first, third, and other odd occurrences, while one becomes zero on the second, fourth, and other even occurrences.

The update `mask ^= 1 << root.val` therefore maintains all nine parities using one small integer. Bit zero is unused because node values range from one through nine, but leaving it zero causes no problem.

**Carry the path mask through recursive DFS.** `dfs(root, mask)` receives the parity state for the strict ancestors of the current node. A `None` child represents no path and returns zero. At a real node, the helper toggles its digit, making the mask describe the path including that node.

Python integers are immutable, and `mask` is a local parameter. Passing it to the left and right calls gives each branch the correct common prefix state. Changes deeper in the left branch do not leak into the right branch.

**Count only root-to-leaf paths.** A path qualifies for this problem only when it ends at a leaf. The condition `root.left is None and root.right is None` identifies exactly those nodes. Internal prefixes are not evaluated even if their parity mask could form a palindrome, because they are not complete root-to-leaf paths.

At a leaf, the expression `mask & (mask - 1)` removes the lowest set bit. If `mask` has no set bits, it is zero and the result is zero. If it has exactly one set bit, subtracting one turns that bit off and lower bits on, and the AND again becomes zero. If it has two or more set bits, removing only the lowest leaves another set bit, so the result is nonzero.

Thus `(mask & (mask - 1)) == 0` is true exactly when zero or one digit has odd frequency. Converting the Boolean with `int` returns one for a pseudo-palindromic leaf path and zero for an invalid one.

**Add independent subtree answers.** At an internal node, every root-to-leaf path continues into exactly one child. The paths through the left and right subtrees are disjoint sets, so their valid counts can be added. `dfs(root.left, mask) + dfs(root.right, mask)` returns the complete count below the current node.

**Trace a path.** For digits `2, 3, 3`, the initial zero mask toggles bit two, then bit three on, then bit three off. Only bit two remains set. The path can be rearranged as `3, 2, 3`, and the bit test returns one.

For digits `2, 3, 1`, bits one, two, and three are all set at the leaf. More than one count is odd, `mask & (mask - 1)` remains nonzero, and the path contributes zero.

**The invariant and proof.** On entry to a real node, each bit of `mask` is the parity of that digit among the strict ancestors. XOR toggling makes it the parity along the path through the current node. This is true at the root because the initial mask zero represents an empty path, and it remains true by induction for every child.

At each leaf, the bit trick implements the exact necessary and sufficient palindrome-permutation condition, so the returned zero or one is correct. At each internal node, summing correct child counts covers every descendant leaf once. Induction upward proves that the initial `dfs(root, 0)` returns the number of pseudo-palindromic root-to-leaf paths.

The approach never stores the actual path and never reconstructs a palindrome. Both would be unnecessary because parity alone decides existence of some palindromic permutation.

## Complexity detail

Let `n` be the number of nodes and `h` the tree height. Each real node is visited once and performs constant-time bit operations and pointer checks. Calls on missing children also total `O(n)`, so time is `O(n)`.

The recursive stack contains at most one call for each node on the active root-to-leaf path, using `O(h)` space. The mask itself occupies a constant number of bits because only digits one through nine exist. This matches the manifest's `O(h)` bound.

A balanced tree has logarithmic height, while a skewed tree can have `h = n`. With as many as `100000` nodes, the latter can exceed Python's default recursion depth; an explicit stack preserves the algorithm with robust `O(h)` storage.

No per-path list or frequency array is allocated. Each recursive frame holds only a node reference, a mask, and return bookkeeping.

## Alternatives and edge cases

- **Iterative DFS with node-mask pairs:** Use an explicit stack to avoid recursion-depth limits while retaining `O(n)` time and `O(h)` traversal storage.
- **Nine-element parity array:** Increment counts or toggle Booleans while traversing and backtrack changes. It is correct but mutation and branch restoration are more error-prone than passing an integer.
- **Store complete root-to-leaf paths:** Count frequencies at each leaf. This repeats work and can use much more memory than the parity summary.
- **Morris traversal:** Threading the tree can reduce traversal stack usage, but restoring path parity and tree links is considerably more complex.
- **Single-node tree:** Its mask has exactly one set bit, so its only path is pseudo-palindromic.
- **All counts even:** The mask is zero and passes the test.
- **Exactly one odd count:** The mask is a power of two and passes.
- **Two odd counts:** At least two bits remain set, so the path fails.
- **Repeated digit:** Every second occurrence toggles its bit back off, exactly capturing even parity.
- **Missing child:** It returns zero and is not treated as a completed path. Only a real node with both children missing is a leaf.
- **One-sided tree:** DFS follows the existing child and adds zero from missing sides; correctness is unchanged.
- **Branches with shared prefix:** They receive the same mask value, then evolve independently because integers are immutable.
- **Digit range one through nine:** The mask has fixed constant width. Larger arbitrary values would require a wider integer or a mapping.
- **Deep skewed tree:** Use an iterative stack in Python if recursion depth may exceed the runtime limit.
- **Permutation not construction:** Passing the parity test proves that a palindrome arrangement exists; the algorithm need not build that arrangement.
