## Description

You are given a string `s` whose characters are decimal digits. Positions in the string use zero-based indexing.

An index `i` is **good** when some contiguous substring ending exactly at `i` has the same character sequence as the ordinary decimal representation of `i`. The substring may begin anywhere at or before `i`, but its final character must be `s[i]`.

Return every good index, arranged in increasing order.
