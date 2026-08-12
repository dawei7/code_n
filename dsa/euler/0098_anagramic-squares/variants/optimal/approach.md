# Anagramic Squares - Optimal Approach

## Algorithm Explanation

Find the largest square number formed by substituting unique digits for letters in a pair of anagram words from `words.txt`.

### Constraint Mapping Strategy:
1. Parse $2000$ words from `words.txt` and group them by canonical sorted letter key `"".join(sorted(word))`.
2. Extract all valid word anagram pairs $(w_1, w_2)$ of size $\ge 2$.
3. Precompute square numbers $S = n^2$ indexed by word length $L$.
4. For each anagram word pair $(w_1, w_2)$ and candidate square $s_1$:
   - Construct character $\leftrightarrow$ digit bijection. Reject if non-injective (multiple letters mapping to the same digit or vice versa).
   - Substitute character mapping into $w_2$ to generate string $s_2$.
   - Reject if $s_2$ contains a leading zero.
   - Verify if $s_2$ is a perfect square.
   - Track and return maximum $\max(\text{int}(s_1), \text{int}(s_2))$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(P \cdot S_L)$ where $P$ is pair count and $S_L$ is candidate squares of length $L$. Runs in $< 0.15\text{s}$.
- **Space Complexity:** $\mathcal{O}(W + S)$ - Hash map word and square structures.
