## Description

You are given variable pairs `equations` and real numbers `values`. For each index `i`, `equations[i] = [A_i,B_i]` together with `values[i]` represents

$$
\frac{A_i}{B_i}=\texttt{values[i]}.
$$

Each variable name is a string. A query `queries[j] = [C_j,D_j]` asks for the value of $C_j/D_j$.

Return one answer per query. If the requested value cannot be determined, return `-1.0` for that query.
