## General

Because the array length is odd, integer division identifies its single middle index as `len(nums) // 2`. Save the value at that position before examining frequencies; sorting would change which value is positional middle and is neither permitted nor useful.

Scan `nums` while counting only entries equal to the saved middle value. The middle position itself guarantees the count reaches at least one. If a second match is encountered, the required frequency can no longer be exactly one, so return `False` immediately. If the scan ends without a second match, the middle position supplied the sole occurrence and return `True`.

This reasoning covers both directions. Returning `False` is justified by two observed positions holding the middle value. Returning `True` is justified because every array position has been examined and exactly the mandatory middle occurrence was found. Repetitions of any other value are deliberately ignored.

## Complexity detail

Let $n = \lvert\texttt{nums}\rvert$. In the worst case the middle value is unique and all $n$ entries must be inspected, so the running time is $O(n)$. The algorithm stores only the middle value and an occurrence counter, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Built-in count:** Comparing `nums.count(nums[len(nums) // 2])` with one is equally $O(n)$ and concise, but the explicit scan makes the early rejection and constant-space reasoning visible.
- **Frequency map:** Counting every value also takes $O(n)$ time but uses $O(U)$ extra space for $U$ distinct integers even though only one frequency matters.
- **Sort before counting:** Saving the positional middle and then sorting permits an $O(n\log n)$ count, but sorting first changes the selected value and answers a different question about the median.
- **Single element:** Its only value is necessarily both the middle element and its sole occurrence, so the result is `True`.
- **Other duplicated values:** They are irrelevant unless they equal the value at the middle index.
- **Duplicate on either side:** A matching value before or after the middle position is enough to make the result `False`.
