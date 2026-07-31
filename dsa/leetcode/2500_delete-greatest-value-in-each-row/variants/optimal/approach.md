## General

**Turn deletion rounds into aligned columns**

Each row always loses its current greatest value. Sort every row in non-decreasing order. Its deletion order is then the row read from right to left. Because all rows have the same length, values with the same sorted column index are removed during the same operation, although processing those aligned columns from left to right reverses the operation order. Reversing the order does not change their sum.

For a fixed sorted column, take the maximum entry among all rows and add it to the answer. This is exactly the value contributed by the corresponding deletion operation: every row supplies its greatest remaining value for that round, and the operation adds the greatest of those supplied values. Visiting every column accounts for all $n$ operations once.

## Complexity detail

Let $m$ be the number of rows and $n$ the number of columns. Sorting each row costs $O(n \log n)$, for $O(m n \log n)$ total time. Scanning the aligned columns costs another $O(mn)$ and is dominated by sorting.

The rows are sorted in place. Python's comparison sort uses $O(\log n)$ auxiliary stack space in the usual case; the column scan uses only scalar state and a generator. This excludes the input matrix itself.

## Alternatives and edge cases

- **Direct simulation:** Repeatedly finding and removing the maximum from every row follows the statement literally, but list searches and deletions can require $O(mn^2)$ time.
- **Max-heaps:** A heap for each row supports each deletion in $O(\log n)$ time and reaches the same asymptotic time bound, but needs $O(mn)$ additional storage and more machinery.
- **Duplicate greatest values:** Removing any occurrence of a tied maximum is equivalent because the occurrences have the same value; sorting preserves the correct multiset of later contributions.
- **One row:** Every element is eventually the only removed candidate for its round, so the answer is the sum of that row.
- **One column:** There is one operation, and its contribution is the maximum value in the column.
