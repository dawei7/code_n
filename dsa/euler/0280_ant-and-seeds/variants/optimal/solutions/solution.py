def solve(grid_size: int = 5) -> str:
    """Find the expected number of steps until all 5 seeds are moved from bottom row to top row in a 5x5 grid, rounded to 6 decimal places.
    
    Time Complexity: O(states * iterations) via Markov Chain SOR Relaxation
    Space Complexity: O(states)
    """
    R = C = grid_size
    state_map = {}
    states = []

    def get_state_id(r, c, carrying, b_mask, t_mask):
        key = (r, c, carrying, b_mask, t_mask)
        if key not in state_map:
            state_map[key] = len(states)
            states.append(key)
        return state_map[key]

    queue = [(R // 2, C // 2, 0, (1 << C) - 1, 0)]
    get_state_id(*queue[0])

    head = 0
    while head < len(queue):
        r, c, carrying, b_mask, t_mask = queue[head]
        head += 1

        if t_mask == (1 << C) - 1:
            continue

        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                n_carry, n_b, n_t = carrying, b_mask, t_mask
                if not carrying and nr == R - 1 and (b_mask & (1 << nc)):
                    n_carry = 1
                    n_b &= ~(1 << nc)
                elif carrying and nr == 0 and not (t_mask & (1 << nc)):
                    n_carry = 0
                    n_t |= (1 << nc)

                n_key = (nr, nc, n_carry, n_b, n_t)
                if n_key not in state_map:
                    get_state_id(*n_key)
                    queue.append(n_key)

    num_states = len(states)
    E = [0.0] * num_states

    adj = []
    for s_idx, (r, c, carrying, b_mask, t_mask) in enumerate(states):
        if t_mask == (1 << C) - 1:
            adj.append([])
            continue

        next_ids = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < R and 0 <= nc < C:
                n_carry, n_b, n_t = carrying, b_mask, t_mask
                if not carrying and nr == R - 1 and (b_mask & (1 << nc)):
                    n_carry = 1
                    n_b &= ~(1 << nc)
                elif carrying and nr == 0 and not (t_mask & (1 << nc)):
                    n_carry = 0
                    n_t |= (1 << nc)

                n_key = (nr, nc, n_carry, n_b, n_t)
                next_ids.append(state_map[n_key])
        adj.append(next_ids)

    omega = 1.9
    for _ in range(2500):
        max_diff = 0.0
        for s_idx in range(num_states):
            if not adj[s_idx]:
                continue
            deg = len(adj[s_idx])
            target_val = 1.0 + sum(E[next_id] for next_id in adj[s_idx]) / deg
            new_val = (1 - omega) * E[s_idx] + omega * target_val
            diff = abs(new_val - E[s_idx])
            if diff > max_diff:
                max_diff = diff
            E[s_idx] = new_val
        if max_diff < 1e-9:
            break

    init_id = state_map[(R // 2, C // 2, 0, (1 << C) - 1, 0)]
    return f"{E[init_id]:.6f}"

