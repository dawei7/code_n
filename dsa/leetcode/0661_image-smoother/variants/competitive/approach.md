## General
Given An **image smoother** is a filter of the size `3 x 3` that can be applied to each cell of an image by rounding down the average of the cell and the eight surrounding cells (i.e., the average of the nine cells in the b..., the algorithm executes a single-pass linear scan through input elements.

## Complexity detail
- **Time Complexity**: $O(R \cdot C)$ — Operation count bound.
- **Space Complexity**: $O(R \cdot C)$ — Auxiliary memory allocation bound.
