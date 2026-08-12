from collections import defaultdict


def solve(target_count: int = 5) -> int:
    """Find the smallest cube for which exactly target_count permutations of its digits are cubes.
    
    Time Complexity: O(N * D log D)
    Space Complexity: O(N * D)
    """
    cubes_by_key = defaultdict(list)
    n = 1
    curr_len = 1

    while True:
        cube = n * n * n
        s_cube = str(cube)
        if len(s_cube) > curr_len:
            # Check completed digit length group
            candidates = [c_list for c_list in cubes_by_key.values() if len(c_list) == target_count]
            if candidates:
                return min(c_list[0] for c_list in candidates)
            curr_len = len(s_cube)

        key = "".join(sorted(s_cube))
        cubes_by_key[key].append(cube)
        n += 1
