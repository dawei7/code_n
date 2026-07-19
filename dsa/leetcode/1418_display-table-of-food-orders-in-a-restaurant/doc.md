# Display Table of Food Orders in a Restaurant

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1418 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, String, Sorting, Ordered Set |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/display-table-of-food-orders-in-a-restaurant/) |

## Problem Description

### Goal

Each restaurant order records a customer's name, their table number, and one food item. Build a display table that summarizes how many orders of every food item came from every occupied table. Customer names do not appear in the result.

The first output row is a header beginning with `"Table"`, followed by all distinct food names in lexicographical order. Each later row represents one table, ordered by its numeric table number, and contains the decimal count for every header food. Counts and table numbers must be returned as strings.

### Function Contract

**Inputs**

- `orders`: an array of $N$ records `[customerName, tableNumber, foodItem]`, where $1 \le N \le 500$.
- Each `tableNumber` is a decimal string representing an integer from $1$ through $500$.
- Customer and food names are nonempty strings of at most 20 English letters and spaces.

Let $T$ be the number of distinct table numbers and $F$ the number of distinct food names.

**Return value**

- A matrix of strings containing the header and $T$ numerically ordered table rows, with food columns ordered lexicographically.

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
