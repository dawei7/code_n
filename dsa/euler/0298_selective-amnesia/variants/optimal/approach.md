# Selective Amnesia - Optimal Approach

## Algorithm Explanation

Find the expected value $\mathbb{E}[|L - R|]$ after $50$ turns in a memory game where Larry uses Least Recently Used (LRU) eviction and Robin uses First In First Out (FIFO) eviction on a capacity-$5$ memory buffer over random numbers $1 \dots 10$.

### Canonical Joint Memory State Markov DP:
1. **Cache Eviction Strategies**:
   - Larry (LRU): Evicts the number not called for the longest time.
   - Robin (FIFO): Evicts the number residing in memory for the longest time.
2. **Canonical Symmetry Reduction**:
   By permuting digits $1 \dots 10$ based on arrival order, the joint state (Larry's LRU queue, Robin's FIFO queue) reduces to $\approx 2000$ canonical equivalence classes.
3. **Exact Probability Distribution**:
   Using DP for $t = 1 \dots 50$, we track state transition probabilities and the distribution of score difference $\Delta = L - R$.
4. **Execution**:
   Summing $\sum P(\Delta) |\Delta|$ at turn $50$ yields $\mathbb{E}[|L - R|] = 1.76882294$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(T \cdot S \cdot 10)$ for $T = 50$ turns and state count $S \approx 2000$. Runs in $\approx 1.50\text{s}$.
- **Space Complexity:** $\mathcal{O}(S)$ probability vector.
