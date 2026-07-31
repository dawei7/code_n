## Description

Given strings `s1`, `s2`, and `s3`, determine whether `s3` can be formed as an interleaving of `s1` and `s2`.

An interleaving divides strings `s` and `t` into $n$ and $m$ non-empty substrings:

$$
s=s_1+s_2+\cdots+s_n, \qquad t=t_1+t_2+\cdots+t_m,
$$

where $\lvert n-m\rvert\le 1$. The pieces are then concatenated while alternating their source, beginning with either string: `s1 + t1 + s2 + t2 + ...` or `t1 + s1 + t2 + s2 + ...`.
