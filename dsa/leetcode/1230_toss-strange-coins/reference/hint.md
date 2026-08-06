## Hint

1. Consider a dynamic-programming formulation.
2. One possible state is `dp[pos][cnt]`, where `pos` identifies the coin position and `cnt` is the number of heads accumulated so far.
3. Use the head and tail probabilities of the current coin to form the state transitions.
4. At the base case `pos == n`, return whether `cnt == target` so outcomes with the wrong head count contribute zero.
