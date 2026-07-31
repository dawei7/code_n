## General

In every round, each row loses its current maximum. Therefore a row's removal sequence is its values in non-increasing order, regardless of how ties are chosen. Sorting every row establishes all of those sequences at once.

Sort each row in ascending order. Values at the same column index then have the same rank within their respective rows: column zero contains every row's smallest value, the next column contains every row's next-smallest value, and so on. Processing these columns from either direction represents the rounds in reverse or forward order. For each column, take its maximum and add it to the answer.

For a fixed rank, sorting places exactly the value that its row removes in the corresponding round at that column. Taking the maximum across the column therefore reproduces the value added to the score for that round. Summing all columns accounts for every round exactly once, so the resulting score matches the prescribed simulation.

## Complexity detail

Let $m$ be the number of rows and $n$ the common number of columns. Sorting all rows costs $O(mn \log n)$ time, and scanning the sorted columns costs $O(mn)$, so the total is $O(mn \log n)$. Python's in-place row sorts may use $O(n)$ auxiliary memory for one row's sort; the later scan uses constant extra space.

## Alternatives and edge cases

- **Repeated maximum removal:** Simulating each round with `max` and removal is direct but scans shrinking rows repeatedly, taking $O(mn^2)$ time.
- **Max-heaps per row:** Heapifying each row and popping once per round costs $O(mn \log n)$ time and $O(mn)$ copied heap space if the input is preserved.
- **Ties:** Equal row maxima are interchangeable, so their choice cannot change any round's cross-row maximum.
- **One row:** Every row value is eventually added, making the answer that row's sum.
- **Zeros:** Zero is a valid matrix value and can be the score contribution for a round.
