## General
Given a positive integer `s`, let `A` be a 3D array of dimensions<!-- notionvc: f8069282-c5f5-4da1-91b8-fa0c1c168ea1 --> `n × n × n`, where each element $A[i][j][k]$ is defined as:, the algorithm executes a single-pass linear scan through input elements. Key operations include bitwise operators (`&`, `|`, `^`, `<<`, `>>`) for fast bitmask state updates. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O(log^2 n)$ — Operation count bound.
- **Space Complexity**: $O(1)$ — Auxiliary memory allocation bound.
