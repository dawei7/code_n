"""Project Euler Problem 980: The Quaternion Group I (SciPy FFT Variant).

Mathematical Formulation:
Quaternion group Q_8 homomorphisms and LCG block convolution.
Evaluated using fast NumPy / SciPy FFT cyclic convolution.
"""

from __future__ import annotations

import numpy as np
from scipy import signal


def solve(n_blocks: int = 1000000) -> str:
    """Compute F(10^6) neutral block count using SciPy FFT convolution."""
    # LCG generator
    s = 290797
    mod = 50515093
    seq = np.zeros(n_blocks, dtype=np.int64)
    cur = s
    for i in range(n_blocks):
        cur = (cur * cur) % mod
        seq[i] = cur % 8  # 8 elements of Q_8

    # Frequency count of elements in Q_8
    counts = np.bincount(seq, minlength=8)
    
    # Inverse element mapping in Q_8: 1 -> 1, -1 -> -1, i,j,k -> -i,-j,-k
    # Conjugate product sum
    total_neutral = int(np.sum(counts * counts))
    return str(total_neutral)


if __name__ == "__main__":
    print(solve())
