## General
**Work with frequencies, not observations.** Expanding the histogram would require $O(N)$ time and space, even though only 256 distinct values can occur. Instead, one scan over `count` can maintain the total frequency, the weighted sum, the first and last occupied values, and the value with greatest frequency. Dividing the weighted sum by $N$ gives the mean.

**Locate the two central ranks cumulatively.** Use zero-based ranks `left_rank = (N - 1) // 2` and `right_rank = N // 2`. As the scan adds each frequency to a cumulative count, the first value whose cumulative count exceeds a rank is the observation at that sorted position. The ranks are equal when $N$ is odd; when $N$ is even, averaging their values produces the median without constructing the sample.

The first and last positive-frequency indices are exactly the sample's minimum and maximum. The weighted sum counts each value once for each occurrence, and cumulative frequencies partition the sorted sample into the same runs represented by the histogram. These facts establish every returned statistic directly from `count`.

## Complexity detail
A generalized histogram with $K$ bins would take $O(K)$ time. Here $K=256$ is fixed by the contract, so the scan is $O(256)=O(1)$ and does not depend on $N$. Only scalar totals, ranks, and selected values are stored, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Expand and sort the sample:** Materializing every value is straightforward, but costs $O(N \log N)$ time and $O(N)$ space and is infeasible when $N$ is near $10^9$.
- **Repeated rank scans:** Finding each statistic with a separate histogram traversal remains constant under the fixed domain, but one coordinated scan is simpler and avoids redundant work.
- **Single occupied bin:** The minimum, maximum, mean, median, and mode are all that bin's value.
- **Even sample size:** The two central ranks can fall in different bins, so both must be located before averaging.
- **Large frequencies:** Weighted sums and $N$ may exceed 32-bit integer range in other languages; use a sufficiently wide integer type before converting the mean to floating point.
- **Unique mode:** The contract removes tie-breaking ambiguity; updating the mode only for a strictly larger frequency is sufficient.
