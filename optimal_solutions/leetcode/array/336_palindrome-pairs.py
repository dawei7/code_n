def solve(words: list[str]) -> list[list[int]]:
    def is_palindrome(s: str) -> bool:
        return s == s[::-1]

    word_to_idx = {word: i for i, word in enumerate(words)}
    results = []

    for i, word in enumerate(words):
        n = len(word)
        # Check every possible split point in the word
        # We go up to n + 1 to handle empty string cases
        for j in range(n + 1):
            prefix = word[:j]
            suffix = word[j:]

            # Case 1: If prefix is a palindrome, we need the reverse of suffix
            # to be placed at the beginning.
            if is_palindrome(prefix):
                reversed_suffix = suffix[::-1]
                if reversed_suffix in word_to_idx and word_to_idx[reversed_suffix] != i:
                    results.append([word_to_idx[reversed_suffix], i])

            # Case 2: If suffix is a palindrome, we need the reverse of prefix
            # to be placed at the end.
            # j < n prevents double counting when suffix is empty (already handled in Case 1)
            if j < n and is_palindrome(suffix):
                reversed_prefix = prefix[::-1]
                if reversed_prefix in word_to_idx and word_to_idx[reversed_prefix] != i:
                    results.append([i, word_to_idx[reversed_prefix]])

    return results
