## General

**Turn an interval into two prefixes.** Let $F(x)$ be the number of index pairs whose sum is at most $x$. Every pair counted by $F(\texttt{upper})$ is no larger than the upper boundary, while $F(\texttt{lower} - 1)$ counts exactly those that are still too small. Their difference therefore leaves precisely the sums in the inclusive interval:

$$
F(\texttt{upper}) - F(\texttt{lower} - 1).
$$

**Count one prefix with two pointers.** Sort `nums`, then place `left` at the smallest value and `right` at the largest. If `nums[left] + nums[right]` is at most the current limit, every position from `left + 1` through `right` also forms a qualifying pair with `left`. The sorted order proves this because each of those values is no greater than `nums[right]`. Add `right - left` pairs at once and advance `left`.

If the two endpoint values instead exceed the limit, pairing the current largest value with anything at or to the right of `left` cannot make that endpoint pair valid. Decrementing `right` is therefore the only useful move. Each pointer moves in one direction, so a complete prefix count takes one linear sweep after sorting. Sorting changes positions but not the multiset of unordered pairs, so duplicate values and pairs formed by different equal-valued indices are still counted with their proper multiplicity.

## Complexity detail

Let $n$ be the length of `nums`. Sorting takes $O(n \log n)$ time, and the two calls to the prefix-count helper each take $O(n)$ time, giving $O(n \log n)$ overall. Python's sort may use $O(n)$ auxiliary space; the pointer sweeps themselves use $O(1)$ additional space.

## Alternatives and edge cases

- **Enumerate every index pair:** Checking all $\binom{n}{2}$ pairs is direct and correct, but its $O(n^2)$ time is too slow for $n$ up to $10^5$.
- **Binary search for each left endpoint:** After sorting, two binary searches can locate the valid partner interval for every position. This also takes $O(n \log n)$ time, but the two-pointer prefix count is simpler and its post-sort work is linear.
- **Inclusive lower boundary:** Subtracting $F(\texttt{lower})$ would incorrectly remove pairs equal to `lower`; using `lower - 1` preserves them.
- **Duplicates:** Equal values at different indices are distinct choices. Adding `right - left` counts every eligible index pair, not merely each distinct pair of values.
- **Negative values:** Sorting and the sum comparisons work unchanged when either or both selected values are negative.
- **Fewer than two values:** No pointer pair exists, so both prefix counts and the final answer are zero.
- **Large answers:** The number of valid pairs can reach $n(n-1)/2$, so implementations in fixed-width languages need a 64-bit result type.
