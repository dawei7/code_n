## General

The legal values occupy the fixed domain from 1 through 100. Count how many times each value occurs. To obtain the smallest sum, scan values upward and consume as many occurrences as possible until `k` have been taken. To obtain the largest sum, perform the symmetric scan downward.

Each scan selects exactly the required multiset. If a smaller available value were omitted from the smallest group in favor of a larger one, exchanging them could only reduce the sum, so the upward greedy scan is minimal. The same exchange reasoning proves that the downward scan maximizes the other sum. Taking the absolute difference of these two optimal sums therefore returns the requested value. Frequency counts naturally preserve duplicate occurrences.

## Complexity detail

Let $N$ be the array length and $V=100$ the value-domain size. Building frequencies takes $O(N)$ time, and the two domain scans take $O(V)$ time, for $O(N+V)$ overall. The frequency array uses $O(V)$ auxiliary space. Under the fixed source bound, both simplify to linear time and constant-bounded auxiliary storage with respect to $N$.

## Alternatives and edge cases

- **Sort the array:** After $O(N\log N)$ sorting, summing the first and last `k` elements is concise, but it does not exploit the small fixed value domain.
- **Repeated minimum and maximum removal:** Selecting one extreme at a time is correct but can rescan and shift the working array, reaching $O(NK)$ or $O(N^2)$ work.
- **Duplicates:** Equal occurrences are counted individually, as shown by the two smallest `2` values in Example 1.
- **Overlapping groups:** When `2 * k > n`, middle occurrences may participate in both independently defined sums.
- **Whole array:** If `k = n`, the largest and smallest sums are identical, so the answer is zero.
- **One element per group:** For `k = 1`, the result is the ordinary array maximum minus minimum.
- **All values equal:** Both sums are equal for every legal `k`.
