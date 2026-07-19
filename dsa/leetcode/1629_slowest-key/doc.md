# Slowest Key

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1629 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Array, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/slowest-key/) |

## Problem Description
### Goal
A tester presses $n$ keypad keys one at a time. `keysPressed[i]` identifies the $i$th key, and the strictly increasing value `releaseTimes[i]` is when that press ends. The first press starts at time 0; every later press starts exactly when its predecessor is released. The same key may appear more than once, with different durations on different presses.

Find the individual keypress with the longest duration. If several presses share that maximum duration, return the lexicographically largest key among those tied presses.

### Function Contract
**Inputs**

- `releaseTimes`: a strictly increasing integer array of length $n$, where $2 \le n \le 1000$ and $1 \le \texttt{releaseTimes[i]} \le 10^9$.
- `keysPressed`: a length-$n$ string of lowercase English letters in the same event order.
- Press 0 lasts `releaseTimes[0]`; press `i > 0` lasts `releaseTimes[i] - releaseTimes[i - 1]`.

**Return value**

Return the character associated with the greatest press duration, breaking a duration tie in favor of the lexicographically largest character.

### Examples
**Example 1**

- Input: `releaseTimes = [9,29,49,50], keysPressed = "cbcd"`
- Output: `"c"`

The `b` press and the second `c` press both last 20, so `c` wins the tie.

**Example 2**

- Input: `releaseTimes = [12,23,36,46,62], keysPressed = "spuda"`
- Output: `"a"`

The final `a` press lasts 16, longer than every earlier press.

**Example 3**

- Input: `releaseTimes = [1,3,5], keysPressed = "abc"`
- Output: `"c"`

The last two presses both last 2, and `c` is lexicographically larger.
