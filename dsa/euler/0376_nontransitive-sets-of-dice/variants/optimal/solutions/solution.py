"""Project Euler Problem 376: Nontransitive Sets of Dice.

Find the number of nontransitive sets of three 6-sided dice with face values in {1, ..., 30}.
"""

from typing import Dict, List, Tuple

THRESHOLD = 19
WIN_STATES = 20
WIN_SPACE = WIN_STATES**3


def build_transitions() -> List[List[Tuple[int, int, int, int, int, int, int]]]:
    """Precompute valid face assignments and incremental win counts."""
    transitions: List[List[Tuple[int, int, int, int, int, int, int]]] = [
        [] for _ in range(7 * 7 * 7)
    ]
    for a_used in range(7):
        for b_used in range(7):
            for c_used in range(7):
                abc = (a_used * 7 + b_used) * 7 + c_used
                options = transitions[abc]
                for da in range(7 - a_used):
                    for db in range(7 - b_used):
                        for dc in range(7 - c_used):
                            na = a_used + da
                            nb = b_used + db
                            nc = c_used + dc
                            next_base = (
                                (na * 7 + nb) * 7 + nc
                            ) * WIN_SPACE
                            d_ba = db * a_used
                            d_cb = dc * b_used
                            d_ac = da * c_used
                            options.append(
                                (next_base, na, nb, nc, d_ba, d_cb, d_ac)
                            )
    return transitions


def solve(max_val: int = 30) -> int:
    """Compute the number of nontransitive sets of 3 dice via dynamic programming over face values."""
    if max_val < 3:
        return 0

    transitions = build_transitions()
    goal_state = ((6 * 7 + 6) * 7 + 6) * WIN_SPACE + 19 * 400 + 19 * 20 + 19

    current: Dict[int, int] = {0: 1}

    for value in range(1, max_val + 1):
        next_layer: Dict[int, int] = {}
        is_last_value = value == max_val

        for state, ways in current.items():
            ac = state % WIN_STATES
            tmp = state // WIN_STATES
            cb = tmp % WIN_STATES
            tmp //= WIN_STATES
            ba = tmp % WIN_STATES
            abc = tmp // WIN_STATES

            for (
                next_base,
                na,
                nb,
                nc,
                d_ba,
                d_cb,
                d_ac,
            ) in transitions[abc]:
                nba = min(19, ba + d_ba)
                ncb = min(19, cb + d_cb)
                nac = min(19, ac + d_ac)

                # Prune states that cannot mathematically reach 19 wins even with all remaining faces
                if nba + 6 * (6 - nb) < THRESHOLD:
                    continue
                if ncb + 6 * (6 - nc) < THRESHOLD:
                    continue
                if nac + 6 * (6 - na) < THRESHOLD:
                    continue

                if is_last_value and (na != 6 or nb != 6 or nc != 6):
                    continue

                key = next_base + nba * 400 + ncb * 20 + nac
                next_layer[key] = next_layer.get(key, 0) + ways

        current = next_layer

    # Divide by 3 for cyclic permutations of the 3 dice {A, B, C}
    return current.get(goal_state, 0) // 3


if __name__ == "__main__":
    print(solve())
