## General
**Square the smaller dimension:** Treat the smaller matrix dimension as the boundary-pair dimension. If rows are no more numerous than columns, pair top and bottom rows and compress columns. Otherwise, pair left and right columns and compress rows. Direct orientation-aware indexing avoids allocating a transposed matrix.

**Compress between two boundaries:** Fix the first boundary and initialize an array of $L$ zeros. As the second boundary advances, add its cells into that array. Each entry then stores the sum along the fixed span for one position in the larger dimension.

**Count one-dimensional target sums:** A contiguous range of the compressed array corresponds exactly to one submatrix with the chosen small-dimension boundaries. Scan its prefix sums with a frequency map. When the running sum is $p$, every earlier prefix equal to $p-\texttt{target}$ defines a range summing to `target`.

Every boundary pair and compressed contiguous range maps to one unique rectangle, so counted ranges are valid and distinct. Conversely, every rectangle has one pair of boundaries in the smaller dimension and one contiguous range in the larger dimension, so it is considered exactly once.

## Complexity detail
There are $O(S^2)$ boundary pairs. Updating and scanning the compressed array costs $O(L)$ for each pair, giving $O(S^2L)$ time. The compressed sums and prefix-frequency map each contain at most $O(L)$ entries, so auxiliary space is $O(L)$.

## Alternatives and edge cases
- **Enumerate four boundaries:** A 2D prefix table makes each rectangle sum constant-time, but there are $O(R^2C^2)$ rectangles.
- **Always pair rows:** It is correct but costs $O(R^2C)$ and can be much worse than pairing columns for a tall matrix.
- **Materialize a transpose:** It simplifies orientation logic but adds $O(RC)$ auxiliary space.
- **Negative values:** Sliding-window methods are invalid because extending a range does not change its sum monotonically; prefix frequencies remain correct.
- **All-zero matrix with zero target:** Every non-empty rectangle qualifies.
- **Single row or column:** The method reduces directly to ordinary subarray-sum counting.
- **Equal sums at different boundaries:** Each coordinate tuple is a distinct submatrix and is counted separately.
