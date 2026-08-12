# Lexicographic Permutations - Optimal Approach

## Algorithm Explanation

To find the $1,000,000^{\text{th}}$ lexicographic permutation of digits $0 \dots 9$, we use the **Factorial Number System (Factoradix)** rather than generating $1,000,000$ permutations sequentially:

1. Convert target rank to 0-indexed: $K = 999999$.
2. For position $i$ from $9$ down to $0$:
   - Calculate factorial size $F = i!$.
   - The index of the next digit is $\text{idx} = \lfloor \frac{K}{F} \rfloor$.
   - Update remaining rank $K \leftarrow K \bmod F$.
   - Select and remove `digits[idx]`.
3. Join selected digits into the resulting number string.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N^2)$ where $N = 10$ digits. Operates in $\mathcal{O}(1)$ time.
- **Space Complexity:** $\mathcal{O}(N)$ - Digits array storage.
