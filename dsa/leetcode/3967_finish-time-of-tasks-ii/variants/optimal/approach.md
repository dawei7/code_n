## General

**Represent one side of every edge.** For adjacent tasks $u$ and $v$, let $M(u\to v)$ be the finish time of task $u$ when the edge to parent $v$ is removed and the entire component on $u$'s side is oriented away from $u$. If the incoming component values from $u$'s other neighbors form a nonempty multiset $S$, the contract gives

$$
M(u\to v)=2\max(S)-\min(S)+\texttt{baseTime[u]}.
$$

When $S$ is empty, $u$ is a leaf in that orientation and the message is simply `baseTime[u]`. Once every message into a task is known, applying the same combination to all its neighbors gives that task's finish time as the root.

**Compute child-to-parent messages.** Temporarily root the tree at task `0` and record an iterative parent-before-child order. Process that order in reverse. Every child's downward message is then available when computing its parent's downward message, so this pass obtains $M(u\to p)$ for every non-root task. Iteration matters because a legal tree can be a 100,000-task chain.

**Reroot without recomputing a component.** Traverse the recorded order forward. At task $u$, each neighbor contributes one incoming value: a child's downward message, or the already propagated upward message from $u$'s temporary parent. Combining all incoming values evaluates $u$ as the actual root. To propagate toward a child $v$, exclude only $M(v\to u)$ and combine the remaining values; that result is $M(u\to v)$.

Excluding one neighbor must remain constant time. While scanning a task's incoming values, retain the two smallest and two largest occurrences. If the removed occurrence equals the minimum, the second minimum becomes `earliest`; otherwise the minimum remains. The maximum is handled symmetrically. Treating duplicate values as separate occurrences is essential: when two neighbors share the minimum or maximum, excluding one must leave the same extreme available.

The reverse pass is correct by induction from temporary leaves toward task `0`: every downward message uses exactly the already correct child-side components. The forward pass begins with all downward messages at `0`; whenever it reaches a task, its parent-side message was computed from every component on that side, so all incoming messages are correct. Excluding each neighbor therefore produces the exact directed message for that edge. Thus every task's root value is evaluated from its exact neighboring components, and taking their minimum returns the required optimum.

## Complexity detail

The adjacency lists contain $2(n-1)$ neighbor entries. Building the traversal, computing downward messages, and scanning every incoming list in the forward pass each take $O(n)$ total time. Constant-time exclusion makes propagation linear even at a high-degree task. The adjacency lists, traversal arrays, messages, and temporary incoming lists occupy $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Recompute a rooted dynamic program for every task:** This directly follows the definition but traverses the tree $n$ times and takes $O(n^2)$ time.
- **Sort every task's incoming values:** Sorting makes exclusion easy but can cost $O(n\log n)$ on a star; two minima and two maxima contain all information this recurrence needs.
- **Recursive rerooting DFS:** It can implement the same messages, but a 100,000-task chain exceeds Python's ordinary recursion depth.
- **One task:** There are no incoming components, so the only task is a leaf and its base time is the answer.
- **One remaining component:** After excluding a degree-one task's only neighbor, the task becomes a leaf; its outgoing message is its base time rather than an extrema formula over an empty set.
- **Duplicate extrema:** The two smallest and largest *occurrences* must retain equal values, or removing one tied neighbor would incorrectly discard the shared extreme.
- **Undirected edge order:** Input order and endpoint order do not identify a root; the temporary traversal supplies parent relationships only for the two-pass computation.
