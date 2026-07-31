## General

An integer written with digits `1` and `2` is even exactly when its last digit is `2`. Therefore, any valid result must choose some occurrence of `2` as its final retained character.

Choose the last `2` in `s` and retain every character from the beginning through that position. Nothing after it can remain because those characters are all later than the chosen final digit, while keeping every earlier character maximizes the result's length. Since all digits are nonzero, any longer retained string represents a larger positive integer than every shorter candidate. No solution ending at an earlier `2` can be longer, so this complete prefix is optimal. If `s` has no `2`, every nonempty subsequence is odd and the answer is empty.

## Complexity detail

Let $N=\lvert\texttt{s}\rvert$. Finding the last `2` and copying the result prefix each take $O(N)$ time in the worst case. Python creates a new returned string of length at most $N$, so the auxiliary/output space is $O(N)$.

## Alternatives and edge cases

- **Enumerate all subsequences:** This considers $2^N$ deletion choices even though only the final retained digit determines parity.
- **Build and test every prefix:** Keeping the latest even prefix is correct, but slicing every prefix can perform $O(N^2)$ total copying.
- **No `2`:** Every nonempty subsequence ends in `1` and is odd, so return `""`.
- **Final character is `2`:** The entire input is already the longest possible even result and must be returned unchanged.
- **Trailing ones:** Delete all characters after the last `2`; deleting any earlier digit would only shorten the number.
