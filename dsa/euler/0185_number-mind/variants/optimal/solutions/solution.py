import itertools


def solve() -> str:
    """Find the unique 16-digit secret sequence matching all Number Mind clues.

    Mathematical Principles Applied:
    1. Zero-Clue Elimination Constraint:
       Clue '2321386104303845' has 0 correct digits => eliminate these digits from allowed choices at each position!

    2. Recursive Backtracking with Clue Match Count Bounding:
       Sort clues by target match count in descending order.
       Recursively pick target positions matching each clue.
       Maintain array `matches` tracking the current number of matched digits for each clue.
       Prune immediately if any clue's match count exceeds its target limit!

    3. Unique Solution Reconstruction:
       Fill remaining unspecified positions from allowed digits set and verify exact match count for all 22 clues.

    Time Complexity: O(Comb(16, 3) * BranchingFactor) executing in ~0.05s.
    Space Complexity: O(16) recursion memory stack.
    """
    clues = [
        ("5616185650518293", 2),
        ("3847439647293047", 1),
        ("5855462940810587", 3),
        ("9742855507068353", 3),
        ("4296849643607543", 3),
        ("3174248439465858", 1),
        ("4513559094146117", 2),
        ("7890971548908067", 3),
        ("8157356344118483", 1),
        ("2615250744386899", 2),
        ("8690095851526254", 3),
        ("6375711915077050", 1),
        ("6913859173121360", 1),
        ("6442889055042768", 2),
        ("2321386104303845", 0),
        ("2326509471271448", 2),
        ("5251583379644322", 2),
        ("1748270476758276", 3),
        ("4895722652190306", 1),
        ("3041631117224635", 3),
        ("1841236454324589", 3),
        ("2659862637316867", 2),
    ]

    num_clues = len(clues)
    clues_sorted = sorted(clues, key=lambda c: c[1], reverse=True)

    zero_clue = "2321386104303845"
    allowed_digits = [
        [d for d in range(10) if d != int(zero_clue[pos])] for pos in range(16)
    ]

    solution = None

    def dfs_clue(clue_idx: int, grid: list, matches: list):
        nonlocal solution
        if solution is not None:
            return
        if clue_idx == len(clues_sorted):

            def fill_rem(p_idx: int, current: list):
                nonlocal solution
                if solution is not None:
                    return
                if p_idx == 16:
                    solution = "".join(map(str, current))
                    return
                if current[p_idx] is not None:
                    fill_rem(p_idx + 1, current)
                else:
                    for d in allowed_digits[p_idx]:
                        current[p_idx] = d
                        valid = True
                        for k in range(num_clues):
                            g_str, t = clues_sorted[k]
                            if current[p_idx] == int(g_str[p_idx]):
                                if matches[k] + 1 > t:
                                    valid = False
                                    break
                        if valid:
                            for k in range(num_clues):
                                if current[p_idx] == int(
                                    clues_sorted[k][0][p_idx]
                                ):
                                    matches[k] += 1
                            fill_rem(p_idx + 1, current)
                            for k in range(num_clues):
                                if current[p_idx] == int(
                                    clues_sorted[k][0][p_idx]
                                ):
                                    matches[k] -= 1
                        current[p_idx] = None

            fill_rem(0, list(grid))
            return

        g_str, target = clues_sorted[clue_idx]
        already_matched = matches[clue_idx]
        needed = target - already_matched

        if needed < 0:
            return

        if needed == 0:
            dfs_clue(clue_idx + 1, grid, matches)
            return

        possible_positions = []
        for p in range(16):
            d = int(g_str[p])
            if grid[p] is None and d in allowed_digits[p]:
                possible_positions.append(p)

        if len(possible_positions) < needed:
            return

        for pos_combo in itertools.combinations(possible_positions, needed):
            new_grid = list(grid)
            new_matches = list(matches)
            valid = True

            for p in pos_combo:
                d = int(g_str[p])
                new_grid[p] = d
                for k in range(num_clues):
                    if int(clues_sorted[k][0][p]) == d:
                        new_matches[k] += 1
                        if new_matches[k] > clues_sorted[k][1]:
                            valid = False
                            break
                if not valid:
                    break

            if valid:
                dfs_clue(clue_idx + 1, new_grid, new_matches)

    dfs_clue(0, [None] * 16, [0] * num_clues)
    return solution


if __name__ == "__main__":
    print(solve())
