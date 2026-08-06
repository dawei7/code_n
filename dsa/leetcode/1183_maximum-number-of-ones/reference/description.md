## Description

Consider a matrix `M` with `width` columns and `height` rows, described by the dimensions `width * height`. Every cell contains exactly one binary value, either `0` or `1`. The matrix must satisfy a local restriction: each contiguous square submatrix with dimensions `sideLength * sideLength` contains at most `maxOnes` entries equal to `1`.

The restriction applies simultaneously to every eligible square position, including square submatrices that overlap one another. Determine the greatest possible number of ones in the entire matrix while respecting that limit in every such square submatrix.
