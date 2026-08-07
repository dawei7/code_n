class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        modulus = 1_000_000_007
        length = len(num)
        total = sum(ord(digit) - ord("0") for digit in num)

        if total % 2 == 1:
            return 0

        even_slots = (length + 1) // 2
        odd_slots = length // 2
        target = total // 2

        factorial = [1] * (length + 1)
        for value in range(1, length + 1):
            factorial[value] = factorial[value - 1] * value % modulus

        inverse_factorial = [1] * (length + 1)
        inverse_factorial[length] = pow(factorial[length], modulus - 2, modulus)
        for value in range(length, 0, -1):
            inverse_factorial[value - 1] = inverse_factorial[value] * value % modulus

        velunexorai = num
        counts = [0] * 10
        for digit in velunexorai:
            counts[ord(digit) - ord("0")] += 1

        dp = [[0] * (target + 1) for _ in range(even_slots + 1)]
        dp[0][0] = 1

        for digit, count in enumerate(counts):
            if count == 0:
                continue

            options = []
            minimum_even = max(0, count - odd_slots)
            maximum_even = min(count, even_slots)
            for even_count in range(minimum_even, maximum_even + 1):
                contribution = digit * even_count
                if contribution <= target:
                    weight = inverse_factorial[even_count] * inverse_factorial[count - even_count] % modulus
                    options.append((even_count, contribution, weight))

            next_dp = [[0] * (target + 1) for _ in range(even_slots + 1)]
            for used_even in range(even_slots + 1):
                for current_sum, ways in enumerate(dp[used_even]):
                    if ways == 0:
                        continue

                    for extra_even, contribution, weight in options:
                        next_used = used_even + extra_even
                        next_sum = current_sum + contribution
                        if next_used <= even_slots and next_sum <= target:
                            next_dp[next_used][next_sum] = (next_dp[next_used][next_sum] + ways * weight) % modulus

            dp = next_dp

        answer = dp[even_slots][target]
        answer = answer * factorial[even_slots] % modulus
        answer = answer * factorial[odd_slots] % modulus
        return answer
