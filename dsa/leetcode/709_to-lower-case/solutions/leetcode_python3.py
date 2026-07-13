class Solution:
    def toLowerCase(self, s: str) -> str:
        characters = []

        for character in s:
            if "A" <= character <= "Z":
                characters.append(chr(ord(character) + 32))
            else:
                characters.append(character)

        return "".join(characters)
