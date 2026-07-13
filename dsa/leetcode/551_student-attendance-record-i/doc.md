# Student Attendance Record I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 551 |
| Difficulty | Easy |
| Topics | String |
| Official Link | [LeetCode](https://leetcode.com/problems/student-attendance-record-i/) |

## Problem Description
### Goal
Given a student's attendance string, each character is `A` for absent, `L` for late, or `P` for present. Award eligibility depends on the complete record rather than only a prefix or the final day.

Return `True` only when the record contains fewer than two `A` characters in total and never contains three or more consecutive `L` characters. Two absences anywhere cause failure, and a run `LLL` causes failure even when no absence occurs. Separated late days do not combine into one run, while present or absent days break a late streak.

### Function Contract
**Inputs**

- `s`: a string containing `P` for present, `A` for absent, and `L` for late

**Return value**

- `True` when both award conditions hold; otherwise `False`

### Examples
**Example 1**

- Input: `s = "PPALLP"`
- Output: `True`

**Example 2**

- Input: `s = "PPALLL"`
- Output: `False`

**Example 3**

- Input: `s = "AA"`
- Output: `False`

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Track the two disqualifying conditions independently**

Maintain an absence count for the whole record and a late-streak length for the current suffix. An `A` increments the first value, while an `L` increments the second.

**Reset a streak when lateness is interrupted**

Any character other than `L` ends the current consecutive-late run, so set the streak back to zero. Earlier late days no longer matter once a present or absent day separates them.

**Reject as soon as a limit is reached**

A second absence permanently violates the total-count condition, and a third consecutive late day permanently violates the streak condition. Return `False` immediately in either case; if the scan finishes, both conditions held everywhere.

**Why the final decision is exact**

After each processed character, the absence count equals the number of `A` characters in the processed prefix, and the streak equals the length of that prefix's trailing run of `L` characters. Reaching either prohibited threshold is therefore exactly an award violation. If neither threshold is ever reached, the complete record has at most one absence and no `LLL` substring.

#### Complexity detail

Each of the `n` characters is inspected at most once, giving $O(n)$ time. The two integer counters use $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Built-in count and substring search:** `s.count("A") < 2 and "LLL" not in s` is also linear and concise, though it may scan the string twice.
- **Recheck every prefix:** is correct but repeats earlier work after each day and takes $O(n^2)$ time.
- **Single absence:** is allowed unless another condition fails.
- **Two nonconsecutive absences:** still disqualify because absences are counted globally.
- **Two consecutive late days:** are allowed; the prohibited run begins at three.
- **Separated late runs:** do not combine because a non-late day resets the streak.
- **Early violation:** can return immediately because later characters cannot repair it.

</details>
