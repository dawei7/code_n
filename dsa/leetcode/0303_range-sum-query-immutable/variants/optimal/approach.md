## General
**Store sums at boundaries, not at elements**

Build `prefix` with one leading zero, where `prefix[i]` equals the sum of the first `i` array elements. The extra entry makes every array boundary—including the boundary before index zero—addressable without a special case.

For an inclusive query `[left, right]`, `prefix[right + 1]` contains the desired range plus everything before `left`. Subtracting `prefix[left]` cancels that earlier prefix and leaves exactly the requested sum.

**Immutability makes one preprocessing pass reusable**

Because `nums` never changes, every prefix value remains correct for the lifetime of the query object. Construction performs the only element-by-element accumulation. Each later query needs two reads and one subtraction, regardless of range width.

For `[-2,0,3,-5,2,-1]`, the prefix array is `[0,-2,-2,1,-4,-2,-3]`. Query `[2,5]` returns `prefix[6] - prefix[2] = - 3 - ( - 2) = - 1`.

**Prefix subtraction includes every requested index exactly once**

By definition,
`prefix[right + 1] = nums[0] + ... + nums[right]`
and
`prefix[left] = nums[0] + ... + nums[left - 1]`.
Their difference cancels precisely the indices before `left`, while indices `left` through `right` occur only in the first sum. Thus every returned value equals its inclusive range sum.

## Complexity detail
Building $n + 1$ prefix entries takes $O(n)$ time. Each of the `q` queries takes $O(1)$, for $O(n + q)$ total time. The prefix array uses $O(n)$ auxiliary space; the returned query results are output storage.

## Alternatives and edge cases
- **Sum each requested slice directly:** uses no preprocessing but costs $O(range length)$ per query and can reach $O(nq)$.
- **Segment tree or Fenwick tree:** supports updates, but immutability makes its logarithmic query cost and additional machinery unnecessary.
- Single-element and full-array queries follow the same subtraction formula. Negative values and zero totals require no special handling.
