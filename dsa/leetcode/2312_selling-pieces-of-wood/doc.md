# Selling Pieces of Wood

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2312 |
| Difficulty | Hard |
| Topics | Array, Dynamic Programming, Memoization |
| Official Link | [LeetCode](https://leetcode.com/problems/selling-pieces-of-wood/) |

## Problem Description
### Goal
An $m\times n$ rectangular board may be sold whole when its ordered
`[height, width]` shape appears in `prices`. It may instead be cut horizontally
or vertically, but each cut must cross the entire current piece and divide it
into exactly two smaller rectangles. The resulting pieces may be cut again any
number of times.

Any listed shape may be sold repeatedly, and pieces without a useful listed
shape may be left unsold. Height and width are not interchangeable: the wood's
grain prevents rotating a piece, so a price for `[h, w]` says nothing about
`[w, h]`. Determine the greatest total revenue obtainable from the original
board.

### Function Contract
**Inputs**

- `m`: The original board's height.
- `n`: The original board's width.
- `prices`: Distinct triples `[height, width, price]`, each giving the sale
  value of one ordered piece shape.

The dimensions satisfy $1\le m,n\le200$. There are from 1 through $2\cdot10^4$
price entries, each listed dimension fits within the original board, and every
listed price is from 1 through $10^6$.

**Return value**

The maximum revenue obtainable through any sequence of full horizontal and
vertical cuts followed by sales of any chosen pieces.

### Examples
**Example 1**

- Input: `m = 3`, `n = 5`, `prices = [[1,4,2],[2,2,7],[2,1,3]]`
- Output: `19`
- Explanation: Two `2 x 2` pieces, one `2 x 1` piece, and one `1 x 4` piece
  sell for $14+3+2=19$.

**Example 2**

- Input: `m = 4`, `n = 6`, `prices = [[3,2,10],[1,4,2],[4,1,3]]`
- Output: `32`
- Explanation: Three `3 x 2` pieces and one `1 x 4` piece sell for $30+2$.
  The `1 x 4` listing cannot be rotated into a `4 x 1` listing.
