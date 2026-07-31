## General

Every character value present in the original string must remain at least once. An operation deletes an occurrence only when another equal occurrence is chosen as its reference. Therefore, it is impossible to remove the final copy of any distinct letter, and the number of distinct characters is a lower bound on the minimized length.

That lower bound is attainable. Whenever a character appears more than once, choose any occurrence that has another equal occurrence on one side. The closest equal occurrence on that side can be deleted. Repeating this removes copies one at a time until exactly one remains. Operations on one letter never create or destroy occurrences of another letter.

Consequently the minimum length is exactly the number of distinct characters in `s`. A set built during one scan records those values, and its final size is the answer; the deletion sequence itself never needs to be constructed.

## Complexity detail

Let $n$ be the length of `s`. Building the set takes $O(n)$ expected time. Because the alphabet contains only $26$ lowercase English letters, the set occupies $O(1)$ space. The benchmark uses `size` as $n$ and contrasts this scan with explicit repeated deletion and shifting.

## Alternatives and edge cases

- **Frequency array:** A fixed array of $26$ counters also takes $O(n)$ time and $O(1)$ space; count its nonzero entries.
- **Simulate deletions:** Removing duplicate occurrences one by one is correct, but mutable-list shifting or immutable-string rebuilding can take $O(n^2)$ time.
- **Sort the string:** Adjacent changes in sorted order reveal the distinct count, but sorting costs $O(n\log n)$ time.
- A length-one string already has its minimum possible length.
- An all-equal string reduces to length one, not zero.
- The location and distance between equal characters do not affect attainability.
- When all characters are distinct, no operation is possible and the original length is returned.

