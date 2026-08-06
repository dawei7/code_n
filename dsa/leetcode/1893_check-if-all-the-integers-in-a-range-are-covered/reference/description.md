## Description

You are given a 2D integer array `ranges` and two integers `left` and `right`. Each `ranges[i] = [start_i, end_i]` represents an **inclusive** interval between `start_i` and `end_i`.

Return `true` *if each integer in the inclusive range* `[left, right]` *is covered by **at least one** interval in* `ranges`. Return `false` *otherwise*.

An integer `x` is covered by an interval `ranges[i] = [start_i, end_i]` if `start_i <= x <= end_i`.
