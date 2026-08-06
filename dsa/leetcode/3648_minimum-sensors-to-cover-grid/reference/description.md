## Description

You are given `n × m` grid and an integer `k`.

A sensor placed on cell `(r, c)` covers all cells whose **Chebyshev distance** from `(r, c)` is **at most** `k`.

The **Chebyshev distance** between two cells `(r_1, c_1)` and `(r_2, c_2)` is `max(|r_1 − r_2|,|c_1 − c_2|)`.

Your task is to return the **minimum** number of sensors required to cover every cell of the grid.
