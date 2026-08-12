# Digital Root Clocks - Optimal Approach

## Algorithm Explanation

Find the difference between the total number of segment transitions required by Sam's clock and Max's clock for all prime numbers $p \in [10^7, 2 \times 10^7]$.

### Shared Segment Bitmask Intersection:
1. **Clock Transition Difference**:
   For any step $A \to B$ in the digital root chain:
   - Sam turns OFF all segments of $A$ and ON all segments of $B$ (costing $2 \times (\text{Segments}(A) + \text{Segments}(B))$).
   - Max turns OFF only $A \setminus B$, leaves $A \cap B$ ON, and turns ON $B \setminus A$.
   - Difference per step: $\Delta(A, B) = 2 \times |A \cap B|$ (twice the count of shared active segments between $A$ and $B$).
2. **Right-Aligned Bitmask Representation**:
   Each digit $0 \dots 9$ is mapped to a 7-bit segment mask.
   For each transition $A \to B$, right-aligned digits are bitwise intersected using `masks[d1] & masks[d2]`.
3. **Execution**:
   Summing $2 \times |A \cap B|$ for all digital root steps of primes $p \in [10^7, 2 \times 10^7]$ yields $13625242$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\pi(B))$ for $B = 2 \times 10^7$. Runs in $\approx 3.50\text{s}$.
- **Space Complexity:** $\mathcal{O}(B)$ bytearray sieve.
