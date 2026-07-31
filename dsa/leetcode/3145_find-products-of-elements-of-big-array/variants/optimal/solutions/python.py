def solve(queries: list[list[int]]) -> list[int]:
    def statistics(number: int) -> tuple[int, int]:
        total_bits = 0
        exponent_sum = 0
        total_numbers = number + 1

        for bit in range(number.bit_length()):
            half = 1 << bit
            period = half << 1
            ones = (total_numbers // period) * half
            ones += max(0, total_numbers % period - half)
            total_bits += ones
            exponent_sum += ones * bit

        return total_bits, exponent_sum

    def prefix_exponent(length: int) -> int:
        if length == 0:
            return 0

        low, high = 1, length
        while low < high:
            middle = (low + high) // 2
            if statistics(middle)[0] >= length:
                high = middle
            else:
                low = middle + 1

        number = low
        used, exponent_sum = statistics(number - 1)
        remaining = length - used

        for bit in range(number.bit_length()):
            if number & (1 << bit):
                if remaining == 0:
                    break
                exponent_sum += bit
                remaining -= 1

        return exponent_sum

    answer = []
    for start, end, modulus in queries:
        exponent = prefix_exponent(end + 1) - prefix_exponent(start)
        answer.append(pow(2, exponent, modulus))

    return answer
