from bisect import bisect_right


def solve(arr: list[int], k: int) -> int:
    operations = 0

    for start in range(k):
        tails: list[int] = []
        length = 0

        for index in range(start, len(arr), k):
            value = arr[index]
            position = bisect_right(tails, value)
            if position == len(tails):
                tails.append(value)
            else:
                tails[position] = value
            length += 1

        operations += length - len(tails)

    return operations
