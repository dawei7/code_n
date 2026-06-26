# Activity Selection Problem

| | |
|---|---|
| **ID** | `greedy_01` |
| **Category** | greedy |
| **Complexity (required)** | $O(N \log N)$ Time, $O(1)$ Space |
| **Difficulty** | 3/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Maximum Length of Pair Chain](https://leetcode.com/problems/maximum-length-of-pair-chain/) |

## Problem statement

Given `N` activities with their start and finish times. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.
Two activities `i` and `j` are non-conflicting if finish\_time[i] \le start\_time[j].

**Input:** Two arrays `start[]` and `finish[]` representing the start and end times of `N` activities.
**Output:** An integer representing the maximum number of activities that can be completed.

## When to use it

- Any problem involving scheduling the maximum number of non-overlapping intervals (Meetings, Tasks, Pair Chains).
- The absolute quintessential introductory Greedy algorithm.

## Approach

**1. The Greedy Choice:**
If you want to pack as many activities into your day as possible, which activity should you always pick first?
- The one that starts the earliest? No, an activity could start at 8:00 AM and last 10 hours, ruining your whole day!
- The shortest activity? No, a short activity might be scheduled right in the middle of the day, forcing you to drop two longer but perfectly placed activities.
- **The one that finishes the earliest!** The earlier an activity finishes, the more "free time" you leave remaining in the rest of your day to pack in other activities!

**2. The Algorithm:**
Combine the `start[]` and `finish[]` arrays into a list of tuples `(start, finish)`.
Sort the list of tuples based purely on their **Finish Time** in ascending order.
Always pick the very first activity in the sorted list.
Then, iterate through the rest of the list. If an activity's start time is \ge the finish time of the *last activity you picked*, pick it! Update your "last finish time" to this new activity's finish time.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for greedy_01: Activity Selection.

Auto-generated from challenges/algorithms/greedy.py:SPECS.
O(n log n) time.
"""


def solve(start, finish, n):
    pairs = sorted(zip(start, finish), key=lambda p: p[1])
    if not pairs:
        return 0
    count = 1
    last_finish = pairs[0][1]
    for s, f in pairs[1:]:
        if s >= last_finish:
            count += 1
            last_finish = f
    return count
```

</details>

## Walk-through

`start = [1, 3, 0, 5, 8, 5]`, `finish = [2, 4, 6, 7, 9, 9]`.

1. Zip and Sort by finish time:
   `[(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]`
2. Pick the first activity: `(1, 2)`.
   `count = 1`. `last_finish = 2`.
3. Check `(3, 4)`. Start `3 >= 2`? YES!
   `count = 2`. `last_finish = 4`.
4. Check `(0, 6)`. Start `0 >= 4`? NO! Skip.
5. Check `(5, 7)`. Start `5 >= 4`? YES!
   `count = 3`. `last_finish = 7`.
6. Check `(8, 9)`. Start `8 >= 7`? YES!
   `count = 4`. `last_finish = 9`.
7. Check `(5, 9)`. Start `5 >= 9`? NO! Skip.

Result `count = 4`. ✓

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N \log N)$ | $O(N)$ |
| **Average** | $O(N \log N)$ | $O(N)$ |
| **Worst** | $O(N \log N)$ | $O(N)$ |

Zipping the arrays and iterating through them takes $O(N)$ time.
Sorting the array of tuples takes $O(N \log N)$ time.
Thus, the sort dominates. Time complexity is $O(N \log N)$.
Space complexity is $O(N)$ to store the combined array of tuples (though if the input is already provided as a single array of objects, space can be $O(1)$ assuming an in-place sort like Quicksort/Heapsort).

## Variants & optimizations

- **Non-overlapping Intervals (LeetCode 435):** Asks for the minimum number of intervals you need to *remove* to make the rest non-overlapping. This is the exact same problem in reverse! The answer is `N - max_activities()`.
- **Minimum Number of Meeting Rooms:** A famous variation! If you are asked how many parallel rooms you need to host ALL activities, sorting by finish time fails. Instead, you must separate start and finish times into two separate sorted arrays, and use a Two-Pointer sliding window approach to track concurrent overlaps!

## Real-world applications

- **CPU Task Scheduling:** An operating system's job scheduler maximizing the throughput of batch processes on a single-core machine.

## Related algorithms in cOde(n)

- **[greedy_04 - Job Sequencing Problem](greedy_04_job-sequencing.md)** — A slightly more advanced scheduling problem where jobs have deadlines and monetary profits.
- **[sort_04 - Merge Sort](../sorting/sort_04_merge-sort.md)** — The $O(N \log N)$ sorting algorithm running under the hood of `activities.sort()`.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
