## General
Given an array of non-overlapping axis-aligned rectangles `rects` where $\text{rects}[i] = [a_{i}, b_{i}, x_{i}, y_{i}]$ indicates that $(a_{i}, b_{i})$ is the bottom-left corner point of the $$i^{\text{th}}$$ rectangle and..., the algorithm executes a single-pass linear scan through input elements.

## Complexity detail
- **Time Complexity**: $O(r + d \log r)$ — Operation count bound.
- **Space Complexity**: $O(r + d)$ — Auxiliary memory allocation bound.
