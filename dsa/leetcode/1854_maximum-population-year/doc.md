# Maximum Population Year

| Field | Value |
|---|---|
| Source | [LeetCode](https://leetcode.com/problems/maximum-population-year/) |
| Frontend ID | 1854 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, Counting, Prefix Sum |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |

## Problem Description

### Goal

Each entry `[birth, death]` in `logs` describes one person's lifetime by calendar year. That person contributes to the population in every year from `birth` through `death - 1`: the birth year is included, while the death year is not.

For every year covered by the allowed range, determine how many logged people are alive. Return the earliest year whose population equals the maximum population attained by any year. Thus, when several years share the same largest count, the smaller year must win.

### Function Contract

**Inputs**

- `logs`: a list of between 1 and 100 pairs `[birth, death]`.
- Each pair satisfies $1950 \le \texttt{birth}<\texttt{death}\le 2050$.
- Let $n=\lvert\texttt{logs}\rvert$.
- Let $Y=101$ be the number of difference-array positions from 1950 through 2050.

**Return value**

- Return the earliest year with the largest number of people satisfying $\texttt{birth}\le\texttt{year}<\texttt{death}$.

### Examples

**Example 1**

- Input: `logs = [[1993, 1999], [2000, 2010]]`
- Output: `1993`

Both occupied ranges have population 1, so the earlier year wins.

**Example 2**

- Input: `logs = [[1950, 1961], [1960, 1971], [1970, 1981]]`
- Output: `1960`

**Example 3**

- Input: `logs = [[2000, 2001], [2001, 2002]]`
- Output: `2000`

The first person's death year is excluded, so both years have population 1.

### Required Complexity

- **Time:** $O(n+Y)$
- **Space:** $O(Y)$

<details>
<summary>Approach</summary>

#### General

Use a difference array indexed by year offset from 1950. For every lifetime, add 1 at its birth index and subtract 1 at its death index. The subtraction at `death` implements the half-open interval `[birth, death)` exactly.

Scan year offsets in increasing order while accumulating the difference values. The running sum after applying a year's change is precisely the population alive during that year: every earlier birth has added one, and every death at or before the year has removed one.

Keep the largest population seen and its year. Update the saved year only when the running population is strictly larger, not when it merely ties. Since scanning is chronological, this preserves the earliest year among all maxima.

#### Complexity detail

Recording all lifetimes takes $O(n)$ time, and scanning the $Y$ year positions takes $O(Y)$ time, for $O(n+Y)$ total. The difference array uses $O(Y)$ space. Under the source's fixed 1950–2050 domain, $Y=101$ is a small constant, but it remains explicit in the bound.

#### Alternatives and edge cases

- **Test every person for every year:** Straightforward, but costs $O(nY)$ time.
- **Sorted birth and death events:** A sweep over event tuples also works, but simultaneous birth/death ordering must preserve the exclusive death boundary.
- **Death year:** A person is not alive during `death`, so decrement at that exact year.
- **Earliest tie:** Replace the answer only for a strictly greater population.
- **Simultaneous death and birth:** Both changes apply before evaluating that year's population.
- **Single lifetime:** Its birth year is the earliest maximum.
- **Boundary years:** Birth may be 1950 and death may be 2050 without indexing outside the difference array.
- **Consecutive non-overlapping lives:** They create equal populations in adjacent years rather than an overlap.

</details>
