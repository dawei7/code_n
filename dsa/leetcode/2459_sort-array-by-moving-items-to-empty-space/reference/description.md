## Description

You are given an integer array `nums` of length $n$ containing every value from $0$ through $n - 1$ exactly once. Values $1$ through $n - 1$ represent numbered items, while `0` represents one empty space.

In one operation, choose any item and move it into the empty position; the item's previous position becomes the new empty space. The array is sorted when all item numbers appear in ascending order and the empty space is at either end. Thus the two valid final layouts are `[0, 1, ..., n - 1]` and `[1, 2, ..., n - 1, 0]`.

Return the minimum number of operations required to reach either valid layout.
