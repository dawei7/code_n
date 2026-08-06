## Description

You are given an array `intervals`, where `intervals[i] = [start_i, end_i]` and every start point is unique.

For each interval `i`, its right interval is an interval `j` whose start satisfies `start_j >= end_i`. Among all
qualifying intervals, choose the one with the smallest start. The two indices may be equal.

Return the chosen original index for every input position. Place `-1` at position `i` when interval `i` has no
right interval.
