## Description

You are given an integer `n`, representing `n` light bulbs arranged in a line and indexed from 0 to `n - 1`.

You are also given an integer `brightness` and a 2D integer array `intervals`, where `intervals[i] = [start_i, end_i]` represents an **inclusive** time interval during which the lighting requirement **must** be satisfied.

At each time unit, every bulb can independently be either on or off. A bulb that is on **illuminates** its own position and its **adjacent** positions, if they exist.

The **total illumination** at a time unit is the number of **illuminated** positions. Each position is counted **at most once**.

For every integer time unit covered by **at least** one interval in `intervals`, the **total illumination** must be **at least** `brightness`. At time units not covered by any interval, all bulbs may remain off. Each bulb that is on consumes 1 unit of energy for that time unit.

Return an integer denoting the **minimum** total energy required.
