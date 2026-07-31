class TreeAncestor:
    def __init__(self, n, parent):
        levels = max(1, n.bit_length())
        self.up = [list(parent)]

        for _ in range(1, levels):
            previous = self.up[-1]
            current = [-1 if ancestor == -1 else previous[ancestor] for ancestor in previous]
            self.up.append(current)

    def getKthAncestor(self, node, k):
        bit = 0

        while k and node != -1:
            if k & 1:
                node = self.up[bit][node]
            k >>= 1
            bit += 1

        return node


def solve(n, parent, operations):
    tree = TreeAncestor(n, parent)
    output = []

    for name, arguments in operations:
        if name == "getKthAncestor":
            output.append(tree.getKthAncestor(arguments[0], arguments[1]))

    return output
