## Description

You are given a 0-indexed integer array `nums` and a positive integer `k`.

An index `i` is `k`-big when both sides of it contain enough smaller values. Specifically, at least `k` different indices before `i` must hold values strictly smaller than `nums[i]`, and at least `k` different indices after `i` must also hold values strictly smaller than `nums[i]`.

Return the number of indices that satisfy both conditions. Equal values do not count as smaller.
