[TOC]

## Solution
 
---

### Approach 1: Bellman-Ford Algorithm


#### Intuition   

> If you are not familiar with the Bellman-Ford algorithm, please refer to our [Bellman-Ford Algorithm Explore Card](https://leetcode.com/explore/learn/card/graph/622/single-source-shortest-path-algorithm/3864/). For the sake of brevity, we will focus only on the usage of Bellman-Ford and not the implementation details.

The algorithm works by relaxing edges in the graph, meaning that it tries to improve the shortest path estimate for each node in the graph until the solution is found. 

Bellman-Ford is typically used to find the shortest path in a weighted graph. In this problem, instead of the shortest distance, we are looking for the **maximum probability**. The length of a path is the sum of the weights of its edges. Here, the probability of a path equals the product of the probabilities of its edges.

Initially, we set the probability to reach the starting node `start` as `1` and all other probabilities as `0`. Then we iteratively relax the edges of the graph by updating the probability to each node if a higher probability is found. 

Considering that a path in the graph without a cycle contains at most `n - 1` edges, the process is repeated `n - 1` times, which is enough to relax every edge of every possible path.

- In the first round, we update the maximum probability of reaching each node `u` from the starting node along the path that contains only one edge `(u, v)`.
- In the second round, we update the maximum probability of reaching each node `u` from the starting node along the path that contains two edges (including `(u, v)`).
- and so on.

After `n - 1` rounds, we have updated `max_prob[end]` to be the maximum probability of reaching `end` from the staring node along every possible path.

<br>

#### Algorithm

1) Initialize an array `maxProb` as the maximum probability to reach each node from the staring node, set `maxProb[start]` as `1`.

2) Relax all edges: for each edge `(u, v)`, if a higher probability of reaching `u` through this edge is found, update the `max_prob[u]` as `max_prob[u] = max_prob[v] * path_prob`, if a higher probability to reach `v` through this edge is found, update the `max_prob[v]`.

3) If we are unable to update any node with a higher probability, we can stop the iteration by proceeding to step 4. Otherwise, repeat step 2 until all edges are relaxed `n - 1` times.

4) Return `max_prob[end]`.

#### Implementation


```python
class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start: int,
        end: int,
    ) -> float:
        max_prob = [0] * n
        max_prob[start] = 1

        for i in range(n - 1):
            # If there is no larger probability found during an entire round of updates,
            # stop the update process.
            has_update = 0
            for j in range(len(edges)):
                u, v = edges[j]
                path_prob = succProb[j]
                if max_prob[u] * path_prob > max_prob[v]:
                    max_prob[v] = max_prob[u] * path_prob
                    has_update = 1
                if max_prob[v] * path_prob > max_prob[u]:
                    max_prob[u] = max_prob[v] * path_prob
                    has_update = 1
            if not has_update:
                break

        return max_prob[end]
```


#### Complexity Analysis

Let $$n$$ be the number of nodes and $$m$$ be the number of edges.

* Time complexity: $$O(n \cdot m)$$

    - The algorithm relaxes all edges in the graph `n - 1` times, each round contains an iteration over all `m` edges.

* Space complexity: $$O(n)$$

    - We only need an array of size $$n$$ to update the maximum probability to reach each node from the starting node.

<br/>

---

### Approach 2: Shortest Path Faster Algorithm 

#### Intuition   

The Shortest Path Faster Algorithm (SPFA) is an improvement of the Bellman–Ford algorithm which computes single-source shortest paths in a weighted directed graph. 

We start at node `start` and traverse all its neighbors, calculating the probability of moving from `start` to each neighbor. We then add these neighbors to a queue, and continue the process for all nodes in the queue until we empty the queue.

The key is maintaining a running maximum probability for each node, and using this maximum to calculate the probabilities for its neighbors. If the probability of traveling from the starting node to a neighbor node through a specific edge is greater than the current maximum probability for that neighbor, we update the maximum probability of this neighbor node, and add this neighbor node to the queue.

Another key point to note is how we calculate the probability of traveling from `start` to a neighbor node. We are given a set of edge weights that represent the probabilities of moving from one node to another. To calculate the probability of traveling from the starting node to a neighbor node through a specific edge, we simply multiply the edge weight (i.e., the probability of traveling through that edge) by the maximum probability of reaching the current node from the starting node. This gives us the probability of reaching the neighbor node through the current edge.

Take the slides below as an example:



![Slide 1](images/slideshow_s1_s1.png)

![Slide 2](images/slideshow_s1_s2.png)

![Slide 3](images/slideshow_s1_s3.png)

![Slide 4](images/slideshow_s1_s4.png)

![Slide 5](images/slideshow_s1_s5.png)

![Slide 6](images/slideshow_s1_s6.png)

![Slide 7](images/slideshow_s1_s7.png)

![Slide 8](images/slideshow_s1_s8.png)

![Slide 9](images/slideshow_s1_s9.png)

![Slide 10](images/slideshow_s1_s10.png)

![Slide 11](images/slideshow_s1_s11.png)

![Slide 12](images/slideshow_s1_s12.png)



> You might wonder, will repeatedly adding the same node back to the queue cause an infinite loop and result in a timeout?

The answer is NO, because we only update the probability of reaching a neighbor node, say `nxt_node` and add it back to `queue` if the current path **increases** the probability of reaching `nxt_node` from the starting node. Moreover, the weight (probability) of each path is less than or equal to 1. Therefore, even if the graph contains a cycle, the product of the probabilities of all edges in the cycle is still less than or equal to 1. Since loops do not increase the probability of reaching a node, paths that contain loops will be excluded from consideration and not added to the queue.

![img](images/c.png)

<br>

#### Algorithm

1) Initialize an empty queue `queue` to store nodes that need to be visited.

2) Initialize an array `max_prob` to store the maximum probability of reaching each node from the starting node. Set the probability of the starting node `max_prob[start]` as 1, and the probability of all other nodes as 0.

3) Add the starting node `start` to the `queue`.

4) While `queue` is not empty, we remove the first node `cur_node` from the queue.

5) For each neighbor of `nxt_node`, calculate the probability of traveling from the starting node to the `nxt_node` through the current edge (`cur_node --- nxt_node`), and update the maximum probability for this neighbor `max_prob[nxt_node]` if necessary.

6) If the probability to this neighbor node is increased, add `nxt_node` to `queue`.

7) Repeat steps 4-6 until `queue` is empty.

8) Return `max_prob[end]`, the maximum probability of reaching the end node `end` from the starting node.

#### Implementation


```python
class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start: int,
        end: int,
    ) -> float:
        graph = defaultdict(list)
        for i, (a, b) in enumerate(edges):
            graph[a].append([b, succProb[i]])
            graph[b].append([a, succProb[i]])

        max_prob = [0.0] * n
        max_prob[start] = 1.0

        queue = deque([start])
        while queue:
            cur_node = queue.popleft()
            for nxt_node, path_prob in graph[cur_node]:

                # Only update max_prob[nxt_node] if the current path increases
                # the probability of reach nxt_node.
                if max_prob[cur_node] * path_prob > max_prob[nxt_node]:
                    max_prob[nxt_node] = max_prob[cur_node] * path_prob
                    queue.append(nxt_node)

        return max_prob[end]
```


#### Complexity Analysis

Let $$n$$ be the number of nodes and $$m$$ be the number of edges.

* Time complexity: $$O(n \cdot m)$$

    - The worst-case running of SPFA is $$O(|V|\cdot|E|)$$. However, this is only the worst-case scenario, and the average runtime of SPFA is better than in Bellman-Ford.

* Space complexity: $$O(n + m)$$
    - We build a hash map `graph` based on all edges, which takes $$O(m)$$ space.
    - The algorithm stores the probability array `max_prob` of size $$O(n)$$ and a queue of vertices `queue`. In the worst-case scenario, there are $$O(m)$$ nodes in `queue` at the same time.

<br/>

---

### Approach 3: Dijkstra's Algorithm

#### Intuition   

> If you are not familiar with the Dijkstra's algorithm, please refer to our [Dijkstra's Algorithm Explore Card](https://leetcode.com/explore/learn/card/graph/622/single-source-shortest-path-algorithm/3862/). For the sake of brevity, we will focus on the usage of the algorithm and not implementation details.

In BFS, we are exploring the graph in a breadth-first manner, which may not always lead to the shortest path. This is because BFS does not take into account the weights of the edges and only considers the number of hops. As shown in the picture below, even though the two paths to `end`
- `0` -- `2`
- `0` -- `1` -- `2`
don't have the maximum probability, we still need to update all the nodes along these paths.

![img](images/d1.png)

In contrast, Dijkstra's algorithm takes into account the weights of the edges and always guarantees to find the highest probability from the source node to any other node in the graph. This is where Dijkstra's algorithm becomes more suitable than BFS, as it takes into account the weights (probabilities) of the edges and can find the path with the highest probability of reaching the end node. 

![img](images/d2.png)

We start from the starting node `start`, and consider its neighbors one by one, updating the probability to each neighboring node `nxt_node` if the probability of reaching `nxt_node` through the current node `cur_node` is higher than the previous stored probability of reaching `nxt_node` (by other paths). In order to always select the node with the highest reaching probability, we use a priority queue `pq` to store the nodes to visit, where the node with the highest probability of being reached from the starting node has the highest priority.

<br>

#### Algorithm

1) Initialize a priority queue `pq` to store nodes that need to be visited, and an array `max_prob` to store the maximum probability to reach each node from the starting node. Set the probability of the starting node as `1`, and the probability of all other nodes as `0`.

2) Add the starting node `start` and its probability to the priority queue.

3) While `pq` is not empty, remove `cur_node`, the node with the highest priority from it.

4) For each neighbor `nxt_node` of the current node `cur_node`, calculate the probability of traveling from the starting node to the `nxt_node` through the current edge `cur_node --- nxt_node`, and update the maximum probability of `nxt_node` if necessary. To update the maximum probability, compare the product of the probability with the current node and the probability of the edge `cur_node --- nxt_node`, with the current maximum probability to the neighbor node. If the product is larger than the maximum probability stored in `max_prob[nxt_node]`, we update the maximum probability `max_prob[nxt_node]` as their product.

5) If the neighbor node `nxt_node` has not been visited, we add it and its probability to the `pq`.

6) Repeat steps 3-5 until the priority queue is empty or the ending node `end` has been reached.

7) Return `max_prob[end]`.

#### Implementation


```python
class Solution:
    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start: int,
        end: int,
    ) -> float:
        graph = defaultdict(list)
        for i, (u, v) in enumerate(edges):
            graph[u].append((v, succProb[i]))
            graph[v].append((u, succProb[i]))

        max_prob = [0.0] * n
        max_prob[start] = 1.0

        pq = [(-1.0, start)]
        while pq:
            cur_prob, cur_node = heapq.heappop(pq)
            if cur_node == end:
                return -cur_prob

            # Mark the node as processed by clearing its adjacency list
            if graph[cur_node]:  # Only clear if the list is not already empty
                for nxt_node, path_prob in graph[cur_node]:
                    if -cur_prob * path_prob > max_prob[nxt_node]:
                        max_prob[nxt_node] = -cur_prob * path_prob
                        heapq.heappush(pq, (-max_prob[nxt_node], nxt_node))
                graph[
                    cur_node
                ].clear()  # Clear the adjacency list after processing

        return 0.0
```


> Note that Python's heapq module only implements min heaps. Since we want higher probabilities to be popped first, we need a max heap. To fix this, we multiply the probabilities by `-1`.

#### Complexity Analysis

Let $$n$$ be the number of nodes and $$m$$ be the number of edges.

* Time Complexity: $$O((n + m) \cdot \log n)$$

   - We build an adjacency list `graph` based on all edges, which takes $$O(m)$$ time.
   - In the worst case, each node could be pushed into the priority queue exactly once, which results in $$O(n \cdot \log n)$$ operations.
   - Each edge is considered exactly once when its corresponding node is dequeued from the priority queue. This takes $$O(m \cdot \log n)$$ time in total, due to the priority queue's $$\log n$$ complexity for insertion and deletion operations.
   
> You can also refer to our [Dijkstra's Algorithm Explore Card](https://leetcode.com/explore/learn/card/graph/622/single-source-shortest-path-algorithm/3862/) for details on the complexity analysis.

* Space Complexity: $$O(n + m)$$

   - We build an adjacency list `graph` based on all edges, which takes $$O(m)$$ space.
   - The algorithm stores the `maxProb` array, which uses $$O(n)$$ space.
   - We use a priority queue to keep track of nodes to be visited, and there are at most $$n$$ nodes in the queue.
   - To sum up, the overall space complexity is $$O(n + m)$$.

<br/>