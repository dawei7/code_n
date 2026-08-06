## Description

You are given an array `start` where `start = [startX, startY]` represents your initial position `(startX, startY)` in a 2D space. You are also given the array `target` where `target = [targetX, targetY]` represents your target position `(targetX, targetY)`.

The **cost** of going from a position `(x1, y1)` to any other position in the space `(x2, y2)` is `|x2 - x1| + |y2 - y1|`.

There are also some **special roads**. You are given a 2D array `specialRoads` where `specialRoads[i] = [x1_i, y1_i, x2_i, y2_i, cost_i]` indicates that the `i^th` special road goes in **one direction** from `(x1_i, y1_i)` to `(x2_i, y2_i)` with a cost equal to `cost_i`. You can use each special road any number of times.

Return the **minimum** cost required to go from `(startX, startY)` to `(targetX, targetY)`.
