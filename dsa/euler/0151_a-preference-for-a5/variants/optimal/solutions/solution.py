def solve() -> str:
    """Find expected number of times supervisor finds a single sheet in envelope (excluding 1st and 16th batches).
    
    Time Complexity: O(States)
    Space Complexity: O(Depth)
    """
    expected_singles = 0.0

    def dfs(state: tuple[int, int, int, int], prob: float, batch_num: int):
        nonlocal expected_singles
        c2, c3, c4, c5 = state
        total_sheets = c2 + c3 + c4 + c5
        if total_sheets == 0:
            return

        # Exclude batch 1 (initial A1 start) and batch 16 (last batch)
        if batch_num not in (1, 16) and total_sheets == 1:
            expected_singles += prob

        if c2 > 0:
            p = c2 / total_sheets
            dfs((c2 - 1, c3 + 1, c4 + 1, c5 + 1), prob * p, batch_num + 1)
        if c3 > 0:
            p = c3 / total_sheets
            dfs((c2, c3 - 1, c4 + 1, c5 + 1), prob * p, batch_num + 1)
        if c4 > 0:
            p = c4 / total_sheets
            dfs((c2, c3, c4 - 1, c5 + 1), prob * p, batch_num + 1)
        if c5 > 0:
            p = c5 / total_sheets
            dfs((c2, c3, c4, c5 - 1), prob * p, batch_num + 1)

    # Batch 2 is the first batch drawing from envelope after cutting A1
    dfs((1, 1, 1, 1), 1.0, 2)

    return f"{expected_singles:.6f}"
