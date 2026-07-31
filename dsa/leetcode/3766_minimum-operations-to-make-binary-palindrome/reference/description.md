## Description

You are given an integer array `nums`. Treat every element independently.

For any `nums[i]`, one operation either increases its value by 1 or decreases its value by 1. You may apply either operation any number of times, including no operations at all.

A value is a **binary palindrome** when its binary representation, written without leading zeros, reads identically from left to right and from right to left.

Return an integer array `ans` of the same length. For every index `i`, `ans[i]` must be the minimum number of unit operations needed to turn `nums[i]` into a binary palindrome.
