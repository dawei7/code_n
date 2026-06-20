# Longest Consecutive Sequence

| | |
|---|---|
| **ID** | `hash_06` |
| **Category** | hashing |
| **Complexity (required)** | $O(N)$ Time, $O(N)$ Space |
| **Difficulty** | 5/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Longest Consecutive Sequence](https://leetcode.com/problems/longest-consecutive-sequence/) |

## Problem statement

Given an unsorted array of integers `nums`, return the length of the longest consecutive elements sequence.
*Crucial constraint:* You must write an algorithm that runs in $O(N)$ time.

**Input:** An integer array `nums`.
**Output:** An integer representing the length of the longest consecutive sequence.

## When to use it

- To find connected contiguous sequences without relying on $O(N \log N)$ sorting.
- A classic test of understanding how $O(1)$ Hash Set lookups can fundamentally alter time complexity.

## Approach

**1. The Sorting Trap:**
The intuitive approach is to sort the array `[100, 4, 200, 1, 3, 2]` into `[1, 2, 3, 4, 100, 200]`, and then just run a simple $O(N)$ for-loop to count streaks.
However, sorting takes $O(N \log N)$ time, which violates the strict $O(N)$ constraint of the problem!

**2. The Hash Set:**
We throw every single number into a Hash Set. This takes $O(N)$ time and allows us to check if any specific number exists in $O(1)$ time.

**3. The Sequence Starter Insight:**
If we just iterate through the array and look up `x+1, x+2, x+3` for every number, we might end up counting the sequence `1, 2, 3, 4` four separate times! (Starting from 1, starting from 2, etc.). This would degrade into $O(N^2)$ time.
How do we ensure we only count a sequence ONCE?
**We ONLY start counting if the current number is the BEGINNING of a sequence!**
How do we know if `x` is the beginning?
Simple: If `x - 1` does NOT exist in the Hash Set!
If `x - 1` exists, `x` is in the middle of some sequence. We completely ignore it and let the `x - 1` iteration handle it!

**4. The Algorithm:**
1. Create a Hash Set of all numbers.
2. Iterate through the `nums` array.
3. For each `num`:
   - Check if `num - 1` is in the set.
   - If YES: Do nothing.
   - If NO: We found a sequence starter! Enter a `while` loop, checking if `num + 1`, `num + 2`, etc., exist in the set. Keep a running tally of the `current_streak`.
4. Update `longest_streak = max(longest_streak, current_streak)`.

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for hash_06: Longest Consecutive Sequence.

Given an unsorted array, return the length of the longest
sequence of consecutive integers. Sort, then walk; O(n
log n). Real O(n) solution uses a set.
"""


def solve(arr, n):
    if n == 0:
        return 0
    s = sorted(set(arr))
    best = 1
    cur = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1] + 1:
            cur += 1
            if cur > best:
                best = cur
        else:
            cur = 1
    return best
```

</details>

## Walk-through

`nums = [100, 4, 200, 1, 3, 2]`.
`num_set = {1, 2, 3, 4, 100, 200}`.
`longest_streak = 0`.

1. `num = 100`:
   - Is `99` in set? NO. Starter found!
   - `while(101 in set)`? NO.
   - `current_streak = 1`. `longest_streak = 1`.
2. `num = 4`:
   - Is `3` in set? YES. Not a starter! Skip.
3. `num = 200`:
   - Is `199` in set? NO. Starter found!
   - `while(201 in set)`? NO.
   - `current_streak = 1`. `longest_streak = 1`.
4. `num = 1`:
   - Is `0` in set? NO. Starter found!
   - `while(2 in set)`? YES. `streak=2`, `curr=2`.
   - `while(3 in set)`? YES. `streak=3`, `curr=3`.
   - `while(4 in set)`? YES. `streak=4`, `curr=4`.
   - `while(5 in set)`? NO. End while loop.
   - `longest_streak = max(1, 4) = 4`.
5. `num = 3`:
   - Is `2` in set? YES. Skip.
6. `num = 2`:
   - Is `1` in set? YES. Skip.

Result `4`. ✓ (The sequence is `1, 2, 3, 4`).

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(N)$ |
| **Average** | $O(N)$ | $O(N)$ |
| **Worst** | $O(N)$ | $O(N)$ |

You might see a `while` loop inside a `for` loop and assume it's $O(N^2)$.
However, the `while` loop ONLY executes for sequence starters. Every single number in the entire array is visited inside the `while` loop exactly ONCE across the entire runtime of the algorithm!
Therefore, the total time spent traversing sequences is bounded by $O(N)$. Combined with the outer $O(N)$ loop, the time complexity is strictly amortized $O(N)$.
Space complexity is $O(N)$ to store the Hash Set.

## Variants & optimizations

- **Union-Find Disjoint Set:** You can also solve this in $O(N \cdot \alpha(N)$) time without a Hash Set by treating each number as a Graph Node, and running Union-Find (`graph_09`) to connect `num` and `num+1` into components. The answer is just the size of the largest connected component!

## Real-world applications

- **Blockchain / Log Continuity:** Verifying that a massive, out-of-order dump of block heights or packet sequence IDs contains no gaps, and finding the longest unbroken chain of valid continuous data.

## Related algorithms in cOde(n)

- **[hash_01 - Two Sum](hash_01_two-sum.md)** — Uses the exact same $O(N)$ set/map lookup trick to replace what would intuitively be an $O(N^2)$ brute force loop.
- **[graph_09 - Union-Find](../graphs/graph_09_union-find.md)** — The graphical alternative approach to grouping consecutive elements together.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
