def solve(bloom_day, m, k):
    flower_count = len(bloom_day)
    if m * k > flower_count:
        return -1

    def can_make(day):
        bouquets = 0
        adjacent = 0

        for bloom in bloom_day:
            if bloom <= day:
                adjacent += 1
                if adjacent == k:
                    bouquets += 1
                    if bouquets == m:
                        return True
                    adjacent = 0
            else:
                adjacent = 0

        return False

    left = min(bloom_day)
    right = max(bloom_day)

    while left < right:
        middle = left + (right - left) // 2
        if can_make(middle):
            right = middle
        else:
            left = middle + 1

    return left
