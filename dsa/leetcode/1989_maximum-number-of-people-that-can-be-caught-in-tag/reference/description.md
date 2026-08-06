## Description

People stand at the indexed positions of the binary array `team`. A value of
`1` marks a person who is “it,” while `0` marks someone who may be caught. A
person who is “it” at index `i` may catch one person at an index from
`i - dist` through `i + dist`, including both endpoints.

Each catcher may catch at most one other person, and each non-catcher may be
caught at most once. Choose the pairings to maximize the total number of caught
people, and return that maximum.
