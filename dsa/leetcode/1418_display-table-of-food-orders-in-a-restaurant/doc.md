# Display Table of Food Orders in a Restaurant

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1418 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Sorting, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [display-table-of-food-orders-in-a-restaurant](https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/) |

## Problem Description
[Open the original LeetCode problem](https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/).

### Goal
Build a display table for restaurant orders. Rows are table numbers in numeric order, columns are food names in lexicographic order, and each cell contains how many times that food was ordered at that table.

### Function Contract
**Inputs**

- `orders`: a list of `[customerName, tableNumber, foodItem]` records.

**Return value**

A table represented as a list of rows. The first row is the header `Table` plus sorted food names; each following row starts with a table number string and then count strings.

### Examples
**Example 1**

- Input: `orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]`
- Output: `[["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]]`

**Example 2**

- Input: `orders = [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]]`
- Output: `[["Table","Canadian Waffles","Fried Chicken"],["1","2","0"],["12","0","3"]]`

**Example 3**

- Input: `orders = [["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]`
- Output: `[["Table","Bean Burrito","Beef Burrito","Soda"],["2","1","1","1"]]`

---

## Solution
### Approach
Hash-map aggregation with sorted dimensions. Count `(table, food)` pairs, collect the set of food names, then emit rows in numeric table order and food-name order.

### Complexity Analysis
- **Time Complexity**: `O(o + f log f + t log t + tf)`, where `o` is the order count, `f` food count, and `t` table count.
- **Space Complexity**: `O(o + f + t)` for counts and dimension sets.

### Reference Implementations
<details>
<summary>python</summary>

```python
from collections import Counter, defaultdict


def solve(orders):
    counts = defaultdict(Counter)
    foods = set()
    for order in orders:
        if len(order) < 3:
            continue
        table = str(order[1])
        food = str(order[2])
        foods.add(food)
        counts[table][food] += 1
    sorted_foods = sorted(foods)
    result = [["Table", *sorted_foods]]
    for table in sorted(counts, key=lambda item: int(item) if item.lstrip("-").isdigit() else item):
        result.append([table, *[str(counts[table][food]) for food in sorted_foods]])
    return result
```
</details>
