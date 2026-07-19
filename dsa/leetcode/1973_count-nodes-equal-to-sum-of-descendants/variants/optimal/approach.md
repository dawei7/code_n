## General
**Process children before their parent**

Use an explicit stack of `(node, visited)` pairs to perform postorder
traversal. The first time a node is popped, push it back as visited and then
push its children. When the visited entry is later popped, both child subtree
sums are already available.

For a node, add the complete subtree sums of its left and right children. This
quantity is exactly the sum of all strict descendants, because those two
subtrees are disjoint and contain every node below the current one. Compare it
with the current value, increment the answer on equality, and store the
current subtree's total as `node.val + descendant_sum`.

**Why every node is counted correctly**

An absent child contributes zero. By postorder induction, every stored child
total equals the sum of all values in that child's subtree. Their sum is
therefore precisely the current node's descendant sum, neither omitting a
descendant nor including the current node. The comparison is consequently
correct for that node. Since the traversal reaches each tree node once, the
final counter includes exactly all qualifying nodes.

## Complexity detail
Each of the $N$ nodes is pushed a constant number of times and processed once,
so the running time is $O(N)$. The explicit stack and subtree-sum map may each
hold $O(N)$ entries. This iterative form also avoids depending on a recursion
limit for a tree whose height can reach $N$.

## Alternatives and edge cases
- **Recursive postorder:** Return each subtree sum while updating a shared
  counter. This is concise and also $O(N)$ time, but a chain of up to $10^5$
  nodes can overflow the call stack.
- **Recompute each subtree:** For every node, launch a separate traversal to
  sum its descendants. A skewed tree makes this take $O(N^2)$ time.
- A leaf qualifies only when its value is zero because its descendant sum is
  zero.
- Zero-valued internal nodes qualify when every descendant value is also zero.
- Repeated values are independent; qualification depends on subtree position,
  not value uniqueness.
- The comparison uses the sum of all descendant levels, not merely the
  immediate children.
