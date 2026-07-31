## General

The definition asks about only two possible comparison positions for each index: `index - k` and `index + k`. There is no need to search a range or maintain a window because values at every other distance are irrelevant.

Scan `nums` once. The left requirement passes when the left comparison index is outside the array or the current value is strictly larger than `nums[index - k]`. The right requirement is symmetric. Add the current value only when both requirements pass. These conditions exactly match the contract: every existing required neighbor is checked, and every nonexistent neighbor is deliberately ignored. Consequently the accumulator contains precisely the sum of the good elements when the scan ends.

## Complexity detail

Let $n$ be the length of `nums`. Each index performs at most two constant-time array lookups and comparisons, so the running time is $O(n)$. The scan uses only the accumulator and a few scalar values, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Searching for comparison indices:** Scanning the whole array to rediscover positions `i - k` and `i + k` for every element is correct but takes $O(n^2)$ time unnecessarily.
- **Slicing or shifted copies:** Building left- and right-shifted arrays can express the same comparisons but uses $O(n)$ extra space.
- **Equality:** A value equal to either existing comparison element is not good because the relation must be strictly greater.
- **One-sided comparison:** Within `k` positions of an array end, only the in-bounds comparison is required.
- **Maximum permitted distance:** When $k = \lfloor n/2 \rfloor$, the same direct boundary tests continue to handle all indices correctly.
