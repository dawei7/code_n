## Description

An integer array `nums` contains $n$ values. For each index $i$, consider only indices that occur strictly to its right. A right-hand index $j$ contributes to the score of $i$ when its value is strictly smaller than `nums[i]` and the two values have different parity: one is even and the other is odd.

Return an integer array `answer` of the same length. Its entry `answer[i]` must equal the number of right-hand indices satisfying all three conditions $i < j < n$, $\texttt{nums[j]} < \texttt{nums[i]}$, and opposite parity.
