## General
Given a **0-indexed** 2D integer array `tires` where $\text{tires}[i] = [f_{i}, r_{i}]$ indicates that the $$i^{\text{th}}$$ tire can finish its $$x^{\text{th}}$$ successive lap in $f_{i} * r_{i}^(x-1)$ seconds, the algorithm executes a single-pass linear scan through input elements.

## Complexity detail
- **Time Complexity**: $O(TL + NL)$ — Operation count bound.
- **Space Complexity**: $O(N + L)$ — Auxiliary memory allocation bound.
