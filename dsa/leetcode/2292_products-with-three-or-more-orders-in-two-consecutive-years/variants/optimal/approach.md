## General
The optimal solution implements an idiomatic, readable, and production-ready approach for **Products With Three or More Orders in Two Consecutive Years**.

- **Core Strategy**: Uses Common Table Expressions (CTEs) and window functions to structure table aggregations.
- **Implementation Design**: Structures relational queries cleanly using standard ANSI SQL / PostgreSQL aggregations (COALESCE, STRING_AGG).
- **Best Practice Standard**: Sourced from doocs/leetcode (software engineering interview standard). Follows industry standard software engineering guidelines with intuitive variable names and robust control flow.

## Complexity detail
- **Time Complexity**: $O(r log r)$ — Operational efficiency across problem constraints.
- **Space Complexity**: $O(g)$ — Auxiliary memory allocation bound.

## Alternatives and edge cases
- **Boundary handling:** Uniformly handles minimal inputs, empty cases, and extreme boundary values without explicit special-casing.
- **Implementation trade-offs:** Prioritizes code readability, maintainability, and standard software engineering patterns while guaranteeing optimal performance.
