# Maximize Distance to Closest Person

| Field | Value |
|---|---|
| Source | LeetCode |
| Frontend ID | 849 |
| Difficulty | Medium |
| Topics | Array |
| Official Link | [LeetCode](https://leetcode.com/problems/maximize-distance-to-closest-person/) |

## Problem Description
### Goal
A 0-indexed array `seats` represents one row of seats. A value of `1` means that someone already occupies that position, and `0` means that the seat is empty. The row is guaranteed to contain at least one occupied seat and at least one empty seat.

Alex will choose one empty seat. For any choice, his distance to the closest person is the smallest absolute index difference between his seat and an occupied seat. Return the largest such closest-person distance that Alex can obtain.

### Function Contract
**Inputs**

- `seats`: a binary array of length $n$, where $2 \leq n \leq 2 \cdot 10^4$, containing at least one `0` and at least one `1`.

**Return value**

Return the maximum possible distance from an empty seat to its closest occupied seat.

### Examples
**Example 1**

- Input: `seats = [1,0,0,0,1,0,1]`
- Output: `2`

Sitting at index `2` leaves the nearest occupied seats two positions away.

**Example 2**

- Input: `seats = [1,0,0,0]`
- Output: `3`

The last seat is three positions from the only person.

**Example 3**

- Input: `seats = [0,1]`
- Output: `1`

### Required Complexity
- **Time:** $O(n)$
- **Space:** $O(1)$

<details>
<summary>Approach</summary>

#### General

**Empty runs have two different boundary shapes**

Track the index `previous` of the latest occupied seat while scanning from left to right. When the first occupied seat appears at index `i`, every earlier seat lies in a leading run bounded on only one side. Its best choice is index `0`, at distance `i`.

For each later occupied seat at index `i`, the empty run is bounded by occupied indices `previous` and `i`. A seat in that interval maximizes its minimum distance by lying as near the midpoint as possible, giving

$$
\left\lfloor \frac{i-\texttt{previous}}{2} \right\rfloor.
$$

After the scan, seats following the last occupied index form another one-sided run. The final seat is farthest, at distance `n - 1 - previous`.

**Why these candidates cover every empty seat**

Every empty position belongs to exactly one leading, interior, or trailing run. Within a one-sided run, distance increases toward the array boundary. Within an interior run, the distance to the closer endpoint increases until the midpoint and then decreases. The candidate computed for each run is therefore its local optimum, and the maximum over all runs is Alex's global optimum.

#### Complexity detail

The algorithm examines each of the $n$ seats once and performs constant work at every occupied position, for $O(n)$ time. It stores only indices and the best distance, using $O(1)$ auxiliary space.

#### Alternatives and edge cases

- **Check every empty seat against every person:** This direct method is correct but can take $O(n^2)$ time.
- **Nearest distance arrays:** Left-to-right and right-to-left passes can store each empty seat's nearest occupied distance in $O(n)$ time, but require $O(n)$ space.
- **Two-pointer run scan:** Explicitly measure each consecutive zero run and classify whether it touches a boundary; it has the same linear bounds.
- **Leading empty run:** With no occupied seat to the left, do not halve the distance to the first person.
- **Trailing empty run:** With no occupied seat to the right, use the entire suffix length.
- **Interior odd separation:** Integer division implements the floor when no single seat is exactly centered.
- **Adjacent occupied seats:** They contribute an interior candidate of zero, but no empty seat lies between them.
- **Only one person:** The farther array endpoint determines the answer.
- **Alternating seats:** Every empty seat is adjacent to a person, so the maximum distance is one.

</details>
