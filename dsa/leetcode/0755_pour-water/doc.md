# Pour Water

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 755 |
| Difficulty | Medium |
| Category | Algorithms |
| Topics | Array, Simulation |
| Supported Languages | python, cpp, java, csharp, javascript, go, kotlin |
| Official Link | [LeetCode](https://leetcode.com/problems/pour-water/) |

## Problem Description

### Goal

Terrain heights are given by an integer array, and `volume` one-unit droplets of water are poured one at a time at index `k`. A droplet first searches left across reachable levels for a lower settling position; if none exists, it searches right under the same rule.

If neither side offers a lower position, the droplet remains at `k`. After each droplet settles, increase that position's height before processing the next droplet, so accumulated water affects later movement. Return the final terrain-plus-water heights after all `volume` units have settled.

### Function Contract

**Inputs**

- `heights`: the current non-negative height at each terrain position.
- `volume`: the number of unit droplets to add.
- `k`: the index where every droplet is poured.

**Return value**

- The final height list after applying the droplets sequentially under the left-before-right flow rule.

### Examples

**Example 1**

- Input: `heights = [2,1,1,2,1,2,2]`, `volume = 4`, `k = 3`
- Output: `[2,2,2,3,2,2,2]`
- Explanation: Successive droplets fill lower reachable positions on both sides before one remains at the pour index.

**Example 2**

- Input: `heights = [1,2,3,4]`, `volume = 2`, `k = 2`
- Output: `[2,3,3,4]`
- Explanation: Both droplets travel left and settle in the lowest reachable positions.
