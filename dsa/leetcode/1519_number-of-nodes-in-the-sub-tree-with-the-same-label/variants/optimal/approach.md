## General

**Rooting the undirected tree**

The input edges are undirected, but subtrees are defined after rooting at node zero. The source builds adjacency list `g` in both directions.

The recursive helper receives current node `i` and parent `fa`. When examining neighbors, it skips `fa` and recursively visits every other neighbor as a child. Because the graph is a tree, this parent check is enough to prevent walking backward or revisiting a node.

**A global counter used as a traversal prefix**

The unusual part is `cnt`. It is one global `Counter` of labels seen so far in depth-first traversal, and values are never decremented when recursion returns.

For node `i` with label `labels[i]`, the entry action is

`ans[i] -= cnt[labels[i]]`.

This stores the negative number of occurrences of that label seen before entering `i`'s subtree.

The code then increments the current node's label and completely traverses every child subtree. After all descendants finish, every node in `i`'s subtree has been visited, and no node that comes later outside that subtree has been visited yet.

The exit action

`ans[i] += cnt[labels[i]]`

adds the global count after the subtree. The difference between after and before is exactly the number of occurrences of `labels[i]` visited inside the subtree.

**Why DFS contiguity makes this work**

A recursive DFS enters a node and finishes every descendant before returning to the parent. Therefore, the visitation events for one subtree form one contiguous interval in traversal order.

For any label $c$,

$$
\text{count of c in subtree i}
=
\text{prefixCountAfter}(c)
-\text{prefixCountBefore}(c).
$$

The two updates to `ans[i]` compute exactly this prefix difference for the node's own label.

The counter must not be decremented on backtracking. It represents a monotone traversal prefix, not the labels on the active recursion path. Decrementing would destroy the after-minus-before interpretation.

**A small trace**

Suppose node `i` has label `a` and two earlier nodes outside its subtree have already contributed `a`. On entry, `ans[i]` becomes minus two. During the subtree traversal, the current node and two descendants with label `a` add three occurrences, so the global count becomes five. On exit, adding five produces three, exactly the subtree answer.

Nodes visited afterward in sibling branches cannot contaminate `ans[i]` because its exit update occurs before DFS leaves `i`.

**Why every answer is assigned correctly**

The current node increments its label before visiting children, so each node counts itself. All descendants are visited before the exit snapshot. Parent and other already completed subtrees are removed algebraically through the entry baseline.

Each node executes exactly one entry and exit pair, so every `ans[i]` is filled once. The Counter can use label characters directly; missing labels begin at zero.

**Comparison with merging frequency arrays**

A common DFS returns a 26-element frequency array from each child and merges it into the parent. The exact source avoids those per-node arrays by using global traversal-prefix differences. It needs only one counter containing at most 26 keys, although it still uses linear adjacency and recursion storage.

**Practical recursion depth**

A chain-shaped tree can create $N$ recursive calls. With $N$ up to one hundred thousand, standard Python recursion limits are insufficient, so the exact source can raise `RecursionError` on valid deep inputs unless the environment adjusts the limit. An iterative traversal with entry and exit events preserves the same prefix-difference idea safely.

## Complexity detail

Building adjacency lists takes $O(N)$ time and space because a tree has $N-1$ edges. DFS visits every node once and examines each undirected edge twice. Counter operations are expected constant time over a fixed 26-letter alphabet, so total time is $O(N)$.

The adjacency list uses $O(N)$ space, the answer uses $O(N)$, and the recursion stack can use $O(N)$ in a chain. The counter itself is $O(1)$ relative to $N$. Overall auxiliary space is $O(N)$, matching the manifest.

The approach does not allocate a 26-entry array per node, improving constants relative to frequency merging.

## Alternatives and edge cases

- **Return 26-count arrays:** Merge child frequencies in postorder. It is straightforward and still $O(N)$ because the alphabet is fixed, but uses larger per-frame data.
- **Iterative entry-exit DFS:** Record the baseline on entry and compute the difference on exit without recursion-limit risk.
- **Leaf node:** Its subtree contains itself only, so its answer is one.
- **All labels equal:** Each answer becomes the size of that rooted subtree.
- **All labels distinct:** Every node's answer is one.
- **Single-node tree:** Entry baseline is zero, the node increments its label, and exit produces one.
- **Parent skip:** It is necessary because adjacency lists contain both edge directions.
- **Global counter not decremented:** This is intentional prefix counting, not an active-path frequency.
- **Deep chain:** Mathematical correctness holds, but recursive Python execution may exceed the stack limit.
- **Required imports:** `defaultdict` and `Counter` must be available from `collections`.
