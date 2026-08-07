[TOC]

## Solution

---

### Overview

According to the problem statement:

-   There are $n$ cities, numbered from $0$ to $n-1$.
-   Initially, each pair of consecutive cities is connected by a one-way road.
-   Formally, for each $i$ where $0 \leq i \leq n-2$, there exists a directed and unweighted edge from city $i$ to city $i+1$.

Additionally, we are given an array of length $q$, called $queries$, where each element represents a new road to be added:

-   Each element in $queries$ is defined as $\text{queries}[i] = [u_i, v_i]$, where:
-   $u_i$ and $v_i$ are the cities between which a new directed and unweighted road will be added at step $i$.
-   It is guaranteed that $u_i < v_i$.

After adding each road in $queries$, we have to determine the length of the shortest path between city $0$ and city $n-1$. Then we will return the result as an array of length $q$, where each element corresponds to the shortest path length after each step.

---

### Approach 1: Breadth First Search (BFS)

#### Intuition

The problem statement naturally suggests a graphical representation, where cities are modeled as nodes and the roads connecting them are represented as edges. This transforms our task into a well-known graph problem: finding the shortest path between two nodes.

However, there's an important distinction: our graph is dynamic, with new edges added at each step. A logical approach is to update the graph with each new road and apply a path-finding algorithm at each step to find the shortest path.

To select the appropriate algorithm, we need to consider the properties of our graph. One notable characteristic is that the edges are unweighted. This implies that the total cost of a path is equivalent to the number of steps taken to reach the destination, or, in other words, the number of layers of nodes that must be explored.

This understanding leads us to implement the [Breadth-First Search (BFS)](https://leetcode.com/explore/learn/card/graph/620/breadth-first-search-in-graph/) algorithm, which is particularly suited for this type of problem.

!?!../Documents/3243/3243_Approach1.json:960,540!?!

If you need a refresher on how BFS works, you can refer to the classic problem [994. Rotting Oranges](https://leetcode.com/problems/rotting-oranges/description).

#### Algorithm

-   Define a helper function `bfs` that, given the number of nodes `n` and the graph's adjacency list `adjList`, returns the number of edges in the shortest path between node `0` and node $n - 1$.

-   Initialize a boolean array `visited` to mark the processed nodes.
-   Initialize a queue `nodeQueue`.
-   Push node `0` into the queue and mark it as visited.
-   Initialize a variable `currentLayerNodeCount` to `1` (since node `0` is already in the queue), `nextLayerNodeCount` to `0`, and `layersExplored` to `0`.
-   Perform BFS until the queue is empty:
-   Iterate over the nodes in the current layer, with `i` ranging from `0` to $currentLayerNodeCount - 1$:
-   Pop the first node, called `currentNode`, from the queue and check whether it is the target node ($n - 1$).
-   If the condition is true, return `layersExplored`.
-   For every `neighbor` in $\text{adjList}[currentNode]$:
-   If `neighbor` has already been visited, continue.
-   Otherwise:
-   Push `neighbor` into the queue.
-   Increment `nextLayerNodeCount` by `1`.
-   Mark `neighbor` as visited.
-   When the loop is over and all nodes in the current layer are processed:
-   Set $currentLayerNodeCount = nextLayerNodeCount$.
-   Set $nextLayerNodeCount = 0$.
-   Increment `layersExplored` by `1`.
-   Since the initial constraint that every two consecutive nodes are connected guarantees that there is always a path between node `0` and node $n - 1$, the algorithm will never exit the BFS loop without having found and returned the shortest path length. Here, simply return a random value, e.g., `-1`.

-   In the main function `shortestDistanceAfterQueries`:
-   Initialize the result array `answer`.
-   Initialize a 2D array `adjList`.
-   Iterate over the first $n - 1$ nodes with `i` ranging from `0` to $n - 2$:
-   Push $i + 1$ to $\text{adjList}[i]$.
-   Enter a new loop to process each query $\text{query}[i] = [u, v]$:
-   Push `v` to $\text{adjList}[u]$.
-   Run `bfs` and push the result to the `answer` array.
-   Finally, return `answer`.

#### Implementation

```python
class Solution:

    # Helper function to perform BFS and find the number of edges in the shortest path from node 0 to node n-1
    def bfs(self, n: int, adj_list: List[List[int]]) -> int:
        visited = [False] * n
        node_queue = deque()

        # Start BFS from node 0
        node_queue.append(0)
        visited[0] = True

        # Track the number of nodes in the current layer and the next layer
        current_layer_node_count = 1
        next_layer_node_count = 0
        # Initialize layers explored count
        layers_explored = 0

        # Perform BFS until the queue is empty
        while node_queue:
            # Process nodes in the current layer
            for _ in range(current_layer_node_count):
                current_node = node_queue.popleft()

                # Check if we reached the destination node
                if current_node == n - 1:
                    return layers_explored  # Return the number of edges in the shortest path

                # Explore all adjacent nodes
                for neighbor in adj_list[current_node]:
                    if visited[neighbor]:
                        continue
                    node_queue.append(
                        neighbor
                    )  # Add neighbor to the queue for exploration
                    next_layer_node_count += (
                        1  # Increment the count of nodes in the next layer
                    )
                    visited[neighbor] = True

            # Move to the next layer
            current_layer_node_count = next_layer_node_count
            next_layer_node_count = 0  # Reset next layer count
            layers_explored += 1  # Increment the layer count after processing the current layer

        return -1  # Algorithm will never reach this point

    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        answer = []
        adj_list = [[] for _ in range(n)]

        # Initialize the graph with edges between consecutive nodes
        for i in range(n - 1):
            adj_list[i].append(i + 1)

        # Process each query to add new roads
        for road in queries:
            u, v = road
            adj_list[u].append(v)  # Add road from u to v
            # Perform BFS to find the shortest path after adding the new road
            answer.append(self.bfs(n, adj_list))

        return answer

```

#### Complexity Analysis

Let $n$ be the number of cities and $q$ the number of queries.

-   Time Complexity: $O(q \times (n + q))$.

    At first glance, the `bfs` function appears to contain three nested loops, which might suggest a time complexity of $O(n^3)$. However, this is misleading. A closer look shows that each part of the BFS algorithm runs in relation to the nodes and edges in the graph after each road (edge) addition.

-   Node Processing (first inner loop): Each node is added to and removed from the queue exactly once, giving a time complexity of $O(n)$ for processing all nodes.
-   Edge Exploration (second inner loop): For each dequeued node, the algorithm checks all its neighbors. Each edge is examined only once, so the total time for edge exploration is $O(e)$, where $e$ is the number of edges in the graph.

    Combining these, the time complexity of each BFS run is $O(n + e)$.

-   Layer-wise Node Processing (outer loop): The outer loop runs based on the number of graph layers rather than the number of nodes, ensuring the BFS explores nodes systematically. This does not increase the overall complexity, which remains $O(n + e)$.

    Each BFS after adding a road incrementally increases the edge count. The time complexity across all $q$ queries is thus:

1. After the 1st road: $O(n + n)$.
2. After the 2nd road: $O(n + n + 1)$.
3. …
4. After the $q$-th road: $O(n + n + q - 1)$.

    Summing these yields:

    $$
    \begin{aligned}
        $\mathcal{O}(n + n)$ + $\mathcal{O}(n + n + 1)$ + \dots + $\mathcal{O}(n + n + q - 1)$ \\
        = $\mathcal{O}(2qn + \frac{q(q-1)$}{2}) \\
        = $\mathcal{O}(q \times (n + q)$)
    \end{aligned}
    $$

-   Space Complexity: $O(n+q)$.

    To represent our graph, we create and continuously update its adjacency list in the form of a 2D array. Initially, this array contains $n-1$ elements, representing the edges between every two consecutive nodes. After processing all queries, the array will contain $n + q - 1$ elements, contributing $O(n + q)$ to the total space complexity.

    In addition to the adjacency list, the `bfs` function creates a 1D array, named `visited` and a queue, called `nodeQueue`, both of which can have a maximum size of $n$.

    Therefore, the overall space complexity remains $O(n+q)$.

---

### Approach 2: Recursive Dynamic Programming (Top-Down)

#### Intuition

Upon closer examination of the graph, we can determine that it is a Directed Acyclic Graph (DAG). This means:

-   Directed Edges: Each road in the graph has a specific direction (is unidirectional).

-   No Cycles: A key characteristic of a DAG is that it does not contain any cycles. In this graph, every road's destination node has a value greater than that of its source node. This property ensures that it is impossible to return to a starting node by following the directed edges.

Using the language of the problem, we can say that for every node $v_i$, the distance to the final node $v_{n-1}$ only depends on two factors:

-   The distance from $v_i$ to the subsequent nodes $v_{i+1}$, $v_{i+2}$, ..., $v_{n-1}$.
-   The distance from the subsequent nodes $v_{i+1}$, $v_{i+2}$, ..., $v_{n-1}$ to the final node $v_{n-1}$.

Specifically the relationship can be expressed as, $distance_{v_i, v_{n-1}} = \min_{j} (distance_{v_i, v_j}+ distance_{v_j, v_{n-1}})$.

In our calculations, we notice that some states overlap, meaning they are needed in various computations but are independent of one another. This characteristic indicates that dynamic programming could help us solve this problem efficiently.

#### Algorithm

-   Define a recursive function `findMinDistance` that, given the number of nodes `n`, the graph's adjacency list `adjList`, the memoization array `dp`, and the node `currentNode`, returns the number of edges in the shortest path from node `currentNode` to node $n - 1$.

-   Base case: if $currentNode = n - 1$, return `0`.
-   Computed case: if $\text{dp}[currentNode] \neq -1$, return $\text{dp}[currentNode]$.
-   Initialize a variable `minDistance` to `n`.
-   For every `neighbor` of `currentNode`:
-   Set $minDistace = min(minDistance, 1 + findMinDistance(..., neighbor))$.
-   Store the computed `minDistance`; set $\text{dp}[currentNode] = minDistance$.
-   Return `minDistance`.

-   In the main function `shortestDistanceAfterQueries`:
-   Initialize an empty result array `answer`.
-   Initialize a memoization array `dp` of size `n`. Initially set all `dp` values to `-1`.
-   Initialize a 2D array `adjList` to represent the graph.
-   Iterate over the first $n - 1$ nodes, with `i` ranging from `0` to $n - 2$:
-   Add `i+1` to $\text{adjList}[i]$ to create initial consecutive edges.
-   Process each query $\text{query}[i] = [u, v]$ in a loop:
-   Add `v` to $\text{adjList}[u]$ to represent the new edge.
-   Run `findMinDistance` for node `0` and append the result to the `answer` array.
-   Reset all values in the `dp` array to `-1`.
-   Finally, return `answer`.

#### Implementation

```python
class Solution:
    # Recursive function to find the minimum distance from the current node to
    # the destination node (n-1)
    def find_min_distance(self, adj_list, n, current_node, dp):
        # We've reached the destination node
        if current_node == n - 1:
            return 0

        # If this node has already been computed, return the stored value
        if dp[current_node] != -1:
            return dp[current_node]

        min_distance = n

        for neighbor in adj_list[current_node]:
            # Recursively find the minimum distance from the neighbor to the destination
            min_distance = min(
                min_distance,
                self.find_min_distance(adj_list, n, neighbor, dp) + 1,
            )

        # Store the computed minimum distance in the dp array and return it
        dp[current_node] = min_distance
        return min_distance

    def shortestDistanceAfterQueries(self, n, queries):
        dp = [-1] * n  # DP array to store minimum distances from each node
        adj_list = [[] for _ in range(n)]

        # Initialize the graph with edges between consecutive nodes
        for i in range(n - 1):
            adj_list[i].append(i + 1)

        answer = []

        # Process each query to add new edges
        for road in queries:
            u = road[0]
            v = road[1]

            # Add the directed edge from u to v
            adj_list[u].append(v)

            # Find the minimum distance from the starting node (0) to the destination (n-1)
            answer.append(self.find_min_distance(adj_list, n, 0, dp))

            # Clear and reset the dp array
            dp = [-1] * n

        return answer  # Return the results for each query
```

#### Complexity Analysis

Let $n$ be the number of cities and $q$ the number of queries.

-   Time Complexity: $O(q \times (n+q))$.

-   Time Complexity: $O(q \times (n+q))$.

    The `findMinDistance` function is called on the starting node (node `0`) each time a query is processed. If the distance for a node is already computed, the function returns the cached value from the `dp` array, avoiding redundant calculations.

    During its first call for node `0`, `findMinDistance` explores all neighbors, iterating over all outgoing edges. Each node is processed only once for distance calculation due to caching in the `dp` array.

    The time complexity of a single `findMinDistance` call on node `0` is $O(e)$, where $e$ represents the current number of edges in the graph. Since each edge is visited exactly once, the computation scales linearly with the number of edges.

    Thus, the total time complexity sums to:

    $$
    \begin{aligned}
        $\mathcal{O}(n)$ +  $\mathcal{O}(n+1)$ + \ldots +  $\mathcal{O}(n+q-1)$ \\
        = $\mathcal{O}(q \times (n+q)$)
    \end{aligned}
    $$

-   Space Complexity: $O(n+q)$.

    Once again, we choose to represent our graph using an adjacency list, the maximum size of which is $O(n + q)$. Additionally, we create a 1D memoization array, called `dp`, with a fixed size of $n$ and we also invoke a recursive function `findMinDistance`, whose depth is $O(n)$, as well. Combining the above, we conclude that the total space complexity is $O(n+q)$.

---

### Approach 3: Iterative Dynamic Programming (Bottom-Up)

#### Intuition

While the top-down dynamic programming approach is often intuitive, it can become less effective in certain situations, particularly due to uncontrolled recursion depth. This is especially true for larger input sizes, where deep recursion can lead to stack overflow errors. To avoid this risk, it is generally considered a good idea to convert recursive dynamic programming solutions into iterative ones.

In an iterative approach, we essentially take each line from the previous recursive algorithm and translate it into its iterative equivalent. A key consideration in this translation is that when we compute $\text{dp}[u]$, it represents the result of the `findMinDistance` function for node `u`. Thus, both the return value and the runtime complexity of `findMinDistance(u)` can be directly replaced with $\text{dp}[u]$.

To implement the iterative approach effectively, we need to recognize the relationship between the calls in the recursive function. We begin our computation at the base case, which occurs when `currentNode` equals $n - 1$, and work our way up to $currentNode = 0$. This means that our bottom-up approach should process nodes in reverse order, starting from $currentNode = n - 1$ and building our results incrementally until we reach $currentNode = 0$. By doing so, we ensure that all necessary values are calculated before they are needed.

!?!../Documents/3243/3243_Approach3.json:960,540!?!

#### Algorithm

-   Define a function `findMinDistance` that, given the number of nodes `n` and the graph's adjacency list `adjList`, returns the number of edges in the shortest path from node `0` to node $n - 1$.

-   Initialize a 1D array of size `n`, called `dp`.
-   Base case: set $dp[n-1] = 0$.
-   Iterate over the first $n - 1$ nodes in reversed order, with `currentNode` from $n - 2$ to `0`. On each iteration:
-   Initialize `minDistance` to `n`.
-   For each `neighbor` of `currentNode`:
-   Set $minDistance = min(minDistance, \text{dp}[neighbor] + 1)$.
-   After exiting the inner loop, set $\text{dp}[currentNode] = minDistance$.
-   Return $\text{dp}[0]$.

-   In the main function `shortestDistanceAfterQueries`:
-   Initialize an empty result array `answer`.
-   Initialize a 2D array `adjList` to represent the graph.
-   Iterate over the first `n-1` nodes, with `i` ranging from `0` to `n-2`:
-   Add `i+1` to $\text{adjList}[i]$ to create initial consecutive edges.
-   Process each query $\text{query}[i] = [u, v]$ in a loop:
-   Add `v` to $\text{adjList}[u]$ to represent the new edge.
-   Run `findMinDistance` and append the result to the `answer` array.
-   Finally, return `answer`.

#### Implementation

```python
class Solution:
    # Function to find the minimum distance from node 0 to node n-1
    def find_min_distance(self, adj_list, n):
        dp = [0] * n
        dp[n - 1] = 0  # Base case: distance to destination (n-1) is 0

        # Iterate from the second last node down to the first node
        for current_node in range(n - 2, -1, -1):
            min_distance = n
            # Explore neighbors to find the minimum distance
            for neighbor in adj_list[current_node]:
                min_distance = min(min_distance, dp[neighbor] + 1)
            # Store the calculated distance for the current node
            dp[current_node] = min_distance

        return dp[0]

    def shortestDistanceAfterQueries(self, n, queries):
        answer = []
        adj_list = [[] for _ in range(n)]

        # Initialize edges between consecutive nodes
        for i in range(n - 1):
            adj_list[i].append(i + 1)

        # Process each query to add new edges
        for road in queries:
            u, v = road[0], road[1]
            adj_list[u].append(v)  # Add the directed edge from u to v

            # Calculate the minimum distance after adding the new edge
            answer.append(self.find_min_distance(adj_list, n))

        return answer
```

#### Complexity Analysis

Let $n$ be the number of cities and $q$ the number of queries.

-   Time Complexity: $O(q \times (n+q))$.

    The `findMinDistance` function iterates over each edge exactly once, so its time complexity for a graph with $e$ edges is $O(e)$.

    Therefore, like the previous approaches, the total time complexity of the algorithm can be expressed as:

    $$
    \begin{aligned}
        $\mathcal{O}(n)$ +  $\mathcal{O}(n+1)$ + ... +  $\mathcal{O}(n+q-1)$ = \\
        $\mathcal{O}(q \times (n+q)$).
    \end{aligned}
    $$

-   Space Complexity: $O(n+q)$.

    The total space complexity is once again determined by the size of the adjacency list which is at most $O(n+q)$.

---