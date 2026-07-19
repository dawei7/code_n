class DistanceLimitedPathsExist:
    def __init__(self, n: int, edgeList: list[list[int]]):
        self.component = list(range(n))
        size = [1] * n

        def find(node: int) -> int:
            while node != self.component[node]:
                self.component[node] = self.component[self.component[node]]
                node = self.component[node]
            return node

        forest: list[list[tuple[int, int]]] = [[] for _ in range(n)]
        for first, second, weight in sorted(edgeList, key=lambda edge: edge[2]):
            root_first = find(first)
            root_second = find(second)
            if root_first == root_second:
                continue
            if size[root_first] < size[root_second]:
                root_first, root_second = root_second, root_first
            self.component[root_second] = root_first
            size[root_first] += size[root_second]
            forest[first].append((second, weight))
            forest[second].append((first, weight))

        for node in range(n):
            self.component[node] = find(node)

        levels = max(1, n.bit_length())
        self.depth = [-1] * n
        self.ancestor = [[0] * n for _ in range(levels)]
        self.maximum = [[0] * n for _ in range(levels)]

        for root in range(n):
            if self.depth[root] != -1:
                continue
            self.depth[root] = 0
            self.ancestor[0][root] = root
            stack = [root]
            while stack:
                node = stack.pop()
                for neighbor, weight in forest[node]:
                    if self.depth[neighbor] != -1:
                        continue
                    self.depth[neighbor] = self.depth[node] + 1
                    self.ancestor[0][neighbor] = node
                    self.maximum[0][neighbor] = weight
                    stack.append(neighbor)

        for level in range(1, levels):
            previous_ancestor = self.ancestor[level - 1]
            current_ancestor = self.ancestor[level]
            previous_maximum = self.maximum[level - 1]
            current_maximum = self.maximum[level]
            for node in range(n):
                middle = previous_ancestor[node]
                current_ancestor[node] = previous_ancestor[middle]
                current_maximum[node] = max(
                    previous_maximum[node],
                    previous_maximum[middle],
                )

    def query(self, p: int, q: int, limit: int) -> bool:
        if self.component[p] != self.component[q]:
            return False

        maximum_edge = 0
        if self.depth[p] < self.depth[q]:
            p, q = q, p

        difference = self.depth[p] - self.depth[q]
        for level in range(len(self.ancestor)):
            if difference & (1 << level):
                maximum_edge = max(maximum_edge, self.maximum[level][p])
                p = self.ancestor[level][p]

        if p == q:
            return maximum_edge < limit

        for level in range(len(self.ancestor) - 1, -1, -1):
            if self.ancestor[level][p] == self.ancestor[level][q]:
                continue
            maximum_edge = max(
                maximum_edge,
                self.maximum[level][p],
                self.maximum[level][q],
            )
            p = self.ancestor[level][p]
            q = self.ancestor[level][q]

        maximum_edge = max(
            maximum_edge,
            self.maximum[0][p],
            self.maximum[0][q],
        )
        return maximum_edge < limit


def solve(operations: list[str], arguments: list[list]) -> list[bool | None]:
    structure = None
    output: list[bool | None] = []
    for operation, values in zip(operations, arguments, strict=True):
        if operation == "DistanceLimitedPathsExist":
            structure = DistanceLimitedPathsExist(values[0], values[1])
            output.append(None)
            continue
        if structure is None:
            raise ValueError("DistanceLimitedPathsExist must be constructed first")
        output.append(structure.query(values[0], values[1], values[2]))
    return output
