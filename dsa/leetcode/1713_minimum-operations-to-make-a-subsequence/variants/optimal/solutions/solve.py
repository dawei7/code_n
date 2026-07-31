from bisect import bisect_left


def solve(target: list[int], arr: list[int]) -> int:
    target_index = {value: index for index, value in enumerate(target)}
    tails: list[int] = []

    for value in arr:
        if value not in target_index:
            continue
        index = target_index[value]
        position = bisect_left(tails, index)
        if position == len(tails):
            tails.append(index)
        else:
            tails[position] = index

    return len(target) - len(tails)
