## General

**Convert a ratio into a zero-sum condition.** Suppose a substring contains $z$ zeros and $o$ ones. It has the required ratio precisely when

$$
z \cdot \texttt{num2} = o \cdot \texttt{num1},
$$

or equivalently when $z \cdot \texttt{num2} - o \cdot \texttt{num1}=0$. Assign each `0` a contribution of `num2` and each `1` a contribution of `-num1`. A substring is valid exactly when the sum of these contributions is zero.

**Equal prefix scores identify every valid interval.** Let the score before the string be zero and update it while scanning each character. The weighted sum of a substring is the score after its right endpoint minus the score before its left endpoint. That difference is zero exactly when the two boundary scores are equal.

Store how many times each score has already occurred, beginning with one occurrence of score zero for the empty prefix. When the current score has appeared $f$ times, each earlier occurrence supplies a distinct left boundary for a valid nonempty substring ending here, so add $f$ to the answer. Then record the current prefix for later endpoints. Every interval has one unique pair of prefix boundaries, which proves that this counts all valid substrings once and only once.

## Complexity detail

Let $n = \lvert\texttt{s}\rvert$. The scan performs constant expected-time hash-map work per character, for $O(n)$ time. At most $n+1$ distinct prefix scores are stored, so the auxiliary space is $O(n)$.

## Alternatives and edge cases

- **Enumerate every substring:** Maintaining zero and one counts while extending every left endpoint is correct but takes $O(n^2)$ time.
- **Count only blocks of length `num1 + num2`:** This misses valid substrings whose counts are larger common multiples of the requested ratio.
- **Floating-point ratios:** Comparing divisions can lose precision and requires special handling for zero counts; the integer cross-product score is exact.
- **No feasible length:** Every valid substring length is a positive multiple of `num1 + num2`, so the answer is zero when that sum exceeds $n$.
- **All one character:** Because both requested ratio components are positive, a substring missing zeros or ones cannot qualify.
- **Repeated prefix score:** If a score has occurred several times, all of those positions form different valid intervals and the full frequency must be added.
- **Whole string and overlaps:** The empty-prefix entry permits a valid prefix or the whole string, while frequency counting naturally includes overlapping intervals.
