class Solution:
    def superEggDrop(self, k: int, n: int) -> int:
        def covers(moves: int) -> bool:
            combinations = 1
            covered = 0
            for used_eggs in range(1, min(k, moves) + 1):
                combinations = (
                    combinations * (moves - used_eggs + 1) // used_eggs
                )
                covered += combinations
                if covered >= n:
                    return True
            return False

        low, high = 1, n
        while low < high:
            moves = (low + high) // 2
            if covers(moves):
                high = moves
            else:
                low = moves + 1
        return low
