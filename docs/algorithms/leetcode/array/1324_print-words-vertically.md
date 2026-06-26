# Print Words Vertically

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1324 |
| Difficulty | Medium |
| Topics | Array, String, Simulation |
| Official Link | [print-words-vertically](https://leetcode.com/problems/print-words-vertically/) |

## Problem Description & Examples
### Goal
Given a sentence, write its words top-to-bottom in columns and return the resulting vertical rows. Trailing spaces must be removed from each returned row.

### Function Contract
**Inputs**

- `s`: sentence containing words separated by single spaces.

**Return value**

The vertical reading of the sentence as a list of strings.

### Examples
**Example 1**

- Input: `s = "HOW ARE YOU"`
- Output: `["HAY","ORO","WEU"]`

**Example 2**

- Input: `s = "TO BE OR NOT"`
- Output: `["TBON","OERO","   T"]`

**Example 3**

- Input: `s = "CONTEST IS COMING"`
- Output: `["CIC","OSO","N M","T I","E N","S G","T"]`

---

## Underlying Base Algorithm(s)
String matrix simulation.

---

## Complexity Analysis
- **Time Complexity**: `O(total characters including padding)`
- **Space Complexity**: `O(total characters in output)`
