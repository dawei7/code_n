# Freedom Trail

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 514 |
| Difficulty | Hard |
| Topics | String, Dynamic Programming, Depth-First Search, Breadth-First Search |
| Official Link | [LeetCode](https://leetcode.com/problems/freedom-trail/) |

## Problem Description
### Goal
The circular string `ring` is engraved around a dial, initially with `ring[0]` aligned at the 12 o'clock position. To spell `key` from left to right, rotate the ring in place clockwise or counterclockwise until the required character is aligned, then press the center button to select it.

Each one-position rotation costs one step and each button press costs one step. Return the minimum total steps needed to spell every character of `key`. Repeated ring characters offer alternative alignments, and the cheapest occurrence for one key character may depend on the positions needed later; the key is guaranteed to be spellable.

### Function Contract
**Inputs**

- `ring`: a nonempty circular string whose index `0` initially faces the selector
- `key`: a nonempty string whose characters all occur in `ring`

**Return value**

- The minimum number of rotations and button presses needed to spell `key` in order

### Examples
**Example 1**

- Input: `ring = "godding", key = "gd"`
- Output: `4`

**Example 2**

- Input: `ring = "godding", key = "godding"`
- Output: `13`

**Example 3**

- Input: `ring = "a", key = "a"`
- Output: `1`
