## General

Bob has no choice of route: in a tree, there is exactly one path from `bob` to the root. Root the tree by recording each node's parent, then walk from `bob` through those parent links. Store Bob's arrival time for every node on that path and use an unreachable sentinel for every other node.

Now consider Alice's visit to a node at depth $d$. Her gate contribution is determined completely by comparing $d$ with Bob's recorded arrival time:

- if Alice arrives first, add the full `amount[node]`;
- if both arrive at time $d$, add half of `amount[node]`;
- if Bob arrived earlier, add nothing because the gate is already open.

Traverse the rooted tree from node $0$, carrying Alice's arrival time and accumulated income. Each traversal state represents the unique root-to-node path, so its income already contains exactly the gate contribution Alice would receive along that path. Whenever the state reaches a leaf, compare its income with the best leaf total seen so far.

This considers every permitted destination once. The arrival-time comparison applies the gate rule exactly at every node, and the maximum over all leaf states is therefore precisely Alice's optimal net income. Iterative traversals avoid recursion-depth failures on a chain of $10^5$ nodes.

## Complexity detail

Let $n$ be the number of nodes. Building the adjacency list, rooting the tree, marking Bob's path, and traversing Alice's choices each take $O(n)$ time, for $O(n)$ total time.

The adjacency list, parent and arrival-time arrays, traversal order, and explicit stack collectively use $O(n)$ space.

## Alternatives and edge cases

- **Two recursive depth-first searches:** One DFS can find Bob's path and another can score Alice's paths in $O(n)$ time, but a depth-$10^5$ tree exceeds Python's normal recursion limit.
- **Recompute every root-to-leaf path:** Searching from the root separately for each leaf is correct, but a tree with many leaves can make this $O(n^2)$.
- **Modify gate values on Bob's path:** After comparing Bob's time with each node's depth, the relevant `amount` values can be halved or zeroed before a maximum root-to-leaf sum; this is equivalent but mutates the input unless a copy is made.
- **Negative amounts:** Alice must reach some leaf, so initialize the answer below every possible path total instead of using zero.
- **Two-node tree:** Node $1$ is the only leaf; the root is not a leaf even though its undirected degree is one.
- **Simultaneous arrival:** Even negative gate prices are halved, which is exact because all amounts are even.
- **Independent stopping:** Bob's arrival times beyond node $0$ do not exist, while Alice continues normally toward her leaf.
