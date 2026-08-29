"""Project Euler Problem 766: Sliding Block Puzzle.

Find the number of reachable configurations by sliding blocks on the 6x5 grid
from the initial configuration. Pieces of the same shape are indistinguishable.
"""

from collections import deque
from typing import Dict, List, Tuple


def _encode_segment(pos_list: List[int]) -> int:
    seg = 0
    shift = 0
    for p in pos_list:
        seg |= p << shift
        shift += 5
    return seg


def _decode_segment(seg_bits: int, k: int) -> List[int]:
    out = [0] * k
    for i in range(k):
        out[i] = (seg_bits >> (5 * i)) & 31
    return out


class Puzzle:
    def __init__(
        self,
        width: int,
        height: int,
        piece_types: List[Dict],
        initial_positions_by_type: List[List[int]],
    ):
        self.W = width
        self.H = height
        self._deltas = (-self.W, self.W, -1, 1)
        self.types = []
        start_piece_index = 0

        for t in piece_types:
            offs = t["offsets"]
            k = t["count"]
            mask_at = [0] * (self.W * self.H)
            limits_at = [None] * (self.W * self.H)

            for pos in range(self.W * self.H):
                x = pos % self.W
                y = pos // self.W
                m = 0
                ok = True
                for dx, dy in offs:
                    xx = x + dx
                    yy = y + dy
                    if xx < 0 or xx >= self.W or yy < 0 or yy >= self.H:
                        ok = False
                        break
                    m |= 1 << (yy * self.W + xx)
                if not ok:
                    continue

                mask_at[pos] = m
                max_up = min(y + dy for dx, dy in offs)
                max_down = min((self.H - 1) - (y + dy) for dx, dy in offs)
                max_left = min(x + dx for dx, dy in offs)
                max_right = min((self.W - 1) - (x + dx) for dx, dy in offs)
                limits_at[pos] = (max_up, max_down, max_left, max_right)

            shift0 = start_piece_index * 5
            seg_bits = 5 * k
            seg_mask = ((1 << seg_bits) - 1) << shift0

            self.types.append(
                {
                    "k": k,
                    "mask_at": mask_at,
                    "limits_at": limits_at,
                    "shift0": shift0,
                    "seg_mask": seg_mask,
                }
            )
            start_piece_index += k

        state = 0
        for ti, tdata in enumerate(self.types):
            k = tdata["k"]
            shift0 = tdata["shift0"]
            pos_list = sorted(initial_positions_by_type[ti])
            seg = _encode_segment(pos_list)
            state |= seg << shift0

        self.initial_state = state

    def count_reachable(self) -> int:
        seen = {self.initial_state}
        q = deque([self.initial_state])

        types = self.types
        deltas = self._deltas

        while q:
            s = q.popleft()

            occ = 0
            decoded_positions = []
            for tdata in types:
                seg = (s & tdata["seg_mask"]) >> tdata["shift0"]
                pos_list = _decode_segment(seg, tdata["k"])
                decoded_positions.append(pos_list)
                mask_at = tdata["mask_at"]
                for p in pos_list:
                    occ |= mask_at[p]

            for ti, tdata in enumerate(types):
                k = tdata["k"]
                pos_list = decoded_positions[ti]
                mask_at = tdata["mask_at"]
                limits_at = tdata["limits_at"]
                shift0 = tdata["shift0"]
                seg_mask = tdata["seg_mask"]

                for j in range(k):
                    pos = pos_list[j]
                    m_old = mask_at[pos]
                    occ_wo = occ ^ m_old

                    limits = limits_at[pos]
                    for dir_idx, delta in enumerate(deltas):
                        limit = limits[dir_idx]
                        if limit <= 0:
                            continue

                        for step in range(1, limit + 1):
                            new_pos = pos + delta * step
                            new_mask = mask_at[new_pos]
                            if new_mask & occ_wo:
                                break

                            new_positions = pos_list[:]
                            new_positions[j] = new_pos

                            idx = j
                            while (
                                idx > 0 and new_positions[idx] < new_positions[idx - 1]
                            ):
                                new_positions[idx], new_positions[idx - 1] = (
                                    new_positions[idx - 1],
                                    new_positions[idx],
                                )
                                idx -= 1
                            while (
                                idx < k - 1
                                and new_positions[idx] > new_positions[idx + 1]
                            ):
                                new_positions[idx], new_positions[idx + 1] = (
                                    new_positions[idx + 1],
                                    new_positions[idx],
                                )
                                idx += 1

                            new_seg = _encode_segment(new_positions)
                            new_state = (s & ~seg_mask) | (new_seg << shift0)

                            if new_state not in seen:
                                seen.add(new_state)
                                q.append(new_state)

        return len(seen)


def solve() -> int:
    """Compute number of reachable configurations for Problem 766 using canonical piece BFS."""
    main = Puzzle(
        width=6,
        height=5,
        piece_types=[
            {"offsets": [(0, 0), (0, 1), (1, 0)], "count": 2},
            {"offsets": [(0, 1), (1, 0), (1, 1)], "count": 2},
            {"offsets": [(0, 0), (0, 1)], "count": 2},
            {"offsets": [(0, 0)], "count": 6},
            {"offsets": [(0, 0), (1, 0), (0, 1), (1, 1)], "count": 1},
            {"offsets": [(0, 0), (1, 0)], "count": 1},
        ],
        initial_positions_by_type=[
            [1, 4],
            [2, 22],
            [11, 16],
            [12, 13, 18, 19, 24, 25],
            [14],
            [26],
        ],
    )
    ans = 0
    for _iter in range(1):
        ans = main.count_reachable()
    return ans


if __name__ == "__main__":
    print(solve())
