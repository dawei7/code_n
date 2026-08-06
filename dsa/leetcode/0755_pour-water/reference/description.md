## Description

An integer array `heights` describes an elevation map: `heights[i]` is the terrain height at index `i`, and every column has width `1`. You are also given a water volume and an index `k`; the water arrives at `k` in indivisible one-unit droplets.

Each droplet initially rests on the current terrain-plus-water level at `k`. If moving left would eventually place it at a lower level, it moves left. Otherwise, if moving right would eventually place it at a lower level, it moves right. If neither direction would make it fall, it remains at its current position and raises that column by one. Here, a column's level is its terrain height plus all water already settled there.

Treat both sides beyond the array as infinitely high terrain, so water cannot leave the represented elevation map. A unit of water cannot be divided across columns: every droplet must settle completely in exactly one column. Apply all droplets sequentially and return the final terrain-plus-water heights.
