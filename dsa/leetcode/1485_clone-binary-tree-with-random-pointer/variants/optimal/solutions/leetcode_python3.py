class Solution:
    def copyRandomBinaryTree(
        self, root: "Optional[Node]"
    ) -> "Optional[NodeCopy]":
        if root is None:
            return None

        copies = {root: NodeCopy(root.val)}
        stack = [root]

        while stack:
            original = stack.pop()
            copied = copies[original]

            for attribute in ("left", "right", "random"):
                target = getattr(original, attribute)
                if target is None:
                    setattr(copied, attribute, None)
                    continue

                if target not in copies:
                    copies[target] = NodeCopy(target.val)
                    stack.append(target)

                setattr(copied, attribute, copies[target])

        return copies[root]
