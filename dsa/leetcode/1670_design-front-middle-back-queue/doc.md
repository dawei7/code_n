# Design Front Middle Back Queue

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 1670 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Linked List, Design, Queue, Doubly-Linked List, Data Stream |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/design-front-middle-back-queue/) |

## Problem Description
### Goal
Implement a `FrontMiddleBackQueue` that supports inserting and removing values at its front, middle, and back. Each push mutates the queue without returning a value. Each pop removes and returns the selected value, or returns `-1` without changing anything when the queue is empty.

When a queue of even length has two possible middle positions, every middle operation uses the frontmost choice. Thus `pushMiddle` inserts at index $\lfloor n/2 \rfloor$ in the current length-$n$ queue, while `popMiddle` removes index $\lfloor (n-1)/2 \rfloor$. At most 1000 operations follow construction.

### Function Contract
**Inputs**

- `operations`: a sequence beginning with `FrontMiddleBackQueue`, followed by method names `pushFront`, `pushMiddle`, `pushBack`, `popFront`, `popMiddle`, or `popBack`.
- `arguments`: one argument list per operation; pushes contain one integer `val`, while construction and pops use empty lists.

Let $q$ be the number of method calls after construction.

**Return value**

Return one result per operation: `null` for construction and pushes, the removed integer for a successful pop, and `-1` for any pop on an empty queue.

### Examples
**Example 1**

- Input: `operations = ["FrontMiddleBackQueue","pushFront","pushBack","pushMiddle","pushMiddle","popFront","popMiddle","popMiddle","popBack","popFront"]`, `arguments = [[],[1],[2],[3],[4],[],[],[],[],[]]`
- Output: `[null,null,null,null,null,1,3,4,2,-1]`

**Example 2**

- Input: push back `1`, `2`, and `3`, then pop the middle three times.
- Output: `[null,null,null,null,2,1,3]`
