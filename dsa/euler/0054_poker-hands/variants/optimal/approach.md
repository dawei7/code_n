# Poker Hands - Optimal Approach

## Algorithm Explanation

Determine the total number of hands won by Player 1 out of $1000$ dealt rounds in `poker.txt`.

### Hand Evaluation Function:
Define card values: $2=2, 3=3, \dots, T=10, J=11, Q=12, K=13, A=14$.

Map each $5$-card hand to a comparable score tuple `(hand_category, kicker_1, kicker_2, ...)`:
- Category 8: Straight Flush / Royal Flush
- Category 7: Four of a Kind
- Category 6: Full House
- Category 5: Flush
- Category 4: Straight
- Category 3: Three of a Kind
- Category 2: Two Pairs
- Category 1: One Pair
- Category 0: High Card

Because Python compares tuples lexicographically element-by-element, comparing `hand_rank(p1_hand) > hand_rank(p2_hand)` resolves all category ranks and tie-breakers in $\mathcal{O}(1)$ time per hand.

## Complexity Analysis

- **Time Complexity:** $\mathcal{O}(N)$ where $N = 1000$ poker games. Runs in $< 0.1\text{s}$.
- **Space Complexity:** $\mathcal{O}(N)$ - Memory for input card strings.
