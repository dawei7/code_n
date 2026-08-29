from typing import List


class Solution:
    def shortestDistanceAfterQueries(
        self, n: int, queries: List[List[int]]
    ) -> List[int]:
        parent = list(range(n + 1))

        def find(i: int) -> int:
            path = []
            while parent[i] != i:
                path.append(i)
                i = parent[i]
            for node in path:
                parent[node] = i
            return i

        ans = []
        cnt = n - 1
        for u, v in queries:
            k = find(u + 1)
            target = find(v)
            while k < v:
                cnt -= 1
                parent[k] = target
                k = find(k + 1)
            ans.append(cnt)
        return ans
