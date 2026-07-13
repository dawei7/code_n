from collections import defaultdict


def solve(root):
    structure_ids = {}
    frequencies = defaultdict(int)
    duplicates = []

    def identify(node):
        if node is None:
            return 0
        key = (node.val, identify(node.left), identify(node.right))
        structure_id = structure_ids.setdefault(key, len(structure_ids) + 1)
        frequencies[structure_id] += 1
        if frequencies[structure_id] == 2:
            duplicates.append(node)
        return structure_id

    identify(root)
    return duplicates
