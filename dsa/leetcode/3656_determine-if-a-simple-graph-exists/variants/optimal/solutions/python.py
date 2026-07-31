from bisect import bisect_right


def solve(degrees: list[int]) -> bool:
    degrees.sort(reverse=True)
    total = sum(degrees)
    if total % 2:
        return False

    prefix = [0]
    for degree in degrees:
        prefix.append(prefix[-1] + degree)

    negated = [-degree for degree in degrees]
    n = len(degrees)

    for count in range(1, n + 1):
        split = bisect_right(negated, -count, lo=count)
        available = (
            count * (count - 1)
            + (split - count) * count
            + prefix[n]
            - prefix[split]
        )
        if prefix[count] > available:
            return False

    return True
