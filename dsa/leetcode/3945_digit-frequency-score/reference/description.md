## Description

Given a positive integer `n`, consider each distinct decimal digit `d` that occurs in its representation. Let `freq(d)` be the number of occurrences of that digit. The contribution of `d` is its value multiplied by that frequency, or `d * freq(d)`.

The score of `n` is the sum of those contributions over all distinct digits. Return that integer score. A zero digit may occur in `n`, but its contribution is zero regardless of how often it appears.
