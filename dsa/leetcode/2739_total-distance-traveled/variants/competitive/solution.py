class Solution:
    def distanceTraveled(self, mainTank: int, additionalTank: int) -> int:
        transfers = min(additionalTank, (mainTank - 1) // 4)
        return 10 * (mainTank + transfers)
