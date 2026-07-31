## Description

An $n$-by-$m$ grid begins with one or more colored source cells. Each row of `sources` has the form `[row, column, color]`; those distinct coordinates start with the specified positive colors, while every other cell starts uncolored with value `0`.

Time advances in simultaneous steps. During one step, every colored cell offers its color to each uncolored cell directly above, below, left, or right of it. A cell reached by several colors during the same step takes the largest offered color. Only uncolored cells can change, so an initially colored cell or a cell filled during an earlier step is never recolored.

Continue until no uncolored cell can be reached, then return the complete grid of final colors.
