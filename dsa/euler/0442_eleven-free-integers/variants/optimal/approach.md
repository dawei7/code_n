# Eleven-free Integers - Optimal Approach

## Algorithm Explanation

Find $E(10^{18})$, the $10^{18}$-th positive integer whose decimal expansion contains no substring equal to $11^k$ for any $k \ge 1$ ($11, 121, 1331, 14641, \dots$).

### Aho-Corasick Automaton, Digit DP & Binary Search:
1. **Forbidden Pattern Trie & Automaton**:
   We construct an Aho-Corasick automaton over string representations of all powers $11^k \le 2 \cdot 10^{18}$.
   The automaton contains $< 200$ states and tracks matching prefixes of forbidden substrings.
2. **Digit DP Count Function**:
   `count_eleven_free(X)` computes the number of eleven-free integers $\le X$ using standard digit DP over the automaton states.
3. **Monotonic Binary Search**:
   Since `count_eleven_free(X)` is strictly increasing, we locate $E(10^{18})$ by binary searching $X \in [10^{18}, 2 \cdot 10^{18}]$ such that `count_eleven_free(X) == 10**18`.
4. **Execution**:
   Binary searching $X$ yields $1295552661530920149$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\log X \cdot \text{Digits} \cdot |\text{DFA}|)$ for $X \approx 10^{18}$. Runs in $\approx 0.05\text{s}$.
- **Space Complexity:** $\mathcal{O}(|\text{DFA}|)$ state transition table.
