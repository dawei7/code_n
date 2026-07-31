## Description

Conway's Game of Life is a cellular automaton introduced by British mathematician John Horton Conway in 1970.

The board is an `m x n` grid. A live cell is represented by `1`, and a dead cell by `0`. Each cell interacts with its eight horizontal, vertical, and diagonal neighbors according to four rules:

- A live cell with fewer than two live neighbors dies from under-population.
- A live cell with two or three live neighbors remains alive in the next generation.
- A live cell with more than three live neighbors dies from over-population.
- A dead cell with exactly three live neighbors becomes alive through reproduction.

Apply these rules to every cell using the same current generation. All births and deaths occur simultaneously.

Given `board`, update it to its next state. Nothing needs to be returned.
