class Solution:
    def sumOfNumbers(self, l: int, r: int, k: int) -> int:
        modulus = 1_000_000_007
        digit_count = r - l + 1
        digit_sum = (l + r) * digit_count // 2
        other_positions = pow(digit_count, k - 1, modulus)
        place_value_sum = (pow(10, k, modulus) - 1) * 111_111_112 % modulus

        return digit_sum * other_positions % modulus * place_value_sum % modulus
