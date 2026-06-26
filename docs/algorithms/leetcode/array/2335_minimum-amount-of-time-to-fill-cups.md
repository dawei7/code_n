# Minimum Amount of Time to Fill Cups

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2335 |
| Difficulty | Easy |
| Topics | Array, Greedy, Sorting, Heap (Priority Queue) |
| Official Link | [minimum-amount-of-time-to-fill-cups](https://leetcode.com/problems/minimum-amount-of-time-to-fill-cups/) |

## Problem Description & Examples
### Goal
Given the initial counts of cold, warm, and hot water cups, determine the minimum number of seconds required to fill all of them. In one second, you can either fill a single cup of any type, or fill two cups of different types.

### Function Contract
**Inputs**

- `amount`: `List[int]` - A list of three non-negative integers `[cold, warm, hot]` representing the initial number of cups of each type. Each element `amount[i]` will be between `0` and `100`.

**Return value**

`int` - The minimum time in seconds to fill all cups.

### Examples
**Example 1**

- Input: `amount = [1, 4, 2]`
- Output: `4`
- Explanation:
    - Second 1: Fill 1 warm and 1 hot cup. `amount = [1, 3, 1]`
    - Second 2: Fill 1 warm and 1 hot cup. `amount = [1, 2, 0]`
    - Second 3: Fill 1 cold and 1 warm cup. `amount = [0, 1, 0]`
    - Second 4: Fill 1 warm cup. `amount = [0, 0, 0]`
    Total time: 4 seconds.

**Example 2**

- Input: `amount = [5, 4, 4]`
- Output: `7`
- Explanation:
    - Second 1: Fill 1 cold and 1 warm cup. `amount = [4, 3, 4]`
    - Second 2: Fill 1 cold and 1 hot cup. `amount = [3, 3, 3]`
    - Second 3: Fill 1 cold and 1 warm cup. `amount = [2, 2, 3]`
    - Second 4: Fill 1 cold and 1 hot cup. `amount = [1, 2, 2]`
    - Second 5: Fill 1 warm and 1 hot cup. `amount = [1, 1, 1]`
    - Second 6: Fill 1 cold and 1 warm cup. `amount = [0, 0, 1]`
    - Second 7: Fill 1 hot cup. `amount = [0, 0, 0]`
    Total time: 7 seconds.

**Example 3**

- Input: `amount = [0, 0, 0]`
- Output: `0`
- Explanation: No cups to fill, so 0 seconds.

---

## Underlying Base Algorithm(s)
This problem can be efficiently solved using a greedy approach, which can be simplified into a direct mathematical formula due to the small, fixed number of cup types (three).

1.  **Greedy Approach (Conceptual):**
    At each second, to minimize the total time, we should prioritize filling two cups of *different* types. This strategy maximizes the reduction in the total number of cups per second. If we can fill two cups, we should always pick the two types that currently have the highest remaining counts. This ensures we reduce the "tallest" stacks of cups, preventing any single type from becoming an overwhelming bottleneck. This process continues until all cups are filled. This can be implemented using a max-heap (priority queue) to efficiently retrieve the two largest counts, or by repeatedly sorting the three cup counts.

2.  **Mathematical Observation (Optimal):**
    Let the counts of the three cup types be `a, b, c` after sorting them in non-decreasing order (i.e., `a <= b <= c`). Let `total_cups = a + b + c`.

    There are two primary scenarios that dictate the minimum time:

    *   **Scenario 1: The largest count `c` is not excessively large compared to the sum of the other two (`c <= a + b`).**
        In this situation, we can always find pairs of different cup types to fill. We can effectively fill two cups per second for most of the duration. The total time will be determined by the total number of cups. Since we fill at most two cups per second, the minimum time is `ceil(total_cups / 2)`. This is because we can always pair the largest with the second largest, or the largest with the smallest, ensuring we reduce the counts as evenly as possible.

    *   **Scenario 2: The largest count `c` is excessively large (`c > a + b`).**
        Here, `c` is the bottleneck. Even if we continuously pair `c` with `a` and `b` until `a` and `b` are completely exhausted, `c` will still have remaining cups. We will spend `a + b` seconds pairing `c` with `a` and `b` (e.g., `a` seconds pairing `c` with `a`, then `b` seconds pairing `c` with `b`). After these `a + b` seconds, `a` and `b` will become 0, and `c` will be reduced to `c - (a + b)`. The remaining `c - (a + b)` cups of type `c` must then be filled one by one, as there are no other types left to pair with. The total time will therefore be `(a + b) + (c - (a + b)) = c`.

    Combining these two scenarios, the minimum time is `max(c, ceil(total_cups / 2))`. This formula elegantly covers both cases.

---

## Complexity Analysis
- **Time Complexity**: `O(1)`.
    Sorting an array of a fixed size (3 elements) takes constant time. The subsequent calculations (sum, max, division) are also constant time operations.
- **Space Complexity**: `O(1)`.
    Only a few variables are used to store cup counts and intermediate results, independent of the input values.
