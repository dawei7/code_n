class Solution:
    def numberOfStableArrays(self, zero: int, one: int, limit: int) -> int:
        modulus = 1_000_000_007
        ending_zero = [[0] * (one + 1) for _ in range(zero + 1)]
        ending_one = [[0] * (one + 1) for _ in range(zero + 1)]

        for used_zero in range(1, min(zero, limit) + 1):
            ending_zero[used_zero][0] = 1
        for used_one in range(1, min(one, limit) + 1):
            ending_one[0][used_one] = 1

        for used_zero in range(1, zero + 1):
            for used_one in range(1, one + 1):
                value = ending_zero[used_zero - 1][used_one] + ending_one[used_zero - 1][used_one]
                if used_zero > limit:
                    value -= ending_one[used_zero - limit - 1][used_one]
                ending_zero[used_zero][used_one] = value % modulus

                value = ending_zero[used_zero][used_one - 1] + ending_one[used_zero][used_one - 1]
                if used_one > limit:
                    value -= ending_zero[used_zero][used_one - limit - 1]
                ending_one[used_zero][used_one] = value % modulus

        return (ending_zero[zero][one] + ending_one[zero][one]) % modulus
