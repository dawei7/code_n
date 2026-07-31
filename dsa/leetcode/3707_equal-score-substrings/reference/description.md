## Description

You are given a string `s` containing lowercase English letters.

Define a string's **score** as the sum of its letters' alphabet positions: `a` contributes `1`, `b` contributes `2`, and so on through `z`, which contributes `26`.

Determine whether some index `i` splits `s` into the two non-empty substrings `s[0..i]` and `s[(i + 1)..(n - 1)]` with equal scores.

Return `true` when at least one such split exists; otherwise, return `false`.
