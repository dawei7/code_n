class Solution:
    def racecar(self, target: int) -> int:
        dp = [0] * (target + 1)

        for distance in range(1, target + 1):
            accelerations = distance.bit_length()
            overshoot_position = (1 << accelerations) - 1

            if overshoot_position == distance:
                dp[distance] = accelerations
                continue

            best = accelerations + 1 + dp[overshoot_position - distance]
            forward_position = (1 << (accelerations - 1)) - 1

            for backward_accelerations in range(accelerations - 1):
                backward_distance = (1 << backward_accelerations) - 1
                remaining = distance - forward_position + backward_distance
                candidate = (
                    accelerations
                    + backward_accelerations
                    + 1
                    + dp[remaining]
                )
                best = min(best, candidate)

            dp[distance] = best

        return dp[target]
