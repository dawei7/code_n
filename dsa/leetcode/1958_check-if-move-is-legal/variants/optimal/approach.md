## General
**Search the eight possible directions**

The placed piece can be an endpoint only along one of the eight horizontal,
vertical, or diagonal rays leaving `(rMove, cMove)`. For each direction, move
one cell at a time. The first cell must have the opposite color, which ensures
that a potential line has at least one middle cell.

**Recognize the closing endpoint**

Continue while cells have the opposite color. The direction forms a good line
exactly when this nonempty run is followed, before leaving the board, by a cell
of the played color. A free cell, the board edge, or an immediate same-colored
cell cannot close a valid line. Returning true for the first successful ray is
sound because one good line is sufficient; if all eight rays fail, no allowed
line orientation remains.

## Complexity detail
The board dimensions are fixed by the contract. There are eight rays and each
contains at most seven cells, so at most 56 cell inspections are required.
This fixed upper bound gives $O(1)$ time. Only direction and coordinate
variables are retained, giving $O(1)$ auxiliary space.

## Alternatives and edge cases
- **Temporarily place the piece and scan complete rows:** This can be made
  correct, but it mutates the input unnecessarily and examines cells unrelated
  to lines having the move as an endpoint.
- **Check only four undirected lines:** Each line has two possible rays from
  the move, so both directions must still be inspected independently.
- An adjacent piece of the played color does not form a good line because at
  least one opposite-colored middle cell is required.
- A run of opposite pieces that reaches the board boundary without a matching
  endpoint is not sufficient.
- A good line elsewhere on the board, or one having the move as a middle cell,
  does not make the proposed move legal.
