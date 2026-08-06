## Description

You are given an array of `intervals`, where `intervals[i] = [start_i, end_i]` and each `start_i` is **unique**.

The **right interval** for an interval `i` is an interval `j` such that `start_j >= end_i` and `start_j` is **minimized**. Note that `i` may equal `j`.

Return *an array of **right interval** indices for each interval `i`*. If no **right interval** exists for interval `i`, then put `-1` at index `i`.
