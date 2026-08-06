## Description

Given an array of strings `words`, determine whether its rows form a valid **word square**.

For every $k$ satisfying

$$
0 \le k < \max(\text{number of rows}, \text{number of columns}),
$$

the $k$th row and the $k$th column must read as the same string. Rows may have different lengths, so equality also
requires the two directions to end at the same place; a character with no reflected counterpart makes the square
invalid.
