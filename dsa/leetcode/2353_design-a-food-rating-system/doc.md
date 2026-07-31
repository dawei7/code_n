# Design a Food Rating System

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2353 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Design, Heap (Priority Queue), Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/design-a-food-rating-system/) |

## Problem Description

### Goal

Design a system that stores distinct food names together with their cuisines
and current integer ratings. After initialization, the system must support
changing the rating of any named food and asking for the highest-rated food
within any cuisine represented by the input.

For a cuisine query, choose the food with the greatest current rating. If
several foods share that rating, return the lexicographically smallest name:
the name that comes first in dictionary order, including the usual rule that a
proper prefix precedes the longer string. Updates change only ratings; every
food permanently retains its original cuisine.

### Function Contract

**Inputs**

- `operations`: A sequence beginning with `"FoodRatings"` and followed by
  `"changeRating"` or `"highestRated"` method names.
- `arguments`: The corresponding argument lists. The constructor receives
  `foods`, `cuisines`, and `ratings`; an update receives `food` and
  `newRating`; a query receives `cuisine`.

The three constructor arrays have the same length $n$, where
$1 \le n \le 2\cdot10^4$. Food names are distinct, names contain one through
ten lowercase English letters, and ratings lie in $[1,10^8]$. Every later food
and cuisine argument is valid. Let $q$ be the number of calls after
construction; $q \le 2\cdot10^4$.

**Return value**

A list aligned with `operations`: `null` for construction and rating changes,
and the selected food name for each cuisine query.

### Examples

**Example 1**

- Input:
  `operations = ["FoodRatings","highestRated","highestRated","changeRating","highestRated","changeRating","highestRated"]`,
  `arguments = [[["kimchi","miso","sushi","moussaka","ramen","bulgogi"],["korean","japanese","japanese","greek","japanese","korean"],[9,12,8,15,14,7]],["korean"],["japanese"],["sushi",16],["japanese"],["ramen",16],["japanese"]]`
- Output: `[null,"kimchi","ramen",null,"sushi",null,"ramen"]`
- Explanation: The updates first make `sushi` the Japanese leader, then tie it
  with `ramen`; lexicographic order selects `ramen`.

**Example 2**

- Input:
  `operations = ["FoodRatings","highestRated","changeRating","highestRated"]`,
  `arguments = [[["apple","apricot"],["fruit","fruit"],[5,5]],["fruit"],["apricot",6],["fruit"]]`
- Output: `[null,"apple",null,"apricot"]`
- Explanation: The initial rating tie selects `apple`; the update gives
  `apricot` the higher rating.

**Example 3**

- Input:
  `operations = ["FoodRatings","changeRating","highestRated"]`,
  `arguments = [[["tea"],["drink"],[10]],["tea",1],["drink"]]`
- Output: `[null,null,"tea"]`
- Explanation: A cuisine containing one food always returns that food.
