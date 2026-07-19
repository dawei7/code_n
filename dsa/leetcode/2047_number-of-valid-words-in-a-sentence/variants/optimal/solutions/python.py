def solve(sentence: str) -> int:
    def valid(token: str) -> bool:
        hyphens = 0
        punctuation = 0

        for index, character in enumerate(token):
            if character.isdigit():
                return False

            if character == "-":
                hyphens += 1
                if (
                    hyphens > 1
                    or index == 0
                    or index == len(token) - 1
                    or not token[index - 1].islower()
                    or not token[index + 1].islower()
                ):
                    return False
            elif character in "!.,":
                punctuation += 1
                if punctuation > 1 or index != len(token) - 1:
                    return False

        return True

    return sum(valid(token) for token in sentence.split())
