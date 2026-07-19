# First Unique Number

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1429 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Hash Table, Design, Queue, Data Stream |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| LeetCode | [Open Problem](https://leetcode.com/problems/first-unique-number/) |

## Problem Description

### Goal

Design a `FirstUnique` object for a stream of integers. It begins with the values in `nums`, preserving their arrival order. A value is unique exactly when it has appeared once among the initial values and every value added so far.

The `showFirstUnique()` operation must return the earliest currently unique value, or `-1` if none exists. The `add(value)` operation appends one occurrence of `value` to the stream and does not return a value. Later additions may invalidate an earlier unique value but never change the order in which values first arrived.

### Function Contract

**Inputs**

- `operations`: a sequence beginning with `"FirstUnique"`, followed by `"showFirstUnique"` and `"add"` calls.
- `arguments`: arguments aligned with `operations`. The constructor receives one integer array `nums`; `add` receives one integer; `showFirstUnique` receives no arguments.
- Let $n$ be the length of the initial array and $q$ the number of later operations.

**Return value**

- A list aligned with the operation trace: `null` for construction and every `add` call, and the requested integer for each `showFirstUnique` call.

### Examples

**Example 1**

- Input: `operations = ["FirstUnique","showFirstUnique","add","showFirstUnique","add","showFirstUnique","add","showFirstUnique"]`, `arguments = [[[2,3,5]],[],[5],[],[2],[],[3],[]]`
- Output: `[null,2,null,2,null,3,null,-1]`

**Example 2**

- Input: `operations = ["FirstUnique","showFirstUnique","add","add","add","add","add","showFirstUnique"]`, `arguments = [[[7,7,7,7,7,7]],[],[7],[3],[3],[7],[17],[]]`
- Output: `[null,-1,null,null,null,null,null,17]`

**Example 3**

- Input: `operations = ["FirstUnique","showFirstUnique","add","showFirstUnique"]`, `arguments = [[[809]],[],[809],[]]`
- Output: `[null,809,null,-1]`
