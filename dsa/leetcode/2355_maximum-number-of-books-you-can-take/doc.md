# Maximum Number of Books You Can Take

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2355 |
| Difficulty | Hard |
| Category | Algorithms |
| Topics | Array, Dynamic Programming, Stack, Monotonic Stack |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/maximum-number-of-books-you-can-take/) |

## Problem Description

### Goal

A bookshelf has $n$ shelves described by the 0-indexed array `books`, where
`books[i]` is the number of books available on shelf $i$. Choose one contiguous
section whose endpoints satisfy $0 \le l \le r < n$, and decide how many books
to take from every shelf in that section without exceeding the corresponding
available amount.

The chosen quantities must be strictly increasing from left to right: for each
$i$ with $l \le i < r$, the number taken from shelf $i$ must be strictly fewer
than the number taken from shelf $i+1$. Return the maximum total number of
books obtainable by any valid choice of contiguous section and quantities.

### Function Contract

**Inputs**

- `books`: A list of $n$ non-negative integers giving the available books on
  each shelf.

The constraints are $1 \le n \le 10^5$ and
$0 \le \texttt{books[i]} \le 10^5$.

**Return value**

Return the greatest possible sum of the strictly increasing quantities taken
from a contiguous section. The result may exceed the range of a 32-bit signed
integer.

### Examples

#### Example 1

- **Input:** `books = [8,5,2,7,9]`
- **Output:** `19`

Taking `1, 2, 7, 9` books from shelves 1 through 4 is valid and totals 19.

#### Example 2

- **Input:** `books = [7,0,3,4,5]`
- **Output:** `12`

Shelves 2 through 4 can contribute `3, 4, 5`, for a total of 12.

#### Example 3

- **Input:** `books = [8,2,3,7,3,4,0,1,4,3]`
- **Output:** `13`

One optimal section is shelves 0 through 3, taking `1, 2, 3, 7`.
