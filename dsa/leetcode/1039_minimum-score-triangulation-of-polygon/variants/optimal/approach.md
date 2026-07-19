## General
**Define a subpolygon interval:** Let `dp[left][right]` be the minimum score for the polygonal chain from vertex `left` through vertex `right`, closed by the edge between those endpoints. Fewer than three vertices require no triangle and have score zero.

**Choose the triangle touching the closing edge:** In any triangulation of an interval with at least three vertices, exactly one triangle uses endpoints `left` and `right`. Let its third vertex be `middle`. That triangle contributes `values[left] * values[middle] * values[right]` and separates the remaining region into independent left and right subpolygons.

**Evaluate every split bottom-up:** For increasing interval lengths, minimize the triangle contribution plus `dp[left][middle]` and `dp[middle][right]` over every interior `middle`. Smaller subintervals are already complete when needed.

Every candidate combines two valid triangulations with their separating triangle, so it forms a valid full triangulation. Conversely, the triangle on the closing edge exists in every triangulation and identifies one of the tested splits. Induction on interval length therefore proves the minimum state and final answer.

## Complexity detail
There are $O(N^2)$ vertex intervals, and each tests $O(N)$ middle vertices, for $O(N^3)$ time. The interval table stores $O(N^2)$ scores.

## Alternatives and edge cases
- **Top-down memoization:** Recursively evaluate the same interval recurrence and cache states for identical $O(N^3)$ time and $O(N^2)$ stored results, plus recursion depth.
- **Enumerate triangulations:** Generate every diagonal arrangement and score it. The number of triangulations is a Catalan number and grows exponentially.
- **Recompute subinterval choices:** Re-evaluating already solved smaller intervals inside every split remains correct but adds another factor of $N$.
- **Triangle input:** With exactly three vertices, there is only one possible score.
- **Equal values:** Every triangulation has the same score of $(N-2)v^3$ when all values equal $v$.
- **Clockwise order:** The array order defines adjacency and cannot be sorted by value.
- **Large vertex values:** Products and total scores require ordinary integer arithmetic without geometric rounding.
