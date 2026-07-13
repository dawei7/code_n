from bisect import bisect_right, insort


def solve(rains):
    dry_days = []
    full = {}
    result = [1] * len(rains)
    for day, lake in enumerate(rains):
        if lake == 0:
            insort(dry_days, day)
            continue
        result[day] = -1
        if lake in full:
            pos = bisect_right(dry_days, full[lake])
            if pos == len(dry_days):
                return []
            dry_day = dry_days.pop(pos)
            result[dry_day] = lake
        full[lake] = day
    return result
