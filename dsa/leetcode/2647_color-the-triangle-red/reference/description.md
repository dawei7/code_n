## Description

An equilateral triangle of side length $n$ is divided into $n^2$ unit equilateral triangles. Its rows are 1-indexed: row $i$ contains $2i-1$ unit triangles, whose coordinates run from $(i,1)$ through $(i,2i-1)$.

Two unit triangles are neighbors exactly when they share a complete side. Initially every unit triangle is white. Choose some triangles to color red, then repeatedly color any white triangle that has at least two red neighbors. The process stops when no such white triangle remains.

Return coordinates for a smallest possible initial red set that eventually makes all $n^2$ triangles red. More than one minimum construction may exist, and any one of them is acceptable.
