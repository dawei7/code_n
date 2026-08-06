## Description

Design the basic behavior of an `Excel` sheet represented by an integer matrix. Its rows are numbered from `1` through `height`, its columns run from `A` through `width`, and every cell begins with value `0`. The sheet supports writing a literal value, reading the current value, and installing a sum formula.

A sum formula may name individual cells or inclusive rectangular ranges. It remains attached to its target cell until a later literal assignment or formula overwrites that cell, so changes to referenced cells must be reflected in the formula's value. When the same cell is included through repeated or overlapping references, each occurrence contributes to the sum.
