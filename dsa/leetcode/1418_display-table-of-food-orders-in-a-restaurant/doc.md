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

### Required Complexity

- **Time:** $O(N + F\log F + T\log T + TF)$
- **Space:** $O(N + TF)$

<details>
<summary>Approach</summary>

#### General

**Aggregate by table and food.** Scan every order once. Insert its food name into a set and increment a nested counter keyed first by the numeric table number and then by the food name. The customer name is irrelevant to the aggregation.

Sort the distinct foods lexicographically to form the header. Sort the counter's table keys numerically, not as strings, so table `"10"` follows `"5"`. For each table, emit its original decimal representation followed by the count for every sorted food, using zero when that pair never occurred.

Every order increments exactly one cell, so the counter contains the required multiplicities. Sorting the two independent dimensions establishes the mandated row and column order, and visiting every header food for every table fills all absent combinations with zero. Therefore the emitted matrix matches the display-table definition.

#### Complexity detail

Reading the $N$ orders takes $O(N)$ time. Sorting the $F$ foods and $T$ tables costs $O(F\log F + T\log T)$, and materializing the table costs $O(TF)$. The counters store at most $N$ populated pairs, while the returned matrix contains $O(TF)$ cells, giving $O(N+TF)$ total space including output.

#### Alternatives and edge cases

- **Rescan all orders per cell:** For each table-food pair, count matching records directly. It is correct but can take $O(NTF)$ time.
- **Sort orders first:** Sorting by table and food can support a grouped scan, but a hash counter is simpler and still needs the final full matrix.
- **Numeric table order:** Convert table strings to integers for sorting; lexicographical order would place `"10"` before `"2"`.
- **Missing pair:** Emit `"0"`, not an absent cell or numeric zero.
- **Repeated identical orders:** Count every record independently, even when customer, table, and food all match.
- **Single order:** The result still contains a two-cell header and one table row.

</details>
