## General

The path may be chosen as part of the output, so select the simplest monotone route: traverse the entire top row from left to right, then traverse the last column from top to bottom. Mark every cell on that route free and every other cell as an obstacle.

The construction can be written row by row. The first row contains `n` free cells. Every later row contains `n - 1` obstacles followed by one free cell. This also covers a one-column grid because the obstacle prefix is empty.

To see why the path is unique, consider any free cell in the top row before the last column. The cell below it is blocked, so a valid path must move right. Once the path reaches the top-right cell, every later free cell is directly below it in the last column, while each cell to the left is blocked; the path must therefore move down until it reaches the destination. There is a valid route and no step offers an alternative, proving that exactly one valid path exists. The same reasoning degenerates correctly to all-right movement when `m = 1` and all-down movement when `n = 1`.

## Complexity detail

The returned strings contain $mn$ characters, and the construction writes each of them once, so the running time is $O(mn)$. The returned grid occupies $O(mn)$ space; beyond that required output, the construction uses $O(1)$ auxiliary state.

Any correct solution must materialize all $mn$ output characters, giving an $\Omega(mn)$ lower bound. Because this construction meets that bound, the package records an asymptotic-optimality certificate instead of trying to distinguish implementations with runtime tiers over the small $25 \times 25$ legal domain.

## Alternatives and edge cases

- **Free first column and bottom row:** Moving down first and then right is a symmetric $O(mn)$ construction with the same uniqueness proof.
- **Build a winding corridor:** A longer simple route can also be isolated, but turns introduce extra adjacency cases without improving the bound or the result.
- **Leave the whole grid free:** This works only when one dimension is one; otherwise several right/down move orders reach the destination.
- **One row:** The first row is the whole output, so every cell is free and the path consists only of right moves.
- **One column:** Each row's obstacle prefix has length zero, so the only column is free and the path consists only of down moves.
- **Maximum dimensions:** The returned grid still contains only 625 characters, but every character must be present and validated.
