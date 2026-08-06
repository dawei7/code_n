## Description

Given an array of unique strings `words`, construct every **word square** available from those strings. A word from
the input may be used more than once within a square, and the completed squares may be returned in any order.

A sequence is a valid word square when its $k$th row and $k$th column read as the same string for every

$$
0 \le k < \max(\text{number of rows}, \text{number of columns}).
$$

For example, `["ball", "area", "lead", "lady"]` is a word square: reading at each position horizontally produces
the same word as reading vertically.
