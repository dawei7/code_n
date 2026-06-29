import heapq
import sys


class DSU:
    def __init__(self, values: list[int]) -> None:
        self.parent = list(range(len(values)))
        self.size = [1] * len(values)
        self.total = values[:]
        self.heap = [(-value, i) for i, value in enumerate(values) if i]
        heapq.heapify(self.heap)

    def find(self, node: int) -> int:
        while self.parent[node] != node:
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node

    def push(self, root: int) -> None:
        heapq.heappush(self.heap, (-self.total[root], root))

    def union(self, a: int, b: int) -> None:
        ra, rb = self.find(a), self.find(b)
        if ra == rb:
            return
        if self.size[ra] < self.size[rb]:
            ra, rb = rb, ra
        self.parent[rb] = ra
        self.size[ra] += self.size[rb]
        self.total[ra] += self.total[rb]
        self.push(ra)

    def change_city(self, city: int, delta: int) -> None:
        root = self.find(city)
        self.total[root] += delta
        self.push(root)

    def max_total(self) -> int:
        while self.heap:
            neg, root = self.heap[0]
            if self.find(root) == root and -neg == self.total[root]:
                return -neg
            heapq.heappop(self.heap)
        return 0


def main() -> None:
    raw = sys.stdin.buffer.read().split()
    if not raw:
        return
    n, m, q = map(int, raw[:3])
    idx = 3
    initial = [0] + list(map(int, raw[idx:idx + n]))
    idx += n
    edges = [None]
    for _ in range(m):
        u, v = int(raw[idx]), int(raw[idx + 1])
        idx += 2
        edges.append((u, v))

    current = initial[:]
    destroyed = [False] * (m + 1)
    queries = []
    for _ in range(q):
        typ = raw[idx].decode()
        idx += 1
        if typ == "D":
            road = int(raw[idx])
            idx += 1
            destroyed[road] = True
            queries.append(("D", road))
        else:
            city = int(raw[idx])
            new_value = int(raw[idx + 1])
            idx += 2
            old_value = current[city]
            current[city] = new_value
            queries.append(("P", city, old_value, new_value))

    dsu = DSU(current)
    for road in range(1, m + 1):
        if not destroyed[road]:
            u, v = edges[road]
            dsu.union(u, v)

    ans = [0] * q
    for i in range(q - 1, -1, -1):
        ans[i] = dsu.max_total()
        query = queries[i]
        if query[0] == "D":
            u, v = edges[query[1]]
            dsu.union(u, v)
        else:
            _, city, old_value, new_value = query
            dsu.change_city(city, old_value - new_value)

    sys.stdout.write("\n".join(map(str, ans)))


if __name__ == "__main__":
    main()
