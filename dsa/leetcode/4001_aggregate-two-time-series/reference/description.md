## Description

You are given two two-dimensional integer arrays, `series1` and `series2`. Every entry is `[timestamp, value]`, and each array's timestamps are strictly increasing.

When a timestamp is absent from one series, that series contributes the value at its next available timestamp, if such an entry exists; it contributes zero when there is no later entry. Form the union of the timestamps explicitly present in either input and, at each one, add the two series' applicable values.

Return the aggregated `[timestamp, summedValue]` pairs in strictly increasing timestamp order. Do not introduce timestamps that are absent from both inputs.
