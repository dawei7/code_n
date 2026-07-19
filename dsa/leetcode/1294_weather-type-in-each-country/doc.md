# Weather Type in Each Country

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1294 |
| Difficulty | Easy |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/weather-type-in-each-country/) |

## Problem Description
### Goal
The `Countries` table maps country identifiers to names, while `Weather` records a country's weather state on a particular day. For each country having weather records during November 2019, compute the average `weather_state` over that month only.

Classify an average at most 15 as `"Cold"`, an average at least 25 as `"Hot"`, and every average strictly between those boundaries as `"Warm"`. Return each qualifying `country_name` with its `weather_type`; countries without a November 2019 record are omitted.

### Function Contract
**Inputs**

- `Countries(country_id, country_name)`: one row per country.
- `Weather(country_id, weather_state, day)`: dated integer weather observations.
- Let $C$ be the number of country rows and $W$ the number of weather rows.

**Return value**

A relation with columns `country_name` and `weather_type`, containing one classified row for each country represented in the November 2019 observations.

### Examples
**Example 1**

- Input: USA has one November value of 15; Australia has values $-2$, $0$, and $3$.
- Output: `[["Australia","Cold"],["USA","Cold"]]`

**Example 2**

- Input: China has November values `[16,18,21]`.
- Output: `[["China","Warm"]]`

**Example 3**

- Input: Morocco has November values `[25,27,31]`.
- Output: `[["Morocco","Hot"]]`
