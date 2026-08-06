## Hint

1. First consider the case in which the selected slot from `slots1` begins later than the selected slot from `slots2`.
2. Use two pointers to examine the possible intersections and test each shared length against `duration`.
3. Mirror the first case when the selected `slots2` interval begins later, then keep the earlier of the feasible options.
