from bisect import bisect_left


class Solution:
    def closestNodes(self, root, queries):
        values = []
        stack = []
        node = root

        while node is not None or stack:
            while node is not None:
                stack.append(node)
                node = node.left
            node = stack.pop()
            values.append(node.val)
            node = node.right

        answer = []
        for query in queries:
            index = bisect_left(values, query)
            if index < len(values) and values[index] == query:
                answer.append([query, query])
            else:
                lower = values[index - 1] if index > 0 else -1
                upper = values[index] if index < len(values) else -1
                answer.append([lower, upper])

        return answer
