## General

**Split matching indices around the current position**

First record, for every value, its total occurrence count and the sum of all
indices carrying it. During a second left-to-right pass, also maintain the
count and index sum already seen for each value.

At index $i$, let $c_L$ matching indices lie to the left with sum $s_L$.
Their total distance is

$$
i c_L-s_L.
$$

After removing those indices and $i$ itself from the totals, let $c_R$ and
$s_R$ describe the matching indices to the right. Their contribution is

$$
s_R-i c_R.
$$

Adding the two expressions gives the answer at $i$ in constant time. Then add
$i$ to its value's seen count and sum.

Every matching index lies on exactly one side of $i$ or equals $i$. The left
formula expands $\sum(i-j)$ over earlier matches, and the right formula expands
$\sum(j-i)$ over later matches; the equal index contributes zero. Thus every
required absolute distance is included exactly once and no different value is
included.

## Complexity detail

Both passes process each of the $n$ indices once with expected constant-time
hash-map operations, for $O(n)$ time. The maps and returned list may contain
$O(n)$ entries, so space usage is $O(n)$.

## Alternatives and edge cases

- **Compare every pair:** For each index, scan the entire array and add
  distances to equal values. This is direct but takes $O(n^2)$ time.
- **Store grouped index lists:** Build each value's sorted occurrence list and
  use a prefix sum within every group. This also achieves $O(n)$ time and
  space.
- A value occurring once has distance sum zero.
- The current index may be included because its self-distance is zero.
- Interleaved value groups remain independent.
- Distance sums may exceed 32-bit range, so fixed-width implementations need
  64-bit result arithmetic.
