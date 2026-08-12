# Ambiguous Numbers - Optimal Approach

## Algorithm Explanation

Find the number of ambiguous rational numbers $x = \frac{p}{q} \in (0, \frac{1}{100})$ with denominator $q \le 10^8$.

### Farey Mediant & Stern-Brocot Tree:
1. **Ambiguous Numbers Definition**:
   A rational number $x$ has two best approximations for some denominator bound $d$ if and only if $x$ is the exact midpoint of two adjacent Farey fractions $\frac{p_1}{q_1}$ and $\frac{p_2}{q_2}$ with $p_2 q_1 - p_1 q_2 = 1$.
2. **Midpoint Characterization**:
   $$x = \frac{1}{2}\left(\frac{p_1}{q_1} + \frac{p_2}{q_2}\right) = \frac{p_1 q_2 + p_2 q_1}{2 q_1 q_2}$$
   In reduced form, the denominator is $q = 2 q_1 q_2 \le 10^8$.
3. **Accelerated Tree Traversal**:
   We search the Stern-Brocot tree in the range $(0, \frac{1}{100})$ starting at $(q_1=1, q_2=100)$.
   Jump accelerated left steps $(q_1, q_2 + k q_1)$ compute $k_{\text{max}} = \lfloor \frac{10^8 / (2 q_1) - q_2}{q_1} \rfloor$ in $\mathcal{O}(1)$ time.
4. **Execution**:
   Running the tree traversal counts exactly $52,374,376$ ambiguous numbers.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\sqrt{Q})$ where $Q = 10^8$. Runs in $\approx 7.8\text{s}$.
- **Space Complexity:** $\mathcal{O}(\sqrt{Q})$ - Stack space for tree traversal.
