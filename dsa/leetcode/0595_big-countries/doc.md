# Big Countries

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 595 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/big-countries/) |

## Problem Description
### Goal
Given a `World` table containing each country's name, continent, area, population, and GDP, classify a country as big when its area is at least `3,000,000` square kilometers or its population is at least `25,000,000`.

Return the `name`, `population`, and `area` of every big country in any order. The two thresholds are inclusive and joined by `or`, so meeting either condition is sufficient; a country does not need to satisfy both, and values exactly equal to a threshold qualify.

### Function Contract
**Inputs**

- `World(name, continent, area, population, gdp)`: country statistics

**Return value**

- Columns `name`, `population`, and `area` for every country satisfying either inclusive threshold

### Examples
**Example 1**

- Input: a country has area `3,000,000`
- Output: that country's name, population, and area

**Example 2**

- Input: a country has population `25,000,000` but smaller area
- Output: that country

**Example 3**

- Input: both measures are below their thresholds
- Output: no row for that country

### Required Complexity

- **Time:** $O(n \log n)$
- **Space:** $O(n)$

<details>
<summary>Approach</summary>

#### General

**Translate both definitions directly**

A country is big when `area >= 3000000` or `population >= 25000000`. Use an `OR` so satisfying either independent measure is sufficient.

**Project only the requested columns**

After filtering, return `name`, `population`, and `area`; continent and GDP do not participate in qualification or output.

**Why the predicate is exact**

The two comparisons use the stated inclusive boundaries. A row satisfying at least one makes the disjunction true and is retained. A row below both makes both branches false and is excluded, covering every possible country row.

**Order only for deterministic local output**

The platform permits any output order. Sorting by name stabilizes local fixture results without changing membership.

#### Complexity detail

Filtering scans `n` rows in $O(n)$ time. The deterministic name sort costs $O(n \log n)$ time and $O(n)$ working space; without ordering, the semantic query is linear.

#### Alternatives and edge cases

- **Union of two filtered queries:** one branch can select large-area countries and another populous countries, but `UNION` must remove countries satisfying both and scans the table twice.
- **Correlated existence test:** can express the same condition but may rescan the table for every country and take $O(n^2)$ time.
- **Use `AND`:** is incorrect because a country need satisfy only one threshold.
- **Area exactly 3,000,000:** qualifies.
- **Population exactly 25,000,000:** qualifies.
- **Both thresholds satisfied:** return the country once.
- **Neither threshold satisfied:** exclude the country.
- **GDP and continent:** do not affect the result.

</details>
