## Description

The array `lights` describes a road with positions from `0` through `n - 1`. A positive value `lights[i] = v` means that a working bulb at position `i` illuminates every road position in the inclusive interval from `max(0, i - v)` through `min(n - 1, i + v)`. A zero means that no working bulb is present there. A position is visible when at least one working bulb illuminates it.

You may add bulbs at any road positions. Every added bulb has radius one: a bulb placed at `j` illuminates the inclusive interval from `max(0, j - 1)` through `min(n - 1, j + 1)`.

Return the minimum number of added bulbs needed so that every road position is visible.
