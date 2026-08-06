## Description

A straight street is modeled as a number line containing several lamps. Each
entry `lights[i] = [position_i, range_i]` describes a lamp centered at
`position_i`. Its light covers every position in the inclusive interval from
`position_i - range_i` through `position_i + range_i`.

The brightness at a position is the number of lamp intervals containing that
position. Return a position with maximum brightness. If the maximum occurs at
several positions, return the smallest such position.
