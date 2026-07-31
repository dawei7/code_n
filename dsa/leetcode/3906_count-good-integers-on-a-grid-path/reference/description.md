## Description

You are given an inclusive integer interval `[l, r]` and a six-character string `directions` containing exactly three `D` moves and three `R` moves. Every integer $x$ in the interval is interpreted as exactly 16 decimal digits by adding leading zeros when necessary.

Write those digits into a $4\times4$ grid in row-major order. Starting at cell `(0, 0)`, follow `directions` in order: `D` moves down one row, and `R` moves right one column. Include the starting digit and the digit after every move, so the path records seven digits and finishes at `(3, 3)`.

The integer is good precisely when those seven visited digits are non-decreasing. Return how many integers in `[l, r]` are good.
