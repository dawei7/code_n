## Description

A dieter records the calories consumed on each day in `calories`, where `calories[i]` is the amount for day `i`. For every possible consecutive sequence of exactly `k` days, let $T$ be the sum of the entries in that window.

The dieter loses one point when $T < \texttt{lower}$ and gains one point when $T > \texttt{upper}$. A total in the inclusive interval $[\texttt{lower}, \texttt{upper}]$ leaves the score unchanged. Starting from zero, evaluate all window starts from `0` through `calories.length - k` and return the accumulated score. Losses may outnumber gains, so the result can be negative.
