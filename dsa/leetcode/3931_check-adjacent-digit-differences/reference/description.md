## Description

The input is a string `s` made entirely of decimal digits. Regard each character as its numeric value and consider every pair formed by two consecutive positions in the string.

For each such pair, measure the absolute difference between its two digit values. The required condition holds only when every one of those differences is at most $2$; a single larger difference makes the whole string fail.

Return `true` when the condition holds for all adjacent pairs, and return `false` otherwise. For two numeric values $a$ and $b$, their absolute difference is $lvert a-b\rvert$.
