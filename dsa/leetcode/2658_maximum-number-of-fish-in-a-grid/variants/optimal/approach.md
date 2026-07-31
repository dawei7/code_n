## General

Positive cells form vertices of a grid graph, with edges between orthogonally adjacent positive cells. From any starting water cell, the fisher can reach exactly that cell's connected component and can collect every fish in it. The answer is therefore the maximum sum of cell values over all positive connected components.

Scan the matrix. Whenever an unvisited positive cell is found, start an iterative depth-first traversal, mark each discovered neighbor before pushing it, and add every popped cell's fish to the component total. Marking on discovery prevents a cell from being pushed more than once even when several neighbors lead to it.

After the traversal finishes, compare its sum with the current maximum. The outer scan eventually starts one traversal for every component because its first encountered cell is initially unvisited. Each traversal visits exactly the cells reachable from that start, so its sum is precisely the fish obtainable from any start in that component. Taking the largest of these sums is optimal; if no traversal starts, the maximum remains zero.

## Complexity detail

Let $m$ and $n$ be the grid dimensions. Each cell is inspected by the outer scan and each positive cell is visited once, with four constant-time neighbor checks, so the running time is $O(mn)$. The visited matrix and traversal stack can each contain $O(mn)$ entries, giving $O(mn)$ auxiliary space.

The benchmark uses `size` as the number of cells in a fully connected square grid. A correct alternative that independently floods from every water cell without sharing visited state completes all legal tiers but takes $O((mn)^2)$ time.

## Alternatives and edge cases

- **Breadth-first search:** A queue discovers the same components with identical $O(mn)$ time and space bounds.
- **Union-find:** Joining adjacent water cells and tracking component weights is correct but adds structure without improving the asymptotic bound.
- **Restart a search at every water cell:** This produces correct component sums but repeats the same traversal and can take $O((mn)^2)$ time.
- Land cells are barriers and contribute no fish.
- Diagonal water cells are not connected unless an orthogonal water path joins them.
- An all-land grid returns `0`, while a single water cell returns its own value.
- The richest component need not contain the largest individual cell.
