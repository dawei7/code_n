# Design Phone Directory

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 379 |
| Difficulty | Medium |
| Topics | Array, Hash Table, Linked List, Design, Queue |
| Official Link | [LeetCode](https://leetcode.com/problems/design-phone-directory/) |

## Problem Description
### Goal
Design a directory managing phone numbers `0` through `maxNumbers - 1`, all initially available. `get()` reserves and returns any currently available number, or returns `-1` when every number is allocated.

`check(number)` reports whether that number is presently available without reserving it. `release(number)` returns an allocated number to the available pool; releasing an already available number has no additional effect. Preserve allocation state across the chronological operation sequence and never hand out one number to two active callers. The app returns results for `get` and `check`, while release produces no value.

### Function Contract
**Inputs**

- `max_numbers`: the number of directory entries
- `operations`: for the app adapter, a chronological list containing `["get"]`, `["check", number]`, and `["release", number]`

**Return value**

- The app adapter returns one value for each `get` or `check` operation. A get returns an available number or `-1`; a check returns a Boolean. Native LeetCode calls the corresponding `PhoneDirectory` methods directly.

### Examples
**Example 1**

- Input: `max_numbers = 3, operations = [["get"],["get"],["check",2],["get"],["check",2]]`
- Output: `[0,1,True,2,False]`

**Example 2**

- Input: `max_numbers = 1, operations = [["get"],["get"]]`
- Output: `[0,-1]`

**Example 3**

- Input: `max_numbers = 2, operations = [["get"],["release",0],["check",0],["get"]]`
- Output: `[0,True,0]`
