## Description

An $m \times n$ picture contains black pixels represented by `"B"` and white pixels represented by `"W"`. Given a
positive integer `target`, count the black pixels at coordinates `(r, c)` that satisfy both rules below:

1. Row `r` and column `c` each contain exactly `target` black pixels.
2. Every row containing a black pixel in column `c` is identical, across all columns, to row `r`.

Return the total number of black coordinates satisfying both rules.
