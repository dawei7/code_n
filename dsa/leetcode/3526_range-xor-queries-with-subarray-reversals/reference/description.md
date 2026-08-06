## Description

You are given an integer array `nums` and a sequence of three-field queries. Process the queries in order while treating `nums` as one mutable sequence. An update query `[1, index, value]` assigns `value` at `index`. A range query `[2, left, right]` computes the bitwise XOR of every element in the inclusive subarray from `left` through `right`. A reversal query `[3, left, right]` reverses that inclusive subarray in place.

Only type-2 queries produce output. Return their XOR results in the same order in which those queries occur. Both point updates and reversals persist, so every later query observes the sequence produced by all earlier operations.
