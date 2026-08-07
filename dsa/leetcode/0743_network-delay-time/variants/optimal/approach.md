## General
Given a network of `n` nodes, labeled from `1` to `n`. You are also given `times`, a list of travel times as directed edges $\text{times}[i] = (u_{i}, v_{i}, w_{i})$, where $u_{i}$ is the source node, $v_{i}$ is the target ..., the algorithm executes a single-pass linear scan through input elements. Edge case handling: guards against empty/null inputs via early returns.

## Complexity detail
- **Time Complexity**: $O((n+e) \log n)$ — Operation count bound.
- **Space Complexity**: $O(n+e)$ — Auxiliary memory allocation bound.
