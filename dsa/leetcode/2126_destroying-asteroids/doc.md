# Destroying Asteroids

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 2126 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Greedy, Sorting |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/destroying-asteroids/) |

## Problem Description

### Goal

A planet begins with the positive integer mass `mass`. Each value in
`asteroids` is the mass of one asteroid, and you may choose the collision order
arbitrarily.

When the planet's current mass is greater than or equal to the chosen
asteroid's mass, that asteroid is destroyed and its entire mass is added to the
planet. If the asteroid is heavier, the planet is destroyed and cannot
continue. Every asteroid must be used exactly once.

Determine whether some ordering lets the planet destroy all asteroids. Equality
is sufficient for a successful collision, and mass gained from earlier
asteroids is available for every later collision.

### Function Contract

**Inputs**

- `mass`: The planet's positive initial mass.
- `asteroids`: A nonempty list of positive asteroid masses. Let
  $n=\lvert\texttt{asteroids}\rvert$.

**Return value**

Return `true` if all asteroids can be destroyed in some order; otherwise return
`false`.

### Examples

#### Example 1

- **Input:** `mass = 10, asteroids = [3, 9, 19, 5, 21]`
- **Output:** `true`

Destroying accessible smaller asteroids first grows the planet enough to
destroy every later one.

#### Example 2

- **Input:** `mass = 5, asteroids = [4, 9, 23, 4]`
- **Output:** `false`

Even after absorbing the other three asteroids, the planet reaches only mass
$22$, which is less than $23$.
