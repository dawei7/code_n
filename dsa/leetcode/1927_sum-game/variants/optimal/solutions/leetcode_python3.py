class Solution:
    def sumGame(self, num: str) -> bool:
        half = len(num) // 2
        left_sum = 0
        right_sum = 0
        left_unknown = 0
        right_unknown = 0

        for index, character in enumerate(num):
            if character == "?":
                if index < half:
                    left_unknown += 1
                else:
                    right_unknown += 1
            elif index < half:
                left_sum += int(character)
            else:
                right_sum += int(character)

        total_unknown = left_unknown + right_unknown
        if total_unknown % 2 == 1:
            return True

        balance = 2 * (left_sum - right_sum) + 9 * (
            left_unknown - right_unknown
        )
        return balance != 0
