## Description

You are given a string `s` containing only lowercase English letters. In one
operation, choose a contiguous substring that is not the entire string, then
sort the chosen characters into non-descending alphabetical order. Characters
outside that substring stay in their current positions.

The objective is to make the complete string non-descending using as few such
operations as possible. The chosen substring may occupy a prefix or suffix as
long as at least one character of the full string is excluded.

Return the minimum operation count. If the restriction against sorting the
entire string makes the target ordering unreachable, return `-1`.
