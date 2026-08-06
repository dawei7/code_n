## Description

Consider a search process on a sequence. While elements remain, it chooses any
current element as a pivot. If the pivot equals the target, the search
succeeds. If it is smaller than the target, the pivot and everything to its
left are removed; if it is larger, the pivot and everything to its right are
removed. The process fails when the sequence becomes empty.

Given an array `nums` of unique integers, count the values guaranteed to be
found for every possible sequence of pivot choices. The input need not be
sorted.
