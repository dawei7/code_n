## Function Contract

**Inputs**

- `s1`: The source block.
- `n1`: The number of times `s1` is concatenated to form `str1`.
- `s2`: The target block.
- `n2`: The number of times `s2` is concatenated to form one copy of `str2`.

**Return value**

- Return the maximum integer `m` such that `s2` repeated `n2 * m` times is a subsequence of `s1` repeated `n1` times.

Characters selected for the subsequence must keep their order, but matches may cross the boundary between consecutive copies of `s1`.
