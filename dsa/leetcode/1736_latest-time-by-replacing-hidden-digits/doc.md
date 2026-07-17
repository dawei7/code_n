# Latest Time by Replacing Hidden Digits

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1736 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | String, Greedy |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/latest-time-by-replacing-hidden-digits/) |

## Problem Description

### Goal

The five-character string `time` has the form `hh:mm`. Each position other than the colon contains either a decimal digit or `?`, which represents one hidden digit that may be replaced independently.

A time is valid when it lies from `00:00` through `23:59`, inclusive. Replace every `?` with a digit so the result is valid and as late as possible within that day, then return the completed string. The input guarantees that at least one valid completion exists.

### Function Contract

**Inputs**

- `time`: a string in `hh:mm` format whose four digit positions may contain `?`.

**Return value**

- Return the lexicographically and chronologically latest valid 24-hour time matching every visible digit.

### Examples

**Example 1**

- Input: `time = "2?:?0"`
- Output: `"23:50"`
- Explanation: The latest hour beginning with `2` is `23`, and the latest minute ending with `0` is `50`.

**Example 2**

- Input: `time = "0?:3?"`
- Output: `"09:39"`
- Explanation: The fixed leading zero limits the hour to `00` through `09`.

**Example 3**

- Input: `time = "1?:22"`
- Output: `"19:22"`
- Explanation: Only the hidden hour digit changes, and `9` gives the latest valid match.

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Choose the hour digits together**

For a hidden first hour digit, choose `2` only when the second hour digit is also hidden or is at most `3`; otherwise choose `1`. Once the first digit is known, a hidden second digit becomes `3` after a leading `2`, or `9` after a leading `0` or `1`. These choices produce the greatest valid hour compatible with the visible digits.

**Maximize each minute position**

Minute validity has independent positional limits: the tens digit is at most `5`, and the ones digit is at most `9`. Replace a hidden minute tens digit with `5` and a hidden minute ones digit with `9`.

**Why local maximum choices are globally valid**

Times in fixed-width `hh:mm` form are ordered first by hour, then by minute. The hour choices maximize the most significant positions without invalidating the pair, and the minute choices maximize the remaining positions independently. No smaller earlier digit can be compensated for by a later digit, so the completed value is the latest possible time.

#### Complexity detail

The input always has four digit positions and one colon. The algorithm performs a fixed number of character checks and replacements regardless of the digits, taking $O(1)$ time and $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Search backward through the day:** Testing times from `23:59` down to `00:00` is correct and still bounded, but it ignores the direct positional structure.
- **Maximize each hour digit independently:** Always choosing `2` for the first digit can make a visible second digit above `3` invalid.
- **Both hour digits hidden:** They become `23`, not `29`.
- **Second hour digit above three:** A hidden first digit must become `1`, allowing hours such as `19`.
- **All digits hidden:** The latest completion is `23:59`.
- **No hidden digits:** The already valid input is returned unchanged.
- **Minute boundary:** A hidden minute tens digit becomes `5`, never `9`.

</details>
