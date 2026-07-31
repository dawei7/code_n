## Description

A sequence is a **wiggle sequence** when the differences between adjacent values strictly alternate in sign. The first difference, when present, may be positive or negative. Any one-element sequence is a wiggle sequence, as is any two-element sequence whose values are unequal.

For example, `[1,7,4,9,2,5]` qualifies because its successive differences are `(6,-3,5,-7,3)`. By contrast, `[1,4,7,2,5]` begins with two positive differences, while `[1,7,4,5,5]` ends with a zero difference, so neither qualifies.

A subsequence keeps the original relative order while deleting any number of elements, including none. Given an integer array `nums`, return the maximum length of a wiggle subsequence obtainable from it.
