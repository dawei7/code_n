class Solution:
    def findWinningPlayer(self, skills: List[int], k: int) -> int:
        champion = 0
        consecutive_wins = 0

        for challenger in range(1, len(skills)):
            if skills[champion] > skills[challenger]:
                consecutive_wins += 1
            else:
                champion = challenger
                consecutive_wins = 1

            if consecutive_wins >= k:
                return champion

        return champion
