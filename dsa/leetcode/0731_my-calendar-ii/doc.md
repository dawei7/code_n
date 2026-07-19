# My Calendar II

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 731 |
| Difficulty | Medium |
| Topics | Array, Binary Search, Design, Segment Tree, Prefix Sum, Ordered Set |
| Official Link | [LeetCode](https://leetcode.com/problems/my-calendar-ii/) |

## Problem Description
### Goal
Design `MyCalendarTwo` for events represented by half-open intervals `[startTime, endTime)`. A double booking is allowed, but a triple booking occurs when three accepted events share a nonempty interval of time.

For each `book(startTime, endTime)` call, return `True` and store the event unless doing so would create a triple booking. If any time would then belong to three events, return `False` and leave the calendar unchanged. Events that only meet at an excluded right endpoint do not overlap.

### Function Contract
**Inputs**

- `operations`: an ordered list of `["book", start, end]` calls representing times `start <= t < end`

**Return value**

- One boolean per operation: `True` if the interval can be stored without creating a triple booking, otherwise `False` with the calendar unchanged

### Examples
**Example 1**

- Input: `operations = [["book",10,20],["book",50,60],["book",10,40],["book",5,15],["book",5,10],["book",25,55]]`
- Output: `[true,true,true,false,true,true]`

**Example 2**

- Input: `operations = [["book",5,10],["book",5,10],["book",5,10]]`
- Output: `[true,true,false]`

**Example 3**

- Input: `operations = [["book",1,5],["book",5,9],["book",3,7],["book",4,6]]`
- Output: `[true,true,true,false]`
