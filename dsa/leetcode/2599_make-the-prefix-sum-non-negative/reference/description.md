## Description

You are given a zero-indexed integer array `nums`. In one operation, choose any element, remove it from its current position, and place it at the end of the array. You may repeat this operation as needed.

For the resulting order, the prefix sum at index `i` is the sum of all elements from index zero through `i`, inclusive. Every one of these prefix sums must be non-negative.

Return the minimum number of move-to-the-end operations required. The input is guaranteed to admit a valid ordering.
