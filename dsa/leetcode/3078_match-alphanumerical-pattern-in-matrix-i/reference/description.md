## Description

You are given a rectangular integer matrix `board`, whose cells are digits from $0$ through $9$, and a rectangular string matrix `pattern`. Every character in `pattern` is either a decimal digit or a lowercase English letter.

A submatrix of `board` matches `pattern` when both have the same dimensions and every pattern cell can be interpreted consistently. A digit character is a fixed literal, so it must equal the corresponding board digit. Every occurrence of the same letter must correspond to the same digit, while two distinct letters must correspond to different digits. Letter assignments are compared with other letter assignments; a letter may use a digit that also appears as a fixed literal elsewhere in the pattern.

Find a matching submatrix and return the row and column of its upper-left cell. If several matches exist, choose the one with the smallest row; within that row, choose the smallest column. If no match exists, return `[-1, -1]`.
