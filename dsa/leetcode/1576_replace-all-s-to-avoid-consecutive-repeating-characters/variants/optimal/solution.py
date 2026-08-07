class Solution:
    def modifyString(self, s: str) -> str:
        characters = list(s)

        for index, character in enumerate(characters):
            if character != "?":
                continue

            previous = characters[index - 1] if index > 0 else ""
            following = characters[index + 1] if index + 1 < len(characters) else ""
            for replacement in "abc":
                if replacement != previous and replacement != following:
                    characters[index] = replacement
                    break

        return "".join(characters)
