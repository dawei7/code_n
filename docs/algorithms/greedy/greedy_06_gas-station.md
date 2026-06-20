# Gas Station (Circular Tour)

| | |
|---|---|
| **ID** | `greedy_06` |
| **Category** | greedy |
| **Complexity (required)** | $O(N)$ Time, $O(1)$ Space |
| **Difficulty** | 5/10 |
| **Interview relevance** | 8/10 |
| **LeetCode Equivalent** | [Gas Station](https://leetcode.com/problems/gas-station/) |

## Problem statement

There are `N` gas stations along a circular route. You are given two integer arrays:
1. `gas[i]`: The amount of gas available at station i.
2. `cost[i]`: The amount of gas required to travel from station i to the next station (i+1) \pmod N.

You start with an empty tank. Return the starting gas station's index if you can travel around the circuit exactly once in the clockwise direction. If it's impossible, return `-1`.
*Constraint:* If a solution exists, it is guaranteed to be unique.

**Input:** Two arrays `gas` and `cost` of size `N`.
**Output:** An integer representing the starting index, or `-1`.

## When to use it

- This is the classic "$O(N^2)$ to $O(N)$ Greedy Single-Pass" interview question.
- Whenever a problem involves completing a circular sequence where cumulative resource gains must outpace cumulative resource drains.

## Approach

**1. The Brute Force:**
Start at index 0. Simulate driving in a circle. If you run out of gas, stop, move the starting point to index 1, and simulate the circle again. This takes $O(N^2)$ time.

**2. Greedy Insight 1 (The Impossible Condition):**
If the total amount of gas available on the entire route is strictly LESS than the total cost of driving the entire route, a circular tour is mathematically impossible, regardless of where you start!
Therefore, if `sum(gas) < sum(cost)`, return `-1` immediately.
*Corollary:* If `sum(gas) >= sum(cost)`, a valid starting point is mathematically guaranteed to exist!

**3. Greedy Insight 2 (The Reset Condition):**
Let's say we start at Station 0 and successfully drive to Station 1, 2, and 3. But when we try to drive from 3 to 4, our tank drops below 0. We failed.
Should we try starting at Station 1? NO!
Because we started at 0 with 0 gas, and arrived at 1 with \ge 0 gas. Starting at 1 with 0 gas is strictly worse! The exact same logic applies to Station 2 and 3.
**If starting at `A` fails to reach `B`, then ANY station between `A` and `B` will also fail to reach `B`!**
The next logical place to attempt starting is `B + 1`!

**4. The Single Pass Algorithm:**
Iterate through the array. Maintain a `current_tank`.
At each station, `current_tank += gas[i] - cost[i]`.
If `current_tank` dips below 0, we failed to reach i+1. We set our `start_index` to i+1, and reset `current_tank` to 0!
Because of Insight 1, if we finish the array and the global sum is \ge 0, whatever `start_index` is currently pointing at is mathematically guaranteed to be the correct answer! We don't even need to simulate the "circular" wrap-around!

## Algorithm

<details>
<summary>Show Algorithm</summary>

```python
"""Optimal solution for greedy_06: Gas Station.

Auto-generated from challenges/algorithms/greedy.py:SPECS.
O(n) time.
"""


def solve(gas, cost, n):
    if sum(gas) < sum(cost):
        return -1
    tank = 0
    start = 0
    for i in range(n):
        tank += gas[i] - cost[i]
        if tank < 0:
            start = i + 1
            tank = 0
    return start
```

</details>

## Walk-through

`gas = [1, 2, 3, 4, 5]`, `cost = [3, 4, 5, 1, 2]`.

1. `i=0` (gas=1, cost=3). `tank = -2`.
   - `tank < 0`! Reset: `start_index = 1`. `tank = 0`.
2. `i=1` (gas=2, cost=4). `tank = -2`.
   - `tank < 0`! Reset: `start_index = 2`. `tank = 0`.
3. `i=2` (gas=3, cost=5). `tank = -2`.
   - `tank < 0`! Reset: `start_index = 3`. `tank = 0`.
4. `i=3` (gas=4, cost=1). `tank = 3`.
   - `tank >= 0`. Keep going!
5. `i=4` (gas=5, cost=2). `tank = 3 + (5-2) = 6`.
   - `tank >= 0`. Loop ends.

Check totals:
`total_gas = 15`. `total_cost = 15`.
`15 >= 15`. Return `start_index = 3`. ✓
*(Starting at index 3: gas goes 4->7->6->4->3. Never dips below 0!)*

## Complexity

| | Time | Space |
|---|---|---|
| **Best** | $O(N)$ | $O(1)$ |
| **Average** | $O(N)$ | $O(1)$ |
| **Worst** | $O(N)$ | $O(1)$ |

The algorithm iterates through the arrays exactly once in a single linear pass. Doing $O(1)$ arithmetic at each step. Time complexity is strictly $O(N)$.
Only primitive integer variables are used (`current_tank`, `total`, `start_index`), so space complexity is perfectly $O(1)$.

## Variants & optimizations

- **Multiple Valid Starts:** The LeetCode problem guarantees a *unique* solution. If multiple solutions are possible and you must return all of them, the single-pass $O(N)$ trick fails. You can concatenate the array to itself (`gas + gas`) to simulate a circle, and use a sliding window/two-pointer approach to find all valid windows of size N in $O(N)$ time!

## Real-world applications

- **Spacecraft Orbit Transfers:** Calculating the specific orbital insertion point (Hohmann transfer) where thruster fuel gains (via gravitational slingshots) exceed continuous life-support and drag costs to reach a stable orbit without running dry.

## Related algorithms in cOde(n)

- **[dp_06 - Kadane's Algorithm](../dynamic/dp_06_kadanes-algorithm.md)** — The exact same "reset to 0 when it drops below a threshold" logic applied to finding the Maximum Subarray!
- **[greedy_07 - Jump Game](greedy_07_jump-game.md)** — Another problem where a single $O(N)$ pass tracks a "max reach" state that resets or fails upon hitting a wall.

---

*This documentation is original content written for cOde(n),
modeled after the canonical structure used by competitive-programming
reference sites. For the canonical encyclopedia entry, follow the
Wikipedia link at the top of the page. Source repository:
<https://github.com/dawei7/code_n>.*
