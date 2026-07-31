## General

Closed doors cannot serve as recognizable landmarks because the interface cannot change them into a distinguishable state. Open doors can be changed, but closing the very first one immediately would destroy the only known reference. The algorithm therefore leaves the first open door untouched.

Move right for at most $2k$ steps while tracking the global step number. When the first open door is encountered, remember its step and keep that door open. Every later open door is closed, and the distance from the remembered step is stored as the current candidate answer.

Within the next full lap, every other initially open door is encountered and closed. The first marked door remains open, so the last open-door encounter is the return to that same house. Its step difference from the first encounter is exactly one complete circumference, $n$. Closing it then removes every open door, preventing any later step from changing the answer.

The first open door is reached in fewer than $n \le k$ moves, and returning to it takes another $n \le k$ moves. Thus it is encountered for the second time within the $2k$-step loop. The recorded final distance is exactly the number of houses.

## Complexity detail

The algorithm performs exactly $2k$ interface iterations, each with constant work, so its time complexity is $O(k)$. It stores only booleans and integer counters, using $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Close the first open door immediately:** This destroys the only guaranteed recognizable marker and leaves closed houses indistinguishable.
- **Stop at the next open door:** Another door may have been open initially, so the first gap between open doors need not be a full lap.
- **Remember visited houses:** The interface exposes no stable house identity to store or compare.
- When the starting house is closed, the initial search still reaches an open door in fewer than $k$ moves.
- With exactly one open door, its next encounter directly measures the full circle.
- For one house, the marker is encountered again after one right move, so the answer is one.
- A loose bound causes harmless extra moves after every door has been closed; the saved answer no longer changes.

