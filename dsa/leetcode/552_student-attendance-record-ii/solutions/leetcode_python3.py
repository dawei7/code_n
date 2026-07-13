class Solution:
    def checkRecord(self, n: int) -> int:
        modulus = 1_000_000_007
        states = [[1, 0, 0], [0, 0, 0]]

        for _ in range(n):
            next_states = [[0, 0, 0], [0, 0, 0]]

            for absences in range(2):
                for late_streak in range(3):
                    ways = states[absences][late_streak]

                    next_states[absences][0] = (
                        next_states[absences][0] + ways
                    ) % modulus

                    if absences == 0:
                        next_states[1][0] = (
                            next_states[1][0] + ways
                        ) % modulus

                    if late_streak < 2:
                        next_states[absences][late_streak + 1] = (
                            next_states[absences][late_streak + 1] + ways
                        ) % modulus

            states = next_states

        return sum(sum(row) for row in states) % modulus

