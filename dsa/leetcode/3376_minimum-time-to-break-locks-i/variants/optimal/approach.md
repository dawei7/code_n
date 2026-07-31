## General

After every lock, the sword's energy resets completely. The only history that affects future waiting time is therefore which locks remain and how many have already been broken. If a subset `mask` contains $b$ broken locks, the current growth factor is fixed:

$$
x=1+bk.
$$

At factor $x$, a lock requiring energy $s$ needs the smallest integer number of minutes whose accumulated energy reaches $s$:

$$
\left\lceil\frac{s}{x}\right\rceil
=
\left\lfloor\frac{s+x-1}{x}\right\rfloor.
$$

Let `best[mask]` be the least time needed to break exactly the locks in `mask`. Start with `best[0] = 0`. For every unbroken lock `i`, add its ceiling-divided waiting time and relax `best[mask | (1 << i)]`. Masks are processed numerically; every transition adds a bit, so its predecessor is always smaller and has already been finalized.

Every possible lock order corresponds to one path from the empty mask to the full mask, and the transition weights exactly equal the minutes spent in that order. Conversely, every DP path chooses each lock once and is a legal breaking order. Taking the minimum incoming cost at every subset therefore yields the minimum over all $n!$ orders without enumerating identical prefixes repeatedly.

## Complexity detail

There are $2^n$ masks, and each examines at most $n$ locks, for $O(n2^n)$ time. The `best` table contains one value per mask, requiring $O(2^n)$ space. Iteration is bottom-up, so no recursion stack is needed.

The benchmark defines `size` as the number of possible mask-to-lock inspections, $n2^n$, across legal instances with four, six, and eight locks. The reference performs work linear in this authored measure by obtaining each population count once per mask. A correct naive bitmask baseline recounts all $n$ bits for every candidate transition, grows as $O(n^2 2^n)$, and must fail scaling while still returning every expected minimum.

## Alternatives and edge cases

- **Enumerate every permutation:** It is source-faithful but repeats the same subset prefixes and costs $O(n!\,n)$ time.
- **Memoized recursion by mask:** It has the same state graph and asymptotic bounds as the bottom-up table, but adds recursion overhead.
- **Greedy weakest-first:** A small lock can raise the factor early, but ceiling effects mean this local choice is not always globally optimal.
- **Greedy strongest-first:** Spending a long time at the initial factor can be worse than postponing a strong lock until energy grows faster.
- **Use floor division:** `strength[i] // x` undercounts whenever the required energy is not divisible by the factor; ceiling division is mandatory.
- **Energy overshoot:** Energy need only reach at least the strength, and all excess disappears when the lock breaks.
- **Equal strengths:** Locks remain distinct mask bits, but swapping equal-strength locks leaves the cost unchanged.
- **Single lock:** The factor never increases before it is broken, so the answer equals its strength.
- **Maximum strength:** Integer arithmetic safely handles $10^6$ without simulation minute by minute.
