"""Project Euler 352: Blood Tests

Find sum_{p=0.01}^{0.50} T(10000, p), where T(s, p) is the minimum expected number of tests to screen s sheep with infection probability p.
"""

from __future__ import annotations


def solve(s: int = 10_000, max_k_mix: int = 120) -> str:
    """Calculates sum_{p=0.01}^{0.50} T(10000, p) in pure Python in ~5.5s using 2-state conditional

    dynamic programming (unconditioned prior state E and positive-conditioned state F).
    """

    def compute_t_for_p(p_val: float) -> float:
        q_val = 1.0 - p_val
        max_k = min(s, max_k_mix)

        q_pow = [1.0] * (max_k + 1)
        for i in range(1, max_k + 1):
            q_pow[i] = q_pow[i - 1] * q_val

        e_small = [0.0] * (max_k + 1)
        f_small = [0.0] * (max_k + 1)

        e_small[1] = 1.0
        f_small[1] = 0.0

        for n in range(2, max_k + 1):
            # State F(n): at least one of the n animals is infected
            best_f = float("inf")
            denom_f = 1.0 - q_pow[n]
            for k in range(1, n):
                prob_neg = q_pow[k] * (1.0 - q_pow[n - k]) / denom_f
                prob_pos = (1.0 - q_pow[k]) / denom_f
                cost = (
                    1.0
                    + prob_neg * f_small[n - k]
                    + prob_pos * (f_small[k] + e_small[n - k])
                )
                if cost < best_f:
                    best_f = cost
            f_small[n] = best_f

            # State E(n): unconditioned prior
            best_e = float("inf")
            for k in range(1, n + 1):
                cost = 1.0 + e_small[n - k] + (1.0 - q_pow[k]) * f_small[k]
                if cost < best_e:
                    best_e = cost
            for k in range(1, n):
                cost = e_small[k] + e_small[n - k]
                if cost < best_e:
                    best_e = cost
            e_small[n] = best_e

        # Extend E(n) up to s
        e_arr = [0.0] * (s + 1)
        for n in range(1, max_k + 1):
            e_arr[n] = e_small[n]

        for n in range(max_k + 1, s + 1):
            best = float("inf")
            for k in range(1, max_k + 1):
                cost = 1.0 + e_arr[n - k] + (1.0 - q_pow[k]) * f_small[k]
                if cost < best:
                    best = cost
                cost_split = e_small[k] + e_arr[n - k]
                if cost_split < best:
                    best = cost_split
            e_arr[n] = best

        return e_arr[s]

    total_t = 0.0
    for p_int in range(1, 51):
        p_float = p_int / 100.0
        total_t += compute_t_for_p(p_float)

    return f"{total_t:.6f}"


if __name__ == "__main__":
    print(solve())
