## General

**Every node defines one candidate subtree**

A subtree is fixed once its root is chosen: it contains that node and all descendants. Therefore, the problem has one candidate per tree node.

The average for a node’s subtree needs two quantities: the sum of all values below that node and the number of nodes below it. A postorder traversal computes both from the corresponding quantities returned by the left and right children.

**Define the recursive summary**

`dfs(root)` returns a pair `(subtree_sum, subtree_count)`.

For an absent child, both values are zero. This neutral pair can be added without special cases when processing a real parent.

For a real node, recursive calls first obtain `ls, ln` from the left and `rs, rn` from the right. The current subtree then has:

`s = root.val + ls + rs`

and:

`n = 1 + ln + rn`.

These formulas count the current node once and combine the two disjoint descendant subtrees.

**Evaluate the candidate before returning**

The current subtree’s average is `s / n`. `n` is at least one for every real node, so division is safe.

`ans = max(ans, s / n)` compares this candidate with the greatest average seen anywhere earlier in postorder. `ans` is declared `nonlocal` because it belongs to the enclosing method scope while the recursive helper updates it.

After evaluation, the helper returns `s, n` to the parent. The same summary both solves the current candidate and supplies exactly what the next level needs.

For the tree `[5,6,1]`, each leaf returns its own value and count one. Their averages update the answer to six and leave it there after the second leaf. The root then combines sum twelve and count three, producing average four. This trace shows why a small subtree can beat the average of the entire tree.

**Why postorder is necessary**

A parent’s sum and count are incomplete until both child subtrees have been summarized. Processing children first guarantees those results are available.

A preorder traversal could still work if it carried more state or revisited nodes, but direct bottom-up aggregation matches the mathematical definition and visits each node only once.

**Why initializing the answer to zero is safe**

All node values are nonnegative. Every subtree average is therefore at least zero, so `ans = 0` is a valid lower bound.

If negative values were permitted, initializing to zero could incorrectly beat every real average. One would then initialize to negative infinity or use the first candidate. The source constraint is what makes the current initialization correct.

**Complete correctness argument**

By induction, a null call returns the correct zero summary. Assuming child calls return their exact sums and counts, the addition formulas return the exact sum and count for the current subtree.

Thus `s / n` is evaluated once for every real node and equals that node’s true subtree average. `ans` retains the maximum of all candidates processed so far. When the root call finishes, every node has been processed, so `ans` is the maximum subtree average in the whole tree.

The division is performed only for comparison with the running answer; parents receive exact integer sums and counts rather than rounded averages. This avoids compounding floating-point error across levels. The accepted tolerance covers the one final division performed for each candidate.

## Complexity detail

Let $N$ be the number of nodes. DFS visits every node once and performs constant arithmetic at each visit, so time is $O(N)$.

The recursion stack depth equals tree height $h$. It is $O(\log N)$ for a balanced tree and $O(N)$ for a completely skewed tree. The manifest states the safe worst-case space bound $O(N)$.

No collection of all subtree summaries is stored; each pair exists only while its ancestor call needs it. Apart from recursion, working space is constant.

## Alternatives and edge cases

- **Store every subtree’s node list:** This repeats descendants across many candidates and can lead to quadratic work.
- **Two separate traversals per node:** Recomputing sum and count for every possible root also costs up to $O(N^2)$.
- **Iterative postorder:** A stack and visited marker can avoid recursion-depth limits while keeping $O(N)$ time.
- **Return average only:** Insufficient because a parent cannot combine child averages without their counts and sums.
- **Single node:** Its sum is its value, count is one, and its own value is returned.
- **Leaf node:** Both null children return zeros, so the leaf average is exactly its value.
- **All zero values:** Every average is zero and the initial answer remains correct.
- **One deep branch:** Recursion space reaches $O(N)$, though time remains linear.
- **Very large subtree sum:** Python integers grow as needed before floating division.
- **Equal maximum averages:** The numeric result is the same regardless of which subtree attains it.
- **Nonempty root:** The contract guarantees at least one node, so some candidate is always evaluated.
- **Input preservation:** The traversal reads values and pointers without modifying the tree.
