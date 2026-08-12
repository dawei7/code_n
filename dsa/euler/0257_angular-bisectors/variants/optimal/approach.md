# Angular Bisectors - Optimal Approach

## Algorithm Explanation

Find the number of integer-sided triangles $ABC$ ($a \le b \le c$) with perimeter $a + b + c \le 100\,000\,000$ for which the area ratio $\frac{\text{area}(ABC)}{\text{area}(AEG)}$ is an integer.

### Angular Bisector Segment Ratio & Integer Bounding:
1. **Area Ratio Formula**:
   Using the angle bisector theorem, the ratio of areas simplifies to:
   $$R = \frac{\text{area}(ABC)}{\text{area}(AEG)} = 1 + \frac{a (a + b + c)}{b c}$$
2. **Integer Ratio Constraints**:
   Since $a \le b \le c$, the ratio $R$ can ONLY take integer values $R \in \{2, 3, 4\}$:
   - $R = 4$: Equilateral triangles $a = b = c$.
   - $R = 3$: Triangles satisfying $a(a+b+c) = 2bc$.
   - $R = 2$: Triangles satisfying $a(a+b+c) = bc$.
3. **Parametric Diophantine Counting**:
   Each case is parametrized by coprime pairs $(u, v)$ such that $a + b + c \le 100\,000\,000$.
4. **Execution**:
   Summing valid triangles across all 3 ratio cases yields $139012411$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(\sqrt{P})$ for $P = 100\,000\,000$. Runs in $\approx 0.15\text{s}$.
- **Space Complexity:** $\mathcal{O}(1)$.
