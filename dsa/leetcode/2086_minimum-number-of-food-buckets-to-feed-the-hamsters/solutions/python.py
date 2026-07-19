def solve(hamsters: str) -> int:
    latest_bucket = -2
    bucket_count = 0

    for index, cell in enumerate(hamsters):
        if cell != "H":
            continue
        if latest_bucket == index - 1:
            continue
        if index + 1 < len(hamsters) and hamsters[index + 1] == ".":
            latest_bucket = index + 1
            bucket_count += 1
        elif index > 0 and hamsters[index - 1] == ".":
            latest_bucket = index - 1
            bucket_count += 1
        else:
            return -1

    return bucket_count
