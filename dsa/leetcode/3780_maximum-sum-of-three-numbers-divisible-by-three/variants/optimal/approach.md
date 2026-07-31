## General

Only each value's remainder modulo three matters for validity. Three selected remainders sum to a multiple of three in exactly four unordered patterns:

$$
(0,0,0),\quad(1,1,1),\quad(2,2,2),\quad(0,1,2).
$$

For each remainder class, retain its three largest values while scanning the array. No smaller value from a class can improve any pattern, because a valid triplet uses at most three values from that class and replacing a chosen value by a larger value of the same remainder preserves divisibility.

After the scan, evaluate every remainder pattern for which the required bucket sizes exist. Sum the required largest values and return the greatest candidate. If none of the four patterns is available, retain the default answer `0`.

These patterns exhaust all three-remainder multisets whose sum is congruent to zero, and each candidate uses the greatest possible values for its pattern. Their maximum is therefore the greatest valid triplet sum.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. Each input value updates a bucket of at most three retained elements, so the running time is $O(N)$. The three constant-size buckets use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Count-and-remainder dynamic programming:** Track the greatest sum for each chosen count from zero through three and each remainder. This is also $O(N)$ time and $O(1)$ space and is the exact native Accepted formulation.
- **Fully sorted remainder buckets:** Sorting or incrementally inserting every value in its bucket is correct but requires more than linear time or space than retaining only three maxima.
- **Exactly three:** A divisible sum formed by fewer elements is irrelevant; every candidate must use three distinct positions.
- **Repeated values:** Equal values remain separate selectable elements when they occupy separate indices.
- **No residue pattern available:** Return `0`, even though all input values are positive.
- **Only one possible triplet:** When $N=3$, return its sum if divisible by three and otherwise return `0`.
