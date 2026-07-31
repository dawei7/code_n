## General

**Turn swaps into zeros inside a target block**

Let $k$ be the total number of ones. Any final block containing all ones has
exactly $k$ positions. For a chosen circular window of that length, every zero
inside must be swapped with a one outside, and each such swap fixes one
position. Thus the window needs exactly as many swaps as it currently contains
zeros.

Compute the zero count in the first length-$k$ window. Slide the window through
all circular starting positions using modular indices, subtracting the element
that leaves and adding the one that enters. Retain the minimum zero count.

Every possible destination block is examined, and its zero count is both a
lower bound and an achievable number of swaps. The smallest count is therefore
the optimum. If there are zero or one ones, no swap is needed.

## Complexity detail

Let $n$ be the array length. Counting ones and sliding through all $n$ circular
windows take $O(n)$ time. Only counters and indices are stored, so auxiliary
space is $O(1)$.

## Alternatives and edge cases

- **Recount every circular window:** Directly summing all $k$ positions for
  every start is correct but takes $O(n^2)$ time when $k=\Theta(n)$.
- **Duplicate the array:** A conventional window over `nums + nums` is simple
  and still takes $O(n)$ time, but uses $O(n)$ extra space.
- With no ones, the empty group requires zero swaps.
- With one one or all ones, the answer is zero.
- The best block may cross the stored array boundary.
