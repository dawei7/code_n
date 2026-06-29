import sys


def solve():
    sys.setrecursionlimit(10**7)
    input = sys.stdin.readline

    MOD = 10**9 + 7

    T = int(input())
    for _ in range(T):
        N, M = map(int, input().split())

        graph = [[] for _ in range(N + 1)]
        visited = [False] * (N + 1)

        for _ in range(M):
            u, v = map(int, input().split())
            graph[u].append(v)
            graph[v].append(u)

        components = 0
        ways = 1

        for i in range(1, N + 1):
            if not visited[i]:
                components += 1
                stack = [i]
                visited[i] = True
                size = 1

                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if not visited[nei]:
                            visited[nei] = True
                            stack.append(nei)
                            size += 1

                ways = (ways * size) % MOD

        print(components, ways)


if __name__ == "__main__":
    solve()
