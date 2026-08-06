## Description

Two teams, named Even and Odd, play a game on a singly linked list whose length is even. The nodes are indexed from zero. Every node at an even index contains an even integer, while every node at an odd index contains an odd integer.

Process the list as consecutive two-node groups: indices $0$ and $1$, then $2$ and $3$, and so on. Within each group, the team associated with the node holding the larger value earns one point. Thus, Even scores when the even-indexed value is larger, and Odd scores when the odd-indexed value is larger.

Determine which team has more points after every pair has been considered. Return `"Even"` or `"Odd"` for the winning team, or `"Tie"` when their scores are equal.
