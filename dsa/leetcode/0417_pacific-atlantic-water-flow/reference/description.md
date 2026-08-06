## Description

A rectangular $m \times n$ island borders two oceans. The Pacific Ocean touches its top and left edges, while the
Atlantic Ocean touches its bottom and right edges. The island is divided into square cells, and `heights[r][c]`
gives the height above sea level at coordinate `(r, c)`.

Rain water may move directly north, south, east, or west into a neighboring cell whose height is less than or equal
to the current height. Water in a boundary cell adjacent to an ocean may flow directly into that ocean.

Return every coordinate `[r, c]` from which rain water can reach both the Pacific and Atlantic oceans.
