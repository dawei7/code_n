## Description

A traveler begins at the origin $(0,0)$ and follows the characters of `moves` on a two-dimensional plane. The fixed commands move one unit in their named directions: `U` goes up, `D` goes down, `L` goes left, and `R` goes right. An underscore is not a fifth movement; it is a wildcard that must be replaced independently by one of those four unit moves.

Choose every underscore's replacement to make the final position as far from the origin as possible. After the entire string has been performed, return that maximum Manhattan distance, namely $\lvert x\rvert+\lvert y\rvert$ for final coordinates $(x,y)$. Only the endpoint matters; the distance reached at an earlier prefix does not determine the answer.
