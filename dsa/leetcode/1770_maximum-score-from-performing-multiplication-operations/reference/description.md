## Description

You are given two **0-indexed** integer arrays `nums` and `multipliers`** **of size `n` and `m` respectively, where `n >= m`.

You begin with a score of `0`. You want to perform **exactly** `m` operations. On the `i^th` operation (**0-indexed**) you will:

<ul>
    <li>Choose one integer `x` from **either the start or the end **of the array `nums`.</li>
    <li>Add `multipliers[i] * x` to your score.
    <ul>
        <li>Note that `multipliers[0]` corresponds to the first operation, `multipliers[1]` to the second operation, and so on.</li>
    </ul>
    </li>
    <li>Remove `x` from `nums`.</li>
</ul>

Return *the **maximum** score after performing *`m` *operations.*
