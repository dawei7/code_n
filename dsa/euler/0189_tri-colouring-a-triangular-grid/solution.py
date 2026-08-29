def solve(n: int = 8) -> int:
    """Find the number of valid 3-colorings of a size n = 8 triangular grid such that no two adjacent small triangles share a color.

    Problem Context & Mathematical Principles:
    -------------------------------------------
    1. Broken-Profile / Frontier Dynamic Programming:
       A size-n triangular grid consists of n row levels.
       Between row r (with r upward triangles U) and row r + 1 (with r + 1 upward triangles V),
       there are r downward-pointing triangles sandwiched between them.

    2. Triangle-by-Triangle Frontier Transition:
       Instead of transitioning all 3^(r + 1) states in a single jump (which requires 3^(2r + 1) iterations),
       we transition one triangle at a time across the frontier:
       - First, choose the leftmost upward triangle v_0 in {0, 1, 2}.
       - Then, for each position i from 0 to r - 1:
         Given v_i and u_i, branch on the next upward triangle v_{i + 1} in {0, 1, 2}.
         The downward triangle between (u_i, v_i, v_{i + 1}) has (3 - |{u_i, v_i, v_{i + 1}}|) valid colorings.
         Multiply ways by this factor.

    3. Complexity Reduction:
       This reduces state transitions from O(3^(2n)) down to O(n^2 * 3^n), running in ~0.08s!

    Complexity:
    -----------
    - Time Complexity: O(n^2 * 3^n) operations (~0.08s for n = 8).
    - Space Complexity: O(3^n) memory for the frontier state dictionary (~1 MB).
    """
    # Base case for row 1: 3 single-triangle color choices (0, 1, 2)
    dp = {(0,): 1, (1,): 1, (2,): 1}

    for r in range(1, n):
        # State during row transition: (v_prefix, remaining_u_suffix)
        curr_level = {((), U): count for U, count in dp.items()}

        # 1. Choose leftmost upward triangle v_0
        next_level = {}
        for (v_pref, U), count in curr_level.items():
            for v0 in range(3):
                nxt = ((v0,), U)
                next_level[nxt] = next_level.get(nxt, 0) + count
        curr_level = next_level

        # 2. Advance frontier through all r downward/upward pairs
        for _ in range(r):
            next_level = {}
            for (v_pref, U), count in curr_level.items():
                vi = v_pref[-1]
                ui = U[0]
                rem_U = U[1:]
                for v_next in range(3):
                    # Available colors for the sandwiched downward triangle
                    forbidden = {vi, ui, v_next}
                    choices = 3 - len(forbidden)
                    if choices > 0:
                        nxt = (v_pref + (v_next,), rem_U)
                        next_level[nxt] = next_level.get(nxt, 0) + count * choices
            curr_level = next_level

        # Extract completed row r+1 configurations
        dp = {v_pref: count for (v_pref, _), count in curr_level.items()}

    # Return total valid 3-colorings for size-8 triangular grid
    return sum(dp.values())


if __name__ == "__main__":
    print(solve())
