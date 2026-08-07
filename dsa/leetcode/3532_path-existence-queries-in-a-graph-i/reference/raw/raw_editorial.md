### Approach 1: Binary Search

#### Intuition

For convenience, we say that two nodes are connected if there exists a path between them.

Since `nums` is sorted in non-decreasing order, if nodes $i$ and $j$ are connected, then every node $k$ satisfying $i < k < j$ is also connected to both of them.

Therefore, the nodes are naturally partitioned into several contiguous intervals with the following properties:

- The difference between the boundary elements of every two adjacent intervals is greater than `maxDiff`.
- Any two nodes within the same interval are connected.

For each query, we only need to determine whether the two queried nodes belong to the same interval.

To do this efficiently, we record the right endpoint of every interval. Then, for each queried node, we use binary search to find the interval containing it by locating the first right endpoint that is greater than or equal to its index. The two queried nodes are connected if and only if they belong to the same interval.

#### Implementation


```python
class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[bool]:
        rights = [i - 1 for i in range(1, n) if nums[i] - nums[i - 1] > maxDiff]
        rights.append(n - 1)
        return [
            bisect_left(rights, x) == bisect_left(rights, y) for x, y in queries
        ]
```


#### Complexity Analysis

Let $n$ be the length of $\textit{nums}$, and let $q$ be the number of queries.

- Time complexity: $O(n + q\log n)$.

- Space complexity: $O(n)$.

---

### Approach 2: Union-Find Set

#### Intuition

We can also solve this problem using the idea of connected components.

As discussed in Approach 1, the nodes in the same connected component always form a contiguous interval of indices. Instead of explicitly maintaining a union-find structure, we simply assign a component ID to each node while traversing the array from left to right.

Let `tags[i]` denote the component ID of node $i$.

During the traversal:
* If `nums[i] - nums[i - 1] > maxDiff`, then node $i$ starts a new connected component, so we set `tags[i] = tags[i - 1] + 1`.
* Otherwise, node $i$ belongs to the same connected component as node $i - 1$, so we set `tags[i] = tags[i - 1]`.

After preprocessing, two queried nodes are connected if and only if they have the same component ID.

#### Implementation


```python
class Solution:
    def pathExistenceQueries(
        self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]
    ) -> List[bool]:
        tags = [0] * n
        for i in range(1, n):
            tags[i] = tags[i - 1] + (
                1 if nums[i] - nums[i - 1] > maxDiff else 0
            )

        return [tags[x] == tags[y] for x, y in queries]
```


#### Complexity Analysis

Let $n$ be the length of $\textit{nums}$, and let $q$ be the number of queries.

- Time complexity: $O(n + q)$.

- Space complexity: $O(n)$.
  
---