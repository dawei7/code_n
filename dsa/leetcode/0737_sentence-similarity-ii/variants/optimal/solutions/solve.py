def solve(
    sentence1: list[str],
    sentence2: list[str],
    similarPairs: list[list[str]],
) -> bool:
    if len(sentence1) != len(sentence2):
        return False

    parent = {}
    size = {}

    def add(word):
        if word not in parent:
            parent[word] = word
            size[word] = 1

    def find(word):
        root = word
        while parent[root] != root:
            root = parent[root]
        while word != root:
            parent_word = parent[word]
            parent[word] = root
            word = parent_word
        return root

    for left, right in similarPairs:
        add(left)
        add(right)
        left_root = find(left)
        right_root = find(right)
        if left_root == right_root:
            continue
        if size[left_root] < size[right_root]:
            left_root, right_root = right_root, left_root
        parent[right_root] = left_root
        size[left_root] += size[right_root]

    for first, second in zip(sentence1, sentence2):
        if first == second:
            continue
        if first not in parent or second not in parent or find(first) != find(second):
            return False
    return True
