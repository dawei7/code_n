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

### Required Complexity

- **Time:** $O(vn)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Trace one droplet across non-rising levels**

Start a candidate destination at `k`. To inspect the left side, move one position at a time while the next height is no greater than the current height; the droplet cannot cross the first upward step. Whenever a strictly lower height is found, remember its index. Updating only on a strict decrease preserves the position closest to `k` when the lowest level is a plateau.

If the left scan found a position lower than `k`, settle there immediately. Otherwise repeat the same scan to the right. If neither direction records a lower position, increment `heights[k]`.

**Apply droplets sequentially**

After each chosen destination is incremented, start the next droplet from the updated profile. This is essential because one unit of water can change the next unit's reachable path or preferred side.

For one direction, the scan visits exactly the contiguous positions the droplet can traverse before an upward barrier. The remembered closest occurrence of the minimum height is therefore its prescribed settling point on that side. Trying the entire left rule before the right rule enforces the required preference, and falling back to `k` covers the only remaining outcome. Repeating this faithful transition produces the final profile.

#### Complexity detail

Let `n` be the terrain length and `v` the volume. Each droplet scans at most `n` positions across the two directions, so total time is $O(vn)$. The profile is updated in place using a constant number of indices, giving $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Enumerate every candidate and recheck its path:** This can reproduce the same choice but may take $O(vn^2)$ time.
- **Balanced structures for basins:** More elaborate range and level data structures can batch large volumes, but they add substantial complexity for the bounded input.
- **Flat lower plateau:** Settle at the lowest position closest to `k`, not at the far end of the plateau.
- **Both sides lower:** The left side has priority even if the right side also offers a valid low point.
- **No lower side:** The droplet stays directly at `k`.
- **Single terrain position:** Every droplet increments that only height.
- **Changing profile:** Never compute all destinations from the original terrain; earlier droplets affect later ones.

</details>
