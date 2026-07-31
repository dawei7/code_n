def solve(hens, grains):
    sorted_hens = sorted(hens)
    sorted_grains = sorted(grains)
    grain_count = len(sorted_grains)

    def can_eat_all(time):
        grain = 0
        for hen in sorted_hens:
            if grain == grain_count:
                return True

            if sorted_grains[grain] < hen:
                left_distance = hen - sorted_grains[grain]
                if left_distance > time:
                    return False
                right_reach = max(
                    hen + time - 2 * left_distance,
                    hen + (time - left_distance) // 2,
                )
            else:
                right_reach = hen + time

            while grain < grain_count and sorted_grains[grain] <= right_reach:
                grain += 1

        return grain == grain_count

    low = -1
    high = 2 * 10**9
    while high - low > 1:
        middle = (low + high) // 2
        if can_eat_all(middle):
            high = middle
        else:
            low = middle

    return high
