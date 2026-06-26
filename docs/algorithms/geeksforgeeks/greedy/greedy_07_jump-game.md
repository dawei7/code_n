# Jump Game (I and II)

| | |
|---|---|
| **ID** | `greedy_07` |
| **Category** | greedy |
| **Complexity (required)** | $O(N)$ Time, $O(1)$ Space |
| **Difficulty** | 6/10 |
| **Interview relevance** | 9/10 |
| **LeetCode Equivalent** | [Jump Game](https://leetcode.com/problems/jump-game/), [Jump Game II](https://leetcode.com/problems/jump-game-ii/) |

## Problem statement

**Jump Game I (Decision):** Given an integer array `nums`. You are initially positioned at the array's first index, and each element in the array represents your *maximum* jump length at that position. Return `true` if you can reach the last index, or `false` otherwise.

**Jump Game II (Optimization):** Same setup, but you are *guaranteed* to be able to reach the last index. Find the **minimum number of jumps** required to reach it.

**Input:** An integer array `nums`.
**Output:** A boolean (Jump Game I), or an integer (Jump Game II).

## When to use it

- To heavily optimize $O(N^2)$ Dynamic Programming array-traversal problems into $O(N)$ Greedy problems.
- Extremely common in FAANG interviews to test if you can spot overlapping forward-reaches.

## Approach: Jump Game I

**1. The "Max Reach" Tracker:**
As we iterate through the array, we want to know the absolute furthest index we can currently reach. Let's call this `max_reach`.
At index `i`, we can jump up to `nums[i]` steps. Therefore, the furthest index we can reach *from* `i` is `i + nums[i]`.
We update `max_reach = max(max_reach, i + nums[i])`.

**2. The Failure Condition:**
What if `max_reach` is sitting at index 3, and we are currently evaluating our loop at `i = 4`?
That means it was mathematically impossible to even reach index 4! We are stranded!
If `i > max_reach` at any point, we return `False`.

**3. The Success Condition:**
If at any point `max_reach >= len(nums) - 1`, we can reach the end! Return `True`.

## Approach: Jump Game II

**1. The "Window of Reach" (BFS logic disguised as Greedy):**
To minimize jumps, we shouldn't just jump as far as possible every time. What if jumping a shorter distance lands us on a massive springboard (e.g. `nums[i] = 100`)?
Instead of a single `max_reach`, we track a "window" of indices we can reach with our current number of jumps.
- `current_end`: The end of our current jump window.
- `farthest`: The absolute furthest index we have discovered so far while iterating *inside* the current window.

**2. The Greedy Trigger:**
We iterate through the array. At every step, we update `farthest = max(farthest, i + nums[i])`.
When our loop iterator `i` reaches the `current_end` of our window, it means we MUST make a jump to continue!
So, we increment our `jump_count`, and we set our new `current_end` to whatever the `farthest` index we discovered was!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for greedy_07: Jump Game.

Auto-generated from challenges/algorithms/greedy.py:SPECS.
O(n) time.
"""


def solve(arr, n):
    if n <= 1:
        return 0
    jumps = 0
    current_end = 0
    farthest = 0
    for i in range(n - 1):
        farthest = max(farthest, i + arr[i])
        if i == current_end:
            jumps += 1
            current_end = farthest
    return jumps
```

</details>

## Walk-through (Jump Game II)

`nums = [2, 3, 1, 1, 4]`. Length 5.
`jumps = 0`, `current_end = 0`, `farthest = 0`.

1. `i = 0` (val 2):
   - `farthest = max(0, 0 + 2) = 2`.
   - `i == current_end` (0 == 0).
   - `jumps = 1`. `current_end = 2`.
2. `i = 1` (val 3):
   - `farthest = max(2, 1 + 3) = 4`.
   - `i == current_end` (1 == 2) -> False.
3. `i = 2` (val 1):
   - `farthest = max(4, 2 + 1) = 4`.
   - `i == current_end` (2 == 2) -> True.
   - `jumps = 2`. `current_end = 4`.
   - `current_end >= 4`. Break!

Result `jumps = 2`. ✓ (Jump from 0 to 1, then 1 to 4).

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(1)$ |
| **Average** | $O(N)$ | $O(1)$ |
| **Worst** | $O(N)$ | $O(1)$ |

Both algorithms use a single linear pass through the array, performing $O(1)$ constant-time arithmetic at each index. Time complexity is strictly $O(N)$.
Only primitive integer variables are used (`max_reach`, `farthest`, `current_end`, `jumps`), making space complexity perfectly $O(1)$.
*(Note: Solving Jump Game II with Top-Down DP takes $O(N^2)$ time and $O(N)$ space. Greedy completely crushes DP here).*

## Variants & optimizations

- **Jump Game III (BFS):** If `nums[i]` allows you to jump FORWARD or BACKWARD to exactly `i + nums[i]` or `i - nums[i]`, the Greedy logic breaks! You must use standard Breadth-First Search (`graph_02`) to find the shortest path.
- **Jump Game VII (Sliding Window):** If you can only jump between `[i + minJump, i + maxJump]`, the overlapping intervals require a combination of Greedy and a Sliding Window or Prefix Sum array.

## Real-world applications

- **Network Routing:** Hop-count optimization in packet-switched networks where different nodes have different transmission range radii (analogous to `nums[i]`).

## Related algorithms in cOde(n)

- **[greedy_06 - Gas Station](greedy_06_gas-station.md)** — Another $O(N)$ array traversal where an accumulator decides success/failure dynamically.
- **[dp_12 - Minimum Jumps to Reach End](../dynamic/dp_12_minimum-jumps-to-reach-end.md)** — The much slower $O(N^2)$ Dynamic Programming approach to this exact problem (often taught before revealing the Greedy solution!).

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
