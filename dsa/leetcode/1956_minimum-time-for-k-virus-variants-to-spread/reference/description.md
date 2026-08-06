## Description

There are $N$ distinct virus variants on an infinite integer grid. Variant
$i$ begins at `points[i]` on day zero; multiple distinct variants may share
the same starting coordinate.

On each following day, every infected grid cell spreads each variant it
contains to its four cardinally adjacent cells. Variants spread independently,
even when several occupy the same cell. Given `k`, return the earliest integer
day on which some grid point contains at least `k` distinct variants.
