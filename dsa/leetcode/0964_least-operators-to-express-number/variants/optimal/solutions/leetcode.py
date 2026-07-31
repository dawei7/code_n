class Solution:
    def leastOpsExpressTarget(self, x: int, target: int) -> int:
        positive = negative = 0
        position = 0

        while target:
            target, digit = divmod(target, x)
            if position == 0:
                positive = digit * 2
                negative = (x - digit) * 2
            else:
                next_positive = min(
                    positive + digit * position,
                    negative + (digit + 1) * position,
                )
                next_negative = min(
                    positive + (x - digit) * position,
                    negative + (x - digit - 1) * position,
                )
                positive, negative = next_positive, next_negative
            position += 1

        return min(positive, negative + position) - 1
