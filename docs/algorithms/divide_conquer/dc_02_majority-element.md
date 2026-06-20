# Majority Element (Divide and Conquer)

| | |
|---|---|
| **ID** | `dc_02` |
| **Category** | divide_conquer |
| **Complexity (required)** | $O(N \log N)$ Time, $O(\log N)$ Space |
| **Difficulty** | 4/10 |
| **Interview relevance** | 7/10 |
| **LeetCode Equivalent** | [Majority Element](https://leetcode.com/problems/majority-element/) |

## Problem statement

Given an array `nums` of size `n`, return the majority element.
The majority element is the element that appears more than `⌊n / 2⌋` times. You may assume that the majority element always exists in the array.
*Constraint:* Demonstrate how to solve this using Divide and Conquer.

**Input:** An integer array `nums`.
**Output:** An integer representing the majority element.

## When to use it

- As an academic exercise to prove you understand how to split an array and merge non-numerical boolean/statistical properties.
- *(Note: In a real interview, you should solve this using Boyer-Moore Voting (`array_05`) for $O(N)$ time and $O(1)$ space. The Divide and Conquer approach is usually requested specifically by the interviewer as a follow-up).*

## Approach

**1. The Divide and Conquer Logic:**
If an array has a majority element, then if we split the array perfectly in half, that same element MUST be the majority element of AT LEAST ONE of the two halves!
Think about it: if an element appears more than N/2 times globally, it is mathematically impossible for it to appear \le N/4 times in the left half AND \le N/4 times in the right half simultaneously.

**2. The Base Case:**
If the array slice is of size 1 (i.e., `left == right`), then that single element is trivially the "majority" element of its tiny slice! Return it.

**3. The Recursive Step (Divide):**
Find the `mid` point.
Recursively call `find_majority(left, mid)` to find the majority element of the left half. Let's call it `left_majority`.
Recursively call `find_majority(mid + 1, right)` to find the majority element of the right half. Let's call it `right_majority`.

**4. The Merge Step (Conquer):**
Now we have the proposed "champions" from the left and right halves.
- If `left_majority == right_majority`: Both halves agree! This element is undeniably the global majority. Return it.
- If `left_majority != right_majority`: The two halves disagree. We must figure out which one is the TRUE global majority for the current slice `[left...right]`.
  How? We simply loop through the current slice `[left...right]` and literally count the occurrences of `left_majority` and `right_majority`!
  Return whichever one has the higher count.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dc_02: Majority Element.

Boyer-Moore: track a candidate and a counter. Walk the array;
on each new element, if the counter is zero, promote it to
candidate. Increment on a match, decrement otherwise. The
candidate at the end is the majority element if one exists.
The setup always produces a list with a majority, so the
candidate is the answer.
"""


def solve(arr, n):
    if n == 0:
        return -1
    candidate = None
    count = 0
    for value in arr:
        if count == 0:
            candidate = value
        count += 1 if value == candidate else -1
    return candidate
```

</details>

## Walk-through

`nums = [2, 2, 1, 1, 1, 2, 2]`. N=7.

1. Split into `[2, 2, 1, 1]` and `[1, 2, 2]`.
2. **Left Half `[2, 2, 1, 1]`:**
   - Split into `[2, 2]` and `[1, 1]`.
   - `[2, 2]` returns `2` (Both sides agreed).
   - `[1, 1]` returns `1` (Both sides agreed).
   - Conquer `[2, 2, 1, 1]`: Champions are `2` and `1`.
     - Count `2` in `[2, 2, 1, 1]`: 2.
     - Count `1` in `[2, 2, 1, 1]`: 2.
     - Tie! (Returns `1` arbitrarily based on `>=` logic).
3. **Right Half `[1, 2, 2]`:**
   - Split into `[1, 2]` and `[2]`.
   - `[1, 2]` returns `2` (after counting 1 vs 1, arbitrarily picks `2`).
   - `[2]` returns `2`.
   - Conquer `[1, 2, 2]`: Champions are `2` and `2`. Agree! Returns `2`.
4. **Global Conquer `[2, 2, 1, 1, 1, 2, 2]`:**
   - Champions are `1` (from left) and `2` (from right).
   - Count `1` in global array: 3.
   - Count `2` in global array: 4.
   - 4 > 3. Returns `2`.

Result is `2`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N \log N)$ | $O(\log N)$ |
| **Average** | $O(N \log N)$ | $O(\log N)$ |
| **Worst** | $O(N \log N)$ | $O(\log N)$ |

The recursion tree has a depth of log_2(N). At each level of the tree, merging requires iterating through the subarray to count occurrences. The total work done at any specific level of the tree sums to exactly N iterations.
By the Master Theorem T(N) = 2T(N/2) + $O(N)$, the time complexity is exactly $O(N \log N)$.
Space complexity is $O(\log N)$ for the recursion call stack.

## Variants & optimizations

- **Boyer-Moore Voting Algorithm:** As mentioned, this is the $O(N)$ optimal approach. You maintain a `candidate` and a `count`. Iterate the array: if `count == 0`, set `candidate = num`. If `num == candidate`, `count += 1`, else `count -= 1`. Because the majority element appears > N/2 times, it is mathematically guaranteed to outlast the cancellations of all other elements combined!

## Real-world applications

- **Fault-Tolerant Systems (Triple Modular Redundancy):** When sensors on an aircraft send multiple slightly conflicting readings, the flight computer groups the readings recursively to find the "majority consensus" value to discard the corrupted sensor data.

## Related algorithms in cOde(n)

- **[array_05 - Boyer-Moore Voting](../arrays/array_05_boyer-moore.md)** — The strictly superior $O(N)$ method for solving this exact problem.
- **[sort_01 - Merge Sort](../sorting/sort_01_merge-sort.md)** — The classic $O(N \log N)$ algorithm that this Divide and Conquer pattern is perfectly modeled after.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
