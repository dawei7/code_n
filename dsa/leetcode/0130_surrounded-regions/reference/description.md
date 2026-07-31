## Description

You are given an $m \times n$ matrix `board` containing only `'X'` and `'O'`. Capture every surrounded region according to these definitions:

- **Connected:** Two cells connect when they share a horizontal or vertical side.
- **Region:** A region consists of `'O'` cells connected through those side adjacencies.
- **Surrounded:** A region is surrounded when none of its `'O'` cells lies on the board's edge; such a region is completely enclosed by `'X'` cells.

Capture a surrounded region by replacing each of its `'O'` cells with `'X'` directly in the original board. Do not return a separate result.
