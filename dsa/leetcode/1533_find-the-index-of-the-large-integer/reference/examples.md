## Examples

**Example 1**

- **Input:** `reader = [7, 7, 7, 7, 10, 7, 7, 7]`
- **Output:** `4`
- **Explanation:** Equal-length half comparisons isolate the half containing 10. `compareSub(0, 3, 4, 7)` returns -1 because `7+7+7+7 = 28 < 10+7+7+7 = 31`. Further halving of range $[4, 7]$ finds index 4.

**Example 2**

- **Input:** `reader = [6, 6, 12]`
- **Output:** `2`
- **Explanation:** Comparing the first two singleton candidates `compareSub(0, 0, 1, 1)` returns 0 because `6 == 6`. Equality proves neither index 0 nor 1 holds the larger value, so the unpaired index 2 is the answer.

**Example 3**

- **Input:** `reader = [9, 12]`
- **Output:** `1`
- **Explanation:** One singleton comparison `compareSub(0, 0, 1, 1)` returns -1 because `9 < 12`, identifying index 1.
