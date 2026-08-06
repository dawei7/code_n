## Hint

For each pair of positions `i` and `j` containing `1` in a newly processed row, that pair can serve as one side of a rectangle. The number of new rectangles contributed by the pair equals the number of earlier rows in which both `row[i]` and `row[j]` were also `1`.
