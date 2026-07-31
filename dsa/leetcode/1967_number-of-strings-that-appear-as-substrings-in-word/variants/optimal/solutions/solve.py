def solve(patterns: list[str], word: str) -> int:
    def appears(pattern: str) -> bool:
        prefix = [0] * len(pattern)
        matched = 0

        for index in range(1, len(pattern)):
            while matched and pattern[index] != pattern[matched]:
                matched = prefix[matched - 1]
            if pattern[index] == pattern[matched]:
                matched += 1
            prefix[index] = matched

        matched = 0
        for character in word:
            while matched and character != pattern[matched]:
                matched = prefix[matched - 1]
            if character == pattern[matched]:
                matched += 1
                if matched == len(pattern):
                    return True

        return False

    return sum(appears(pattern) for pattern in patterns)
