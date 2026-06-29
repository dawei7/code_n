import sys
from itertools import permutations

def permuteUnique(nums):
    result = []
    nums.sort()
    used = [False] * len(nums)
    path = []

    def backtrack():
        if len(path) == len(nums):
            result.append(list(path))
            return
        for i in range(len(nums)):
            if used[i] or (i > 0 and nums[i] == nums[i - 1] and (not used[i - 1])):
                continue
            path.append(nums[i])
            used[i] = True
            backtrack()
            used[i] = False
            path.pop()
    backtrack()
    return result

def solve():
    input_lines = sys.stdin.read().strip().split('\n')
    index = 0
    t = int(input_lines[index].strip())
    index += 1
    while t > 0:
        t -= 1
        n = int(input_lines[index].strip())
        index += 1
        arr = list(map(int, input_lines[index].strip().split()))
        index += 1
        permutations = permuteUnique(arr)
        print(len(permutations))
        for p in permutations:
            print(' '.join(map(str, p)))


if __name__ == "__main__":
    solve()
