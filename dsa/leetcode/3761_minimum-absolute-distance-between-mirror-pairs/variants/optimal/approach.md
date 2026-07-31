## General

Scan indices from left to right. Before processing index `j`, store earlier indices keyed by the value obtained after reversing their array element. A lookup under `nums[j]` therefore finds exactly an earlier index `i` satisfying `reverse(nums[i]) == nums[j]`; reversing the current value instead would incorrectly make the directional condition symmetric.

For each reversed-value key, retain only its latest earlier index. If two earlier indices produce the same key, the later one is closer to every future `j`, so the older index can never yield a better distance. After checking the current value against the map, reverse it and store `j` under that result for future positions. The smallest possible distance is one, allowing an immediate return when it is found.

Decimal reversal can be performed by repeatedly taking the last digit and appending it to a new integer. This naturally removes leading zeros from the reversed representation because zeros extracted first do not change the accumulating value.

## Complexity detail

Let $n$ be the array length. Each value contains at most ten decimal digits under the given bound, so reversal takes constant bounded work and the full scan takes expected $O(n)$ time using a hash table. At most one map entry is stored per processed index, giving $O(n)$ auxiliary space.

## Alternatives and edge cases

- **Enumerate all index pairs:** Reversing each left value and checking every later position is correct but takes $O(n^2)$ time.
- **Reverse the later value:** This is wrong for values ending in zero because the definition reverses only `nums[i]`.
- **Store the earliest index:** The earliest occurrence creates longer future distances; keep the latest index for each reversed key instead.
- **Trailing zeros:** Arithmetic reversal turns `120` into `21`, matching the source's omitted-leading-zero rule.
- **Palindromic values:** Two occurrences of a decimal palindrome form a mirror pair because reversal leaves the value unchanged.
- **No match:** If no lookup succeeds, return `-1` rather than the initial sentinel distance.
