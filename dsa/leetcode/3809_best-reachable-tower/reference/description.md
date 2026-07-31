## Description

You are given a two-dimensional integer array `towers`. Each entry `towers[i] = [x_i, y_i, q_i]` describes the coordinates $(x_i,y_i)$ of the $i$th tower and its quality factor $q_i$.

Your location is supplied as `center = [cx, cy]`, together with an integer `radius`. A tower is **reachable** exactly when its Manhattan distance from `center` is at most `radius`.

Among the reachable towers:

- Select the coordinates of a tower having the maximum quality factor.
- If several reachable towers share that maximum quality, select the lexicographically smallest coordinate. Return `[-1, -1]` when no tower is reachable.

The **Manhattan distance** between cells $(x_i,y_i)$ and $(x_j,y_j)$ is

$$
\lvert x_i-x_j\rvert+\lvert y_i-y_j\rvert.
$$

A coordinate `[x_i, y_i]` is **lexicographically smaller** than `[x_j, y_j]` when $x_i<x_j$, or when $x_i=x_j$ and $y_i<y_j$.

The notation $\lvert x\rvert$ denotes the **absolute value** of $x$.
