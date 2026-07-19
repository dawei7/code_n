## General
Let $n$ be the number of tree nodes and $w$ its maximum level width.

**Traverse one complete level at a time.** Breadth-first search stores the current frontier in a queue. At the start of a level, record its size. Remove exactly that many nodes before beginning the next level, appending each removed node's non-null children to the queue's tail.

**Return only a neighbor from the same frontier.** When the removed node is the target object, inspect its position within the recorded level size. If another current-level node remains, it is at the queue's front and is the nearest node to the right. If the target was the last of those recorded nodes, return `null` even though the queue may already contain children for the next level.

Breadth-first traversal visits nodes in increasing depth and left-to-right order within each depth. The fixed `level_size` boundary separates same-level nodes from children appended during processing. Therefore the first queue element after a non-final target is exactly its immediate right neighbor, while a final target has none. Identity comparison ensures a different node with the same value cannot trigger the answer.

**Adapting identity for local fixtures.** The app follows `target_path` from the already constructed root to recover the exact target object, then applies the same breadth-first logic as the native solution. This makes duplicate-value cases unambiguous without changing the platform artifact.

## Complexity detail
Each node enters and leaves the queue at most once, so time is $O(n)$. The queue holds at most one level plus children being assembled for the next, bounded by $O(w)$ nodes. Following the target path uses time proportional to the tree height and $O(1)$ extra space.

## Alternatives and edge cases
- **Store complete level lists:** Building each BFS level and searching it for `u` is also $O(n)$ but allocates an additional list for the frontier.
- **Repeated root-to-node searches:** Determine the target depth, then independently search from the root for the depth of every candidate. This is correct but can take $O(n^2)$ time.
- **Compare node values:** This is incorrect when distinct nodes store equal values; the platform provides the target object itself.
- The root is the only node on level zero, so its answer is always `null`.
- A node may have a nearest right neighbor under a different parent.
- Children already queued for the next level must never be returned for a rightmost target.
