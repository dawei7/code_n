## Description

You are given an integer array `heights` of length `n`, where `heights[i]` is the height of the $i$th block in an exercise routine.

You begin on the ground at height `0`. Choose any order in which to visit the blocks, but jump onto every block exactly once.

- A jump from a block of height `a` to a block of height `b` burns $(a-b)^2$ calories.
- If `heights[i]` is visited first, the initial jump from the ground burns $(0-\texttt{heights}[i])^2$ calories.

Return the maximum total calories that can be burned by choosing the jumping sequence optimally.
