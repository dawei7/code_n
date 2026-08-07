[TOC]

## Solution

---

### Overview

We are given the `root` of a binary tree and an integer `k`, where we want to find the `k-th` largest level sum of the tree. A level sum of a tree for a given level can be defined as the sum of the values of all nodes that all have equal distance from the `root`. 

### Approach 1: Level Order Traversal + Max Heap 

### Intuition

To calculate the sum of each level in a tree, we can use level order traversal, which processes nodes level by level. This is similar to breadth-first search (BFS), where we visit all neighbors of a node before moving on. However, unlike traditional BFS, all nodes at a given level are processed together in level-order traversal. So, for each level `i`, we visit all nodes and maintain a `sum` variable to track the sum of nodes for that level.  

Since we need to find the `k-th` largest sum, we can store each level's sum in a max heap. By removing the first `k-1` elements from the heap, the `k-th` largest element remains at the top and can be accessed directly.  

### Algorithm

1. Initialize a max heap/priority queue `pq` 
2. Initialize a queue `bfsQueue` to maintain the ordering of which nodes to visit for our level order traversal
3. Start by adding `root` to `bfsQueue`
4. Perform level order traversal. While `bfsQueue` is not empty:
    * Initialize `size` to be the current number of nodes of `bfsQueue`, which are all the nodes for the current level that we want to visit
    * For `size` iterations:
        * Initialize `sum` to `0`
        * Visit the next node by removing the next node in `bfsQueue`. Store it in `poppedNode`
        * Update `sum`: `sum += poppedNode.val`
        * Add the left and right children of `poppedNode` to the queue, if they exist. These children will be a part of the next level of the tree that will be visited in the next iteration. 
    * `sum` now contains a level order sum. Add it to `pq`
5. If `pq` has less than `k` sums, then return -1 because we have less than `k` levels in our tree
6. Otherwise, remove the first `k-1` elements from `pq`, and then return the top element: `pq.peek()`

### Implementation


```python
class Solution:
    def kthLargestLevelSum(self, root: TreeNode, k: int) -> int:
        # max heap
        pq = []
        bfs_queue = deque()
        bfs_queue.append(root)

        while bfs_queue:
            # level order traversal
            size = len(bfs_queue)
            level_sum = 0
            for _ in range(size):
                node = bfs_queue.popleft()
                level_sum += node.val
                if node.left:
                    # add left child
                    bfs_queue.append(node.left)
                if node.right:
                    # add right child
                    bfs_queue.append(node.right)

            # Make sum negative to maintain a max heap
            heapq.heappush(pq, -level_sum)

        if len(pq) < k:
            return -1

        for _ in range(k - 1):
            heapq.heappop(pq)

        # Convert sum back to positive
        return -heapq.heappop(pq)
```


### Complexity Analysis 

Let $N$ be the total number of nodes in our tree.

* Time Complexity: $O((N + K) \cdot \log N)$

    The level order traversal takes $O(N)$ time. Since our heap can have a maximum of $O(N)$ elements, adding a sum to the heap takes $O(\log N)$ time, resulting in a total heap build time of $O(N \cdot \log N)$. Popping $k-1$ elements from the heap takes $O(k \cdot \log N)$ time. Therefore, the overall time complexity is $O((N + K) \cdot \log N)$.

* Space Complexity: $O(N)$

    The space usage is determined by both the level-order traversal queue and the heap. The queue, which reaches its maximum size when storing all nodes at the last level, requires $O(N)$ space. The heap, in the worst case (such as when the tree is a single path of $N$ nodes), can also take up to $O(N)$ space. Therefore, the overall space complexity is $O(N)$.  

### Approach 2: Level Order Traversal + Min Heap

### Intuition

In Approach 1, our max heap stored sums for all levels of the tree, making heap operations costly. In Approach 2, we use a min heap instead, where the smallest level sum is at the top. As we add new level sums, if the heap size exceeds `k`, we remove the top element. This ensures that, after processing all level sums, our heap contains the `k` largest sums, with the `k-th` largest at the top, which we can return. All smaller sums would have been evicted earlier whenever the heap size exceeded `k`. By limiting the heap size to `k`, where $k \leq \log N$, we reduce the overall time complexity.  

### Algorithm

1. Initialize a min heap/priority queue `pq` 
2. Initialize a queue `bfsQueue` to maintain the ordering of which nodes to visit for our level order traversal
3. Start by adding `root` to `bfsQueue`
4. Perform level order traversal. While `bfsQueue` is not empty:
    * Initialize `size` to be the current number of nodes of `bfsQueue`, which are all the nodes for the current level that we want to visit
    * For `size` iterations:
        * Initialize `sum` to `0`
        * Visit the next node by removing the next node in `bfsQueue`. Store it in `poppedNode`
        * Update `sum`: `sum += poppedNode.val`
        * Add the left and right children of `poppedNode` to the queue, if they exist. These children will be a part of the next level of the tree that will be visited in the next iteration. 
    * `sum` now contains a level order sum. Add it to `pq`
    * If size of `pq` now exceeds `k` elements, remove the top element.
5. If `pq` has less than `k` sums, then return -1 because we have less than `k` levels in our tree
6. Top element is the `k-th` largest sum so return it: `pq.peek()`

### Implementation


```python
class Solution:
    def kthLargestLevelSum(self, root, k):
        # min heap of size k
        # at the end, top element is kth largest
        pq = []
        bfs_queue = deque()
        bfs_queue.append(root)

        while bfs_queue:
            # level order traversal
            size = len(bfs_queue)
            sum_val = 0
            for _ in range(size):
                popped_node = bfs_queue.popleft()
                sum_val += popped_node.val
                if popped_node.left is not None:
                    # add left child
                    bfs_queue.append(popped_node.left)
                if popped_node.right is not None:
                    # add right child
                    bfs_queue.append(popped_node.right)

            heapq.heappush(pq, sum_val)
            if len(pq) > k:
                # evict top element
                heapq.heappop(pq)
        if len(pq) < k:
            return -1
        return pq[0]
```


### Complexity Analysis

Let $N$ be the total number of nodes in our tree.

* Time Complexity: $O(N \cdot \log k)$

    The level order traversal requires $O(N)$ time. We add to the heap a maximum of $O(N)$ times, with a maximum heap size of $k$, so building the heap takes $O(N \cdot \log k)$.

* Space Complexity: $O(N)$

    The space complexity is dominated by the level order traversal queue and the heap. The queue will reach $O(N)$ at the last level, while the heap has a maximum size of $O(k)$. Therefore, the total space complexity is $O(N)$.