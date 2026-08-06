## Description

A nonempty array is consecutive when every adjacent difference is `1`, or when every adjacent difference is `-1`. The direction must remain consistent throughout the array: a sequence that first rises and then falls is not consecutive. A one-element array is consecutive without needing an adjacent difference.

The value of a subarray is the sum of its elements. Consider every nonempty contiguous subarray of `nums` that satisfies the consecutive rule, add all of their values, and return the result modulo $10^9+7$.
