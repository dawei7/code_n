## Function Contract

**Inputs**

- `s`: A nonempty string of lowercase English letters.

Let $N = \lvert\texttt{s}\rvert$. An operation selects indices `left` and
`right` with `0 <= left <= right < N`, except that `left = 0` and
`right = N - 1` may not both hold. It replaces `s[left:right + 1]` by those
same characters sorted in non-descending alphabetical order.

**Return value**

Return the minimum number of permitted operations needed to make the whole
string non-descending. Return `-1` if no sequence of permitted operations can
do so.
