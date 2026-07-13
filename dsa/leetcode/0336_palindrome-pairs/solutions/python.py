def _palindrome_pairs(words: list[str]) -> list[list[int]]:
    index_by_word = {word: index for index, word in enumerate(words)}
    pairs: list[list[int]] = []

    for index, word in enumerate(words):
        for split in range(len(word) + 1):
            prefix = word[:split]
            suffix = word[split:]

            if prefix == prefix[::-1]:
                partner = index_by_word.get(suffix[::-1])
                if partner is not None and partner != index:
                    pairs.append([partner, index])

            if split < len(word) and suffix == suffix[::-1]:
                partner = index_by_word.get(prefix[::-1])
                if partner is not None and partner != index:
                    pairs.append([index, partner])

    return pairs


def solve(words: list[str]) -> list[list[int]]:
    return _palindrome_pairs(words)
