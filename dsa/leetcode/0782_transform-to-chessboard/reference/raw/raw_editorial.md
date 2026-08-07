[TOC]

---
### Approach #1: Dimension Independence [Accepted]

**Intuition**

After a swap of columns, two rows that were the same stay the same, and two rows that were different stay different.  Since the final state of a chessboard has only two different kinds of rows, there must have originally been only two different kinds of rows.

Furthermore, these rows must have had half zeros and half ones, (except when the length is odd, where there could be an extra zero or one), and one row must be the opposite (`0` changed to `1` and vice versa) of the other row.  This is because moves do not change these properties either.

Similarly, the above is true for columns.

Now, because a row move followed by a column move is the same as a column move followed by a row move, we can assume all the row moves happen first, then all the column moves.  (Note: it is *not* true that a row move followed by another row move is the same as those moves backwards.)

Since there are only two kinds of rows, we want the minimum number of moves to make them alternating; and similarly for columns.  This reduces to a one dimensional problem, where we have an array like `[0, 1, 1, 1, 0, 0]` and we want to know the least cost to make it `[0, 1, 0, 1, 0, 1]` or `[1, 0, 1, 0, 1, 0]`.

**Algorithm**

For each set of rows (and columns respectively), make sure there are only 2 kinds of lines in the right quantities that are opposites of each other.

Then, for each possible ideal transformation of that line, find the minimum number of swaps to convert that line to it's ideal and add it to the answer.  For example, `[0, 1, 1, 1, 0, 0]` has two ideals `[0, 1, 0, 1, 0, 1]` or `[1, 0, 1, 0, 1, 0]`; but `[0, 1, 1, 1, 0]` only has one ideal `[1, 0, 1, 0, 1]`.

In Java, we use integers to represent the rows as binary numbers.  We check the number of differences with `[1, 0, 1, 0, 1, 0, ...]` by xoring with `0b010101010101.....01 = 0x55555555`.  To make sure we don't add extra large powers of 2, we also bitwise-AND by `0b00...0011...11` where there are `N` ones in this mask.


```python
class Solution(object):
    def movesToChessboard(self, board):
        N = len(board)
        ans = 0
        # For each count of lines from {rows, columns}...
        for count in (collections.Counter(map(tuple, board)),
                      collections.Counter(zip(*board))):

            # If there are more than 2 kinds of lines,
            # or if the number of kinds is not appropriate ...
            if len(count) != 2 or sorted(count.values()) != [N/2, (N+1)/2]:
                return -1

            # If the lines are not opposite each other, impossible
            line1, line2 = count
            if not all(x ^ y for x, y in zip(line1, line2)):
                return -1

            # starts = what could be the starting value of line1
            # If N is odd, then we have to start with the more
            # frequent element
            starts = [+(line1.count(1) * 2 > N)] if N%2 else [0, 1]

            # To transform line1 into the ideal line [i%2 for i ...],
            # we take the number of differences and divide by two
            ans += min(sum((i-x) % 2 for i, x in enumerate(line1, start))
                       for start in starts) / 2

        return ans
```


**Complexity Analysis**

* Time Complexity:  $$O(N^2)$$, where $$N$$ is the number of rows (and columns) in `board`.

* Space Complexity:  $$O(N)$$, the space used by `count`.