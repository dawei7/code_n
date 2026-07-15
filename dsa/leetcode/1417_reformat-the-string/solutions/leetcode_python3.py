class Solution:
    def reformat(self, s: str) -> str:
        letters = [character for character in s if character.isalpha()]
        digits = [character for character in s if character.isdigit()]
        if abs(len(letters) - len(digits)) > 1:
            return ""
        if len(digits) >= len(letters):
            first, second = digits, letters
        else:
            first, second = letters, digits

        reformatted = []
        for index, character in enumerate(first):
            reformatted.append(character)
            if index < len(second):
                reformatted.append(second[index])
        return "".join(reformatted)
