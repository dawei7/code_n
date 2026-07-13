# Rabbits in Forest

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 781 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Math, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/rabbits-in-forest/) |

## Problem Description

### Goal

Each surveyed rabbit reports how many other rabbits in the forest have the same color. An answer `y` therefore describes a possible color group containing exactly $y + 1$ rabbits, including the respondent.

Given all reported answers, return the minimum total number of rabbits that could be in the forest. Rabbits giving different answers cannot share a color, while rabbits giving the same answer may belong to one group or to several separate groups of that size. Unsurveyed group members must still be counted.

### Function Contract

**Inputs**

- `answers`: a list of nonnegative integers, where an entry `y` claims that exactly `y` other rabbits have the respondent's color.

**Return value**

- The minimum forest population consistent with every response.

### Examples

**Example 1**

- Input: `answers = [1,1,2]`
- Output: `5`
- Explanation: The two rabbits answering `1` can form one color group of two; the rabbit answering `2` requires a group of three.

**Example 2**

- Input: `answers = [10,10,10]`
- Output: `11`
- Explanation: All three respondents can belong to a single color group of size eleven.

**Example 3**

- Input: `answers = []`
- Output: `0`
- Explanation: No surveyed rabbits impose any required population.

### Required Complexity

- **Time:** $O(n)$
- **Space:** $O(u)$

<details>
<summary>Approach</summary>

#### General

**Translate an answer into a group size**

A rabbit answering `y` belongs to a color group containing exactly $y + 1$ rabbits. Only rabbits with the same answer can share such a group, because every member of one color sees the same number of same-colored companions.

**Pack equal answers into full groups**

If answer $y$ appears $c$ times, at most $y+1$ of those respondents can occupy one color group. The minimum number of required groups is therefore $\lceil c/(y+1)\rceil$. Each group contributes its entire size, including any same-colored rabbits that were not surveyed.

Summing `ceil(count / group_size) * group_size` over distinct answers is feasible: partition each frequency into groups of capacity `group_size`, with only the final group possibly containing unreported members. Fewer groups cannot hold all respondents, while these packed groups satisfy every report, so the sum is minimal.

#### Complexity detail

Counting all `n` responses and then visiting each distinct answer takes $O(n)$ time. The frequency table stores `u` distinct answers, using $O(u)$ auxiliary space.

#### Alternatives and edge cases

- **Track remaining group capacity:** While scanning, start a new group when an answer has no open slots and consume a slot otherwise; this also takes $O(n)$ time and $O(u)$ space.
- **Sort equal answers together:** Grouping runs after sorting is correct but takes $O(n \log n)$ time.
- **Rescan for every distinct answer:** Repeatedly counting occurrences in the original list can degrade to $O(n^2)$ time.
- **Empty survey:** Return zero because there are no constraints to satisfy.
- **Zero answers:** Each such rabbit claims a unique color group of size one.
- **Partial final group:** Even one respondent forces the full declared group size to exist.
- **Frequency exceeding one group:** Split equal responses across as many separate colors of that size as necessary.

</details>
