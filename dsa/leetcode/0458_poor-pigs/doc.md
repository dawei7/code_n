# Poor Pigs

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 458 |
| Difficulty | Hard |
| Topics | Math, Dynamic Programming, Combinatorics |
| Official Link | [LeetCode](https://leetcode.com/problems/poor-pigs/) |

## Problem Description
### Goal
Exactly one of `buckets` buckets is poisoned. A pig that drinks poison dies after `minutesToDie`, and the experiment has `minutesToTest` total minutes. You may arrange several simultaneous testing rounds and let each pig drink mixtures from selected buckets in each round.

Return the minimum number of pigs needed to identify the poisoned bucket with certainty. Each pig has one observable state for every completed death interval plus a final surviving state, so combined pig outcomes must distinguish all buckets. Testing schedules may encode buckets through those states; simply assigning one pig per bucket is not required. The answer depends on the number of full rounds available.

### Function Contract
**Inputs**

- `buckets`: the number of buckets, exactly one of which is poisoned
- `minutesToDie`: minutes between consuming poison and the observable outcome
- `minutesToTest`: total minutes available for the experiment

**Return value**

- The minimum number of pigs sufficient to identify the poisoned bucket with certainty

### Examples
**Example 1**

- Input: `buckets = 1000, minutesToDie = 15, minutesToTest = 60`
- Output: `5`

**Example 2**

- Input: `buckets = 4, minutesToDie = 15, minutesToTest = 15`
- Output: `2`

**Example 3**

- Input: `buckets = 4, minutesToDie = 15, minutesToTest = 30`
- Output: `2`
