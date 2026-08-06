## Description

A circular street contains an unknown number $n$ of houses. From any house, moving right advances to the next house, and moving right from the last house wraps to the first. You begin at an arbitrary house and know only a positive upper bound $k$, where $1 \le n \le k \le 10^5$.

Each house has a door that may initially be open or closed, with at least one door guaranteed open. The restricted `Street` interface lets you inspect the current door, close it if it is open, and move one house to the right. It does not expose house identities, permit opening a door, or reveal your position.

Use only that interface to determine and return the exact number of houses.
