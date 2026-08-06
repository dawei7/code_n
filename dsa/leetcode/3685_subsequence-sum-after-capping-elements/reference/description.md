## Description

<p data-end="320" data-start="259">You are given an integer array `nums` of size `n` and a positive integer `k`.

<p data-end="294" data-start="163">An array **capped** by value `x` is obtained by replacing every element `nums[i]` with `min(nums[i], x)`.

<p data-end="511" data-start="296">For each integer <code data-end="316" data-start="313">x</code> from 1 to <code data-end="332" data-start="329">n</code>, determine whether it is possible to choose a **<span data-keyword="subsequence-array-nonempty">subsequence</span>** from the array capped by `x` such that the sum of the chosen elements is **exactly** <code data-end="510" data-start="507">k</code>.

<p data-end="788" data-start="649">Return a **0-indexed** boolean array <code data-end="680" data-start="672">answer</code> of size <code data-end="694" data-start="691">n</code>, where <code data-end="713" data-start="702">answer[i]</code> is <code data-end="723" data-start="717">true</code> if it is possible when using <code data-end="764" data-start="753">x = i + 1</code>, and <code data-end="777" data-start="770">false</code> otherwise.
