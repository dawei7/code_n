## Description

Given an integer array `nums`, call a non-empty **subarray** valid when its leftmost element is not larger than any other element inside that subarray. A subarray is contiguous. Equality is allowed, and two equal value sequences at different index boundaries are separate subarrays for counting purposes.

Return the total number of valid subarrays. Every single-element subarray is valid because it contains no later element smaller than its first value. For a fixed starting position, extending the right boundary remains valid until the first strictly smaller value is included; every extension reaching that value or passing it is invalid.
