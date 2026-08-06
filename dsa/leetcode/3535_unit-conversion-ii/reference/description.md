## Description

There are $n$ units labeled from `0` through `n - 1`. Each entry `[source, target, factor]` in `conversions` states that one unit of `source` is equal to `factor` units of `target`. The $n-1$ given conversions guarantee that unit `0` can be converted to every other unit through a unique sequence of conversions. A conversion may be followed either in its stated direction or in reverse.

Each query `[unitA, unitB]` asks how many units of `unitB` equal one unit of `unitA`. This value can be a fraction. Interpret division modulo the prime $10^9+7$: if the exact ratio is $p/q$, return

$$
p \cdot q^{-1} \bmod (10^9+7),
$$

where $q^{-1}$ is the modular multiplicative inverse of $q$. Return one modular conversion factor for every query, preserving query order.
