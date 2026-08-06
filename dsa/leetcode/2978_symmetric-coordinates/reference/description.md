## Description

The `Coordinates` table stores integer ordered pairs `(X, Y)` and may contain
duplicate rows. Two physical rows form a symmetric pair when one stores
`(X1, Y1)` and the other stores `(Y1, X1)`.

Return each unique symmetric coordinate once, using only the orientation that
satisfies `X <= Y`. A diagonal coordinate `(X, X)` is symmetric only when that
row occurs at least twice, because the pair must use two rows.

Order the result first by `X` and then by `Y`, both ascending.
