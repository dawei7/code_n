class Solution:
    def reformatNumber(self, number: str) -> str:
        digits = "".join(character for character in number if character.isdigit())
        blocks = []
        index = 0

        while len(digits) - index > 4:
            blocks.append(digits[index : index + 3])
            index += 3

        remaining = len(digits) - index
        if remaining == 4:
            blocks.append(digits[index : index + 2])
            blocks.append(digits[index + 2 :])
        else:
            blocks.append(digits[index:])

        return "-".join(blocks)
