## General

Create a value table for the lowercase alphabet. Its default entry for a letter is that letter's one-indexed alphabet position, and every character in `chars` replaces its entry with the corresponding value from `vals`.

After this transformation, the problem is exactly the maximum-subarray-sum problem over the sequence of character values. Maintain `current`, the largest cost of a substring ending at the current character. Extending a negative-cost prefix can only reduce every future substring that includes it, so update `current` to the larger of zero and `current + value`.

Maintain `best` as the largest `current` seen. Both variables begin at zero because the empty substring is a legal candidate. Consequently, an input whose character values are all negative correctly returns zero, while every positive run is considered as it is scanned.

The recurrence is correct because an optimal substring ending at a position has only two possibilities: it extends the optimal nonnegative substring ending immediately before that position, or it begins at the current position after discarding a harmful prefix. The zero option represents discarding the entire current run.

## Complexity detail

Let $n=\lvert s\rvert$ and $k=\lvert\texttt{chars}\rvert$. Initializing the custom values takes $O(k)$ time and scanning `s` takes $O(n)$ time, for $O(n+k)$ total time.

The value table has exactly 26 entries, so the auxiliary-space bound is $O(1)$.

## Alternatives and edge cases

- **Enumerating every substring:** Incrementally summing each start/end pair is correct but takes $O(n^2)$ time.
- **Prefix sums with minimum-prefix tracking:** This also gives an $O(n)$ solution, but Kadane's recurrence expresses the same decision with less state.
- **All negative values:** The empty substring has cost zero and must beat every negative nonempty substring.
- **Unlisted characters:** Their values are alphabet positions, not zero or an absent-map default.
- **Positive custom values:** Overrides may be larger than $26$ and can make a substring containing them dominate ordinary letters.
- **Repeated characters:** Every occurrence uses the same resolved value and is processed independently in the running sum.
