## Description

You are given an integer array `nums`. Begin at index `0` and make one or more forward hops until reaching the last index. A hop from index $i$ to a strictly later index $j$ contributes $(j-i)\cdot\texttt{nums[j]}$ to the score.

You may choose any increasing sequence of visited indices as long as it starts at `0` and ends at the final element. Return the maximum total score achievable across all such hopping paths. The value at the departure index does not affect a hop; only its distance and the destination value do.
