class Solution:
    def sumOfPower(self, nums: List[int]) -> int:
        modulus = 1_000_000_007
        nums.sort()

        answer = 0
        weighted_minima = 0
        for strength in nums:
            answer = (answer + strength * strength * (strength + weighted_minima)) % modulus
            weighted_minima = (2 * weighted_minima + strength) % modulus
        return answer
