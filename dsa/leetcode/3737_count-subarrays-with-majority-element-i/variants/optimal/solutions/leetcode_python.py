class Solution:
    def countMajoritySubarrays(self, nums: List[int], target: int) -> int:
        frequency = {0: 1}
        balance = 0
        smaller_prefixes = 0
        answer = 0

        for value in nums:
            if value == target:
                smaller_prefixes += frequency.get(balance, 0)
                balance += 1
            else:
                balance -= 1
                smaller_prefixes -= frequency.get(balance, 0)

            answer += smaller_prefixes
            frequency[balance] = frequency.get(balance, 0) + 1

        return answer
