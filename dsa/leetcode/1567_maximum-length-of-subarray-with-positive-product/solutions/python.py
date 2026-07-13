def solve(nums):
    positive = 0
    negative = 0
    best = 0
    for num in nums:
        if num == 0:
            positive = 0
            negative = 0
        elif num > 0:
            positive += 1
            negative = negative + 1 if negative else 0
        else:
            positive, negative = (negative + 1 if negative else 0), positive + 1
        best = max(best, positive)
    return best
