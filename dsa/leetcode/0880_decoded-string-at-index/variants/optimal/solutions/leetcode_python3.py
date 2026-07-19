class Solution:
    def decodeAtIndex(self, s: str, k: int) -> str:
        decoded_length = 0
        final_index = 0

        for final_index, character in enumerate(s):
            if character.isdigit():
                decoded_length *= int(character)
            else:
                decoded_length += 1
            if decoded_length >= k:
                break

        for index in range(final_index, -1, -1):
            character = s[index]
            if character.isdigit():
                decoded_length //= int(character)
                k = (k - 1) % decoded_length + 1
            else:
                if k == decoded_length:
                    return character
                decoded_length -= 1

        raise AssertionError("the decoded tape must contain position k")
