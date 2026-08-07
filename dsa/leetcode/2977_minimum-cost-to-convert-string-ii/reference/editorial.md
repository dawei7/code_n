### Approach: Trie + Floyd's Algorithm + Dynamic Programming

#### Intuition

We need to find the minimum cost to convert the string $\textit{source}$ into $\textit{target}$, allowing the string to be split into several parts of $\textit{source}$, each part undergoing several conversions, and finally concatenating to obtain $\textit{target}$.

Therefore, this suggests that we should use dynamic programming. Let $f[i]~(0 \leq i < n)$ represent the minimum cost to convert the prefix of $\textit{source}$ up to index $i$ into the corresponding part of $\textit{target}$, where $n$ is the length of the string $\textit{source}$. We have two state transitions:

- If $\textit{source}[i] = \textit{target}[i]$, then no conversion is needed, and we can directly have:

    $f[i] \leftarrow f[i - 1]$

- In addition, for the general case, we take any suffix of arbitrary length, denote $x = \textit{source}[j+1..i]$ (left-open, right-closed), and the minimum cost to convert $x$ into $y = \textit{target}[j+1..i]$ is $G(x, y)$. Then we have:

    $f[i] \leftarrow f[j] + G(x, y)$

When performing state transitions, we maintain the minimum value of $f[i]$, with the boundary condition $f[-1] = 0$, and the final answer is $f[n - 1]$.

Next, we need to consider how to quickly obtain $G(x, y)$, which can adopt the Floyd algorithm from [2976. Minimum Cost to Convert String I](https://leetcode.com/problems/minimum-cost-to-convert-string-i/):

- For each string in $\textit{original}$ and $\textit{changed}$, we assign a unique identifier, resulting in a total of $p~(1 \leq p \leq 2m)$ identifiers, where $m$ is the length of the array $\textit{original}$;

- We consider these $p$ strings as $p$ nodes on the graph $G$. For each triplet $(\textit{original}[i], \textit{changed}[i], \textit{cost}[i])$, we add an edge from $\textit{original}[i]$ to $\textit{changed}[i]$ in $G$ with the edge weight of $\textit{cost}[i]$;

- In this way, when we need to compute the minimum cost to transform $x = \textit{source}[j+1..i]$ (left-open, right-closed) into $y = \textit{target}[j+1..i]$, we first check if there are corresponding nodes for $x$ and $y$. If there are, the minimum cost is the shortest path between the corresponding nodes in the graph $G$.

When using a traditional hash table for assignment, considering that dynamic programming itself already has a time complexity of $O(n^2)$, a string-based hash table requires $O(n)$ time for each operation, leading to an overall time complexity of $O(n^3)$, which exceeds the time limit. There are two methods to optimize this:

- Use rolling hash with strings to compute the hash value of any substring in $O(1)$ time and obtain the corresponding number based on the hash value;

- Using a trie, when $i$ increases and $j$ remains unchanged in dynamic programming, the corresponding suffix gains one character each time, which exactly corresponds to traversing to child nodes in the trie. Thus, by first traversing $j$ and then $i$ in dynamic programming, we can move on the trie in $O(1)$ time and obtain the corresponding index.

The code corresponding to the second method is as follows.

#### Implementation

```python
INF = 10**18
INF_INT = 10**9

class Solution:
    def minimumCost(
        self,
        source: str,
        target: str,
        original: List[str],
        changed: List[str],
        cost: List[int],
    ) -> int:
        n = len(source)
        m = len(original)

        child = [[-1] * 26]
        tid = [-1]

        def new_node() -> int:
            child.append([-1] * 26)
            tid.append(-1)
            return len(child) - 1

        idx = -1

        def add(word: str) -> int:
            nonlocal idx
            node = 0
            for ch in word:
                c = ord(ch) - 97
                nxt = child[node][c]
                if nxt == -1:
                    nxt = new_node()
                    child[node][c] = nxt
                node = nxt
            if tid[node] == -1:
                idx += 1
                tid[node] = idx
            return tid[node]

        edges = []
        for i in range(m):
            x = add(original[i])
            y = add(changed[i])
            edges.append((x, y, cost[i]))

        P = idx + 1
        if P == 0:
            return 0 if source == target else -1

        dist = [[INF_INT] * P for _ in range(P)]
        for i in range(P):
            dist[i][i] = 0
        for x, y, w in edges:
            if w < dist[x][y]:
                dist[x][y] = w

        for k in range(P):
            dk = dist[k]
            for i in range(P):
                di = dist[i]
                dik = di[k]
                if dik == INF_INT:
                    continue
                base = dik
                for j in range(P):
                    nd = base + dk[j]
                    if nd < di[j]:
                        di[j] = nd

        dp = [INF] * (n + 1)
        dp[0] = 0

        s_arr = [ord(c) - 97 for c in source]
        t_arr = [ord(c) - 97 for c in target]

        for j in range(n):
            if dp[j] >= INF:
                continue

            base = dp[j]

            if source[j] == target[j] and base < dp[j + 1]:
                dp[j + 1] = base

            u = 0
            v = 0
            for i in range(j, n):
                u = child[u][s_arr[i]]
                v = child[v][t_arr[i]]
                if u == -1 or v == -1:
                    break
                uid = tid[u]
                vid = tid[v]
                if uid != -1 and vid != -1:
                    w = dist[uid][vid]
                    if w != INF_INT:
                        ni = i + 1
                        cand = base + w
                        if cand < dp[ni]:
                            dp[ni] = cand

        ans = dp[n]
        return -1 if ans >= INF else ans
```

#### Complexity Analysis

Let $n$ be the length of arrays $\textit{source}$ and $\textit{target}$, $m$ be the length of arrays $\textit{original}$, $\textit{changed}$, and $\textit{cost}$, and $L$ be the average length of the strings in arrays $\textit{original}$ and $\textit{changed}$.

- Time complexity: $O(n^2 + m^3 + mL)$.

  The time complexity of constructing the trie is $O(mL)$, the time complexity of computing the shortest path is $O(m^3)$, and the time complexity of dynamic programming is $O(n^2)$.

- Space complexity: $O(n + m^2 + mL)$.

  The space required for the trie is $O(mL)$, for the graph $G$ it is $O(m^2)$, and for dynamic programming it is $O(n)$.

---