## Description

Consider an array of length `n` that was sorted in ascending order and then rotated between `1` and `n` times. For example, starting from `nums = [0, 1, 2, 4, 5, 6, 7]`:

- Four rotations produce `[4, 5, 6, 7, 0, 1, 2]`.
- Seven rotations produce `[0, 1, 2, 4, 5, 6, 7]` again.

One rotation changes `[a[0], a[1], a[2], ..., a[n-1]]` into `[a[n-1], a[0], a[1], a[2], ..., a[n-2]]`.

Given such a sorted and rotated array `nums` whose elements are unique, return its minimum element. Your algorithm must run in $O(\log n)$ time.
