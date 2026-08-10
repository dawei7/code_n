## General

A subsequence may skip characters while preserving their original order. The algorithm therefore considers intervals of the input string and asks for the best palindromic subsequence that can be formed inside each interval.

Define `dp[i][j]` as the length of the longest palindromic subsequence in the inclusive substring `s[i : j + 1]`.

The answer is `dp[0][n - 1]` because that interval contains the whole string.

**Base intervals of length one.** Every one-character string is a palindrome of length one, so `dp[i][i] = 1` for all indices `i`. These diagonal cells anchor longer intervals.

The table was initialized with zeros. Cells representing an empty interior, such as `dp[i + 1][i]` for two adjacent matching characters, remain zero. That lets the matching recurrence produce `0 + 2 = 2` without a separate length-two branch.

**When the endpoint characters match.** If `s[i] == s[j]`, those two equal characters can serve as the outer pair of a palindrome. The best palindrome inside them has length `dp[i + 1][j - 1]`, so

$$
dp[i][j]=dp[i+1][j-1]+2.
$$

For this longest-subsequence problem, an optimal solution exists that uses both matching endpoints. Adding them around an optimal inner palindrome cannot hurt, and any palindrome excluding one endpoint is no longer than the best achievable with the matching pair and appropriate interior subsequence.

For adjacent equal characters, the interior is empty and contributes zero, producing length two.

**When endpoint characters differ.** They cannot both be the two outer ends of one palindrome. At least one must be excluded. The best result is therefore the better of:

- skip the left character, giving `dp[i + 1][j]`;
- skip the right character, giving `dp[i][j - 1]`.

Thus

$$
dp[i][j]=\max(dp[i+1][j],dp[i][j-1]).
$$

This does not require knowing which actual subsequence is chosen because the contract asks only for its length.

**Fill states only after their dependencies.** The outer loop increases `j` from one to `n - 1`. For a fixed right endpoint, the inner loop decreases `i` from `j - 1` to zero.

Then `dp[i + 1][j]` has already been computed earlier in the same inner loop because its left index is larger. Both `dp[i][j - 1]` and `dp[i + 1][j - 1]` belong to an earlier right-endpoint column and are already complete. The fill order therefore respects every recurrence dependency.

For `s = "cbbd"`, the two middle `b` characters create a length-two state. The outer `c` and `d` differ, so later states choose the better inner option, and the whole interval returns two.

For `"bbbab"`, matching `b` endpoints and overlapping interval choices allow the table to build a subsequence of four `b` characters even though they need not be contiguous. This is why a substring-expansion algorithm would solve a different problem.

**Why the interval recurrence covers every subsequence.** Base length-one intervals are correct. Assume all shorter intervals are correct. For `[i, j]`, matching endpoints can wrap the optimal inner palindrome, while differing endpoints force every valid palindrome to exclude at least one endpoint and therefore lie in one of the two shorter intervals. The recurrence selects the best complete possibility in either case. Induction proves every table cell, including the full-string answer. Skipped characters require no separate operation: excluding an endpoint moves to a smaller interval, and repeated exclusions represent any permitted sequence of skips while retaining order.

The string is guaranteed nonempty, so `dp[0][-1]` refers to a valid last column and no empty-string return is required.

## Complexity detail

There are $n(n+1)/2 = O(n^2)$ relevant interval states. Each is filled with constant arithmetic and comparisons, so time is $O(n^2)$.

The exact source allocates an $n$ by $n$ table, using $O(n^2)$ space. This differs from the optimal manifest's $O(n)$ space claim, which corresponds to the editorial's space-compressed DP. The current and previous dependency values can indeed be compressed into one dimension, but this implementation retains every interval.

## Alternatives and edge cases

- **Top-down memoization:** Recursively apply the same endpoint recurrence and cache `(i, j)` states. It has $O(n^2)$ time and space plus recursion.
- **One-dimensional DP:** Carefully overwrite interval values while preserving the previous diagonal value. It reduces space to $O(n)$ and matches the manifest.
- **Longest common subsequence with reversed string:** The LPS length equals the LCS length of `s` and its reverse. This also takes $O(n^2)$ time but introduces a second string and less direct reasoning.
- **Longest palindromic substring expansion:** It is incorrect here because subsequences may delete interior characters and need not be contiguous.
- **One character:** Its diagonal state is one and is returned directly.
- **Two equal characters:** The zero-initialized empty-interior cell yields two.
- **Two different characters:** The maximum of the two singleton states is one.
- **Repeated characters:** Matching endpoints can be selected even with skipped characters between them.
- **Input nonempty:** The return `dp[0][-1]` relies on `n >= 1`.
