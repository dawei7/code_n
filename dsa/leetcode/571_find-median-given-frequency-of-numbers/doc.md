# Find Median Given Frequency of Numbers

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 571 |
| Difficulty | Hard |
| Topics | Database |
| Official Link | [LeetCode](https://leetcode.com/problems/find-median-given-frequency-of-numbers/) |

## Problem Description
### Goal
Given a `Numbers` table whose rows contain a distinct number and the frequency with which it occurs, interpret the table as a multiset in which each number is repeated exactly that many times. Find the median value that would result if this expanded multiset were sorted in non-decreasing order.

For an odd total frequency, the median is the value at the single central position. For an even total, it is the arithmetic mean of the two central values. Return the result in a column named `median`, rounded to one decimal place, without requiring the repeated rows to be physically materialized.

### Function Contract
**Inputs**

- `Numbers(num, frequency)`: each distinct number and its positive occurrence count

**Return value**

- A one-row result grid with column `median`

### Examples
**Example 1**

- Input frequencies: `1:1, 2:1, 3:1`
- Output: `2.0`

**Example 2**

- Input frequencies: `1:1, 3:1`
- Output: `2.0`

**Example 3**

- Input frequency: `7:100`
- Output: `7.0`

### Required Complexity

- **Time:** $O(R \log R)$
- **Space:** $O(R)$

<details>
<summary>Approach</summary>

#### General

**Map each number to an expanded-rank interval**

Order rows by `num`. A cumulative sum of `frequency` gives the last expanded position occupied by the current number; subtracting its frequency gives the number of positions strictly before it.

**Know the complete multiset size**

A second window sum without ordering gives the total frequency `T` on every row.

**Select intervals touching the center**

Keep a row when `2 * cumulative >= T` and `2 * previous_cumulative <= T`. For odd $T$, this selects the interval containing the single middle position. For even $T$, it selects the interval or two adjacent intervals containing the two middle positions.

**Average the selected values**

If both middle positions belong to one frequency interval, that number appears once in the selected relation and averaging it returns itself. If they fall in two intervals, averaging the two numbers gives the conventional even-size median. Round to one decimal place.

**Why the interval conditions are exact**

A row covers expanded positions `previous + 1` through `cumulative`. Doubling positions avoids fractional middle ranks. The first inequality says the interval reaches at least the lower center, and the second says it begins no later than the upper center. Their conjunction is precisely interval overlap with the central rank or ranks.

#### Complexity detail

For `R` distinct-number rows, the cumulative window typically sorts by `num` in $O(R \log R)$ time and stores $O(R)$ ranked rows. The total-frequency window is linear after that ordering.

#### Alternatives and edge cases

- **Expand every occurrence:** is conceptually simple but uses time and space proportional to the total frequency, which may be far larger than `R`.
- **Correlated cumulative sums:** avoids expansion but may rescan all `R` rows for every number and take $O(R^2)$ time.
- **Odd total frequency:** exactly one expanded middle position determines the median.
- **Even total frequency:** average the two middle values, even when they differ.
- **One number:** its value is the median regardless of frequency.
- **Both centers in one interval:** select that row once; duplicating it is unnecessary for the average.
- **Negative values:** numeric ordering and averaging work unchanged.

</details>
