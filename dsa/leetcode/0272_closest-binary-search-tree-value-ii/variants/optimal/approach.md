## General

**Turn the BST into a sorted stream**

An inorder traversal visits a binary search tree in ascending value order: first the left subtree, then the node, then the right subtree. The exact protected solution exploits this order and keeps only a deque `q` containing at most `k` consecutive visited values.

The manifest describes a different optimal technique based on merging predecessor and successor iterators. The source actually uses recursive inorder traversal plus a sliding window. The two methods should not be conflated: this explanation follows the exact deque-based implementation and documents its true bounds.

Why does sorted order help? In a sorted sequence, the $k$ values closest to a fixed target form one contiguous block. Suppose two chosen values surround an unchosen value. The middle value lies numerically between them, so it cannot be farther from the target than both endpoints. Replacing a farther chosen endpoint with that middle value would produce an equally good or better selection. Under the guarantee that the closest set is unique, the answer is therefore one definite length-$k$ window in sorted order.

**Fill the initial window**

During inorder traversal, the first `k` encountered values are appended to `q`. Before `q` reaches size `k`, no choice is necessary because the final answer must contain `k` values and fewer than `k` candidates have been seen.

The deque remains sorted because values arrive in ascending order and are appended on the right. Its left endpoint `q[0]` is the smallest value currently retained, and the next inorder value `root.val` is greater than every value already in the deque.

**Decide whether a new value should slide the window**

Once `q` already has `k` elements, a newly visited value creates `k+1` candidates across the current window and its immediate right neighbor. A length-$k$ contiguous window cannot keep both extremes. The decision is therefore between:

- keeping the old left endpoint `q[0]` and rejecting the new right value; or
- removing `q[0]` and appending the new value, shifting the window one position right.

The source compares their absolute distances from `target`. If the new value is strictly closer, it removes the left endpoint with `popleft()` and appends the new value. The deque again has exactly `k` sorted, consecutive values.

If the new value is at least as far as `q[0]`, the source returns from that DFS call without changing the deque. The `>=` comparison retains the smaller, earlier value in a tie. The problem guarantees a unique set of `k` closest values, so a boundary tie that could create two different valid sets does not occur on legal inputs; either tie choice would otherwise require an explicit problem rule.

**Why the left endpoint is the only retained value that can be displaced**

The deque represents a contiguous window in the sorted values already processed. The new value lies immediately to its right in traversal order. Any length-$k$ contiguous block selected from these `k+1` consecutive candidates must drop either the first or the last candidate. Dropping an interior value while retaining both endpoints would leave a gap and could not be the unique closest block.

Comparing the two endpoints consequently decides which of the two possible windows is better. If the new right endpoint is closer than the old left endpoint, shift right. Otherwise, keep the current window.

There is also an intuitive distance view. Values below the target become closer as they increase toward it; values above the target become farther as they continue increasing. Sliding the window discards older far-left values while the newly seen right values improve the selection. Once the new right value fails to beat the left endpoint, the best window has been reached.

**Why the first failed comparison permits early stopping**

Suppose `q` is full and the current inorder value `x` satisfies

$$
\lvert x-\texttt{target}\rvert
\ge
\lvert \texttt{q[0]}-\texttt{target}\rvert.
$$

This failure cannot occur while both `q[0]` and `x` are at or below the target, because `q[0] < x \le \texttt{target}` would make `x` strictly closer. Therefore, by the time shifting stops, `x` is on the target's right side. Every later inorder value $y$ satisfies $y>x>\texttt{target}$ and is even farther from the target than `x`. If `x` cannot enter the window, no later value can enter it either.

The helper can thus skip `x` and its right subtree. The implementation returns only from the current recursive call rather than propagating a dedicated global stop flag. That still preserves correctness. When control returns to an ancestor whose left subtree contained the stopping point, that ancestor's value is even larger than `x`. The ancestor reaches the same distance comparison, returns without changing `q`, and skips its own right subtree. This repeats up the call stack. The source may perform a few additional ancestor comparisons, but it never admits a later, worse value.

**A precise window invariant**

After processing any prefix of the inorder sequence before stopping, `q` contains the best length-`min(k, prefix length)` contiguous window for that prefix. Initially this is true because every seen value is retained. When `q` is full and a new value arrives, there are exactly two relevant adjacent windows: the old window and the one shifted right by one. Comparing their differing endpoints chooses the better one while their other `k-1` values are identical.

If the old window wins, distance monotonicity to the right proves it will also beat every future shifted window, so traversal can stop. If the shifted window wins, deque operations establish the invariant for the enlarged prefix. When traversal finishes or safely stops, the invariant yields the globally closest window, which is the required set.

**Trace the main example**

For the BST `[4,2,5,1,3]`, inorder values are `[1,2,3,4,5]`. With `target = 3.714286` and `k = 2`:

| Current value | Deque before decision | Comparison | Deque afterward |
|---:|---|---|---|
| 1 | `[]` | Fewer than 2 values | `[1]` |
| 2 | `[1]` | Fewer than 2 values | `[1,2]` |
| 3 | `[1,2]` | 3 is closer than 1 | `[2,3]` |
| 4 | `[2,3]` | 4 is closer than 2 | `[3,4]` |
| 5 | `[3,4]` | 5 is not closer than 3 | stop with `[3,4]` |

Returning `[3,4]` is valid because answer order is unrestricted. For the one-node example with `k=1`, the traversal appends `1`, reaches the end, and returns `[1]`.

**Why the deque never returns too few values**

The constraints guarantee `k <= n`. Early stopping is possible only in the branch executed when `len(q) >= k`, so it cannot occur before `q` is full. If stopping never occurs, inorder traversal eventually visits all $n$ nodes and must fill the deque. The final conversion `list(q)` therefore always contains exactly `k` values for legal input.

## Complexity detail

Let $n$ be the number of tree nodes and $h$ its height. Every node is visited at most once, and deque operations are $O(1)$. Early stopping may avoid a suffix of the inorder traversal, but in the worst case it does not. For example, if the target is larger than every node, each new value is closer than the old left endpoint, so traversal reaches all $n$ nodes. The exact source therefore has $O(n)$ worst-case time.

The recursive inorder traversal uses up to $O(h)$ call-stack frames. The deque holds at most $k$ integers. Exact auxiliary space is consequently $O(h+k)$, excluding the returned list. Converting the deque to a list takes $O(k)$ time and creates $O(k)$ output storage.

These bounds differ materially from the manifest's $O(h+k)$ time and $O(h)$ space, which belong to the predecessor/successor iterator algorithm summarized there. Two lazy BST iterators can descend to the target in $O(h)$ setup and produce only $k$ selected values, whereas this protected solution may scan a long inorder prefix. Its deque also explicitly stores $k$ values.

For a balanced tree, $h=O(\log n)$, so exact auxiliary space is $O(\log n+k)$ but time remains $O(n)$ in the worst case. For a skewed tree, $h=O(n)$, making the recursive stack itself linear.

## Alternatives and edge cases

- **Predecessor and successor iterators:** Build two stacks around the target, then repeatedly take the closer next predecessor or successor. This achieves $O(h+k)$ time and $O(h)$ iterator space, satisfies the balanced-tree follow-up, and is the algorithm described by the manifest rather than the exact source.
- **Inorder array plus two pointers:** Materialize all $n$ sorted values, locate the target insertion point, and expand toward the closer side until `k` values are chosen. It is easy to understand but requires $O(n)$ array space and $O(n+k)$ time.
- **Size-`k` max heap:** Traverse every node and retain the closest `k` values by distance. It works for any binary tree in $O(n\log k)$ time and $O(k+h)$ space, but it does not exploit sorted inorder order.
- **Sort all values by distance:** Collecting and sorting costs $O(n\log n)$ time and $O(n)$ storage, more than needed.
- **`k = 1`:** The deque holds the best single value seen. It slides while later values become closer and stops as soon as they cease improving.
- **`k = n`:** No comparison branch runs because the deque is not full until the final node. Every tree value is returned, as required.
- **Target below the minimum:** The first `k` inorder values are the closest. Once the next value is examined, it is farther than the smallest retained endpoint, so traversal stops.
- **Target above the maximum:** Distances decrease throughout inorder traversal. The window keeps sliding and finishes with the largest `k` values after visiting all nodes.
- **Boundary-distance tie:** The source keeps the existing smaller endpoint because it uses `>=` to reject the new value. The unique-answer guarantee excludes a tie that would make two different closest sets equally valid.
- **Answer order:** The deque is returned in ascending BST order. This is acceptable because the contract permits any order.
- **Skewed tree:** Recursion depth can reach $n$ and may exceed Python's interpreter recursion limit at the largest constraint. An iterative inorder traversal preserves the window logic while replacing call-stack risk with an explicit $O(h)$ stack.
- **Nonempty-tree guarantee:** The algorithm assumes `root` contains at least one node and `k >= 1`. An empty tree would return too few values and is outside the contract.
- **No global stop flag:** A local early return is sufficient because every ancestor and later inorder value lies still farther to the right and will also be rejected. Adding a propagated Boolean could avoid the small number of ancestor comparisons but would not change the worst-case bound.
