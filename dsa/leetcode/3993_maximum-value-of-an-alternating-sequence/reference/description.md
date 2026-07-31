## Description

You are given three positive integers `n`, `s`, and `m`. Consider integer sequences `seq` of length `n` whose first element is fixed as `seq[0] = s`.

The sequence must alternate strictly in one of the two possible directions:

$$
\texttt{seq[0]} > \texttt{seq[1]} < \texttt{seq[2]} > \texttt{seq[3]} < \cdots
$$

or

$$
\texttt{seq[0]} < \texttt{seq[1]} > \texttt{seq[2]} < \texttt{seq[3]} > \cdots.
$$

In addition, the absolute difference between every pair of adjacent elements must be at most `m`. A sequence containing only one element is considered alternating.

Among every valid sequence satisfying these rules, return the largest value that any element can attain.
