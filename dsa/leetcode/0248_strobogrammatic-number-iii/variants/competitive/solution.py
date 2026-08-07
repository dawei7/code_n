class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        pairs = (("0", "0"), ("1", "1"), ("6", "9"), ("8", "8"), ("9", "6"))
        total = 0

        for length in range(len(low), len(high) + 1):
            digits = [""] * length

            def search(left: int, right: int) -> None:
                nonlocal total
                if left > right:
                    value = "".join(digits)
                    if length == len(low) and value < low:
                        return
                    if length == len(high) and value > high:
                        return
                    total += 1
                    return
                for first, second in pairs:
                    if left == 0 and length > 1 and first == "0":
                        continue
                    if left == right and first != second:
                        continue
                    digits[left], digits[right] = first, second
                    search(left + 1, right - 1)

            search(0, length - 1)
        return total
