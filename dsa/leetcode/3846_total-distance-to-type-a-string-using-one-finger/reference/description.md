## Description

A special keyboard arranges the 26 lowercase English letters in three rows. Rows and columns use zero-based indices, and the unused positions at the ends of the last two rows contain no keys.

| Row | Column 0 | Column 1 | Column 2 | Column 3 | Column 4 | Column 5 | Column 6 | Column 7 | Column 8 | Column 9 |
|---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|:---:|
| 0 | `q` | `w` | `e` | `r` | `t` | `y` | `u` | `i` | `o` | `p` |
| 1 | `a` | `s` | `d` | `f` | `g` | `h` | `j` | `k` | `l` | — |
| 2 | `z` | `x` | `c` | `v` | `b` | `n` | `m` | — | — | — |

You must type a lowercase string `s` with one finger. Before the first character is typed, the finger rests on the `a` key at coordinate $(1,0)$. To type each character in order, move the finger from its current key to that character's key.

The distance between coordinates $(r_1,c_1)$ and $(r_2,c_2)$ is their Manhattan distance:

$$
\lvert r_1-r_2\rvert+\lvert c_1-c_2\rvert.
$$

Return the sum of the distances traveled while typing the entire string.
