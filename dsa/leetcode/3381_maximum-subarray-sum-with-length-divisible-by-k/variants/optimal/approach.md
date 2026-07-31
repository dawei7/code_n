## General

Let prefix index $j$ denote the number of elements before a boundary, and let $P_j$ be the sum of `nums[0:j]`. A subarray between prefix indices $i$ and $j$ has length $j-i$ and sum $P_j-P_i$.

The length is divisible by `k` exactly when the two prefix indices have the same remainder:

$$
j-i\equiv0\pmod{k}
\quad\Longleftrightarrow\quad
i\bmod k=j\bmod k.
$$

For a fixed ending boundary $j$, maximizing $P_j-P_i$ therefore means subtracting the smallest earlier prefix sum whose index has remainder $j\bmod k$. Keep one minimum for each of the `k` remainders. Initialize remainder zero with $P_0=0$ so subarrays beginning at index zero are eligible, and initialize every other remainder as unseen.

Process boundaries $j=1$ through $n$. After adding the next value to the running prefix sum, compare it with the stored minimum for remainder $j\bmod k$, then update that minimum. Comparing before updating prevents an empty subarray from being selected. Every valid subarray ends at some boundary and is compared against the best possible start for its remainder, so the largest candidate is the required answer.

## Complexity detail

Each array element causes one prefix update and a constant amount of work, for $O(n)$ time. The remainder minima occupy $O(k)$ space.

The benchmark defines `size` as $n$ and uses legal lengths 16, 32, and 64 with `k = 7`. The reference performs one pass. A correct slower baseline enumerates every start and end boundary, checks divisible lengths, and therefore takes $O(n^2)$ time while returning the same sums.

## Alternatives and edge cases

- **Enumerate all subarrays:** Maintaining a running sum avoids a third loop, but examining every pair of boundaries still costs $O(n^2)$ time.
- **Store every prefix sum by remainder:** This can recover valid candidates, but only the minimum earlier value in each remainder class can maximize a later difference; retaining all values wastes $O(n)$ space.
- **Sliding window:** Eligible lengths are `k`, `2 * k`, and so on, rather than one fixed length, so a single fixed-size window misses valid choices.
- **Update before comparing:** When the current remainder is already initialized, this permits subtracting the current prefix from itself and incorrectly introduces an empty length-zero candidate.
- **All negative values:** Initialize the answer below every possible sum instead of zero, because the maximum valid sum may be negative.
- **`k` equals `n`:** Only the entire array is eligible, and the prefix-remainder method still returns its sum.
- **Large magnitudes:** A valid sum may exceed 32-bit range because both $n$ and `nums[i]` are large; use a wide integer type outside Python.
