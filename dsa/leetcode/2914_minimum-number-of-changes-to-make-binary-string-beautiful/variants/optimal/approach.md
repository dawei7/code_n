## General

**Every fixed pair must become uniform.** In any beautiful partition, each
part has even length and begins at an even index because all preceding parts
also have even length. Therefore positions `0` and `1` lie in the same uniform
part, as do positions `2` and `3`, and so on. If the two bits in one of these
fixed pairs differ, at least one of them must change in every valid result.

**The lower bound is independently attainable.** Inspect the string two
characters at a time. An equal pair costs nothing; for a mismatched pair,
change either character to match the other at cost one. After doing this for
every pair, each length-two block is uniform, so those blocks themselves form
a valid beautiful partition. The construction uses exactly one change for
each pair that established the unavoidable lower bound, proving that their
count is the minimum.

## Complexity detail

Let $n=\lvert s\rvert$. The algorithm examines each of the $n/2$ fixed pairs
once, taking $O(n)$ time. It keeps only the running mismatch count, so its
auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Dynamic programming over all partitions:** Testing every even-length final part can find the same optimum in $O(n^2)$ time, but the fixed-pair characterization makes partition choices unnecessary.
- **Count total zeros and ones:** Global character counts do not determine beauty; the positions of mismatches inside fixed pairs matter.
- **Greedy run merging:** Choosing which neighboring runs to merge obscures the independent one-change lower bound for each mismatched pair.
- **Length two:** The only possible part is the full string, so unequal bits cost one and equal bits cost zero.
- **Already uniform:** A uniform even-length string is beautiful as one part and needs no changes.
- **Several even runs:** A string such as `"001100"` is already beautiful because each run can be a separate even-length part.
- **Alternating string:** Every fixed pair disagrees, so exactly $n/2$ changes are necessary.
