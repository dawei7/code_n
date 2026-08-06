## Description

This is an interactive problem. Ships are hidden at distinct integer-coordinate points in a Cartesian plane, and any integer point contains at most one ship. Their positions cannot be read or enumerated directly.

The supplied `Sea` interface exposes `hasShips(topRight, bottomLeft)`. It reports whether at least one ship lies inside the inclusive axis-aligned rectangle whose upper-right and lower-left corners are the two given points.

For a target rectangle identified by `topRight` and `bottomLeft`, return its exact number of ships. The target contains at most $10$ ships. A submission is judged Wrong Answer if it makes more than $400$ calls to `hasShips`; attempting to bypass the hidden interface is outside the problem contract.
