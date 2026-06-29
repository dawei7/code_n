from collections import defaultdict


def solve():
    def countPairs(vedaN):
        vedaPairs = vedaN * (vedaN - 1) // 2
        return vedaPairs

    vedaT = int(input())
    for _ in range(vedaT):
        vedaN = int(input())
        vedaFrequency = defaultdict(int)
        for vedaNum in map(int, input().split()):
            vedaFrequency[vedaNum] += 1

        vedaTotalPairs = countPairs(vedaN)
        for vedaNum, vedaFreq in vedaFrequency.items():
            vedaPairsWithNum = countPairs(vedaFreq)
            vedaTotalPairs -= vedaPairsWithNum

        print(vedaTotalPairs)


if __name__ == "__main__":
    solve()
