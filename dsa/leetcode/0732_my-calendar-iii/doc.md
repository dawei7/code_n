# My Calendar III

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 732 |
| Difficulty | Hard |
| Topics | Binary Search, Design, Segment Tree, Prefix Sum, Ordered Set |
| Official Link | [LeetCode](https://leetcode.com/problems/my-calendar-iii/) |

## Problem Description
### Goal
A `k`-booking exists when `k` events share a nonempty intersection of time. Design `MyCalendarThree` to accept every event represented by the half-open interval `[startTime, endTime)`.

After permanently adding each event, return the largest integer `k` for which a `k`-booking exists among all events received so far. The reported maximum may stay the same or increase as bookings accumulate. Events that only touch at an endpoint do not overlap because `endTime` is excluded.

### Function Contract
**Inputs**

- `operations`: an ordered list of `["book", start, end]` calls representing times `start <= t < end`

**Return value**

- One integer per operation: the calendar's maximum overlap after permanently adding that interval

### Examples
**Example 1**

- Input: `operations = [["book",10,20],["book",50,60],["book",10,40],["book",5,15],["book",5,10],["book",25,55]]`
- Output: `[1,1,2,3,3,3]`

**Example 2**

- Input: `operations = [["book",5,10],["book",5,10],["book",5,10],["book",5,10]]`
- Output: `[1,2,3,4]`

**Example 3**

- Input: `operations = [["book",1,5],["book",5,9],["book",3,7],["book",4,6]]`
- Output: `[1,1,2,3]`
