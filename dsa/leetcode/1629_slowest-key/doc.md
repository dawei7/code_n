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

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Convert cumulative releases into individual durations.** Initialize the best pair from press 0, whose start time is fixed at zero. For each later index `i`, subtract the preceding release time from the current one. This local difference is exactly the interval during which `keysPressed[i]` was held.

**Compare duration before the tie-break key.** Replace the current answer when the new duration is greater. When durations are equal, replace it only if the new key is lexicographically larger. No comparison of key characters may override a strictly longer duration.

Every press is examined once and its exact duration is compared with the best of the preceding presses. After processing index `i`, the stored pair is therefore the required duration/key maximum for the prefix through `i`, including the specified tie rule. At the final index, that prefix is the entire test sequence.

#### Complexity detail

The scan performs constant work for each of the $n$ presses, taking $O(n)$ time. It stores only the preceding release time and current best duration and key, so auxiliary space is $O(1)$.

#### Alternatives and edge cases

- **Materialize and sort durations:** Sorting `(duration, key)` pairs gives the same answer in $O(n\log n)$ time and $O(n)$ space but does unnecessary work.
- **Compare every pair of presses:** Testing whether each press dominates all others is correct but takes $O(n^2)$ time.
- The first press starts at zero, so its duration is not a difference with another release time.
- Repeated occurrences of one key are separate presses and can have different durations.
- A tie is resolved by the key character, not by the earlier or later event position.
- Strictly increasing release times guarantee every duration is positive.

</details>
