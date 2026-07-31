## Description

You receive an integer array `nums` and a positive integer `k`. Begin with exactly `k` resource units, then process every array element from left to right. Processing `nums[i]` consumes `nums[i]` units from the currently available resource.

Whenever the available amount is smaller than the next requirement, you may perform an operation that adds another `k` resource units. The value of `k` never changes. Operations have increasing costs: the first costs `1`, the second costs `2`, and the cost continues to rise by one for each later operation.

Find the minimum total operation cost that makes it possible to process the complete array in order. Because this total can be large, return it modulo $10^9+7$.
