# Can You Eat Your Favorite Candy on Your Favorite Day?

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1744 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/can-you-eat-your-favorite-candy-on-your-favorite-day/) |

## Problem Description

### Goal

`candiesCount[i]` is the available number of candies of type $i$. Starting on day `0`, you must eat at least one candy per day until none remain, and you must finish every candy of type $i-1$ before eating any of type $i$. You may cross from one type to the next during the same day.

Each query `[favoriteType, favoriteDay, dailyCap]` asks whether some valid eating schedule can include at least one candy of `favoriteType` on `favoriteDay`, while never eating more than `dailyCap` candies on any day. Return one boolean answer per query.

### Function Contract

**Inputs**

- `candiesCount`: positive counts for candy types in their mandatory eating order.
- `queries`: triples `[favoriteType, favoriteDay, dailyCap]`, with zero-indexed days and types.

Let $n$ be the number of candy types and $q$ the number of queries.

**Return value**

- Return a length-$q$ boolean list; each value states whether at least one schedule satisfying that query's cap can eat the requested type on the requested day.

### Examples

**Example 1**

- Input: `candiesCount = [7,4,5,3,8], queries = [[0,2,2],[4,2,4],[2,13,1000000000]]`
- Output: `[true,false,true]`
- Explanation: Type `0` can still be in progress on day `2`; type `4` cannot be reached that early under cap `4`; type `2` can be delayed through day `13`.

**Example 2**

- Input: `candiesCount = [5,2,6,4,1], queries = [[3,1,2],[4,10,3],[3,10,100],[4,100,30],[1,3,1]]`
- Output: `[false,true,true,false,false]`
- Explanation: Each query has its own independent cap and therefore its own feasible range of cumulative consumption.

**Example 3**

- Input: `candiesCount = [2,2], queries = [[1,0,3]]`
- Output: `[true]`
- Explanation: On day `0`, eating both type-`0` candies followed by one type-`1` candy is valid.
