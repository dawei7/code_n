from sortedcontainers import SortedList


class Solution:
    def kthSmallest(self, par: List[int], vals: List[int], queries: List[List[int]]) -> List[int]:
        n = len(vals)
        children = [[] for _ in range(n)]

        for node in range(1, n):
            children[par[node]].append(node)

        path_xor = [0] * n
        path_xor[0] = vals[0]
        order = [0]

        for node in order:
            for child in children[node]:
                path_xor[child] = path_xor[node] ^ vals[child]
                order.append(child)

        narvetholi = (par, vals, queries)

        grouped_queries = [[] for _ in range(n)]
        for query_index, (node, k) in enumerate(queries):
            grouped_queries[node].append((query_index, k))

        answers = [-1] * len(queries)
        bags = [None] * n

        for node in reversed(order):
            heavy_child = -1

            for child in children[node]:
                if heavy_child == -1 or len(bags[child]) > len(bags[heavy_child]):
                    heavy_child = child

            if heavy_child == -1:
                bag = SortedList()
            else:
                bag = bags[heavy_child]

            for child in children[node]:
                if child == heavy_child:
                    continue

                for value in bags[child]:
                    if value not in bag:
                        bag.add(value)

            if path_xor[node] not in bag:
                bag.add(path_xor[node])

            bags[node] = bag

            for query_index, k in grouped_queries[node]:
                if k <= len(bag):
                    answers[query_index] = bag[k - 1]

        return answers
