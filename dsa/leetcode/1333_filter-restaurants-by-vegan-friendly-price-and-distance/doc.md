# Filter Restaurants by Vegan-Friendly, Price and Distance

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1333 |
| Difficulty | Medium |
| Topics | Array, Sorting |
| Official Link | [LeetCode](https://leetcode.com/problems/filter-restaurants-by-vegan-friendly-price-and-distance/) |

## Problem Description
### Goal
Each row of `restaurants` describes one restaurant as `[id, rating, veganFriendly, price, distance]`. Select only records that satisfy the requested dietary, price, and distance filters.

The price and distance limits are inclusive. When the input flag `veganFriendly` is 1, a selected record must also have its own vegan-friendly field set to 1; when the flag is 0, either kind of restaurant is permitted.

Return the selected restaurant IDs ordered by decreasing rating. If two selected restaurants have equal ratings, put the larger ID first.

### Function Contract
**Inputs**

- `restaurants`: an array of $n$ five-integer records, where $1\le n\le10^4$. In each record, the distinct ID, rating, price, and distance are between 1 and $10^5$, and the vegan-friendly field is 0 or 1.
- `vegan_friendly`: either 0 to allow every restaurant or 1 to require a vegan-friendly record.
- `max_price`: an inclusive price limit between 1 and $10^5$.
- `max_distance`: an inclusive distance limit between 1 and $10^5$.

**Return value**

The IDs of all qualifying restaurants, sorted by rating descending and then ID descending.

### Examples
**Example 1**

- Input: `restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]`, `vegan_friendly = 1`, `max_price = 50`, `max_distance = 10`
- Output: `[3,1,5]`

**Example 2**

- Input: `restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]`, `vegan_friendly = 0`, `max_price = 50`, `max_distance = 10`
- Output: `[4,3,2,1,5]`

**Example 3**

- Input: `restaurants = [[1,4,1,40,10],[2,8,0,50,5],[3,8,1,30,4],[4,10,0,10,3],[5,1,1,15,1]]`, `vegan_friendly = 0`, `max_price = 30`, `max_distance = 3`
- Output: `[4,5]`
