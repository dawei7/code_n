## Note

The result must not contain consecutive horizontal segments of the same height. For example, `[..., [2,3], [4,5], [7,5], [11,5], [12,7], ...]` is invalid because the three adjacent height-`5` segments should be merged. Their compact form is `[..., [2,3], [4,5], [12,7], ...]`.
