# The Number of Full Rounds You Have Played

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1904 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [The Number of Full Rounds You Have Played](https://leetcode.com/problems/the-number-of-full-rounds-you-have-played/) |

## Problem Description

### Goal

An online chess tournament starts a new 15-minute round at `00:00`, `00:15`, `00:30`, and every other quarter-hour through `23:45`. You are given the times at which you log in and log out, using the 24-hour `hh:mm` format.

Count only rounds whose complete interval lies within your connected session. If `logoutTime` is earlier than `loginTime`, the session crosses midnight into the next day. The two times are guaranteed to differ.

### Function Contract

**Inputs**

- `loginTime`: the session's start time in `hh:mm` format.
- `logoutTime`: the session's end time in `hh:mm` format.
- Hours range from `00` through `23`, and minutes from `00` through `59`.

**Return value**

Return the number of complete 15-minute tournament rounds played from login through logout, accounting for a possible midnight crossing.

### Examples

**Example 1**

- Input: `loginTime = "09:31", logoutTime = "10:14"`
- Output: `1`
- Explanation: Only the round from `09:45` through `10:00` is fully contained in the session.

**Example 2**

- Input: `loginTime = "21:30", logoutTime = "03:00"`
- Output: `22`
- Explanation: Ten complete rounds occur before midnight and twelve after it.

**Example 3**

- Input: `loginTime = "00:00", logoutTime = "00:15"`
- Output: `1`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Put both times on one minute axis.** Parse each clock time as `60 * hour + minute`. If logout is numerically earlier than login, add $1440$ minutes to logout, representing the next day. The session is then one ordinary half-open interval on a non-wrapping timeline.

**Round inward to complete boundaries.** The first round that can be fully played begins at the first multiple of $15$ not earlier than login:

$$
S = 15\left\lceil\frac{\textit{start}}{15}\right\rceil.
$$

The last usable round ends at the last multiple of $15$ not later than logout:

$$
E = 15\left\lfloor\frac{\textit{end}}{15}\right\rfloor.
$$

When $E \ge S$, the number of complete quarter-hour intervals is $(E-S)/15$. Otherwise there is no full round, so clamp the result at zero. These inward boundaries exclude partial rounds at both ends and handle midnight without separate before/after counts.

#### Complexity detail

Parsing two fixed-width strings and performing a fixed number of integer operations takes $O(1)$ time and $O(1)$ space. The legal domain contains only one day's 1,440 minute positions, so a `bounded_domain` certificate replaces meaningless runtime scaling with exhaustive validation of every distinct login/logout pair.

#### Alternatives and edge cases

- **Simulate every quarter-hour:** At most 96 rounds exist per day, but direct arithmetic is simpler and constant work.
- **Round login downward:** This incorrectly counts a round that had already started when the player logged in.
- **Round logout upward:** This incorrectly counts a round that was unfinished at logout.
- **Crossing midnight:** Add one day to logout only when its clock value is earlier than login.
- **Short session:** Even a positive-duration session can contain zero complete rounds.
- **Exact boundaries:** A login on a quarter-hour and logout on the following quarter-hour count exactly one round.

</details>
