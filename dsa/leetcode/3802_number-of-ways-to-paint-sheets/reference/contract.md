## Function Contract

**Inputs**

- `n`: The number of sheets in the ordered row.
- `limit`: An array where `limit[i]` is the maximum segment length allowed for color `i`.

Both color segments must be nonempty. Their lengths sum to $n$, and their order matters because one color covers the first segment and the other covers the second.

**Return value**

Return the number of distinct valid full-row paintings, reduced modulo $1{,}000{,}000{,}007$.
