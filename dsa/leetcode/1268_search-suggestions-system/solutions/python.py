class _TrieNode:
    __slots__ = ("children", "product", "suggestions")

    def __init__(self):
        self.children = {}
        self.product = None
        self.suggestions = []


def solve(products, search_word):
    nodes = [_TrieNode()]

    for product in products:
        node_index = 0
        for character in product:
            child_index = nodes[node_index].children.get(character)
            if child_index is None:
                child_index = len(nodes)
                nodes[node_index].children[character] = child_index
                nodes.append(_TrieNode())
            node_index = child_index
        nodes[node_index].product = product

    path = []
    stack = [(0, False)]
    while stack:
        node_index, exiting = stack.pop()
        if exiting:
            path.pop()
            continue

        path.append(node_index)
        node = nodes[node_index]
        if node.product is not None:
            for prefix_index in path[1:]:
                suggestions = nodes[prefix_index].suggestions
                if len(suggestions) < 3:
                    suggestions.append(node.product)

        stack.append((node_index, True))
        for character in sorted(node.children, reverse=True):
            stack.append((node.children[character], False))

    answer = []
    node_index = 0
    missing = False
    for character in search_word:
        if not missing:
            child_index = nodes[node_index].children.get(character)
            if child_index is None:
                missing = True
            else:
                node_index = child_index
        answer.append([] if missing else list(nodes[node_index].suggestions))
    return answer
