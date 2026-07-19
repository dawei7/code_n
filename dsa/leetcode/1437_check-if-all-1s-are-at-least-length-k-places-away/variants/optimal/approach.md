## General
**Remember only the most recent one.** Scan `nums` from left to right and store the index `previous` of the last encountered `1`. Zero entries require no update.

**Translate the spacing rule into an index gap.** At a new one at index `i`, there are `i - previous - 1` positions between it and the preceding one. The requirement fails exactly when this count is smaller than `k`, equivalently when `i - previous <= k`. Return `false` immediately in that case; otherwise update `previous = i`.

**Why consecutive ones are sufficient.** Among all earlier ones, the most recent has the largest index and therefore the smallest distance to the current one. If the current one is far enough from that nearest predecessor, it is even farther from every earlier one. Checking each consecutive pair of ones consequently proves the condition for every pair. If no check fails, return `true`.

## Complexity detail
The scan examines each of the $n$ entries once, giving $O(n)$ time. One previous index is retained, so auxiliary space is $O(1)$.

## Alternatives and edge cases
- **Compare every pair of ones:** This directly checks the definition but can take $O(n^2)$ time when the array contains many ones.
- **Collect all one indices:** Comparing adjacent collected indices is linear but uses $O(n)$ extra space unnecessarily.
- **No ones or one one:** There is no pair that can violate the condition, so return `true`.
- **Zero required spacing:** Every binary array is valid because adjacent ones have zero positions between them.
- **Exact boundary:** An index gap of `k + 1` leaves exactly `k` positions and is valid.
- **Leading and trailing zeroes:** They do not affect distances between ones.
