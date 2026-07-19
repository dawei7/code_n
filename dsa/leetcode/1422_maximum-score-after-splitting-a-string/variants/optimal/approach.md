## General
**Count right-side ones before splitting.** Initially, every `1` belongs to the unsplit right side. Store their total, along with a left-zero count starting at zero.

Move the split boundary from left to right, processing positions zero through `n - 2` so the final character always remains in the right part. When the crossed character is `0`, increment the left-zero count. When it is `1`, decrement the right-one count. Their sum is then the score of the boundary immediately after that character; retain the largest sum.

Each update transfers exactly the crossed character from right to left. Thus the two counters equal the score definition at every legal boundary, and every legal boundary is considered once. The maximum recorded value is therefore the optimal score.

## Complexity detail
Counting the initial ones and scanning the $n-1$ legal boundary positions take $O(n)$ time. The two counters and maximum use $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Count both substrings per split:** Slicing and recounting each side is direct but takes $O(n^2)$ time.
- **Prefix arrays:** Store zero prefixes and one suffixes. This also takes $O(n)$ time but uses $O(n)$ extra space unnecessarily.
- **Length two:** There is exactly one legal split.
- **All zeros:** The best boundary leaves one character on the right and scores $n-1$.
- **All ones:** The best boundary leaves one `1` on the right and also scores $n-1$.
- **Zero score:** The string `"10"` has a legal split whose two counted categories are both absent.
- **Nonempty parts:** Never evaluate a boundary after the last character.
