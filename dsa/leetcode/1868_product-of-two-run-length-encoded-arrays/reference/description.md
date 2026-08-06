## Description

A run-length encoding represents an integer array as pairs `[value, frequency]`. Each pair expands to `frequency` consecutive copies of `value`, and adjacent pairs never store the same value. Two such encodings, `encoded1` and `encoded2`, represent arrays of equal decoded length.

Multiply the two decoded arrays element by element, then return the run-length encoding of that product array. The returned encoding must also be compressed: if consecutive product positions have the same value, they belong to one pair whose frequency covers the whole run. Process the encodings directly rather than materializing the potentially much longer decoded arrays.
