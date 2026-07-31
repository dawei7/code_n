## Description

Given an integer stream and a window size, calculate the moving average over the integers currently in the sliding window.

Implement the `MovingAverage` class:

- `MovingAverage(int size)` initializes an object whose window can contain up to `size` stream values.
- `double next(int val)` appends `val` and returns the average of the last `size` values, or of all values seen so far when fewer than `size` have arrived.
