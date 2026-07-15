# Day of the Week

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1185 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Math |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/day-of-the-week/) |

## Problem Description

### Goal

You are given a valid calendar date as three integers: `day`, `month`, and `year`, in that order. Determine which day of the week corresponds to that date under the Gregorian calendar.

Return exactly one of `"Sunday"`, `"Monday"`, `"Tuesday"`, `"Wednesday"`, `"Thursday"`, `"Friday"`, or `"Saturday"`. Every input year is from `1971` through `2100`, inclusive. The known reference date January 1, 1971 was a Friday.

### Function Contract

**Inputs**

- `day`: The valid one-based day within the given month.
- `month`: The month number from `1` for January through `12` for December.
- `year`: A Gregorian year satisfying $1971\le\texttt{year}\le2100$.
- The three integers always describe a valid date, including the Gregorian leap-year rules for February.

**Return value**

- The full English weekday name corresponding to the input date, with the capitalization shown above.

### Examples

**Example 1**

- Input: `day = 31`, `month = 8`, `year = 2019`
- Output: `"Saturday"`

**Example 2**

- Input: `day = 18`, `month = 7`, `year = 1999`
- Output: `"Sunday"`

**Example 3**

- Input: `day = 15`, `month = 8`, `year = 1993`
- Output: `"Sunday"`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Normalize January and February.** Zeller's congruence treats March as the first month of its arithmetic year. When the input month is January or February, add `12` to the month and subtract `1` from the year. Thus those months become months `13` and `14` of the preceding year, placing the leap-day adjustment at the end of the transformed year.

**Separate century and year components.** Let $c=\lfloor y/100\rfloor$ be the century and let $r=y\bmod100$ be the year within that century after normalization. For normalized month $m$ and day $d$, compute

$$
w=\left(\left\lfloor\frac{c}{4}\right\rfloor-2c+r+
\left\lfloor\frac{r}{4}\right\rfloor+
\left\lfloor\frac{13(m+1)}{5}\right\rfloor+d-1\right)\bmod7.
$$

The century and quarter-year terms account for ordinary and leap years, while the month term accounts for the varying month lengths. The residue $w$ uses `0` for Sunday through `6` for Saturday, so it directly indexes the required weekday-name list. Python's nonnegative modulo result also removes any concern about a negative intermediate sum.

#### Complexity detail

The calculation uses a fixed number of integer divisions, additions, multiplications, and one seven-element lookup, regardless of the date. It therefore takes $O(1)$ time and $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Count forward from January 1, 1971:** Advancing one valid date at a time is easy to verify against the given Friday anchor, but its work grows with the number of elapsed days.
- **Standard-library calendar type:** A date library is concise, but the arithmetic method is portable to environments where such a type or formatter is unavailable.
- **Leap-year February:** Years divisible by `400` are leap years; years divisible by `100` but not `400` are not, which distinguishes `2000` from `2100`.
- **January and February:** They must be reassigned to months `13` and `14` of the previous year before applying the congruence.
- **Boundary years:** Both `1971` and `2100` are included in the valid range.
- **Negative intermediate value:** Apply modulo after the entire congruence so the final weekday residue is normalized into $0$ through $6$.

</details>
