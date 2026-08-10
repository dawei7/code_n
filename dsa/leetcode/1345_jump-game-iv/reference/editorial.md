
## Solution

---

### Overview

You probably can guess from the problem title, this is the fourth problem in the series of [Jump Game](https://leetcode.com/problems/jump-game/) problems. Those problems are similar, but have considerable differences, making their solutions quite different.

Here, two approaches are introduced: *Breadth-First Search* approach and *Bidirectional BFS* approach.

---

### Approach 1: Breadth-First Search

Most solutions start from a brute force approach and are optimized by removing unnecessary calculations. Same as this one.

A naive brute force approach is to iterate all the possible routes and check if there is one reaches the last index. However, if we already checked one index, we do not need to check it again. We can mark the index as visited by storing them in a `visited` set.

From convenience, we can store nodes with the same value together in a `graph` dictionary. With this method, when searching, we do not need to iterate the whole list to find the nodes with the same value as the next steps, but only need to ask the precomputed dictionary. However, to prevent stepping back, we need to clear the dictionary after we get to that value.

```python
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        graph = {}
        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]

        curs = [0]  # store current layers
        visited = {0}
        step = 0

        # when current layer exists
        while curs:
            nex = []

            # iterate the layer
            for node in curs:
                # check if reached end
                if node == n-1:
                    return step

                # check same value
                for child in graph[arr[node]]:
                    if child not in visited:
                        visited.add(child)
                        nex.append(child)

                # clear the list to prevent redundant search
                graph[arr[node]].clear()

                # check neighbors
                for child in [node-1, node+1]:
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.append(child)

            curs = nex
            step += 1

        return -1
```

**Complexity Analysis**

Assume $N$ is the length of `arr`.

* Time complexity: $\mathcal{O}(N)$ since we will visit every node at most once.

* Space complexity: $\mathcal{O}(N)$ since it needs `curs` and `nex` to store nodes.

---

### Approach 2: Bidirectional BFS

In the later part of our original BFS method, the layer may be long and takes a long time to compute the next layer. In this situation, we can compute the layer from the end, which may be short and takes less time.

```python
class Solution:
    def minJumps(self, arr) -> int:
        n = len(arr)
        if n <= 1:
            return 0

        graph = {}
        for i in range(n):
            if arr[i] in graph:
                graph[arr[i]].append(i)
            else:
                graph[arr[i]] = [i]

        curs = set([0])  # store layers from start
        visited = {0, n-1}
        step = 0

        other = set([n-1]) # store layers from end

        # when current layer exists
        while curs:
            # search from the side with fewer nodes
            if len(curs) > len(other):
                curs, other = other, curs
            nex = set()

            # iterate the layer
            for node in curs:

                # check same value
                for child in graph[arr[node]]:
                    if child in other:
                        return step + 1
                    if child not in visited:
                        visited.add(child)
                        nex.add(child)

                # clear the list to prevent redundant search
                graph[arr[node]].clear()

                # check neighbors
                for child in [node-1, node+1]:
                    if child in other:
                        return step + 1
                    if 0 <= child < len(arr) and child not in visited:
                        visited.add(child)
                        nex.add(child)

            curs = nex
            step += 1

        return -1
```

**Complexity Analysis**

Assume $N$ is the length of `arr`.

* Time complexity: $\mathcal{O}(N)$ since we will visit every node at most once, but usually faster than approach 1.

* Space complexity: $\mathcal{O}(N)$ since it needs `curs`, `other` and `nex` to store nodes.