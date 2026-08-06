## Description

Consider an $m\times n$ grid in which exactly $k$ cells contain the distinct checkpoint values from $1$ through $k$. Every other cell contains zero. A path may begin at any cell and may move one step at a time up, down, left, or right.

Construct a path that visits every grid cell exactly once. When the path reaches numbered cells, their values must appear in the order $1,2,\ldots,k$; zero-valued cells may occur anywhere between those checkpoints.

Return the coordinates in visit order. Any valid path is acceptable. Return an empty array when no path can satisfy both the full-cover and checkpoint-order requirements.
