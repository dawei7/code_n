## Description

Spherical balloons are attached to a flat wall representing the $xy$-plane. Each balloon is described only by its horizontal diameter: `points[i] = [x_start, x_end]`. Its exact vertical position is unknown.

An arrow may be fired vertically upward from any coordinate $x$ on the $x$-axis. It continues upward without limit and bursts every balloon whose closed horizontal span contains that coordinate, so a balloon is hit when $x_{start} \le x \le x_{end}$. There is no limit on how many arrows may be fired.

Given all balloon intervals, return the minimum number of arrows needed to burst every balloon.
