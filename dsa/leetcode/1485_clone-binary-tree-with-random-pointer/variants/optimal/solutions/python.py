def solve(nodes):
    return [
        None if entry is None else [entry[0], entry[1]]
        for entry in nodes
    ]
