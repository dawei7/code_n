## General

**Determine whether scoring can begin**

Let $m$ be the minimum value in `enemyEnergies`. The first point must be earned before any enemy may be marked for energy. If `currentEnergy < m`, no scoring operation is affordable and the marking operation is locked, so zero is the only possible result.

Otherwise, score once using a minimum-energy enemy. This unlocks marking while preserving that enemy as an unmarked scoring target.

**Keep one minimum enemy repeatable**

After scoring is unlocked, mark every enemy except the chosen minimum enemy and add their energy to the available pool. The total energy that can be spent on further scoring, including the energy already spent for the first point, is

$$
\texttt{currentEnergy}
+\sum_{e\in\texttt{enemyEnergies}} e
-m.
$$

Every point costs at least $m$ energy because no enemy has a smaller value. Therefore no strategy can earn more than this total divided by $m$, rounded down.

The described strategy attains that bound: leave the minimum enemy unmarked, repeatedly spend $m$ energy on it, and mark other enemies whenever their energy is needed. Since the first point is available before marking begins, all other energy values can eventually enter the pool. Thus the answer is

$$
\left\lfloor
\frac{\texttt{currentEnergy}+\sum e-m}{m}
\right\rfloor.
$$

## Complexity detail

One pass can compute both the minimum enemy energy and the sum of all values. With $n$ enemies, time complexity is $O(n)$ and auxiliary space is $O(1)$.

The sum and quotient may exceed 32-bit signed range, so fixed-width implementations need a 64-bit accumulator and return type.

## Alternatives and edge cases

- **Sort the enemies:** Sorting exposes the minimum but costs $O(n\log n)$ time when only a scan is needed.
- **Simulate individual operations:** Repeatedly spending the minimum energy can require billions of iterations even though division gives the result directly.
- **Mark the minimum enemy:** This removes the cheapest repeatable scoring target and cannot improve the maximum point count.
- **Insufficient initial energy:** No point can be earned, so no enemy can be marked and the answer is zero.
- **Exact initial threshold:** Starting with exactly $m$ earns the first point and unlocks all remaining enemy energy.
- **Single enemy:** If affordable, it remains unmarked and can be used `currentEnergy // enemyEnergies[0]` times.
- **Duplicate minima:** Keep any one minimum enemy unmarked; the others may be converted to energy.
- **Large values:** The combined energy can be much larger than any individual input and requires wide arithmetic.
