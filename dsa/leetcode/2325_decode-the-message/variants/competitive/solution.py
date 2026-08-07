from string import ascii_lowercase


class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        substitution = {" ": " "}
        next_letter = 0
        for character in key:
            if character not in substitution:
                substitution[character] = ascii_lowercase[next_letter]
                next_letter += 1

        return "".join(substitution[character] for character in message)
