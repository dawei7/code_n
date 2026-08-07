### Approach 1: Hash Table + Binary Search

#### Intuition

First, we need to clarify an important observation: to find the nearest element with the same value as a given element $x$, we only need to consider the first matching element encountered when traversing left or right from $x$.

Next, we preprocess the array by storing the positions of each value using a hash table. The key is the element value, and the corresponding value is a list of indices where this element appears in the array.

For each value, its position list has no adjacent element to the left of the first occurrence and no adjacent element to the right of the last occurrence. This creates boundary issues when computing distances. Since the array is cyclic, we can handle this by adding two artificial positions:

- Insert $(\text{last position} - n)$ at the beginning
- Append $(\text{first position} + n)$ at the end

This ensures that every position has both a left and right neighbor, eliminating the need for explicit boundary checks.

For each query, we retrieve the position list corresponding to the queried value using the hash table. Then, we use binary search to locate the position of the query index within this list. Finally, we compute the distance to its immediate neighbors on both sides and take the minimum.

#### Implementation


```python
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        nums_pos = defaultdict(list)

        for i in range(n):
            nums_pos[nums[i]].append(i)

        for pos in nums_pos.values():
            x = pos[0]
            pos.insert(0, pos[-1] - n)
            pos.append(x + n)

        for i in range(len(queries)):
            x = nums[queries[i]]
            pos_list = nums_pos[x]
            if len(pos_list) == 3:
                queries[i] = -1
                continue
            pos = bisect.bisect_left(pos_list, queries[i])
            queries[i] = min(
                pos_list[pos + 1] - pos_list[pos],
                pos_list[pos] - pos_list[pos - 1],
            )

        return queries
```


#### Complexity Analysis

Let $n$ be the length of the array $\textit{nums}$, and $m$ be the number of queries.

- Time complexity: $O(n + m \log n)$.

- Space complexity: $O(n)$.

### Approach 2: Preprocessing Nearest Left and Right Positions + Hash Table

#### Intuition

In this approach, we preprocess the nearest positions of elements with the same value on both the left and right sides for every index. We store these in two arrays:

- $\textit{left}[i]$: the nearest index to the left of $i$ with the same value
- $\textit{right}[i]$: the nearest index to the right of $i$ with the same value

To compute these efficiently, we use a hash table to track the most recent occurrence of each value.

We traverse the array twice:

- First pass (left to right, from $-n$ to $n - 1$): used to fill the $\textit{left}$ array
- Second pass (right to left, from $2n - 1$ to $0$): used to fill the $\textit{right}$ array

The extended traversal handles the cyclic nature of the array.

For each query index $i$, we check whether the nearest same-value element is at a distance equal to $n$. If so, it means the element appears only once in the array, so the answer is $-1$. Otherwise, we compute the distances to the nearest matching elements on both sides and take the minimum.

#### Implementation


```python
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        n = len(nums)
        left = [0] * n
        right = [0] * n
        pos = {}

        for i in range(-n, n):
            if i >= 0:
                left[i] = pos.get(nums[i], -n)
            pos[nums[(i + n) % n]] = i

        pos.clear()
        for i in range(2 * n - 1, -1, -1):
            if i < n:
                right[i] = pos.get(nums[i], 2 * n)
            pos[nums[i % n]] = i

        for i in range(len(queries)):
            x = queries[i]
            if x - left[x] == n:
                queries[i] = -1
            else:
                queries[i] = min(x - left[x], right[x] - x)

        return queries
```


#### Complexity Analysis

Let $n$ be the length of the array $\textit{nums}$, and $m$ be the number of queries.

- Time complexity: $O(n + m)$.

- Space complexity: $O(n)$.

---