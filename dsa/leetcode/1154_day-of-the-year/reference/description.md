### 1. Description

Given a string `date` representing a <a href="https://en.wikipedia.org/wiki/Gregorian_calendar" target="_blank">Gregorian calendar</a> date formatted as `YYYY-MM-DD`, return *the day number of the year*.

### 2. Function Contract

**Inputs**

- `date`: Input parameter (`str`).

**Return value**

- Returns `int`.

### 3. Examples

#### Example 1

- **Input:** $date = "2019-01-09"$
- **Output:** `9`
- **Explanation:** Given date is the 9th day of the year in 2019.

#### Example 2

- **Input:** $date = "2019-02-10"$
- **Output:** `41`

### 4. Constraints

- $\text{date.length} = 10$

- $\text{date}[4] = \text{date}[7] = '-'$, and all other $\text{date}[i]$'s are digits

- `date` represents a calendar date between Jan 1^st, 1900 and Dec 31^st, 2019.
