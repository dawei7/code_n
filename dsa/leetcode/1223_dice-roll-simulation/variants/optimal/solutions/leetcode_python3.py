from typing import List


class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        modulus = 1_000_000_007
        states = [[0] * (rollMax[face] + 1) for face in range(6)]
        for face in range(6):
            states[face][1] = 1

        for _ in range(1, n):
            next_states = [[0] * (rollMax[face] + 1) for face in range(6)]
            face_totals = [sum(row) % modulus for row in states]
            all_total = sum(face_totals) % modulus
            for face in range(6):
                next_states[face][1] = (all_total - face_totals[face]) % modulus
                for run_length in range(1, rollMax[face]):
                    next_states[face][run_length + 1] = states[face][run_length]
            states = next_states

        return sum(sum(row) for row in states) % modulus
