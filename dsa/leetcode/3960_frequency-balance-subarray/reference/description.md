## Description

Given an integer array `nums`, consider each nonempty contiguous subarray and the occurrence count of every distinct value inside it.

A subarray is **frequency balanced** when it contains just one distinct value. If it contains multiple distinct values, there must instead be some positive integer $f$ for which every distinct value occurs either $f$ or $2f$ times. Both of those frequency levels must actually be represented by at least one value.

Return the length of the longest frequency balance subarray. A subarray with several distinct values all occurring equally often does not satisfy the second rule, because it has only one frequency level.
