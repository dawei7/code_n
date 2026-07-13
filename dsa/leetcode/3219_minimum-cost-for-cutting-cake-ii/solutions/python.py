def solve(m: int, n: int, horizontal_cut: list[int], vertical_cut: list[int]) -> int:
    # Sort cuts in descending order to apply the greedy strategy
    horizontal_cut = sorted(horizontal_cut, reverse=True)
    vertical_cut = sorted(vertical_cut, reverse=True)

    h_idx = 0
    v_idx = 0

    # Number of segments currently created
    h_segments = 1
    v_segments = 1

    total_cost = 0

    # Process cuts until all are used
    while h_idx < len(horizontal_cut) and v_idx < len(vertical_cut):
        # If the current horizontal cut is more expensive, perform it
        if horizontal_cut[h_idx] >= vertical_cut[v_idx]:
            total_cost += horizontal_cut[h_idx] * v_segments
            h_segments += 1
            h_idx += 1
        else:
            # Otherwise, perform the vertical cut
            total_cost += vertical_cut[v_idx] * h_segments
            v_segments += 1
            v_idx += 1

    # Add remaining horizontal cuts
    while h_idx < len(horizontal_cut):
        total_cost += horizontal_cut[h_idx] * v_segments
        h_idx += 1

    # Add remaining vertical cuts
    while v_idx < len(vertical_cut):
        total_cost += vertical_cut[v_idx] * h_segments
        v_idx += 1

    return total_cost
