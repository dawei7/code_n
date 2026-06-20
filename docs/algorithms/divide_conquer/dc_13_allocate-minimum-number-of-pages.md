# Allocate Minimum Number of Pages

| | |
|---|---|
| **ID** | `dc_13` |
| **Category** | divide_conquer |
| **Complexity (required)** | $O(N log(Sum - Max)$) Time, $O(1)$ Space |
| **Difficulty** | 8/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Split Array Largest Sum](https://leetcode.com/problems/split-array-largest-sum/) |

## Problem statement

Given an array of integer `arr` of size `N`, where `arr[i]` represents the number of pages in the i-th book.
There are `M` students. Your task is to allocate all the books to the students such that:
1. Every student gets at least one book.
2. Each book is allocated to only one student.
3. Book allocation is strictly contiguous (e.g., a student cannot get book 1 and book 3 without getting book 2).
The objective is to **minimize the maximum number of pages** assigned to any single student.

**Input:** An integer array `arr` and an integer `M`.
**Output:** An integer representing the minimized maximum number of pages. Return -1 if allocation is impossible (M > N).

## When to use it

- The absolute most famous "Binary Search on Answer Space" problem (often colloquially called Min-Max or Max-Min).
- If a problem asks you to "Minimize the Maximum X" or "Maximize the Minimum Y" across contiguous subarrays, it is almost certainly solved using this pattern.

## Approach

**1. Define the Answer Space (Decrease and Conquer):**
What is the absolute *minimum* possible answer? If we had M=N students, each student gets exactly one book. The student who gets the thickest book determines the maximum pages. Thus, the minimum possible answer is `max(arr)`.
What is the absolute *maximum* possible answer? If we only had M=1 student, that poor student has to read EVERY book. Thus, the maximum possible answer is `sum(arr)`.
The perfect optimal answer MUST lie somewhere in the continuous integer range `[max(arr), sum(arr)]`.

**2. The Validation Function (The "Is it Possible?" test):**
If I pick a random number `mid` from that range (let's say 50 pages), how do I know if it's possible to allocate the books such that NO student reads MORE than 50 pages?
We just greedily hand out books!
- `current_pages = 0`, `students_needed = 1`.
- Iterate through the books.
- If `current_pages + book > mid`, we can't give this book to the current student! They would exceed the 50-page limit.
- We must hand this book to a NEW student. `students_needed += 1`, `current_pages = book`.
- After checking all books, if `students_needed > M`, then 50 pages is strictly too small! We forced too many students to exist.

**3. The Binary Search:**
- Binary search `mid` between `low = max(arr)` and `high = sum(arr)`.
- If `is_possible(mid)` is TRUE: It means `mid` pages is a valid ceiling! But we want to MINIMIZE the maximum. So we save `mid` as a candidate `ans`, and try an even smaller ceiling: `high = mid - 1`.
- If `is_possible(mid)` is FALSE: `mid` pages is too restrictive (requires too many students). We must increase our ceiling: `low = mid + 1`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for dc_13: Allocate Minimum Number of Pages.

Given an array arr[] of n book page counts and m
"""


def solve(arr, n, m):
    """Binary search on the answer.

    Low = max(arr) (one student reads the longest book alone).
    High = sum(arr) (one student reads everything).
    The first `mx` for which we can split into <= m blocks
    is the answer.
    """
    lo = max(arr) if arr else 0
    hi = sum(arr)
    while lo < hi:
        mid = (lo + hi) // 2
        # Greedy: how many students do we need for max = mid?
        needed = 1
        pages = 0
        for pages_i in arr:
            if pages + pages_i <= mid:
                pages += pages_i
            else:
                needed += 1
                pages = pages_i
        if needed <= m:
            hi = mid
        else:
            lo = mid + 1
    return lo
```

</details>

## Walk-through

`arr = [12, 34, 67, 90]`, `m = 2`.
`low = max(arr) = 90`.
`high = sum(arr) = 203`.

1. **Loop 1:**
   - `mid = (90 + 203) // 2 = 146`.
   - `is_possible(146)`:
     - S1 gets 12, 34, 67 (Total 113. Next book 90 makes 203 > 146).
     - S2 gets 90.
     - `students_needed = 2`. `2 <= 2`. True!
   - `ans = 146`. Move lower: `high = 146 - 1 = 145`.
2. **Loop 2:**
   - `mid = (90 + 145) // 2 = 117`.
   - `is_possible(117)`:
     - S1 gets 12, 34, 67 (Total 113. Next 90 makes 203 > 117).
     - S2 gets 90.
     - `students_needed = 2`. `2 <= 2`. True!
   - `ans = 117`. Move lower: `high = 117 - 1 = 116`.
3. **Loop 3:**
   - `mid = (90 + 116) // 2 = 103`.
   - `is_possible(103)`:
     - S1 gets 12, 34 (Total 46. Next 67 makes 113 > 103).
     - S2 gets 67. (Total 67. Next 90 makes 157 > 103).
     - S3 gets 90.
     - `students_needed = 3`. `3 <= 2`. FALSE!
   - Ceiling is too tight. Move higher: `low = 103 + 1 = 104`.
*(... Binary search narrows in on 113 ...)*

Result is `113`. ✓ (S1 gets `12+34+67=113`, S2 gets `90`. The max is `113`).

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(1)$ |
| **Average** | $O(N * log(Sum - Max)$) | $O(1)$ |
| **Worst** | $O(N * log(Sum - Max)$) | $O(1)$ |

The binary search range size is `S - M` (where `S` is sum, `M` is max). The while loop runs log(S-M) times.
Inside the while loop, `is_possible` runs an $O(N)$ linear scan of the array.
Total time complexity is strictly $O(N log(Sum - Max)$).
Space complexity is $O(1)$.

## Variants & optimizations

- **Koko Eating Bananas (LeetCode 875):** "Minimize the eating speed K such that Koko eats all bananas within H hours." The exact same algorithm! Answer space is `[1, max(piles)]`. `is_possible(K)` just sums `ceil(pile / K)` and checks if it's \le H.
- **Aggressive Cows (SPOJ):** "Maximize the minimum distance between C cows placed in N stalls." Answer space `[1, max(stalls) - min(stalls)]`. Binary search for the maximum valid distance!

## Real-world applications

- **Load Balancing:** Distributing contiguous chunks of a sequential batch-processing job (like a massive video rendering timeline) across M worker servers, such that the server with the heaviest load finishes as quickly as possible.

## Related algorithms in cOde(n)

- **[searching_01 - Binary Search](../searching/search_01_binary-search.md)** — The foundation of this algorithmic pattern.
- **[dc_10 - Floor Square Root](dc_10_floor-square-root.md)** — Another application of Binary Search on a continuous Answer Space.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
