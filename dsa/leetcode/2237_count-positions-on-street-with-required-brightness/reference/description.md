## Description

A straight street contains the integer positions from $0$ through $n-1$. Each
street lamp is described by `lights[i] = [position_i, range_i]`. That lamp
illuminates every position in the inclusive interval from
`max(0, position_i - range_i)` through
`min(n - 1, position_i + range_i)`; clipping keeps its coverage within the
street.

The brightness of a position is the number of lamps whose illuminated
intervals contain it. A 0-indexed array `requirement` gives the minimum
brightness required at every street position. Return the number of positions
whose actual brightness is at least their corresponding requirement.
