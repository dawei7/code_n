# Reformat Date

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1507 |
| Difficulty | Easy |
| Topics | String |
| Official Link | [LeetCode](https://leetcode.com/problems/reformat-date/) |

## Problem Description
### Goal

You are given a valid calendar date written as `Day Month Year`. The day is an integer from 1 through 31 followed by its English ordinal suffix, such as `1st`, `2nd`, `3rd`, or `20th`. The month is one of the twelve three-letter abbreviations from `Jan` through `Dec`, and the four-digit year lies from 1900 through 2100.

Convert this date to `YYYY-MM-DD` form. The year remains first, while the month and day must each use exactly two digits, including a leading zero when necessary.

### Function Contract
**Inputs**

- `date`: A valid date string containing exactly three space-separated fields: an ordinal day, an English month abbreviation, and a four-digit year from 1900 through 2100.
- The ordinal day uses one of the suffixes `st`, `nd`, `rd`, or `th`. No validity checking or calendar correction is required.

**Return value**

Return the same date as a string in `YYYY-MM-DD` format, with two-digit month and day fields.

### Examples
**Example 1**

- Input: `date = "20th Oct 2052"`
- Output: `"2052-10-20"`

**Example 2**

- Input: `date = "6th Jun 1933"`
- Output: `"1933-06-06"`

**Example 3**

- Input: `date = "26th May 1960"`
- Output: `"1960-05-26"`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Separate the three fixed-format fields**

Splitting on spaces produces `day`, `month`, and `year`. The year already has the required four digits. A fixed lookup table maps each month abbreviation to its two-digit position, avoiding locale-sensitive date parsing.

The final two characters of the day field are always its ordinal suffix. Remove those characters, parse the remaining one- or two-digit number, and format it with width two. This handles every suffix uniformly: the algorithm does not need separate rules for `st`, `nd`, `rd`, and `th` because the input is guaranteed valid.

Finally, join the unchanged year, mapped month, and padded day with hyphens. Each output field then has exactly the required width and represents the same date.

**Why fixed parsing is sufficient**

There are always three fields in the same order, the month spelling comes from a closed twelve-item set, and the day suffix always occupies exactly two characters. Therefore every extraction uses a guaranteed boundary. The transformation changes only notation; it neither computes weekdays nor validates month lengths.

#### Complexity detail

Every legal input has at most 13 characters, and the month table always has twelve entries. Splitting, looking up the month, converting the day, and constructing the ten-character result therefore perform bounded work independent of a scalable input quantity, giving $O(1)$ time.

The parsed fields, fixed month table, and output occupy bounded space, so auxiliary space is $O(1)$. A `bounded_domain` certificate replaces runtime scaling because the source contract cannot produce growing legal inputs.

#### Alternatives and edge cases

- **Month-list search:** store the abbreviations in calendar order and use the index plus one. This is still constant time because there are exactly twelve months, though a direct map states the conversion more explicitly.
- **Date-library parsing:** a library can parse and reformat the date, but ordinal suffixes may require preprocessing and locale behavior adds unnecessary complexity.
- **Conditional month chain:** twelve `if` branches avoid a collection but are longer and easier to mistype than a lookup table.
- **Single-digit days:** values such as `6th` must become `06`, not `6`.
- **Ordinal exceptions:** `11th`, `12th`, and `13th` are already valid inputs; removing the final two characters works without reproducing suffix grammar.
- **Boundary years:** years 1900 and 2100 remain unchanged because they already contain four digits.
- **January and December:** the lookup must map the endpoints to `01` and `12`.
- **Calendar validity:** the contract guarantees a real date, so the solution should not reject or normalize the supplied fields.

</details>
