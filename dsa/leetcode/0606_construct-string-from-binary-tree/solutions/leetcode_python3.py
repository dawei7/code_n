class Solution:
    def tree2str(self, root: 'TreeNode') -> str:
        if root is None:
            return ""

        tokens = []
        actions = [("node", root)]

        while actions:
            action, value = actions.pop()
            if action == "text":
                tokens.append(value)
                continue

            node = value
            tokens.append(str(node.val))

            if node.right is not None:
                actions.append(("text", ")"))
                actions.append(("node", node.right))
                actions.append(("text", "("))

                actions.append(("text", ")"))
                if node.left is not None:
                    actions.append(("node", node.left))
                actions.append(("text", "("))
            elif node.left is not None:
                actions.append(("text", ")"))
                actions.append(("node", node.left))
                actions.append(("text", "("))

        return "".join(tokens)

