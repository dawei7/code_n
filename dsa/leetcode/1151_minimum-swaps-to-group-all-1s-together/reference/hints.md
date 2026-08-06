## Hints

1. First determine how many ones the final contiguous group must contain; that group size is fixed.
2. The required size is the total number of `1` values in the entire array. Call this number $k$.
3. Consider each subarray of length $k$ as a possible final block and ask how many swaps it needs.
4. That number of swaps equals the number of zeros inside the chosen subarray.
5. Avoid recounting all of those zeros from scratch after shifting the subarray by one position.
6. Use a fixed-size sliding window.
