# Next Closest Time

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 681 |
| Difficulty | Medium |
| Topics | Hash Table, String, Backtracking, Enumeration |
| Official Link | [LeetCode](https://leetcode.com/problems/next-closest-time/) |

## Problem Description
### Goal
Given a valid 24-hour time in `HH:MM` format, find the next clock time whose four displayed digits are all taken from the original display. A digit that appears once in the input may be reused any number of times in the result.

Move forward chronologically and return the first valid display encountered, preserving the `HH:MM` format. If no later time on the same day works, continue after midnight into the following day. The answer must be strictly later in cyclic time, so returning the unchanged display is allowed only after a full-day wrap.

### Function Contract
**Inputs**

- `time`: a valid zero-padded 24-hour time string

**Return value**

- The closest strictly later cyclic time display constructible from the input's digits

### Examples
**Example 1**

- Input: `time = "19:34"`
- Output: `"19:39"`

**Example 2**

- Input: `time = "23:59"`
- Output: `"22:22"`

**Example 3**

- Input: `time = "11:11"`
- Output: `"11:11"`

### Required Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Generate displays from the allowed digits**

Remove the colon and take the set of displayed digits. Enumerate every four-position selection with repetition from this set. At most four digits are available, so there are at most $4^{4} = 256$ arrangements.

**Reject arrangements that are not valid times**

Interpret the first two selected digits as an hour and the last two as a minute. Keep only hours below 24 and minutes below 60. Convert each valid display to minutes since midnight.

**Measure forward distance on the daily cycle**

For a candidate minute value, compute its forward difference from the input modulo 1,440. A zero difference represents the same display on the next day, so treat it as 1,440 rather than zero. Choose the valid candidate with the smallest positive cyclic difference. The original display is always constructible, guaranteeing a fallback after one full day.

**Why the chosen candidate is the next time**

Enumeration covers every display using only allowed digits, including repeated uses, and validity filtering removes exactly the impossible clock readings. Modular distance is precisely the number of forward minutes required to reach each remaining display. Minimizing that positive distance therefore returns the first legal display encountered in time order.

#### Complexity detail

The clock domain and the number of input digit positions are fixed. At most 256 arrangements are generated, each with constant work, so time and auxiliary space are both $O(1)$ with respect to input size.

#### Alternatives and edge cases

- **Advance one minute at a time:** test each new display until its digits are allowed; it is simple and bounded by 1,440 iterations, but runtime depends on the cyclic waiting distance.
- **Scan all 1,440 clock displays:** collect valid candidates and select the minimum cyclic distance; this is also constant for the fixed clock domain but performs more work than digit enumeration.
- **Greedily increment individual positions:** can be fast, but hour and minute validity plus carry and wrap rules make the case analysis error-prone.
- The returned time must be strictly later, so the identical display represents the next day's occurrence.
- Input digits may be reused more times than they originally appeared.
- Leading zeros are display digits and must be preserved in the returned `HH:MM` format.

</details>
