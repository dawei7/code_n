


def solve():
    class Solution:
        def getLetterCombinations(self, inputDigits: str):
            if not inputDigits:
                return []

            keypad = {
                '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
                '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
            }

            result = []
            current = []

            def backtrack(index):
                if index == len(inputDigits):
                    result.append("".join(current))
                    return

                for ch in keypad[inputDigits[index]]:
                    current.append(ch)
                    backtrack(index + 1)
                    current.pop()

            backtrack(0)
            return result


if __name__ == "__main__":
    solve()
