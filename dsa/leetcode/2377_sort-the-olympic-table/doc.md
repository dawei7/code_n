# Sort the Olympic Table

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2377 |
| Difficulty | Easy |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/sort-the-olympic-table/) |

## Problem Description

### Goal

The `Olympic` table contains one row per country and records its gold, silver, and bronze medal counts. Return every row and all four columns, reordered to form the Olympic ranking table.

Countries with more gold medals come first. Equal gold counts are resolved by more silver medals, then equal silver counts by more bronze medals. If all three medal counts tie, order the tied country names in ascending lexicographical order.

### Function Contract

**Inputs**

- `Olympic(country, gold_medals, silver_medals, bronze_medals)`: One row per country; `country` is the primary key.

Let $R$ denote the number of rows in `Olympic`.

**Return value**

- Return columns `country`, `gold_medals`, `silver_medals`, and `bronze_medals` for every input row.
- Sort by `gold_medals` descending, then `silver_medals` descending, then `bronze_medals` descending, and finally `country` ascending.

### Examples

#### Example 1

- **Input:** `Olympic = [["China",10,10,20],["South Sudan",0,0,1],["USA",10,10,20],["Israel",2,2,3],["Egypt",2,2,2]]`
- **Output:** `[["China",10,10,20],["USA",10,10,20],["Israel",2,2,3],["Egypt",2,2,2],["South Sudan",0,0,1]]`
- **Explanation:** China precedes USA by country name after all medals tie; Israel precedes Egypt because its bronze count is greater.
