class Solution:
    def concatHex36(self, n: int) -> str:
        digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

        def convert(value: int, base: int) -> str:
            encoded = []
            while value:
                value, remainder = divmod(value, base)
                encoded.append(digits[remainder])
            return "".join(reversed(encoded)) or "0"

        square = n * n
        return convert(square, 16) + convert(square * n, 36)
