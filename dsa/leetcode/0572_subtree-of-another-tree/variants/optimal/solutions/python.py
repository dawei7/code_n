"""Null-marked preorder KMP matching for LeetCode 572."""


def solve(root, sub_root) -> bool:
    def serialize(tree):
        tokens = []
        stack = [tree]

        while stack:
            node = stack.pop()
            if node is None:
                tokens.append((0, 0))
                continue
            tokens.append((1, node.val))
            stack.append(node.right)
            stack.append(node.left)

        return tokens

    pattern = serialize(sub_root)
    failure = [0] * len(pattern)

    for index in range(1, len(pattern)):
        matched = failure[index - 1]
        while matched and pattern[index] != pattern[matched]:
            matched = failure[matched - 1]
        if pattern[index] == pattern[matched]:
            matched += 1
        failure[index] = matched

    matched = 0
    for token in serialize(root):
        while matched and token != pattern[matched]:
            matched = failure[matched - 1]
        if token == pattern[matched]:
            matched += 1
            if matched == len(pattern):
                return True

    return False
