## Description

You are given a 2D integer array `points`, where `points[i] = [x_i, y_i]`. You are also given an integer `w`. Your task is to **cover** **all** the given points with rectangles.

Each rectangle has its lower end at some point `(x_1, 0)` and its upper end at some point `(x_2, y_2)`, where `x_1 <= x_2`, `y_2 >= 0`, and the condition `x_2 - x_1 <= w` **must** be satisfied for each rectangle.

A point is considered covered by a rectangle if it lies within or on the boundary of the rectangle.

Return an integer denoting the **minimum** number of rectangles needed so that each point is covered by **at least one** rectangle*.*

**Note:** A point may be covered by more than one rectangle.
