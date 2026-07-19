from typing import List


class Solution:
    def isSolvable(self, words: List[str], result: str) -> bool:
        addends = list(words)
        max_length = max(map(len, addends + [result]))
        leading = {word[0] for word in addends + [result] if len(word) > 1}
        coefficients = {}
        for word in addends:
            for place, letter in enumerate(reversed(word)):
                coefficients[letter] = coefficients.get(letter, 0) + 10**place
        for place, letter in enumerate(reversed(result)):
            coefficients[letter] = coefficients.get(letter, 0) - 10**place
        assignment = {}
        used = [False] * 10

        if len(result) < max(map(len, addends)):
            return False
        if len(set("".join(addends) + result)) > 10:
            return False

        def search(column: int, row: int, total: int) -> bool:
            if column == max_length:
                return total == 0

            if row < len(addends):
                word = addends[row]
                if column >= len(word):
                    return search(column, row + 1, total)

                letter = word[-1 - column]
                if letter in assignment:
                    return search(column, row + 1, total + assignment[letter])

                digits = (
                    range(9, -1, -1)
                    if len(addends) == 2 and coefficients[letter] > 0
                    else range(10)
                )
                for digit in digits:
                    if used[digit] or (digit == 0 and letter in leading):
                        continue
                    assignment[letter] = digit
                    used[digit] = True
                    if search(column, row + 1, total + digit):
                        return True
                    used[digit] = False
                    del assignment[letter]
                return False

            letter = result[-1 - column] if column < len(result) else None
            digit = total % 10
            carry = total // 10

            if letter is None:
                return digit == 0 and search(column + 1, 0, carry)
            if letter in assignment:
                return assignment[letter] == digit and search(column + 1, 0, carry)
            if used[digit] or (digit == 0 and letter in leading):
                return False

            assignment[letter] = digit
            used[digit] = True
            if search(column + 1, 0, carry):
                return True
            used[digit] = False
            del assignment[letter]
            return False

        return search(0, 0, 0)
