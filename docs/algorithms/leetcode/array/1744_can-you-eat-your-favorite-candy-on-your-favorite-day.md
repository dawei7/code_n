# Can You Eat Your Favorite Candy on Your Favorite Day?

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1744 |
| Difficulty | Medium |
| Topics | Array, Prefix Sum |
| Official Link | [can-you-eat-your-favorite-candy-on-your-favorite-day](https://leetcode.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/) |

## Problem Description & Examples
### Goal
Candy types must be eaten in order from type `0` upward. For each query, decide whether it is possible to eat at least one candy of a favorite type on a favorite day, while eating between `1` and `dailyCap` candies per day.

### Function Contract
**Inputs**

- `candiesCount`: count of candies for each type.
- `queries`: a list of `[favoriteType, favoriteDay, dailyCap]` queries.

**Return value**

Return a boolean answer for each query.

### Examples
**Example 1**

- Input: `candiesCount = [7,4,5,3,8], queries = [[0,2,2],[4,2,4],[2,13,1000000000]]`
- Output: `[true,false,true]`

**Example 2**

- Input: `candiesCount = [5,2,6,4,1], queries = [[3,1,2],[4,10,3],[3,10,100]]`
- Output: `[false,true,true]`

**Example 3**

- Input: `candiesCount = [1,1,1], queries = [[0,0,1],[1,0,1],[2,2,1]]`
- Output: `[true,false,true]`

---

## Underlying Base Algorithm(s)
Use prefix sums to know the range of candy positions belonging to each type. By day `d`, the eater has eaten at least `d + 1` candies and at most `(d + 1) * dailyCap` candies. A query is possible if this eaten-count range overlaps the 1-indexed position range of the favorite type.

---

## Complexity Analysis
- **Time Complexity**: `O(n + q)`
- **Space Complexity**: `O(n)`
