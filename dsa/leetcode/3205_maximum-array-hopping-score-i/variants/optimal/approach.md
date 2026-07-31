## General

**Rewrite a hop as unit-interval contributions**

A hop from `i` to `j` scores `(j - i) * nums[j]`. This is equivalent to assigning `nums[j]` points to each of the unit intervals

$$
(i,i+1),(i+1,i+2),\ldots,(j-1,j).
$$

Every valid route partitions the intervals from index `0` to index `n-1` among its hops. For the interval immediately after index `i`, the landing point of its covering hop must be some position to the right of `i`. Its contribution can therefore never exceed the largest value in `nums[i + 1:]`.

**Attain every suffix maximum**

Scan landing positions from right to left while maintaining the largest value seen. Add that suffix maximum once for each interval. The resulting sum is

$$
\sum_{i=0}^{n-2}\max_{j>i}\texttt{nums}[j].
$$

These independently maximal interval contributions are simultaneously achievable. Read the right-to-left record maxima in increasing index order and hop through those record positions, ending at `n-1`. Each interval is then covered by the earliest selected landing point to its right, whose value is exactly that interval's suffix maximum.

Thus the suffix-max sum is both an upper bound on every route and the score of a valid route. The reverse scan computes the optimum without explicitly reconstructing the hops.

## Complexity detail

The scan visits the $n-1$ possible landing positions once. It uses $O(n)$ time and $O(1)$ auxiliary space; the running maximum and score are the only additional values.

The score can exceed a 32-bit signed integer in other languages, so implementations should use a sufficiently wide integer type for the accumulation.

## Alternatives and edge cases

- **Dynamic programming over previous indices:** Setting `dp[j]` to the best score ending at `j` and trying every `i < j` is direct and correct, but it costs $O(n^2)$ time and $O(n)$ space.
- **Monotonic stack of record maxima:** A stack can reconstruct the useful landing indices in linear time, but the score alone needs only the running suffix maximum.
- **Always jump directly to the end:** This ignores a larger intermediate landing value and can lose score before the final hop.
- **Two elements:** The only legal hop lands at index `1`, so the answer is `nums[1]`.
- **Strictly increasing values:** The final value is every interval's suffix maximum, making the direct hop optimal.
- **Strictly decreasing values:** Every next position becomes a new suffix maximum, so visiting each index attains the optimum.
- **Equal values:** Splitting or combining hops gives the same total because every interval has the same contribution.
- **Starting value:** `nums[0]` never weights a hop and does not affect the answer.

