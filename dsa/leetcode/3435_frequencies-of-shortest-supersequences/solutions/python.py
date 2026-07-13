from itertools import combinations


def solve(words):
    letters = sorted(set("".join(words)))
    index = {letter: pos for pos, letter in enumerate(letters)}
    m = len(letters)
    edges = [(index[word[0]], index[word[1]]) for word in words]

    def acyclic(duplicated: set[int]) -> bool:
        state = [0] * m

        def dfs(node: int) -> bool:
            state[node] = 1
            for source, target in edges:
                if source != node or target in duplicated:
                    continue
                if state[target] == 1:
                    return False
                if state[target] == 0 and not dfs(target):
                    return False
            state[node] = 2
            return True

        for node in range(m):
            if node in duplicated or state[node] != 0:
                continue
            if not dfs(node):
                return False
        return True

    answers = []
    for duplicate_count in range(m + 1):
        for combo in combinations(range(m), duplicate_count):
            duplicated = set(combo)
            if not acyclic(duplicated):
                continue
            freq = [0] * 26
            for letter, pos in index.items():
                freq[ord(letter) - ord("a")] = 2 if pos in duplicated else 1
            answers.append(freq)
        if answers:
            return answers

    return []
