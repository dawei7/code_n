## Description

A city's **skyline** is the outer contour of the silhouette made by all its buildings when viewed from a distance. Given the positions and heights of the buildings, return the skyline they form together.

Each entry `buildings[i] = [left_i, right_i, height_i]` describes one building:

- `left_i` is the x-coordinate of its left edge.
- `right_i` is the x-coordinate of its right edge.
- `height_i` is its height.

Every building is a rectangle standing on a perfectly flat surface at height `0`.

Represent the skyline as key points sorted by x-coordinate: `[[x_1,y_1],[x_2,y_2],...]`. Each point begins a horizontal contour segment. The final point is the exception: its height is always `0`, marking where the skyline ends at the right edge of the last building. Ground-level gaps between the leftmost and rightmost buildings remain part of the contour.
