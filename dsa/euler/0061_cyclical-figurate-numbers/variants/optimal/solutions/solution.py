def generate_polygons() -> dict[int, list[tuple[int, int, int]]]:
    """Generate 4-digit polygonal numbers for types k in {3..8} mapped to (full_number, prefix_2, suffix_2).

    Polygonal Formulas P_{k, n}:
    P_{3, n} = n*(n + 1) / 2      (Triangle)
    P_{4, n} = n^2                (Square)
    P_{5, n} = n*(3n - 1) / 2     (Pentagonal)
    P_{6, n} = n*(2n - 1)         (Hexagonal)
    P_{7, n} = n*(5n - 3) / 2     (Heptagonal)
    P_{8, n} = n*(3n - 2)         (Octagonal)
    """
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
            # Filter 4-digit numbers where suffix >= 10 (so next 2-digit prefix is a valid 4-digit number)
            if val >= 1000 and str(val)[2] != "0":
                prefix = val // 100
                suffix = val % 100
                nums.append((val, prefix, suffix))
            n += 1
        poly_map[k] = nums
    return poly_map


def solve() -> int:
    """Find the sum of the ordered set of six 4-digit cyclic numbers representing triangle, square, pentagonal, hexagonal, heptagonal, and octagonal numbers.

    Mathematical Principles Applied:
    1. Cyclic 2-Digit Linkage:
       A 6-element sequence (x_1, x_2, ..., x_6) is cyclic iff suffix(x_i) == prefix(x_{i+1})
       and suffix(x_6) == prefix(x_1).

    2. Type Permutation & Symmetry Breaking:
       Each of the 6 numbers MUST belong to a distinct polygonal type k in {3, 4, 5, 6, 7, 8}.
       Fixing P_8 (octagonal, which has the fewest 4-digit candidates: 40 elements) as the start node
       breaks cyclic symmetry and prunes DFS search depth dramatically.

    Time Complexity: O(6! * B^6) pruned by DFS matching to ~0.001s execution.
    Space Complexity: O(1) auxiliary space.
    """
    poly_map = generate_polygons()

    def dfs(chain: list[tuple[int, int, int]], unused_types: list[int]) -> list[int] | None:
        """Depth-first search to build a 6-element cyclic chain across unused polygonal types."""
        # Base case: all 6 polygonal types used
        if not unused_types:
            # Cyclic closure test: suffix of last number equals prefix of first number
            if chain[-1][2] == chain[0][1]:
                return [c[0] for c in chain]
            return None

        curr_suffix = chain[-1][2]

        # Branch on each remaining unused polygonal type
        for t in unused_types:
            next_unused = [x for x in unused_types if x != t]
            for num, prefix, suffix in poly_map[t]:
                # Prefix matching link: prefix of candidate must equal current suffix
                if prefix == curr_suffix:
                    res = dfs(chain + [(num, prefix, suffix)], next_unused)
                    if res:
                        return res
        return None

    # Fix octagonal numbers (type 8) as the root to break cyclic symmetry
    for start_item in poly_map[8]:
        remaining_types = [3, 4, 5, 6, 7]
        result = dfs([start_item], remaining_types)
        if result:
            # Return sum of the six 4-digit cyclic polygonal numbers
            return sum(result)

    return -1


if __name__ == "__main__":
    print(solve())
