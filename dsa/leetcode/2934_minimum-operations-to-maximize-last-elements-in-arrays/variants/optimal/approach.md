## General

**Only two final maxima are possible.** The values at the last index either
remain in their original arrays or are swapped with each other. These two
orientations completely determine the candidate maxima for both arrays. Test
both and include one operation in the cost of the swapped orientation.

**Every earlier vertical pair is then independent.** Fix candidate maxima
$M_1$ and $M_2$. At an earlier index with values $(x,y)$, leaving the pair in
place is legal exactly when $x\le M_1$ and $y\le M_2$. If that placement is
illegal but the swapped placement satisfies $y\le M_1$ and $x\le M_2$, the
swap is forced and contributes one operation. If neither placement fits, the
entire final orientation is impossible.

Whenever both placements fit, keeping the pair costs less and cannot affect
any other index, so it is always optimal. Therefore a single scan gives the
minimum cost for each fixed last orientation: count precisely the forced
swaps, or reject the orientation at its first impossible pair. The smaller of
the two feasible orientation costs is globally optimal because every valid
final state uses one of those two last-pair arrangements.

## Complexity detail

Let $n$ be the common array length. Each of the two last-pair orientations
scans the first $n-1$ vertical pairs once, taking $O(n)$ total time. Only
counters and candidate maxima are stored, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Enumerate all swap subsets:** Testing every one of the $2^n$ index subsets is correct but exponential and ignores the independence created by fixed final maxima.
- **Repeated prefix validation:** Rechecking all previously placed pairs after each decision is correct but takes $O(n^2)$ time.
- **Single-element arrays:** Both only elements are already maxima, so zero operations are optimal.
- **Equal values:** The condition asks for a maximum, not a unique maximum; equality with a last value is valid.
- **Swap the last pair:** Its cost must be included even when every earlier pair then remains unchanged.
- **Both orientations impossible:** Return `-1`; a different combination of earlier swaps cannot change either candidate final maximum.
