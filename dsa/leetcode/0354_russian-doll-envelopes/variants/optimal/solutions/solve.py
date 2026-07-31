from bisect import bisect_left


def solve(envelopes: list[list[int]]) -> int:
    ordered = sorted(envelopes, key=lambda envelope: (envelope[0], -envelope[1]))
    tails: list[int] = []
    for _, height in ordered:
        position = bisect_left(tails, height)
        if position == len(tails):
            tails.append(height)
        else:
            tails[position] = height
    return len(tails)
