# Flea Circus - Optimal Approach

## Algorithm Explanation

Find the expected number of unoccupied squares on a $30 \times 30$ grid after $50$ rings of the bell, rounded to $6$ decimal places.

### Linearity of Expectation & Independent 2D Random Walks:
1. **Linearity of Expectation**:
   Let $E$ be the expected count of empty squares. By linearity of expectation:
   $$E = \sum_{r=0}^{29} \sum_{c=0}^{29} \mathbb{P}(\text{square } (r, c) \text{ is unoccupied})$$
2. **Flea Independence**:
   Since all $900$ fleas move independently:
   $$\mathbb{P}(\text{square } (r, c) \text{ is unoccupied}) = \prod_{(r_0, c_0)} \left(1 - P_{(r_0, c_0)}(r, c, 50)\right)$$
   where $P_{(r_0, c_0)}(r, c, 50)$ is the transition probability distribution for a flea starting at $(r_0, c_0)$ to land on $(r, c)$ after $50$ steps.
3. **Distribution Simulation**:
   For each of the $900$ flea starting positions, we simulate $50$ steps of $2\text{D}$ Markov transitions across the $30 \times 30$ grid.
4. **Execution**:
   Multiplying complement probabilities for all $900$ squares yields $330.721154$.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N^4 \cdot \text{steps})$ for $N = 30$ and $\text{steps} = 50$. Runs in $\approx 6.0\text{s}$.
- **Space Complexity:** $\mathcal{O}(N^4)$ to store state distributions.
