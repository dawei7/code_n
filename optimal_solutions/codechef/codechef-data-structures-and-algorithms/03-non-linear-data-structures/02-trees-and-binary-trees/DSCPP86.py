


def solve():
    class Codechef:

        leaves = 0

        @staticmethod
        def dfs(vertex, adj_matrix):
            child_present = False
            # Traversing through children of vertex through this for loop
            for i in range(len(adj_matrix)):
                if adj_matrix[vertex][i] == 1:
                    child_present = True
                    Codechef.dfs(i, adj_matrix)
            # Using the logic that a leaf node does not have any children
            if not child_present:
                Codechef.leaves += 1

        @staticmethod
        def main():
            import sys
            input = sys.stdin.read
            data = input().split()

            index = 0
            N = int(data[index])
            index += 1

            adj_matrix = [[0] * N for _ in range(N)]

            for _ in range(N - 1):
                a = int(data[index])
                b = int(data[index + 1])
                adj_matrix[a][b] = 1
                index += 2

            Codechef.dfs(0, adj_matrix)
            print(Codechef.leaves)

    if __name__ == "__main__":
        Codechef.main()


if __name__ == "__main__":
    solve()
