# Daily Temperatures

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 739 |
| Difficulty | Medium |
| Topics | Array, Stack, Monotonic Stack |
| Official Link | [LeetCode](https://leetcode.com/problems/daily-temperatures/) |

## Problem Description
### Goal
Given an array `temperatures` representing consecutive daily temperatures, determine for each day how long you must wait until a future day with a warmer temperature.

Return an array of the same length where `answer[i]` is the smallest positive number of days to a later index `j` with `temperatures[j] > temperatures[i]`. If no future day is strictly warmer, store `0` at that position. An equal temperature does not end the wait.

### Function Contract
**Inputs**

- `temperatures`: an ordered list of daily integer temperatures

**Return value**

- A list of the same length where position $i$ stores the smallest positive $j-i$ with `temperatures[j] > temperatures[i]`, or `0` when no such $j$ exists

### Examples
**Example 1**

- Input: `temperatures = [73,74,75,71,69,72,76,73]`
- Output: `[1,1,4,2,1,1,0,0]`

**Example 2**

- Input: `temperatures = [30,40,50,60]`
- Output: `[1,1,1,0]`

**Example 3**

- Input: `temperatures = [30,60,90]`
- Output: `[1,1,0]`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Keep only days still waiting for an answer**

Scan temperatures from left to right and store indices whose next warmer day has not yet appeared. Their temperatures are nonincreasing from the bottom to the top of the stack: any smaller top would already have been resolved by the day that introduced a larger value below it.

**Resolve every colder stack top with the current day**

For a current temperature at index `i`, repeatedly pop while it is strictly greater than the temperature at the stack top `j`. The current day is the first warmer day for `j`: every intervening day was processed while `j` remained unresolved, so none was warmer. Store `i-j` and continue because the same current value may resolve several colder days.

**Preserve equal temperatures as unresolved**

The comparison must be strict. An equal current temperature does not answer the older day, so its index is pushed above the older equal index. A future warmer value may then pop both and assign different distances.

**Why every reported distance is the nearest one**

An index enters the stack when its day is processed and leaves only upon the first later temperature strictly above it. If it is popped at `i`, no earlier day between the two could have been warmer, otherwise that earlier scan would have popped it. Indices left after the final day have no later warmer temperature and correctly retain their initialized zero answers.

#### Complexity detail

Each of the `n` indices is pushed once and popped at most once, so total time is $O(n)$ despite the nested-looking loop. The answer and unresolved-index stack each use $O(n)$ space.

#### Alternatives and edge cases

- **Scan forward from every day:** stop at the first warmer value for each index; it is simple but takes $O(n^2)$ time on constant or decreasing temperatures.
- **Scan right to left with jump distances:** previously computed waits can skip over nonwarmer days in linear time, but the boundary reasoning is less direct.
- **Temperature-bounded lookup:** because values lie in a small fixed range, track the nearest future index for each warmer temperature; this is linear with a constant temperature factor.
- **Equal temperatures:** equality is not warmer and must not resolve a waiting day.
- **Strictly increasing input:** every day except the last waits exactly one day.
- **Nonincreasing input:** no index is popped, so every answer is zero.
- **Single day:** there is no later day, yielding `[0]`.
- **Multiple pops:** one hot day may be the nearest warmer day for several unresolved earlier indices.

</details>
