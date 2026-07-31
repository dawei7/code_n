## Description

You receive an integer array `nums` and a positive integer `k`. Select exactly one nonempty contiguous subarray of `nums`, then apply exactly one operation to every value in that selected range: either multiply every selected value by `k`, or divide every selected value by `k`.

Division rounds toward zero. Equivalently, use the floor of the quotient for a positive value and the ceiling for a negative value. The same operation must be used throughout the chosen range.

After changing the array, select a nonempty contiguous subarray and consider its sum. This second subarray does not have to equal the range modified by the operation; the two ranges may overlap only partly or may be different. Return the largest subarray sum obtainable over every legal operation range, operation choice, and final sum range.
