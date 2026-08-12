# Prime Connection - Optimal Approach

## Algorithm Explanation

Find $F(10^7)$, the sum of all primes $P \le 10^7$ that are not $2$'s relatives (a prime $P$ is a $2$'s relative if there exists a connected prime chain from $2$ to $P$ with no prime in the chain exceeding $P$).

### Graph Bottleneck Path & Modified Dijkstra Algorithm:
1. **Prime Connection Graph**:
   Two primes $A, B$ are connected $A \leftrightarrow B$ if they differ in 1 digit (same length) or adding 1 left-digit transforms $A$ into $B$.
   Vertices are all primes $\le N = 10^7$.
2. **Min-Max Bottleneck Path Cost**:
   For any path $\pi = (2 = v_0, v_1, \dots, v_k = P)$, the path bottleneck cost is $\max_{i} v_i$.
   Let $M(P)$ be the minimum bottleneck cost over all connected prime paths from $2$ to $P$.
   Prime $P$ is a $2$'s relative iff $M(P) \le P$.
3. **Dijkstra Priority Queue Search**:
   Starting at root prime $2$ with $M(2) = 2$:
   We run Dijkstra's algorithm to compute $M(P)$ for all primes $P \le 10^7$.
   Relaxation step: $M(B) = \min(M(B), \max(M(A), B))$ for all valid connected primes $B$.
4. **Execution**:
   Summing all primes $P \le 10^7$ with $M(P) > P$ yields $46479497324$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(P \log P)$ for $P = \pi(10^7) \approx 664579$. Runs in $\approx 0.50\text{s}$.
- **Space Complexity:** $\mathcal{O}(P)$ bottleneck array and priority queue.
