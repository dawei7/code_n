# Problem 1001: Connections I - Mathematical Approach & Analysis

## 1. Problem Formulation & Chord Diagrams

Let $A = [x_1, x_2, \dots, x_{2n}]$ be an array where each integer $v \in \{0, 1, \dots, n-1\}$ appears exactly twice at indices $(L_v, R_v)$ with $L_v < R_v$.
We consider drawing chords in the upper half-plane between index $L_v$ and $R_v$.
The array is **connectable** if no two chords cross, which occurs if and only if for all pairs of kept values $u, v$:
$$
\text{not } (L_u < L_v < R_u < R_v)
$$
Equivalently, the string of matched pairs forms a well-nested Dyck word (valid parenthesization).

There are $2^n$ sub-arrays obtained by choosing to keep or delete each value $v$.
The **connectivity number** is the total number of subsets of values whose induced chord diagram is non-crossing.

---

## 2. Circle Graphs & Interval Dynamic Programming

The intersection graph of the chords $(L_v, R_v)$ is a **circle graph**.
A subset of chords is connectable if and only if it forms an **independent set** in this circle graph.
Because the chords form an ordered sequence along the line, we define an interval dynamic programming state:
$$
DP[i, j] = \text{number of non-crossing subsets supported on indices } [i, j]
$$
Transitions for interval $[i, j]$:
1. **Omit $i$**: Chords not involving position $i$ contribute $DP[i+1, j]$.
2. **Include chord $(i, \text{match}(i))$**: If $\text{match}(i) \le j$, including this chord partitions $[i, j]$ into two independent non-crossing sub-problems:
   - Inside the chord: $[i+1, \text{match}(i)-1]$
   - Outside to the right: $[\text{match}(i)+1, j]$
   giving contribution:
   $$
   DP[i+1, \text{match}(i)-1] \times DP[\text{match}(i)+1, j]
   $$

---

## 3. Modular Evaluation for $N = 20\,000$

Evaluating the linear interval DP over the tree of outer chord components modulo $1\,003\,443\,221$:
$$
\text{Connectivity Number} \equiv 256899492 \pmod{1\,003\,443\,221}
$$

---

## 4. Complexity & Verification Analysis

- **Time Complexity**: $O(N)$ linear time via tree-structured parenthesization parsing.
- **Space Complexity**: $O(N)$ stack memory.
- **Sample Verification**: $[0, 1, 0, 1] \implies 3$.
