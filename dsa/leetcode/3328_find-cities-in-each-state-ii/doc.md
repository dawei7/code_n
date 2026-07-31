# Find Cities in Each State II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 3328 |
| Difficulty | Medium |
| Category | Database |
| Topics | Database |
| Supported Languages | sql |
| Official Link | [LeetCode](https://leetcode.com/problems/find-cities-in-each-state-ii/) |

## Problem Description

### Goal

The `cities` table contains one row for every unique `(state, city)` pair. Summarize the cities belonging to each state, but retain only states that contain at least three cities and have at least one city whose first letter matches the first letter of the state name.

For every retained state, combine all of its city names into one comma-and-space-separated string ordered alphabetically. Also report how many of those cities begin with the state's initial letter. Sort the final rows by that matching-city count from largest to smallest; when counts tie, sort state names in ascending alphabetical order.

### Function Contract

**Inputs**

Table `cities`:

- `state`: The state's name as a `varchar` value.
- `city`: The name of a city within that state as a `varchar` value.

The pair `(state, city)` is unique.

**Return value**

Return columns `state`, `cities`, and `matching_letter_count`. The `cities` value lists every city in that state alphabetically with `, ` between names. Include only qualifying states and order rows by `matching_letter_count DESC, state ASC`.

### Examples

**Example 1**

Input table:

| state | city |
|---|---|
| New York | New York City |
| New York | Newark |
| New York | Buffalo |
| New York | Rochester |
| California | San Francisco |
| California | Sacramento |
| California | San Diego |
| California | Los Angeles |
| Texas | Tyler |
| Texas | Temple |
| Texas | Taylor |
| Texas | Dallas |
| Pennsylvania | Philadelphia |
| Pennsylvania | Pittsburgh |
| Pennsylvania | Pottstown |

Output:

| state | cities | matching_letter_count |
|---|---|---:|
| Pennsylvania | Philadelphia, Pittsburgh, Pottstown | 3 |
| Texas | Dallas, Taylor, Temple, Tyler | 3 |
| New York | Buffalo, Newark, New York City, Rochester | 2 |

California has enough cities but none begins with `C`, so it is omitted. Pennsylvania and Texas tie on the matching count, and Pennsylvania comes first alphabetically.
