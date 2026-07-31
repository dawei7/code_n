## Function Contract

**Inputs**

- `nums`: A nonempty integer array whose zero values must be moved into one suffix.

Let $N=\lvert\texttt{nums}\rvert$ and let $Z$ be the number of zeroes in `nums`. One operation exchanges `nums[i]` and `nums[j]` for any distinct indices $i$ and $j$; adjacent positions are not required. Only the zero-versus-nonzero distinction affects the answer.

**Return value**

Return the minimum number of allowed swaps needed to make the last $Z$ positions zero and the first $N-Z$ positions nonzero.
