## Function Contract

**Inputs**

- `s`: A non-empty string of lowercase English letters.

Let $N=\lvert\texttt{s}\rvert$. Every result is a subsequence of `s`. An occurrence can be deleted only while another copy of the same letter remains, so the final string contains every distinct letter that occurred in `s` at least once. It may retain additional copies; deleting every duplicate is not necessarily lexicographically optimal.

**Return value**

Return the lexicographically smallest subsequence reachable under the deletion rule.
