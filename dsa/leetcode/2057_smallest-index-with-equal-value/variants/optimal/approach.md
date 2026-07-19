## General
**Order supplies the minimum**

Scan indices from left to right and compare `index % 10` with the current value. Return immediately on equality. Since every smaller index has already failed, the first match is necessarily the requested smallest one.

**Handling the absence of a match**

If the scan reaches the end, every legal index has been tested and rejected, so return `-1`. No stored history is needed: each decision depends only on the current index and value.

## Complexity detail
In the worst case, all $n$ entries are inspected once, giving $O(n)$ time. The scan keeps only the current pair and uses $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Collect all matches:** Building a list and taking its minimum is correct but uses unnecessary $O(n)$ space and cannot stop early.
- **Repeated prefix search:** Rescanning every prefix for its first match is correct but can take $O(n^2)$ time on a no-match array.
- Index zero qualifies only when `nums[0]` is zero.
- Indices at least ten compare using the repeated remainder, not their full index value.
- Several positions may qualify; only the smallest is returned.
