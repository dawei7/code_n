# Minimum Cost to Set Cooking Time

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2162 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Math, Enumeration |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/minimum-cost-to-set-cooking-time/) |

## Problem Description

### Goal

A microwave accepts between one and four digit presses. Before interpreting
the entry, it pads the pressed sequence on the left with zeros to obtain four
digits. The first two digits form a minute value and the last two form a second
value; the cooking duration is the sum of those minutes and seconds. Both
fields may exceed ordinary clock notation, so an entry such as `0960` is valid
and represents $9\cdot 60+60=600$ seconds.

Your finger begins over one specified digit. Moving it to a different digit
costs `moveCost`, while every press costs `pushCost`; repeated presses of the
same digit require no additional move. Find the minimum fatigue cost of an
entry whose interpreted duration is exactly `targetSeconds`.

### Function Contract

**Inputs**

- `startAt`: the digit, from `0` through `9`, where the finger begins.
- `moveCost`: the positive cost of moving the finger to a different digit.
- `pushCost`: the positive cost of pressing the current digit once.
- `targetSeconds`: the required duration, from `1` through `6039` seconds.

An entry uses at most four digits. After left-padding, its minute and second
fields must both lie from `00` through `99`.

**Return value**

Return the minimum total movement and pressing cost among all entries that
represent exactly `targetSeconds`.

### Examples

#### Example 1

- **Input:** `startAt = 1, moveCost = 2, pushCost = 1, targetSeconds = 600`
- **Output:** `6`

Pressing `1000` represents ten minutes. The finger presses `1`, moves once to
`0`, and presses `0` three times, for a total cost of $6$.

#### Example 2

- **Input:** `startAt = 0, moveCost = 1, pushCost = 2, targetSeconds = 76`
- **Output:** `6`

The entry `76` is padded to `0076`. It requires two moves and two presses.

#### Example 3

- **Input:** `startAt = 9, moveCost = 1, pushCost = 100000, targetSeconds = 6039`
- **Output:** `400000`

The largest legal duration is entered as `9999`; the finger never moves and
four presses are required.
