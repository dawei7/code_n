class Codechef:

    def __init__(self, n):
        self.n = n
        self.adjMatrix = [[0] * n for _ in range(n)]

    def add_edge(self, u, v):
        self.adjMatrix[u][v] = 1

    def print_adj_matrix(self):
        for row in self.adjMatrix:
            print(' '.join(map(str, row)))

def solve():
    n = int(input())
    graph = Codechef(n)
    for _ in range(n - 1):
        u, v = map(int, input().split())
        graph.add_edge(u, v)
    graph.print_adj_matrix()


if __name__ == "__main__":
    solve()
