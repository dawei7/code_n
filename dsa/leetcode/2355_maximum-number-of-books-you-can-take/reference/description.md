## Description

A bookshelf has $n$ shelves described by the 0-indexed array `books`, where `books[i]` is the number of books available on shelf $i$. Choose one contiguous section whose endpoints satisfy $0 \le l \le r < n$, and decide how many books to take from every shelf in that section without exceeding the corresponding available amount.

The chosen quantities must be strictly increasing from left to right: for each $i$ with $l \le i < r$, the number taken from shelf $i$ must be strictly fewer than the number taken from shelf $i+1$. Return the maximum total number of books obtainable by any valid choice of contiguous section and quantities.
