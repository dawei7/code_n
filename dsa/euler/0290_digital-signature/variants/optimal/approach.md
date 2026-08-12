# Digital Signature - Optimal Approach

## Algorithm Explanation

Find the number of integers $0 \le n < 10^{18}$ such that the sum of the digits of $n$ equals the sum of the digits of $137 n$.

### Digit Dynamic Programming with Multiplicative Carry:
1. **LSB-to-MSB Digit Processing**:
   We generate digits $d \in [0, 9]$ of $n$ from lowest to highest power of $10$ ($18$ digit positions).
2. **Carry & Difference Tracking**:
   At each digit position $pos$, given incoming carry $c \in [0, 136]$:
   - Value $V = 137 \cdot d + c$
   - New digit of $137 n$ is $V \bmod 10$, and next carry is $\lfloor V / 10 \rfloor$.
   - Digit sum difference accumulator updates: $\Delta_{\text{new}} = \Delta + d - (V \bmod 10)$.
3. **Terminal Residual Carry Condition**:
   After processing $18$ digits, any remaining carry $c_{\text{final}}$ contributes $\text{digit\_sum}(c_{\text{final}})$ to the digit sum of $137 n$.
   Thus, valid paths satisfy $\Delta_{\text{final}} = \text{digit\_sum}(c_{\text{final}})$.
4. **Execution**:
   Running Digit DP over $18$ digits yields $20444710234716473$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(D \cdot C \cdot \Delta \cdot 10)$ for $D = 18$ digits and max carry $C = 136$. Runs in $\approx 0.90\text{s}$.
- **Space Complexity:** $\mathcal{O}(C \cdot \Delta)$ state dictionary.
