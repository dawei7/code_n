# Single-Row Keyboard

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1165 |
| Difficulty | Easy |
| Category | Algorithms |
| Topics | Hash Table, String |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/single-row-keyboard/) |

## Problem Description

### Goal

A special keyboard places all $26$ lowercase English letters in one row. The string `keyboard` gives their left-to-right layout at indices `0` through `25`, with every letter appearing exactly once. A finger begins at index `0`.

To type a character, move the finger from its current index $i$ to that character's index $j$. This movement takes $\lvert i-j \rvert$ time, and the finger remains at $j$ for the next character. Given `word`, calculate the total time required to type the entire string with that one finger.

### Function Contract

**Inputs**

- `keyboard`: A length-$26$ permutation of the lowercase English letters.
- `word`: A lowercase English string of length $m$, where $1 \le m \le 10^4$.

**Return value**

- The sum of the finger-movement times needed to type `word`, starting from keyboard index `0`.

### Examples

**Example 1**

- Input: `keyboard = "abcdefghijklmnopqrstuvwxyz"`, `word = "cba"`
- Output: `4`

The finger moves from index `0` to `2`, then to `1`, and finally back to `0`, costing `2 + 1 + 1`.

**Example 2**

- Input: `keyboard = "pqrstuvwxyzabcdefghijklmno"`, `word = "leetcode"`
- Output: `73`

### Required Complexity

- **Time:** $O(m)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Index the fixed layout once.** Build a mapping from each letter to its index in `keyboard`. Since every lowercase English letter occurs exactly once, every character in `word` has one well-defined destination.

**Accumulate consecutive movements.** Set `current = 0` and `total = 0`. For each character in `word`, obtain its mapped destination, add `abs(destination - current)` to `total`, and then assign `current = destination`. This follows the typing process in order: after a character is typed, its key is precisely the starting position for the next movement.

The running sum contains the cost of every required move exactly once, including the initial move from index `0`. Therefore, after the final character, `total` is the requested typing time.

#### Complexity detail

Building the position map scans the fixed $26$-character keyboard. The word scan performs constant work per character, so the total time is $O(26+m)=O(m)$. The map has exactly $26$ entries, which is $O(1)$ space because the alphabet is fixed.

#### Alternatives and edge cases

- **Call `keyboard.index` for each character:** This is correct, but each lookup scans up to $26$ fixed positions; it remains $O(m)$ under this problem's fixed alphabet and differs only by a constant factor.
- **Simulate one-index steps:** Moving a cursor one position at a time also stays $O(m)$ because every movement is at most $25$, but directly adding the absolute difference is simpler.
- **Repeated letter:** Typing the same character consecutively adds zero after the first occurrence because the finger is already on its key.
- **First key:** A word beginning with `keyboard[0]` incurs zero initial movement.
- **Reversed layout:** Indices come from `keyboard`, not alphabetical order.

</details>
