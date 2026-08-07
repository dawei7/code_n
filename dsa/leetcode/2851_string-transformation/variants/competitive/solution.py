class Solution:
    def numberOfWays(self, s: str, t: str, k: int) -> int:
        MODULUS = 1_000_000_007
        n = len(s)

        combined = t + "#" + s + s[:-1]
        prefix = [0] * len(combined)
        rotations = 0
        for index in range(1, len(combined)):
            matched = prefix[index - 1]
            while matched and combined[index] != combined[matched]:
                matched = prefix[matched - 1]
            if combined[index] == combined[matched]:
                matched += 1
            prefix[index] = matched
            if matched == n:
                rotations += 1

        power = pow(n - 1, k, MODULUS)
        sign = 1 if k % 2 == 0 else MODULUS - 1
        inverse_n = pow(n, MODULUS - 2, MODULUS)
        same = (power + (n - 1) * sign) % MODULUS * inverse_n % MODULUS
        different = (power - sign) % MODULUS * inverse_n % MODULUS

        answer = rotations * different
        if s == t:
            answer += same - different
        return answer % MODULUS
