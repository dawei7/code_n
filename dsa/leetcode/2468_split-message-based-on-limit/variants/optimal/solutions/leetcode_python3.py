from typing import List


class Solution:
    def splitMessage(self, message: str, limit: int) -> List[str]:
        digit_sum = 0

        for parts in range(1, len(message) + 1):
            digit_sum += len(str(parts))
            denominator_digits = len(str(parts))

            if limit <= 2 * denominator_digits + 3:
                continue

            capacity = (
                parts * (limit - denominator_digits - 3) - digit_sum
            )
            if capacity < len(message):
                continue

            answer = []
            start = 0
            for index in range(1, parts + 1):
                suffix = f"<{index}/{parts}>"
                payload_length = limit - len(suffix)
                answer.append(
                    message[start : start + payload_length] + suffix
                )
                start += payload_length
            return answer

        return []
