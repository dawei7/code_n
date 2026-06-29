


def solve():
    def reconstruct(traversal: list):
        n = len(traversal)
        nodes = [Node(val) for val in traversal]
        for i in range(n):
            left_index = 2 * i + 1
            right_index = 2 * i + 2
            if left_index < n:
                nodes[i].left = nodes[left_index]
            if right_index < n:
                nodes[i].right = nodes[right_index]
        return nodes[0]


if __name__ == "__main__":
    solve()
