## General
**Express every range sum as an ordered prefix pair**

Build prefix sums with an initial zero. The sum of `nums[i:j]` is `prefix[j] - prefix[i]`, so a valid subarray corresponds to an ordered pair $i < j$ satisfying `lower <= prefix[j] - prefix[i] <= upper`.

A divide-and-conquer split counts three disjoint groups: pairs entirely in the left prefix half, pairs entirely in the right half, and cross pairs whose earlier index is left of the split and later index is right of it. Recursive calls count the first two groups and leave each half sorted by prefix value.

**Two monotone boundaries count all cross pairs**

For one left-half prefix value `P`, scan the sorted right half with two pointers. Advance the first while `right - P < lower`; advance the second while `right - P <= upper`. The half-open interval between them contains exactly the valid right prefixes for `P`.

As left values are visited in sorted order, both numeric thresholds `P + lower` and `P + upper` only increase. Neither right pointer ever moves backward, so all cross pairs at one recursion level are counted in linear time. The strict comparison at the lower pointer and inclusive comparison at the upper pointer are what make both range endpoints inclusive.

**Merge the halves instead of sorting them again**

After counting, merge the two sorted prefix halves into one auxiliary buffer and copy that interval back. A fresh `sorted()` call at every recursion node would add an extra logarithmic factor; the linear merge preserves the standard merge-sort bound.

Every valid ordered prefix pair belongs uniquely to the left recursion, right recursion, or cross group of its first separating recursion node. The two-pointer window counts every cross pair exactly once, and the merge changes only value order used by ancestors—not the already enforced original-index side of the split. Thus the final count is exact.

## Complexity detail
Each recursion level performs linear cross-pair scanning and linear merging across all prefix values. There are $O(\log n)$ levels, giving $O(n \log n)$ time. The prefix array, merge buffer, and recursion stack use $O(n)$ space overall.

## Alternatives and edge cases
- **Enumerate all subarrays with rolling sums:** avoids recomputing sums but still takes $O(n^2)$ time.
- **Fenwick tree with coordinate compression:** also achieves $O(n \log n)$ by querying prior prefixes inside a numeric interval.
- **Sliding window:** fails because negative values destroy monotonicity of the running sum.
- Repeated equal prefixes represent distinct index pairs and must all be counted. Equal lower and upper bounds are valid, and prefix sums may exceed 32-bit range even when individual values do not.
