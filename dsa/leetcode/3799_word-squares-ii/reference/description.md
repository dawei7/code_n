## Description

You are given an array `words` of distinct four-letter strings. Every character is a lowercase English letter.

A word square is an ordered choice of four distinct words, written as `(top, left, right, bottom)`. The four words occupy the corresponding sides of a square: `top` and `bottom` are read from left to right, while `left` and `right` are read from top to bottom.

The letters must agree at all four corners:

- `top[0] == left[0]`
- `top[3] == right[0]`
- `bottom[0] == left[3]`
- `bottom[3] == right[3]`

Return every valid word square that can be formed from `words`. Sort the result in ascending lexicographic order by the tuple `(top, left, right, bottom)`.
