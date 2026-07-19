## General
**The target occupies one consecutive block**

In non-decreasing order, every value smaller than `target` appears before every copy of `target`, and every larger value appears afterward. Therefore the target block starts at the number of smaller elements. Its length is exactly the number of elements equal to `target`.

**Recovering indices without constructing the sorted array**

Scan `nums` and count `smaller`, the values below `target`, and `equal`, the values equal to it. The answer is the consecutive range

$$
\{\textit{smaller},\textit{smaller}+1,\ldots,
\textit{smaller}+\textit{equal}-1\}.
$$

If `equal` is zero, this range is empty. Otherwise it is already increasing, so no additional sorting is needed.

**Why the range is exact**

After sorting, precisely `smaller` elements must precede the first target. The next `equal` positions must all contain the indistinguishable target copies, and no other position can contain one. Thus the constructed range contains every target index once and no non-target index.

## Complexity detail
The counts require one or two linear scans of the $n$ values, so the time is $O(n)$. Apart from the returned list of $k$ indices, the algorithm stores only counters, giving $O(1)$ auxiliary space. The output itself occupies $O(k)$ space.

## Alternatives and edge cases
- **Sort and scan:** Directly sorting `nums` follows the statement literally but costs $O(n \log n)$ time in general.
- **Counting array over values:** The bounded value range permits a frequency array, but it uses extra fixed storage and is unnecessary for one target.
- **Binary search after sorting:** Lower and upper bounds locate the block quickly only after paying the sorting cost.
- If every value equals `target`, all indices from `0` through `n - 1` are returned.
- If the target is absent, `equal` is zero and the result is empty.
- Values equal to the target are not included in the `smaller` count.
