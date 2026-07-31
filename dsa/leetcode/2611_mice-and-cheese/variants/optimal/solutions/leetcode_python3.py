class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        gains = [first - second for first, second in zip(reward1, reward2)]
        gains.sort(reverse=True)
        return sum(reward2) + sum(gains[:k])
