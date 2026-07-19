# My Calendar I

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 729 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Design, Segment Tree, Ordered Set |
| Official Link | [LeetCode](https://leetcode.com/problems/my-calendar-i/) |

## Problem Description
### Goal
Design `MyCalendar` to store event bookings. A call `book(startTime, endTime)` proposes the half-open interval `[startTime, endTime)`, containing all real times `x` with `startTime <= x < endTime`.

Return `True` and store the event when adding it would not cause a double booking; otherwise return `False` and leave the calendar unchanged. A double booking exists when two events have a nonempty time intersection. Events whose endpoints merely touch do not overlap because the ending time is excluded.

### Function Contract
**Inputs**

- `operations`: an ordered list of `["book", start, end]` calls, where each interval contains times `start <= t < end`

**Return value**

- One boolean per operation: `True` when that booking is accepted and stored, otherwise `False` with calendar state unchanged

### Examples
**Example 1**

- Input: `operations = [["book",10,20],["book",15,25],["book",20,30]]`
- Output: `[true,false,true]`

**Example 2**

- Input: `operations = [["book",1,2],["book",2,3],["book",0,1]]`
- Output: `[true,true,true]`

**Example 3**

- Input: `operations = [["book",5,10],["book",5,10]]`
- Output: `[true,false]`
