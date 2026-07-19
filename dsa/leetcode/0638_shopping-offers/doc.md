# Shopping Offers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 638 |
| Difficulty | Medium |
| Topics | Array, Dynamic Programming, Backtracking, Bit Manipulation, Memoization, Bitmask |
| Official Link | [LeetCode](https://leetcode.com/problems/shopping-offers/) |

## Problem Description
### Goal
In a store with `n` item types, `price[i]` is the individual price of item `i`, and `needs[i]` is the exact number of pieces you want. Each row in `special` gives quantities of all `n` items followed by the bundle's sale price.

Return the lowest total price needed to satisfy all quantities exactly. You may buy items individually and may use any special offer multiple times, but you are not allowed to buy more of any item than `needs` requests, even when an overfilled bundle would cost less. Offers may be combined in any order.

### Function Contract
**Inputs**

- `price`: the individual price of each of `M` item types
- `special`: bundle rows containing `M` item quantities followed by that bundle's price
- `needs`: the exact required quantity of each item type

**Return value**

- The minimum total cost that satisfies all needs exactly

### Examples
**Example 1**

- Input: `price = [2,5]`, `special = [[3,0,5],[1,2,10]]`, `needs = [3,2]`
- Output: `14`

**Example 2**

- Input: `price = [2,3,4]`, `special = [[1,1,0,4],[2,2,1,9]]`, `needs = [1,2,1]`
- Output: `11`

**Example 3**

- Input: `price = [2,3]`, `special = []`, `needs = [2,1]`
- Output: `7`
