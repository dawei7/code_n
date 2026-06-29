


def solve():
    class Codechef:

        adj = [[] for _ in range(100001)]

        @staticmethod
        def dfs(node, parent, d, maxd):
            maxd[0] = max(d, maxd[0])
            for v in Codechef.adj[node]:
                if v != parent:
                    Codechef.dfs(v, node, d + 1, maxd)

        @staticmethod
        def main():
            import sys
            input = sys.stdin.read
            data = input().split()

            index = 0
            n = int(data[index])
            index += 1

            for i in range(1, n):
                u = int(data[index])
                v = int(data[index + 1])
                Codechef.adj[u].append(v)
                Codechef.adj[v].append(u)
                index += 2

            maxd = [0]
            Codechef.dfs(1, -1, 0, maxd)
            print(maxd[0])

    if __name__ == "__main__":
        Codechef.main()


if __name__ == "__main__":
    solve()
