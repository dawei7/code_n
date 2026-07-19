# Generate Random Point in a Circle

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 478 |
| Difficulty | Medium |
| Topics | Math, Geometry, Rejection Sampling, Randomized |
| Official Link | [LeetCode](https://leetcode.com/problems/generate-random-point-in-a-circle/) |

## Problem Description
### Goal
Construct a generator for a circle with the supplied positive radius and center `(x_center, y_center)`. Each `randPoint()` call must return a floating-point point lying inside or on that circle.

Points must be uniform over the circle's area, so equal-area regions have equal probability; choosing the radius uniformly would incorrectly concentrate samples near the center. Successive calls produce independent samples using the available random source. Translate generated offsets by the center and never return a point outside the boundary. The app provides deterministic random values to verify the mapping, while the native class uses the standard random source.

### Function Contract
**Inputs**

- `radius`, `x_center`, `y_center`: the circle geometry
- `random_values`: the app's deterministic cyclic stream of values in `[0, 1]`
- `draws`: the number of points to generate in the app trace

**Return value**

- The generated point list. The native artifact exposes a constructor and `randPoint()` using the standard random source.

### Examples
**Example 1**

- Input: `radius = 1, x_center = 0, y_center = 0, random_values = [0, 0], draws = 2`
- Output: `[[0, 0], [0, 0]]`

**Example 2**

- Input: `radius = 2, x_center = 1, y_center = -1, random_values = [0.25, 0], draws = 1`
- Output: `[[2, -1]]`

**Example 3**

- Input: `radius = 4, x_center = -2, y_center = 3, random_values = [0.25, 0.25], draws = 1`
- Output: `[[-2, 5]]`
