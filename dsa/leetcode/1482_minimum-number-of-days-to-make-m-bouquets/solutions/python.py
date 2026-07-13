def solve(bloom_day, m, k):
    need = int(m) * int(k)
    if need > len(bloom_day):
        return -1

    def can_make(day):
        bouquets = adjacent = 0
        for bloom in bloom_day:
            if bloom <= day:
                adjacent += 1
                if adjacent == k:
                    bouquets += 1
                    adjacent = 0
            else:
                adjacent = 0
        return bouquets >= m

    left, right = min(bloom_day), max(bloom_day)
    while left < right:
        mid = (left + right) // 2
        if can_make(mid):
            right = mid
        else:
            left = mid + 1
    return left
