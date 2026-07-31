## General

For every processed prefix, retain both the largest and smallest products obtainable from a non-empty subset. The minimum is as important as the maximum because multiplying a negative minimum by another negative value can create the next maximum.

Initialize both states with `nums[0]`, which enforces the non-empty requirement. When a new `value` arrives, an optimal subset of the extended prefix has one of four forms: the previous maximum unchanged, `value` alone, the previous maximum multiplied by `value`, or the previous minimum multiplied by `value`. Their maximum becomes the new maximum. The analogous minimum over the same possibilities becomes the new minimum.

Save both old states before updating either one, so every candidate refers to the same preceding prefix. The four possibilities exhaust whether the new index is omitted, starts a fresh one-element subset, or extends a previous subset whose product is an extreme. Any non-extreme previous product lies between the two extremes; multiplication by a fixed value maps its best possible result to one of those endpoints. Induction therefore proves that the final maximum is the strongest non-empty group.

## Complexity detail

Let $n$ be the number of scores. Each value performs a fixed number of multiplications and comparisons, so time is $O(n)$. Four scalar state values suffice, giving $O(1)$ auxiliary space. The benchmark uses `size` as $n$ and compares this scan with correct enumeration of all $2^n-1$ non-empty subsets.

## Alternatives and edge cases

- **Enumerate every subset:** Bitmask enumeration directly follows the definition but takes $O(n2^n)$ time.
- **Greedy sign counting:** Multiplying positives and paired negatives can achieve $O(n)$ time too, but requires careful special cases for zeros and a lone negative.
- **Track only the maximum:** This loses a large-magnitude negative product that could become optimal after multiplication by another negative.
- A single negative element must be returned because the group cannot be empty.
- Zero beats a lone negative when both are available.
- Multiple zeros do not change the best positive product when one exists.
- The old maximum and minimum must be captured before either state is overwritten.
