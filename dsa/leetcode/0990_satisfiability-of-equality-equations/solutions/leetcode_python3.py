class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        parent = list(range(26))
        size = [1] * 26

        def find(node):
            while node != parent[node]:
                parent[node] = parent[parent[node]]
                node = parent[node]
            return node

        for equation in equations:
            if equation[1] != "=":
                continue
            left = find(ord(equation[0]) - ord("a"))
            right = find(ord(equation[3]) - ord("a"))
            if left == right:
                continue
            if size[left] < size[right]:
                left, right = right, left
            parent[right] = left
            size[left] += size[right]

        for equation in equations:
            if equation[1] == "!":
                left = find(ord(equation[0]) - ord("a"))
                right = find(ord(equation[3]) - ord("a"))
                if left == right:
                    return False

        return True
