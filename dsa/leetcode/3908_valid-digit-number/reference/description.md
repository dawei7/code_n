## Description

You receive a nonnegative integer `n` and one decimal digit `x`. Treat the usual decimal representation of `n` as its ordered digit sequence. The number satisfies the first part of the validity rule only when that sequence contains at least one occurrence of `x`.

The leading digit is subject to a separate restriction: `n` must not start with `x`. Return `true` exactly when both requirements hold at the same time—`x` occurs somewhere in `n`, but the most significant digit is different from `x`. Otherwise, return `false`.
