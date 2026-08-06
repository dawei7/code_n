## Description

An $m \times n$ grid contains one person in each cell, and
`heights[i][j]` gives that person's positive height. A person may look only
to the right within the same row or downward within the same column.

The person in one cell can see a later person in one of those directions
exactly when every person strictly between them is shorter than both endpoint
people. Return an $m \times n$ matrix whose entry at `(i, j)` counts everyone
visible to the right or below the person in that cell.
