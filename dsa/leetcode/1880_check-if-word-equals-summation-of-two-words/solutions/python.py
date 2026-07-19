def solve(firstWord: str, secondWord: str, targetWord: str) -> bool:
    def numerical_value(word: str) -> int:
        value = 0
        for character in word:
            value = value * 10 + ord(character) - ord("a")
        return value

    return (
        numerical_value(firstWord) + numerical_value(secondWord)
        == numerical_value(targetWord)
    )
