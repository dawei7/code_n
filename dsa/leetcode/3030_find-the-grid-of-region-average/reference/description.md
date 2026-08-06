## Description

You are given `m x n` grid `image` which represents a grayscale image, where `image[i][j]` represents a pixel with intensity in the range `[0..255]`. You are also given a **non-negative** integer `threshold`.

Two pixels are **adjacent** if they share an edge.

A **region** is a `3 x 3` subgrid where the **absolute difference** in intensity between any two **adjacent** pixels is **less than or equal to** `threshold`.

All pixels in a region belong to that region, note that a pixel can belong to **multiple** regions.

You need to calculate a `m x n` grid `result`, where `result[i][j]` is the **average** intensity of the regions to which `image[i][j]` belongs, **rounded down** to the nearest integer. If `image[i][j]` belongs to multiple regions, `result[i][j]` is the **average **of the** rounded-down average **intensities of these regions, **rounded down** to the nearest integer. If `image[i][j]` does** not** belong to any region, `result[i][j]` is **equal to** `image[i][j]`.

Return the grid `result`.
