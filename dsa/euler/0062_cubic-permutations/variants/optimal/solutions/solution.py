from collections import defaultdict


def solve(target_count: int = 5) -> int:
    """Find the smallest cube for which exactly 5 permutations of its digits are also perfect cubes.

    Mathematical Principles Applied:
    1. Sorted Digit Signature Anagram Hash Map:
       For a perfect cube c = n^3, compute its sorted digit signature key = "".join(sorted(str(c))).
       All cubes that are digit permutations of each other share the exact same signature key.

    2. Grouping by Digit Length:
       Permutations of a d-digit number MUST also be d-digit numbers.
       Therefore, when the digit length of n^3 increases from L to L+1, all candidates for length L
       are fully accumulated and can be evaluated.

    3. Minimal Base Cube Extraction:
       Return the minimum cube c_0 in the matching candidate signature group.

    Time Complexity: O(N * D log D) for N ≈ 10,000 (executes in ~0.02s).
    Space Complexity: O(N * D) memory for hash map.
    """
    cubes_by_key = defaultdict(list)
    n = 1
    curr_len = 1

    # Generate cubes n^3 sequentially
    while True:
        cube = n * n * n
        s_cube = str(cube)

        # When digit length of cube increases, evaluate completed length group
        if len(s_cube) > curr_len:
            # Collect all signature groups with exactly target_count (5) cubes
            candidates = [c_list for c_list in cubes_by_key.values() if len(c_list) == target_count]
            if candidates:
                # Return the smallest initial cube among matching candidate groups
                return min(c_list[0] for c_list in candidates)

            # Update current digit length group
            curr_len = len(s_cube)

        # Compute sorted digit signature key
        key = "".join(sorted(s_cube))
        cubes_by_key[key].append(cube)

        n += 1


if __name__ == "__main__":
    print(solve())
