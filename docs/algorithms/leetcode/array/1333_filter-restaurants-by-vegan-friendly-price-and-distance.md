# Filter Restaurants by Vegan-Friendly, Price and Distance

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1333 |
| Difficulty | Medium |
| Topics | Array, Sorting |
| Official Link | [filter-restaurants-by-vegan-friendly-price-and-distance](https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/) |

## Problem Description & Examples
### Goal
Filter restaurant records by vegan requirement, maximum price, and maximum distance. Return ids sorted by rating descending, then id descending.

### Function Contract
**Inputs**

- `restaurants`: records `[id, rating, veganFriendly, price, distance]`.
- `veganFriendly`: if `1`, only vegan-friendly restaurants are allowed; if `0`, either kind is allowed.
- `maxPrice`: maximum allowed price.
- `maxDistance`: maximum allowed distance.

**Return value**

Restaurant ids after filtering and sorting.

### Examples
**Example 1**

- Input: `restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]`, `veganFriendly = 1`, `maxPrice = 50`, `maxDistance = 10`
- Output: `[3,1,5]`

**Example 2**

- Input: `restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]`, `veganFriendly = 0`, `maxPrice = 50`, `maxDistance = 10`
- Output: `[4,3,2,1,5]`

**Example 3**

- Input: `restaurants = [[1,5,1,10,10],[2,5,1,20,5]]`, `veganFriendly = 1`, `maxPrice = 15`, `maxDistance = 10`
- Output: `[1]`

---

## Underlying Base Algorithm(s)
Filtering and custom sorting.

---

## Complexity Analysis
- **Time Complexity**: `O(n log n)`
- **Space Complexity**: `O(n)`
