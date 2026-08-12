import itertools


def generate_polygons() -> dict[int, list[tuple[int, int, int]]]:
    """Generate 4-digit polygonal numbers mapped to (full_number, prefix_2, suffix_2)."""
    funcs = {
        3: lambda n: n * (n + 1) // 2,
        4: lambda n: n * n,
        5: lambda n: n * (3 * n - 1) // 2,
        6: lambda n: n * (2 * n - 1),
        7: lambda n: n * (5 * n - 3) // 2,
        8: lambda n: n * (3 * n - 2),
    }

    poly_map = {}
    for k, fn in funcs.items():
        nums = []
        n = 1
        while True:
            val = fn(n)
            if val >= 10000:
                break
            if val >= 1000 and str(val)[2] != '0':  # Suffix cannot start with '0' for a 4-digit next prefix
                prefix = val // 100
                suffix = val % 100
                nums.append((val, prefix, suffix))
            n += 1
        poly_map[k] = nums
    return poly_map


def solve() -> int:
    """Find sum of the ordered set of six 4-digit cyclic polygonal numbers (P3..P8).
    
    Time Complexity: O(6! * B^6) with heavy backtracking pruning
    Space Complexity: O(1)
    """
    poly_map = generate_polygons()
    types = [3, 4, 5, 6, 7, 8]

    def dfs(chain: list[tuple[int, int, int]], unused_types: list[int]) -> list[int] | None:
        if not unused_types:
            if chain[-1][2] == chain[0][1]:
                return [c[0] for c in chain]
            return None

        curr_suffix = chain[-1][2]
        for t in unused_types:
            next_unused = [x for x in unused_types if x != t]
            for num, prefix, suffix in poly_map[t]:
                if prefix == curr_suffix:
                    res = dfs(chain + [(num, prefix, suffix)], next_unused)
                    if res:
                        return res
        return None

    # Fix type 8 (octagonal) first to break symmetry
    for start_item in poly_map[8]:
        remaining_types = [3, 4, 5, 6, 7]
        result = dfs([start_item], remaining_types)
        if result:
            return sum(result)

    return -1
