## Description

You have $n$ sheets arranged in order and an array `limit` of length $m`. Color `i` may be applied to at most `limit[i]` sheets.

Paint every sheet subject to all of these conditions:

- Use exactly two distinct colors.
- Each chosen color covers one contiguous segment of sheets.
- The segment painted with color `i` contains no more than `limit[i]` sheets.

Return the number of valid paintings modulo $10^9+7$.
