## Description

You are given two 0-indexed strings `firstString` and `secondString`, both containing only lowercase English letters. Consider every index quadruple $(i,j,a,b)$ satisfying

$$
0 \le i \le j < \lvert\texttt{firstString}\rvert
\quad\text{and}\quad
0 \le a \le b < \lvert\texttt{secondString}\rvert.
$$

The quadruple is eligible when the inclusive substring `firstString[i:j + 1]` equals `secondString[a:b + 1]`. Among all eligible quadruples, find the minimum possible value of $j-a$.

Return how many eligible quadruples attain that global minimum. If the two strings have no equal nonempty substrings, return zero.
