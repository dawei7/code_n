# Concealed Square - Optimal Approach

## Algorithm Explanation

Find the unique positive integer $x$ whose square has the form $1\_2\_3\_4\_5\_6\_7\_8\_9\_0$.

### Modular Arithmetic & Search Space Reduction:
1. **Trailing Zeros**:
   Since $x^2$ ends in `0`, it must end in `00`, implying $x = 10y$ for an integer $y$, and $y^2 = 1\_2\_3\_4\_5\_6\_7\_8\_9$.
2. **Last Digit Pruning**:
   Since $y^2$ ends in `9`, $y$ must end in `3` or `7`.
3. **Range Pruning**:
   - Lower bound: $y \ge \lfloor\sqrt{10203040506070809}\rfloor = 101010101$.
   - Upper bound: $y \le \lfloor\sqrt{19293949596979899}\rfloor = 138902662$.
4. **Execution**:
   Iterating $y$ by steps of $10$ for $y \equiv 3, 7 \pmod{10}$ checks $\approx 7.5 \times 10^6$ candidates, finding $x = 1389019170$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}\left(\frac{\sqrt{1.93 \times 10^{16}} - \sqrt{1.02 \times 10^{16}}}{10}\right) \approx 7.5 \times 10^6$ iterations. Runs in $\approx 2.0\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
