## Function Contract

**Inputs**

- `s`: A nonempty string containing only lowercase English letters, to be typed from left to right.

Let $P(x)=(r_x,c_x)$ be the coordinate of letter $x$ in the keyboard table. For $N=\lvert\texttt{s}\rvert$, define $p_0=P(\texttt{a})$ and $p_i=P(\texttt{s[i - 1]})$ for $1\le i\le N$. The distance paid for character $i$ is

$$
d_i=\lvert p_i.r-p_{i-1}.r\rvert+\lvert p_i.c-p_{i-1}.c\rvert.
$$

After a character is typed, the finger remains on that character's key and becomes the starting position for the next move.

**Return value**

Return the integer total

$$
\sum_{i=1}^{N}d_i.
$$

Typing a character already under the finger contributes zero distance.
