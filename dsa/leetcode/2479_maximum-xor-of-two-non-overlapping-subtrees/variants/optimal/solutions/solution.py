from typing import List


class Solution:
    def maxXor(self, n: int, edges: List[List[int]], values: List[int]) -> int:
        graph = [[] for _ in range(n)]
        for node_a, node_b in edges:
            graph[node_a].append(node_b)
            graph[node_b].append(node_a)

        parent = [-1] * n
        order = [0]
        for node in order:
            for neighbor in graph[node]:
                if neighbor == parent[node]:
                    continue
                parent[neighbor] = node
                order.append(neighbor)

        subtree_sum = values[:]
        for node in reversed(order[1:]):
            subtree_sum[parent[node]] += subtree_sum[node]

        highest_bit = max(subtree_sum).bit_length() - 1
        trie = [[-1, -1]]

        def insert(value: int) -> None:
            trie_node = 0
            for bit in range(highest_bit, -1, -1):
                digit = (value >> bit) & 1
                if trie[trie_node][digit] == -1:
                    trie[trie_node][digit] = len(trie)
                    trie.append([-1, -1])
                trie_node = trie[trie_node][digit]

        def maximum_xor(value: int) -> int:
            trie_node = 0
            score = 0
            for bit in range(highest_bit, -1, -1):
                digit = (value >> bit) & 1
                opposite = digit ^ 1
                if trie[trie_node][opposite] != -1:
                    score |= 1 << bit
                    trie_node = trie[trie_node][opposite]
                else:
                    trie_node = trie[trie_node][digit]
            return score

        answer = 0
        has_completed_subtree = False
        stack = [(0, False)]

        while stack:
            node, exiting = stack.pop()
            if exiting:
                insert(subtree_sum[node])
                has_completed_subtree = True
                continue

            if has_completed_subtree:
                answer = max(answer, maximum_xor(subtree_sum[node]))

            stack.append((node, True))
            for neighbor in reversed(graph[node]):
                if neighbor != parent[node]:
                    stack.append((neighbor, False))

        return answer
