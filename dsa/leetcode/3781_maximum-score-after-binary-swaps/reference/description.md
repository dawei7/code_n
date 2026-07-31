## Description

You are given an integer array `nums` of length `n` and a binary string `s` of the same length.

The score begins at zero. In any current arrangement of `s`, every index containing `'1'` contributes the corresponding value `nums[i]` to that score.

You may perform zero or more operations. An operation chooses an index `i` with `0 <= i < n - 1` whose adjacent characters are `s[i] = '0'` and `s[i + 1] = '1'`, then swaps those two characters. Thus, an operation moves that `'1'` one position to the left.

Return the greatest score attainable after any legal sequence of such swaps.
