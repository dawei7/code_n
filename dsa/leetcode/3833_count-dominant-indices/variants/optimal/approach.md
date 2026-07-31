## General

Scan the array from right to left while retaining only two facts about the suffix already passed: its sum and its element count. Seed these values with the rightmost element, which itself is excluded from consideration because its right suffix is empty.

Before evaluating index `i`, let `right_sum` be the sum of `nums[i + 1:]` and let `right_count` be its length. The definition asks whether

$$
\texttt{nums[i]} > \frac{\texttt{right\_sum}}{\texttt{right\_count}}.
$$

Because `right_count` is positive, this is exactly equivalent to the integer comparison `nums[i] * right_count > right_sum`. The multiplication avoids floating-point arithmetic and preserves the required strict inequality.

After testing the index, add `nums[i]` to the suffix sum and increase the suffix count. These updates make the stored values exactly describe the suffix needed by the next index to the left. Thus every eligible index is tested once against precisely its complete right suffix, every dominant index is counted, and no non-dominant or rightmost index can enter the answer.

## Complexity detail

Let $N=\lvert\texttt{nums}\rvert$. The scan performs constant work for each of the first $N-1$ indices, so it takes $O(N)$ time. The running sum, count, loop index, and answer use $O(1)$ auxiliary space.

The benchmark defines size as $N$ and uses strictly descending arrays, so every eligible index is dominant. The accepted reverse scan and an independent forward scan backed by suffix sums both scale linearly. The slower control recomputes each right-suffix sum directly and therefore performs quadratic total work.

## Alternatives and edge cases

- **Suffix-sum array:** Precompute the sum beginning at every position and scan forward. This also takes $O(N)$ time, but it spends $O(N)$ auxiliary space that the reverse running sum avoids.
- **Recompute every suffix:** Summing `nums[i + 1:]` for each index follows the definition directly, but overlapping suffix work makes it $O(N^2)$.
- **Floating-point averages:** Dividing before comparing is readable, yet cross multiplication expresses the strict relation exactly and avoids rounding concerns.
- **Singleton array:** Its only element is the rightmost element, so the answer is `0`.
- **Equality with the average:** Dominance is strict; a value equal to its suffix average must not be counted.
- **Average versus every element:** A value can exceed the suffix average without exceeding the suffix maximum, as in `[6,10,1]`.

