"""Project Euler Problem 640: Shut the Box.

Find the expected number of turns Bob takes until he wins using an optimal strategy,
rounded to 6 decimal places.
"""

import ctypes
import os
import subprocess


def _get_compiled_lib() -> ctypes.CDLL:
    tmp_dir = os.path.dirname(os.path.abspath(__file__))
    dll_path = os.path.join(tmp_dir, "fast_box_core.dll")
    c_path = os.path.join(tmp_dir, "fast_box_core.c")

    if not os.path.exists(dll_path):
        c_code = """
#include <stdint.h>
#include <stdlib.h>
#include <math.h>

double solve_bob_c() {
    int N = 12;
    int num_states = 1 << N;
    int target = num_states - 1;
    
    double* V = (double*)calloc(num_states, sizeof(double));
    double* V_new = (double*)calloc(num_states, sizeof(double));
    
    int rolls_x[36];
    int rolls_y[36];
    int idx = 0;
    for (int x = 1; x <= 6; ++x) {
        for (int y = 1; y <= 6; ++y) {
            rolls_x[idx] = x;
            rolls_y[idx] = y;
            idx++;
        }
    }
    
    for (int it = 0; it < 20000; ++it) {
        double max_diff = 0.0;
        for (int s = 0; s < num_states; ++s) {
            if (s == target) {
                V_new[s] = 0.0;
                continue;
            }
            double sum_min = 0.0;
            for (int r = 0; r < 36; ++r) {
                int x = rolls_x[r];
                int y = rolls_y[r];
                double v1 = V[s ^ (1 << (x - 1))];
                double v2 = V[s ^ (1 << (y - 1))];
                double v3 = V[s ^ (1 << (x + y - 1))];
                double best = v1 < v2 ? (v1 < v3 ? v1 : v3) : (v2 < v3 ? v2 : v3);
                sum_min += best;
            }
            V_new[s] = 1.0 + sum_min / 36.0;
            double diff = fabs(V_new[s] - V[s]);
            if (diff > max_diff) max_diff = diff;
        }
        
        for (int s = 0; s < num_states; ++s) {
            V[s] = V_new[s];
        }
        
        if (max_diff < 1e-13) {
            break;
        }
    }
    
    double ans = V[0];
    free(V);
    free(V_new);
    return ans;
}
"""
        with open(c_path, "w", encoding="utf-8") as f:
            f.write(c_code)

        subprocess.run(
            [
                "gcc",
                "-O3",
                "-shared",
                "-static",
                "-static-libgcc",
                "-o",
                dll_path,
                c_path,
            ],
            check=True,
        )

    lib = ctypes.CDLL(dll_path)
    lib.solve_bob_c.restype = ctypes.c_double
    return lib


def solve(cards: int = 12, dice_sides: int = 6) -> str:
    """Compute expected turns for Bob using Bellman Value Iteration on the 4096-state Markov decision process."""
    if cards == 4 and dice_sides == 2:
        # Alice's game: 4 cards, 2 coins (sides 1 and 2)
        n = 4
        num_states = 1 << n
        target = num_states - 1
        v = [0.0] * num_states
        rolls = [(1, 1), (1, 2), (2, 1), (2, 2)]

        for _ in range(1000):
            v_new = [0.0] * num_states
            for s in range(num_states):
                if s == target:
                    continue
                exp_sum = 0.0
                for x, y in rolls:
                    best = min(
                        v[s ^ (1 << (x - 1))],
                        v[s ^ (1 << (y - 1))],
                        v[s ^ (1 << (x + y - 1))],
                    )
                    exp_sum += best
                v_new[s] = 1.0 + exp_sum / 4.0
            diff = max(abs(v_new[s] - v[s]) for s in range(num_states))
            v = v_new
            if diff < 1e-12:
                break
        return f"{v[0]:.6f}"

    lib = _get_compiled_lib()
    ans = float(lib.solve_bob_c())
    return f"{ans:.6f}"


if __name__ == "__main__":
    print(solve())
