def can_place_balls(positions, k, min_dist):
    count = 1
    last_pos = positions[0]
    for i in range(1, len(positions)):
        if positions[i] - last_pos >= min_dist:
            count += 1
            last_pos = positions[i]
            if count == k:
                return True
    return False

def solve():
    n, k = map(int, input().split())
    positions = list(map(int, input().split()))
    positions.sort()
    left, right, result = (0, 2000000000, 0)
    while left <= right:
        mid = left + (right - left) // 2
        if can_place_balls(positions, k, mid):
            result = mid
            left = mid + 1
        else:
            right = mid - 1
    print(result)


if __name__ == "__main__":
    solve()
