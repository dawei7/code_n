## Function Contract

**Inputs**

- `capacity`: A nonempty array whose value at index `i` is the capacity of box
  `i`.
- `itemSize`: The minimum capacity a box needs in order to store the item.

Let $N = \lvert\texttt{capacity}\rvert$. An index `i` is eligible when
`capacity[i] >= itemSize`. Indexing is zero-based.

**Return value**

Return the smallest index among the eligible boxes having minimum capacity.
Return `-1` when no eligible box exists.
