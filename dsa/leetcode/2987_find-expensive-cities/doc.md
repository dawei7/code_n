# Find Expensive Cities

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2987 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/find-expensive-cities/) |

## Problem Description
### Goal
The `Listings` table contains one uniquely identified home listing, its city,
and its price on each row. The national average home price is the average over
all listing rows, so every listed home contributes once.

Compute each city's average listing price and return the cities whose average
strictly exceeds that national average. A city whose average merely equals the
national value does not qualify. Return only the `city` column, sorted in
ascending order.

### Function Contract
**Inputs**

- `Listings(listing_id, city, price)`: uniquely identified home listings

Let $R$ be the number of listing rows.

**Return value**

Return qualifying city names in ascending order.

### Examples
**Example 1**

- Input: The published Chicago, LosAngeles, SanFrancisco, and NewYork listings
- Output: `[("Chicago"),("LosAngeles")]`

**Example 2**

- Input: One city containing every listing
- Output: No rows, because its average equals the national average.

**Example 3**

- Input: Cities with respective listing averages `100` and `0`
- Output: Only the first city.
