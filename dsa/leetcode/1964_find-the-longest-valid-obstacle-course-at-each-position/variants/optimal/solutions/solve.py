from bisect import bisect_right


def solve(obstacles: list[int]) -> list[int]:
    tails: list[int] = []
    answer: list[int] = []

    for height in obstacles:
        length = bisect_right(tails, height)
        answer.append(length + 1)

        if length == len(tails):
            tails.append(height)
        else:
            tails[length] = height

    return answer
