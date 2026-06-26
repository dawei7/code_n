# Find All Possible Recipes from Given Supplies

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2115 |
| Difficulty | Medium |
| Topics | Array, Hash Table, String, Graph Theory, Topological Sort |
| Official Link | [find-all-possible-recipes-from-given-supplies](https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/) |

## Problem Description & Examples
### Goal
Determine which named recipes can be prepared from the initial supplies and from other recipes that become available. A recipe may be returned only after every ingredient in its corresponding ingredient list can be obtained.

### Function Contract
**Inputs**

- `recipes`: a list of distinct recipe names.
- `ingredients`: `ingredients[i]` lists everything needed to make `recipes[i]`.
- `supplies`: the items available before any recipe is made.

**Return value**

A list containing every recipe that can eventually be prepared, in any order.

### Examples
**Example 1**

- Input: `recipes = ["bread", "sandwich"]`, `ingredients = [["yeast", "flour"], ["bread", "ham"]]`, `supplies = ["yeast", "flour", "ham"]`
- Output: `["bread", "sandwich"]`

**Example 2**

- Input: `recipes = ["bread"]`, `ingredients = [["yeast", "flour"]]`, `supplies = ["yeast"]`
- Output: `[]`

**Example 3**

- Input: `recipes = ["a", "b"]`, `ingredients = [["b"], ["a"]]`, `supplies = []`
- Output: `[]`

---

## Underlying Base Algorithm(s)
Use topological sorting. Treat available supplies as resolved nodes, map each ingredient to the recipes waiting for it, and count each recipe's unresolved ingredients. Whenever a count reaches zero, add that recipe to the result and process it as a newly available supply. Cycles without an externally supplied entry never reach zero.

---

## Complexity Analysis
- **Time Complexity**: `O(R + I + S)`, where `I` is the total number of ingredient occurrences.
- **Space Complexity**: `O(R + I + S)`
