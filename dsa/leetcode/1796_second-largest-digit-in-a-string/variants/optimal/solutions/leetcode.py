class Solution:
    def secondHighest(self, s: str) -> int:
        largest = -1
        second_largest = -1

        for character in s:
            if "0" <= character <= "9":
                digit = ord(character) - ord("0")
                if digit > largest:
                    second_largest = largest
                    largest = digit
                elif second_largest < digit < largest:
                    second_largest = digit

        return second_largest
