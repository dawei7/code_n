


def solve():
    class Codechef:

        adj = [[] for _ in range(100001)]
        nodes_at_level_k = []

        @staticmethod
        def dfs(u, parent, k, level):
            if level == k:
                Codechef.nodes_at_level_k.append(u)
            for v in Codechef.adj[u]:
                if v != parent:
                    Codechef.dfs(v, u, k, level + 1)

        @staticmethod
        def main():
            import sys
            input = sys.stdin.read
            data = input().split()

            index = 0
            n = int(data[index])
            k = int(data[index + 1])
            index += 2

            if k < 0 or k >= n:
                print(f"Invalid value for k: {k}", file=sys.stderr)
                return

            # Initialize adjacency list
            for i in range(1, n):
                u = int(data[index])
                v = int(data[index + 1])
                if u >= len(Codechef.adj) or v >= len(Codechef.adj):
                    print(f"Node index out of bounds: u = {u}, v = {v}", file=sys.stderr)
                    return
                Codechef.adj[u].append(v)
                Codechef.adj[v].append(u)
                index += 2

            Codechef.dfs(1, 0, k, 0)
            Codechef.nodes_at_level_k.sort()

            print(' '.join(map(str, Codechef.nodes_at_level_k)))

    if __name__ == "__main__":
        Codechef.main()


if __name__ == "__main__":
    solve()
