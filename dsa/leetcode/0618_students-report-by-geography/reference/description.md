## Description

A school has students from `Asia`, `Europe`, and `America`. Pivot the `continent` values in `Student` into three output columns so that every student name appears beneath the corresponding continent.

Within each continent column, list names in ascending alphabetical order. The output headers must be `America`, `Asia`, and `Europe`, in that order. Names with the same alphabetic rank across the three continent-specific lists share an output row; when a shorter list has no name at a rank that still exists for America, that cell is `NULL`.

The generated test data guarantees that America has at least as many students as Asia and at least as many as Europe.
