### Approach 1: Reversed Breadth-First Search

#### Intuition

We use breadth-first search to find the shortest path from the end of the array, $n - 1$, back to the starting index $0$.

Preprocessing: Use the Sieve of Eratosthenes to compute the list of prime factors for all numbers in the range, stored in $\textit{factors}$.

Mapping: Traverse the array, and whenever a number is prime, store its index in $\textit{edges}$. These act as "transit stations" that enable long-distance jumps.

During the breadth-first search, for the current index $i$ in the queue $q$, we consider three types of movements:
- Adjacent movement: move to $i - 1$ or $i + 1$.
- Jump movement: for each prime factor $p$ of $\textit{nums}[i]$, jump to all indices $j$ stored in $\textit{edges}[p]$.

We return the depth of the BFS once index $0$ is reached.

#### Implementation


```python
MX = 1_000_001
factors = [[] for _ in range(MX)]
for i in range(2, MX):
    if not factors[i]:
        for j in range(i, MX, i):
            factors[j].append(i)


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        edges = defaultdict(list)
        for i, a in enumerate(nums):
            if len(factors[a]) == 1:
                edges[a].append(i)
        res = 0
        seen = [False] * n
        seen[-1] = True
        q = [n - 1]
        while True:
            q2 = []
            for i in q:
                if i == 0:
                    return res
                if i > 0 and not seen[i - 1]:
                    seen[i - 1] = True
                    q2.append(i - 1)
                if i < n - 1 and not seen[i + 1]:
                    seen[i + 1] = True
                    q2.append(i + 1)
                for p in factors[nums[i]]:
                    for j in edges[p]:
                        if not seen[j]:
                            seen[j] = True
                            q2.append(j)
                    edges[p].clear()
            q = q2
            res += 1
```


#### Complexity Analysis

Let $\textit{MX}$ be the maximum value in the array, and let $n$ be the length of the array.

- Time complexity: $O(\textit{MX}\log \textit{MX}) + O(n \log \textit{MX})$.

    - The preprocessing step takes $O(\textit{MX}\log \textit{MX})$.
    - The BFS traversal takes $O(n \log \textit{MX})$, since each index and each prime factor group is processed at most once.

- Space complexity: $O(\textit{MX}\log \log \textit{MX})$.
  
  This is primarily used to store the prime factor table.

### Approach 2: Forward Breadth-First Search

#### Intuition

This approach tackles the problem using breadth-first search, but moving in the forward direction rather than backward.

Unlike Approach 1, which searches backward from index `n - 1` down to `0`, this approach starts at index `0` and progressively works its way toward `n - 1`. The direction flip changes how we think about the problem, previously our solution revolved around "what led us here?", and now we are asking "where can we go from here?"

When building the edges map, we group indices by their shared prime factors. This is the key insight that unlocks long-distance jumps. Two indices that share a prime factor can reach each other in a single step, even if they're far apart in the array. However, we only trigger these jumps when the current value is prime, which keeps the search from exploding into unnecessary branches.

The queue starts with just `[0]`, and we mark `seen[0]` as true to make sure we don't revisit the starting point. From there, BFS fans out level by level, exploring reachable indices in order of increasing distance. The moment we land on index `n - 1`, we stop and return the answer immediately rather than waiting for the full search to finish.

#### Implementation


```python
MX = 1_000_001
factors = [[] for _ in range(MX)]
for i in range(2, MX):
    if not factors[i]:
        for j in range(i, MX, i):
            factors[j].append(i)


class Solution:
    def minJumps(self, nums: List[int]) -> int:
        n = len(nums)
        edges = defaultdict(list)
        for i, a in enumerate(nums):
            for p in factors[a]:
                edges[p].append(i)
        res = 0
        seen = [False] * n
        seen[0] = True
        q = [0]
        while True:
            q2 = []
            for i in q:
                if i == n - 1:
                    return res
                if i > 0 and not seen[i - 1]:
                    seen[i - 1] = True
                    q2.append(i - 1)
                if i < n - 1 and not seen[i + 1]:
                    seen[i + 1] = True
                    q2.append(i + 1)
                if len(factors[nums[i]]) == 1:
                    p = nums[i]
                    for j in edges[p]:
                        if not seen[j]:
                            seen[j] = True
                            q2.append(j)
                    edges[p].clear()
            q = q2
            res += 1
```


#### Complexity Analysis

Let $\textit{MX}$ be the maximum value in the array, and let $n$ be the length of the array.

- Time complexity: $O(\textit{MX}\log \textit{MX}) + O(n \log \textit{MX})$

    - The preprocessing step takes $O(\textit{MX}\log \textit{MX})$.
    - The BFS traversal takes $O(n \log \textit{MX})$, since each index and each prime factor group is processed at most once.

- Space complexity: $O(\textit{MX}\log \log \textit{MX})$
  
  This is primarily used to store the prime factor table.

---