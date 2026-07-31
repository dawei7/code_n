## Description

An $m \times n$ grid named `rooms` uses three kinds of cells:

- `-1` represents a wall or obstacle.
- `0` represents a gate.
- `INF` represents an empty room, where `INF` is the 32-bit signed maximum $2^{31}-1=2147483647$. A valid distance in this problem is always smaller than `INF`.

Replace every reachable empty room with its distance to the nearest gate. An empty room that cannot reach any gate must remain `INF`.
