# Queue Reconstruction by Height

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 406 |
| Difficulty | Medium |
| Topics | Array, Binary Indexed Tree, Segment Tree, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/queue-reconstruction-by-height/) |

## Problem Description
### Goal
Each person is represented by `[height, k]`, where `k` states how many people standing before that person must have height greater than or equal to `height`. The input contains the people in no useful queue order and may include repeated pairs as separate individuals.

Return any ordering of the same person occurrences that satisfies every stated count. For each output position, inspect only earlier people and count those meeting its height threshold; that number must equal its `k`. A valid reconstruction is guaranteed, and several queue orders may work. Do not change heights or counts, omit people, or introduce new pairs.

### Function Contract
**Inputs**

- `people`: an unordered list of `[height, k]` pairs guaranteed to describe at least one valid queue

**Return value**

- Return any ordering containing the same people in which every pair's preceding tall-enough count equals `k`.

### Examples
**Example 1**

- Input: `people = [[7,0],[4,4],[7,1],[5,0],[6,1],[5,2]]`
- Output: `[[5,0],[7,0],[5,2],[6,1],[4,4],[7,1]]`

**Example 2**

- Input: `people = [[6,0],[5,0],[4,0],[3,2],[2,2],[1,4]]`
- Output: `[[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]`

**Example 3**

- Input: `people = [[5,0]]`
- Output: `[[5,0]]`
