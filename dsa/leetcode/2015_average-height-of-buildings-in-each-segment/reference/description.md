## Description

A straight street is represented by a number line. Each building
`[start, end, height]` occupies the half-closed interval `[start, end)`,
including its start but excluding its end.

Describe every covered part of the street with the minimum number of
non-overlapping segments. For each covered segment, report its left endpoint,
right endpoint, and the integer-division average of the heights of all
buildings present there. Adjacent covered regions with the same average must be
merged, even if their active building sets differ. Uncovered gaps are omitted
and prevent merging across them. The returned segments may appear in any
order.
