## General
Given There is a special kind of apple tree that grows apples every day for `n` days. On the $$i^{\text{th}}$$ day, the tree grows $\text{apples}[i]$ apples that will rot after $\text{days}[i]$ days, that is on day $i + \te..., the algorithm solves **Maximum Number of Eaten Apples** directly. It utilizes a priority queue (`heapq`) to maintain dynamic minimum/maximum element ordering.

## Complexity detail
- **Time Complexity**: $O((n + E) \log n)$ — Operation count bound.
- **Space Complexity**: $O(n)$ — Auxiliary memory allocation bound.
