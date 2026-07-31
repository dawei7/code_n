## Description

You are given a collection `points` of distinct points in the integer coordinate plane. Each entry `points[i] = [x_i, y_i]` identifies one point.

Whenever a point becomes **activated**, every point sharing its x-coordinate or its y-coordinate also becomes activated. Those newly activated points apply the same rule, so propagation continues until it cannot reach another point.

You must add exactly one point at an integer coordinate `(x, y)` that is not already present. Activation starts from this new point. Choose its coordinate to maximize the final number of activated points, counting the added point itself, and return that maximum.
