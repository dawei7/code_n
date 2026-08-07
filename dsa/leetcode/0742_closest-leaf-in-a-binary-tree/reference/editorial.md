[TOC]

### Approach #1: Convert to Graph [Accepted]

**Intuition**

Instead of a binary tree, if we converted the tree to a general graph, we could find the shortest path to a leaf using breadth-first search.

**Algorithm**

We use a depth-first search to record in our graph each edge traveled from parent to node.

After, we use a breadth-first search on nodes that started with a value of `k`, so that we are visiting nodes in order of their distance to `k`. When the node is a leaf (it has one outgoing edge, where the `root` has a "ghost" edge to `null`), it must be the answer.

```python
class Solution(object):
    def findClosestLeaf(self, root, k):
        graph = collections.defaultdict(list)
        def dfs(node, par = None):
            if node:
                graph[node].append(par)
                graph[par].append(node)
                dfs(node.left, node)
                dfs(node.right, node)

        dfs(root)
        queue = collections.deque(node for node in graph
                                  if node and node.val == k)
        seen = set(queue)

        while queue:
            node = queue.popleft()
            if node:
                if len(graph[node]) <= 1:
                    return node.val
                for nei in graph[node]:
                    if nei not in seen:
                        seen.add(nei)
                        queue.append(nei)
```

**Complexity Analysis**

* Time Complexity: $O(N)$ where $N$ is the number of nodes in the given input tree. We visit every node a constant number of times.

* Space Complexity: $O(N)$, the size of the graph.

---
### Approach #2: Annotate Closest Leaf [Accepted]

**Intuition and Algorithm**

Say from each node, we already knew where the closest leaf in its subtree is. Using any kind of traversal plus memoization, we can remember this information.

Then the closest leaf to the target (in general, not just subtree) has to have the lowest common ancestor with the `target` that is on the path from the `root` to the `target`. We can find the path from `root` to `target` via any kind of traversal, and look at our annotation for each node on this path to determine all leaf candidates, choosing the best one.

```python
class Solution(object):
    def findClosestLeaf(self, root, k):
        annotation = {}
        def closest_leaf(root):
            if root not in annotation:
                if not root:
                    ans = float('inf'), None
                elif not root.left and not root.right:
                    ans = 0, root
                else:
                    d1, leaf1 = closest_leaf(root.left)
                    d2, leaf2 = closest_leaf(root.right)
                    ans = min(d1, d2) + 1, leaf1 if d1 < d2 else leaf2
                annotation[root] = ans
            return annotation[root]

        #Search for node.val == k
        path = []
        def dfs(node):
            if not node:
                return
            if node.val == k:
                path.append(node)
                return True
            path.append(node)
            ans1 = dfs(node.left)
            if ans1:
                return True
            ans2 = dfs(node.right)
            if ans2:
                return True
            path.pop()

        dfs(root)
        dist, leaf = float('inf'), None
        for i, node in enumerate(path):
            d0, leaf0 = closest_leaf(node)
            d0 += len(path) - 1 - i
            if d0 < dist:
                dist = d0
                leaf = leaf0

        return leaf.val
```

**Complexity Analysis**

* Time and Space Complexity: $O(N)$. The analysis is the same as in *Approach #1*.