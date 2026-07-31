def solve(num: str) -> str:
    best = ""
    for index in range(len(num) - 2):
        if num[index] == num[index + 1] == num[index + 2] and num[index] > best:
            best = num[index]
    return best * 3
