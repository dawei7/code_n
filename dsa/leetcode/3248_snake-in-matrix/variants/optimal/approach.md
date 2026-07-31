## General

Let $c$ be the number of commands.

In row-major numbering, moving horizontally changes the flattened position by one: `RIGHT` adds $1$ and `LEFT` subtracts $1$. Moving vertically preserves the column and changes the row by one, so `DOWN` adds $n$ and `UP` subtracts $n$.

Map the four command strings to these displacements and sum them from the initial position zero. After any processed prefix, the running total equals `row * n + column` for the snake's actual cell: this is true initially, and each command adds exactly the change produced by its corresponding coordinate move. It therefore remains true after the complete sequence.

The input guarantees every intermediate coordinate is valid. No boundary correction, clamping, or wraparound behavior should be added.

## Complexity detail

Each of the $c$ commands performs one lookup and addition, for $O(c)$ time. The direction table has four fixed entries and the running position is one integer, so auxiliary space is $O(1)$.

## Alternatives and edge cases

- **Track row and column separately:** Updating a coordinate pair and converting with `row * n + column` at the end is equally correct but stores two changing values instead of one.
- **Build the matrix:** Materializing all $n^2$ labels is unnecessary because the position formula is already known.
- **Validate every boundary:** The contract guarantees a valid path; validation adds work without changing legal results.
- Opposite moves cancel when they occur along a valid path.
- A vertical move changes the position by $n$, not by one.
- The same command may occur many times as long as every prefix stays in bounds.
- Returning to the starting cell produces position zero.
- The bottom-right cell has position $n^2-1$.
- Intermediate positions matter for validity even though only the final position is returned.
