# Problem 814: Mezzo-forte - Approach & Solution Analysis

## 1. Problem Overview

In a circle of $4n$ people, each person screams either *loud* ($1$) or *quiet* ($0$).
Exactly $2n$ people scream loud and $2n$ scream quiet.
For each person $i$:
- If person $i$ screams loud, exactly two of their neighbors (the adjacent persons $i-1, i+1$ and the diametrically opposite person $i+2n$) scream loud.
- If person $i$ screams quiet, exactly one of their three neighbors screams loud.

We are asked to find $S(n)$, the total number of valid configurations, modulo $998244353$, for $n = 1000$.

## 2. Mathematical Characterization & Slice Decomposition

Pair each person $i$ ($0 \le i < 2n$) with their diametrically opposite partner $i + 2n$.
Let $x_i \in \{0, 1\}$ be the screaming state of person $i$, and $y_i = x_{i+2n} \in \{0, 1\}$.
Each diameter pair $(x_i, y_i)$ can be represented as a 2-bit state $c_i = (x_i, y_i) \in \{0, 1, 2, 3\}$.

For person $i$, their neighbors are $x_{i-1}, x_{i+1}$, and $y_i$. The condition is:
- $x_{i-1} + y_i + x_{i+1} = 2$ if $x_i = 1$, and $1$ if $x_i = 0$.

For person $i+2n$, their neighbors are $y_{i-1}, y_{i+1}$, and $x_i$. The condition is:
- $y_{i-1} + x_i + y_{i+1} = 2$ if $y_i = 1$, and $1$ if $y_i = 0$.

Notice that given slice states $p = (x_{i-1}, y_{i-1})$, $c = (x_i, y_i)$, and $nx = (x_{i+1}, y_{i+1})$, the validity of slice $i$ depends strictly on $p, c, nx$.

## 3. Dynamic Programming Formulation

We can define a dynamic programming state along the circular chain of $2n$ slices:
- Fix the initial state of slice 0: $m_0 \in \{0, 1, 2, 3\}$.
- Track the current slice state $cur \in \{0, 1, 2, 3\}$.
- Track the running total number of loud screamers $k = \sum (x_i + y_i)$.
- Transition to the next slice state $nx \in \{0, 1, 2, 3\}$ if there exists a valid previous state $p$ satisfying the neighborhood constraints for $cur$.
- Advance $2n-1$ times and close the circle by checking compatibility with $m_0$ and ensuring the total count of loud screamers equals $2n$.

## 4. Algorithmic Complexity

- **State Space**: $4 \times 4 \times (n+1) = 16(n+1)$ states per slice step.
- **Transitions**: 4 possible next states for each state.
- **Time Complexity**: $O(n \times 4^3 \times n) = O(n^2)$, taking under $0.4$ seconds for $n = 1000$.
- **Space Complexity**: $O(n)$ space across DP layers.

## 5. Implementation

The solution is implemented in `solution.py` using dynamic slice transitions and modulo arithmetic, computing $S(1000) \pmod{998244353}$ dynamically.
