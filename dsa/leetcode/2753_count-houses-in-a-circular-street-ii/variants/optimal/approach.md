## General

**Use an open door as a marker**

The interface exposes no house index and allows doors only to be closed, not opened. At least one door is initially open, so an open door is the only state that can serve as a recognizable marker.

The first while loop moves right until `isDoorOpen()` is true. It leaves that first found door open. Because the street has $n\le k$ houses and at least one open door, this search takes fewer than $n$ moves and must terminate.

**Why the first open door must remain open initially**

If the algorithm closed its marker immediately, it could no longer distinguish returning to that house from reaching any door that was initially closed.

Leaving it open creates a state that survives until the traversal comes back. Meanwhile, every later open door can be closed so that only the marker remains open by the end of the first lap.

**Walk exactly k steps from the marker**

The for loop performs one `moveRight()` for each `i` from one through `k`. The integer `i` is the distance traveled from the marker position.

Whenever the newly reached door is open:

- assign `ans = i`;
- close that door.

This both records the distance to the open reference and removes it from future consideration.

**What happens to other initially open doors**

Before completing a full lap, the walk may encounter several initially open doors. Each updates `ans` to its current distance and is closed.

These temporary answer values are not yet the street length, but overwriting is intentional. The algorithm is interested in the final open door encountered during the bounded traversal.

**Returning to the marker reveals n**

After exactly $n$ right moves, the walk returns to the first open door. That marker is still open because it was skipped before the loop.

At `i=n`, the condition is true, so `ans` becomes `n` and the marker is closed. This is the exact desired count.

**Why later steps cannot overwrite n**

By the time the first full lap ends:

- every other initially open door was encountered and closed;
- the marker has just been closed;
- initially closed doors were never opened.

Therefore all doors are now closed. If `k>n`, remaining loop iterations see only closed doors and leave `ans=n` unchanged.

Because $n\le k$, the loop is guaranteed to reach the marker before it ends.

**Trace four all-open houses with k ten**

Start at the first open marker. At distances one, two, and three, other open doors are found, recorded, and closed.

At distance four, the walk returns to the marker, sets `ans=4`, and closes it. Distances five through ten encounter only closed doors, so four remains the answer.

**Trace mixed doors**

Suppose a five-house street has open doors at marker distance two and four as well as the marker. The loop sets `ans` to two, then four, closing those doors. At distance five it returns to the marker, sets `ans=5`, and closes it. No later open door exists.

**Why ans is always assigned**

Even if no other open door exists, the marker itself is revisited after $n$ moves. Since $n\le k$, that revisit occurs inside the loop and assigns `ans` before return.

Python therefore never reaches `return ans` with an unbound variable for legal inputs.

**State left behind**

The procedure closes every door. Restoring initial door states is impossible with the provided interface and is not required by the contract.


The search finds and preserves one open marker. During the next $k$ right moves, every other open door encountered before a full lap is closed. Exactly after $n$ moves, the traversal returns to the preserved marker, records distance $n$, and closes it. All doors are then closed, so later moves cannot change the answer. Since $n\le k$, this event always occurs, and the returned value is exactly the number of houses.

## Complexity detail

Finding the first open door takes at most $n-1$ moves. The bounded loop performs exactly $k$ moves and checks. Total time is $O(n+k)=O(k)$ because $n\le k$.

The algorithm stores only loop index `i` and `ans`, using $O(1)$ auxiliary space. Door states in the Street object are modified in place and are not additional allocated storage.

Each Street API call is assumed $O(1)$ under the problem interface.

## Alternatives and edge cases

- **Close the first open door immediately:** Loses the unique return marker and cannot distinguish a full lap.
- **Use a closed door as marker:** Impossible because initially closed doors are indistinguishable and cannot be opened.
- **Editorial two-k traversal:** Also works; this exact source first locates a marker and then uses exactly `k` bounded moves.
- **One house:** The first loop stops immediately, the first right move returns to the marker, and answer is one.
- **All doors open:** Every non-marker door is closed before the marker revisit.
- **Exactly one open door:** No temporary answer occurs; the marker revisit assigns `n`.
- **n equals k:** The marker is reached on the final iteration.
- **k larger than n:** Extra moves see all doors closed and do not change `ans`.
- **Final state:** Every door is closed.
- **Guaranteed open door:** Ensures the initial search terminates.
