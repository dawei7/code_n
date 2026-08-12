# Darts - Optimal Approach

## Algorithm Explanation

Find the total number of distinct checkout combinations in Darts with a total score strictly less than $100$.

### Rules & Combinatorial Structure:
1. **First 2 Darts (Non-Final Darts)**:
   - Can land on any region: Miss ($0$), Singles ($S_1 \dots S_{20}, S_{25}$), Doubles ($D_1 \dots D_{20}, D_{25}$), or Trebles ($T_1 \dots T_{20}$). Total $63$ region options.
   - The ordering of the first $2$ darts does not matter ($d_1, d_2$ is identical to $d_2, d_1$). We iterate unordered pairs $d_1 \le d_2$.
2. **Final Dart (Checkout Dart)**:
   - Must land on a Double ($D_1 \dots D_{20}, D_{25}$). Total $21$ double options.
   - The final dart defines a unique checkout target.

### Strategy:
1. Construct list of $63$ normal dart region choices.
2. Construct list of $21$ checkout double region choices.
3. Iterate all $\frac{63 \times 64}{2} = 2016$ unordered pairs of first $2$ darts $(d_1, d_2)$ with $d_1 \le d_2$.
4. Combine each pair with all $21$ checkout doubles ($2016 \times 21 = 42336$ total valid checkouts).
5. Accumulate count of checkouts with total score $\text{val}(d_1) + \text{val}(d_2) + \text{val}(d_3) < 100$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}\left(\frac{N(N+1)}{2} \cdot D\right)$ where $N = 63, D = 21$ ($42336$ iterations). Runs in $< 0.015\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$ - Memory overhead is constant.
