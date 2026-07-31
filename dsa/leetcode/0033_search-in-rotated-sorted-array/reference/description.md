## Description

An integer array with distinct values was originally sorted in ascending order. Before it reaches the function, it may have been left-rotated at an unknown index $k$, where $1 \le k < n$. Such a rotation changes

```text
[nums[0], ..., nums[k-1], nums[k], ..., nums[n-1]]
```

into

```text
[nums[k], ..., nums[n-1], nums[0], ..., nums[k-1]].
```

For example, rotating `[0, 1, 2, 4, 5, 6, 7]` left by three positions produces `[4, 5, 6, 7, 0, 1, 2]`.

Given the possibly rotated array `nums` and an integer `target`, return the target's index or `-1` if it is absent. The algorithm must run in $O(\log n)$ time.
