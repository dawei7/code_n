## General

Every node defines exactly one subtree: the node itself together with all descendants below it. Its subtree sum is

`node.val + left_subtree_sum + right_subtree_sum`.

This dependency naturally requires postorder traversal. Both child sums must be known before the current node's sum can be computed.

`dfs(root)` returns the sum of the subtree rooted at `root`. For `None`, it returns zero because an empty child contributes no value to its parent's sum. This zero is an arithmetic identity, not a subtree sum to count; the frequency map is updated only for real nodes.

**Compute every subtree once.** For a real node, the recursive calls

`l, r = dfs(root.left), dfs(root.right)`

fully process the left and right subtrees and return their totals. The current total is then `s = l + r + root.val`. `cnt[s] += 1` records that one more node has this exact subtree sum, and `s` is returned to the parent for reuse.

The reuse is what makes the traversal linear. A slower approach could start a fresh sum traversal at every node, repeatedly visiting descendants. Postorder calculates each child's sum once and immediately feeds it into the parent's calculation.

For tree `[5, 2, -3]`, the leaf two returns sum two and increments frequency of two. Leaf negative three does the same for negative three. The root then combines `2 + (-3) + 5 = 4` and records four. All three sums have frequency one, so all are modes.

For `[5, 2, -5]`, leaf two records two, leaf negative five records negative five, and the root sum is also two. Frequency of two becomes two, making it the unique result.

Negative node values and negative subtree sums require no special handling. `Counter` accepts any integer key, and addition follows the definition directly. Different subtrees can produce the same sum even if their shapes and values differ; those occurrences must increase the same frequency key.

**Find the maximum only after traversal.** Once `dfs(root)` finishes, `cnt` contains one entry update for every node. `mx = max(cnt.values())` identifies the highest occurrence count. The list comprehension returns every sum `k` whose count `v` equals `mx`.

The tree is guaranteed nonempty, so `cnt` has at least one entry and `max` is safe. If an empty tree were allowed, the method would need a separate result policy before taking the maximum.

The problem permits any output order. Python's `Counter` preserves insertion order in current implementations, but correctness does not depend on it. The comprehension may return tied sums in the order their subtrees completed during postorder.

**Why the frequency map is complete and exact.** By induction, `dfs` returns the correct subtree sum. The base case correctly returns zero for an absent child. Assuming the two recursive child results are correct, adding them to the current value gives the sum of every node in the current subtree exactly once. The function increments that sum once for the current root. Because DFS is invoked once for each real node, every rooted subtree contributes one and only one frequency update.

Afterward, selecting precisely keys with the maximum count is exactly the definition of returning all most frequent subtree sums. Combining these two facts proves the result.

The answer values are sums, not node values and not nodes. A leaf's subtree sum happens to equal its value, while an internal node's sum usually combines many values.

## Complexity detail

Let $n$ be the number of nodes and $h$ the tree height. DFS visits each node once and performs constant dictionary work on average, taking $O(n)$ time. Finding the maximum and filtering up to $n$ distinct sums takes another $O(n)$, so total time remains $O(n)$.

The counter can store one distinct sum per node, using $O(n)$ space. Recursion uses $O(h)$ stack space, which is $O(n)$ for a skewed tree. The returned list can also contain $O(n)$ sums when all frequencies tie. Overall space is $O(n)$.

## Alternatives and edge cases

- **Recompute each subtree independently:** Traverse from every node to sum descendants. In a skewed tree this repeats work and reaches $O(n^2)$ time.
- **Iterative postorder:** Use an explicit stack with visited markers, then compute sums bottom-up. It avoids recursion depth but still needs $O(n)$ state.
- **Store node-to-sum map:** It is unnecessary here because each sum is immediately returned to the parent; only frequency by sum must persist.
- **Single node:** Its value is the only subtree sum and therefore the unique mode.
- **All sums distinct:** Every frequency is one, so all subtree sums are returned.
- **Several sums tied:** The comprehension includes every key with count `mx`; output order is unrestricted.
- **Negative and zero sums:** They are ordinary integer dictionary keys and require no sentinel.
- **Nonempty-tree guarantee:** It ensures `max(cnt.values())` is defined.
- **Deep skewed tree:** Recursive depth can reach the node count and may approach Python's recursion limit; iterative postorder is the runtime-safe alternative.
