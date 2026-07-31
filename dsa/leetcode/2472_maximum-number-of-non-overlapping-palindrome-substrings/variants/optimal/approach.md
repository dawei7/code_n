## General

**Reduce every useful palindrome to one of two lengths.** If a palindrome has length greater than `k + 1`, removing its first and last characters preserves the palindrome property. Repeating that operation leaves a palindrome of length exactly `k` or `k + 1`. The shorter range finishes no later and can never make subsequent non-overlapping choices harder. Therefore it is sufficient to test only those two lengths.

**Take the first finish that becomes possible.** Scan right endpoints from left to right. For each endpoint, test the length-`k` and length-`k + 1` ranges that end there, provided the range begins after the last chosen palindrome. When either candidate is palindromic, select it immediately and move the available boundary past its right endpoint.

This greedy commitment is safe because it has the earliest possible ending among all valid next selections. In any optimal solution, replace its first selected palindrome with this one: the replacement begins within the still-available suffix and ends no later, so every later selection remains available. Applying the same exchange argument after each commitment proves that the scan obtains the maximum count.

Each palindrome test compares mirrored characters with two pointers and stops at the first mismatch. No substring copy or palindrome table is required.

## Complexity detail

Let $n = \lvert\texttt{s}\rvert$. There are $O(n)$ right endpoints, at most two candidates per endpoint, and each candidate takes $O(k)$ time to check, so the total time is $O(nk)$. The scan, boundary, counters, and two palindrome pointers use $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Quadratic palindrome table plus prefix DP:** Precomputing every palindromic range and optimizing each prefix is conceptually direct, but costs $O(n^2)$ time and $O(n^2)$ space.
- **Center expansion with interval scheduling:** Enumerating qualifying palindromes around every center and then selecting intervals can also become quadratic unless the same length reduction is used.
- **Minimum threshold of one:** Every character is itself a valid palindrome, so the answer is the full string length; the general scan reaches that result naturally.
- **Length `k + 1` candidates:** Testing only length `k` misses valid odd/even parity cases such as `s = "ababa", k = 4`.
- **Equal contents:** Two selected substrings may spell the same text; only their index ranges must be disjoint.
