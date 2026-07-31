## General

The initial door states cannot identify a full lap: an open door encountered later might simply have been open before the algorithm began. First erase that uncertainty. Close the current door and move right exactly `k` times. Because the cycle contains $n \le k$ houses, those moves visit every house at least once, so every door is closed afterward.

Open the current door to create a unique marker. Then repeatedly move right and increment a counter. All other doors are closed, so the first open door encountered must be the marker. A rightward walk returns to its starting house after exactly $n$ moves, making the counter at that moment the number of houses.

The method also handles $n=1$: after opening the only door, one right move returns immediately to that same door and produces a count of one.

## Complexity detail

The reset phase makes exactly $k$ iterations. The counting phase makes $n$ iterations, and $n \le k$, so the total time is $O(k+n)=O(k)$. Only the loop counter and house count are stored, giving $O(1)$ auxiliary space.

## Alternatives and edge cases

- **Trust an initially open door:** Stopping at the next open door is incorrect because multiple doors may begin open and none is known to be the starting house.
- **Remember visited houses:** The interface exposes no house identity, and storing identifiers would also violate the constant-space goal.
- **Move in both directions:** A single consistent direction is sufficient; changing direction adds bookkeeping without revealing extra information.
- The clearing phase must cover `k` houses, not merely stop after seeing a closed door.
- A loose bound may cause several complete reset laps, but all doors remain closed and correctness is unchanged.
- A one-house street still requires one counting move before the marker is seen again.
