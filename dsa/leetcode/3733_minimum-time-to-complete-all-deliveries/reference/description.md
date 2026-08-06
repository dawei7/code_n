## Description

You are given two integer arrays of size 2: `d = [d_1, d_2]` and `r = [r_1, r_2]`.

Two delivery drones are tasked with completing a specific number of deliveries. Drone `i` must complete `d_i` deliveries.

Each delivery takes **exactly** one hour and **only one** drone can make a delivery at any given hour.

Additionally, both drones require recharging at specific intervals during which they cannot make deliveries. Drone `i` must recharge every `r_i` hours (i.e. at hours that are multiples of `r_i`).

Return an integer denoting the **minimum** total time (in hours) required to complete all deliveries.
