## Hint

**Hint 1:** Order every worker-bike pair first by distance, then by worker index, and finally by bike index. If $P=WB$ is the total number of pairs, consider whether the same ordering can be obtained in less than $O(P\log P)$ time.

**Hint 2:** Traverse the ordered pairs and accept a pair only when neither its worker nor its bike has already been used.
