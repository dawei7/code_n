## General
**Collapse the two XOR conditions into one interval condition**

Define the prefix XOR $P_r$ as the XOR of the first $r$ elements:

$$
P_0 = 0,
\qquad
P_r = \texttt{arr[0]} \mathbin{\oplus} \cdots \mathbin{\oplus}
\texttt{arr[r-1]}.
$$

For a proposed triplet, the two adjacent parts cover the whole interval from
`i` through `k`. Because XOR is associative and $x \mathbin{\oplus} x=0$,
their XOR values are equal exactly when their combined XOR is zero:

$$
a=b
\iff
a \mathbin{\oplus} b=0
\iff
P_i=P_{k+1}.
$$

The equality therefore depends only on the two outer prefix positions, not on
the split position `j`.

**Count every legal split between matching prefix positions**

Suppose the same prefix XOR occurs at positions $p$ and $r$, with $p<r$.
These positions describe the array interval from `p` through `r - 1`,
whose XOR is zero. Setting `i = p` and `k = r - 1`, any split
`j` from `p + 1` through `r - 1` makes the two adjacent XORs equal.
There are exactly $r-p-1$ such splits.

Thus, when processing prefix position $r$, every earlier occurrence $p$ of
the same prefix value contributes $r-p-1$. Directly iterating over all earlier
positions would still take quadratic time, so the contributions must be
aggregated.

**Aggregate contributions with two hash tables**

For each prefix value $x$, maintain:

- `count[x]`: the number of earlier positions $p$ with $P_p=x$;
- `position_sum[x]`: the sum of those earlier positions.

If $c=\texttt{count[x]}$ and $s=\texttt{position_sum[x]}$, the total
contribution of all matching earlier positions to the current position $r$ is

$$
\sum_{p:P_p=x}(r-p-1)=c(r-1)-s.
$$

After adding this amount to the answer, record the current position in both
tables. Initialize prefix value zero with position $0$ before scanning the
array so zero-XOR intervals beginning at index zero are included.

Every valid triplet has one unique pair of outer prefix positions $(i,k+1)$
and one legal split between them, so it is counted once by this contribution.
Conversely, each contribution comes from equal prefix XORs and therefore
constructs an interval with total XOR zero; every counted split in that
interval satisfies the original equality. This proves that the accumulated
total is exactly the requested count.

## Complexity detail
There are $n+1$ prefix positions. Each array element performs one XOR and a
constant expected number of hash-table lookups and updates, so the total time
is $O(n)$. At most $n+1$ distinct prefix XOR values can be stored across the
two tables, giving $O(n)$ auxiliary space.

## Alternatives and edge cases
- **Enumerate outer endpoints with prefix XORs:** For each `i` and `k`,
  test whether $P_i=P_{k+1}$ and add $k-i$ when they match. This is simpler
  than enumerating all three indices but still takes $O(n^2)$ time.
- **Enumerate all three indices:** Computing or comparing both adjacent XORs
  for every $(i,j,k)$ is unnecessarily expensive; even with prefix XOR
  queries, there are $O(n^3)$ candidate triplets.
- **Single element:** No indices can satisfy $i<j\le k$, so the answer is
  zero even though the initial and final prefix XOR values may be considered.
- **Repeated prefix values:** One prefix value can occur many times. Both its
  occurrence count and the sum of its positions are necessary; retaining only
  the count loses the distance-dependent number of split positions.
- **Equal adjacent values:** Two equal neighboring values have XOR zero, so
  they contribute the triplet formed by the sole split between them.
- **Large element values:** XOR operates directly on the integer bit patterns;
  the numeric magnitude up to $10^8$ does not change the algorithm or require
  an array indexed by value.
