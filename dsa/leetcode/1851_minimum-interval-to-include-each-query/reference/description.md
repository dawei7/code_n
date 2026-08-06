## Description

You are given a 2D integer array `intervals`, where `intervals[i] = [left_i, right_i]` describes the `i^th` interval starting at `left_i` and ending at `right_i` **(inclusive)**. The **size** of an interval is defined as the number of integers it contains, or more formally `right_i - left_i + 1`.

You are also given an integer array `queries`. The answer to the `j^th` query is the **size of the smallest interval** `i` such that `left_i <= queries[j] <= right_i`. If no such interval exists, the answer is `-1`.

Return *an array containing the answers to the queries*.
