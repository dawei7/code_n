## General

**Preserve identities while sorting arrivals**

Chair assignments must be simulated in arrival order, but the answer refers to the original friend index. The solution appends each original index `i` directly to `times[i]`, turning each row into `[arrival, leaving, i]`, then sorts `times`.

Because all arrival times are distinct, sorting lists lexicographically orders friends by arrival without needing a tie rule. The appended index travels with the times and identifies `targetFriend` after sorting.

This modifies the caller's input: every inner list gains an element and the outer list is reordered. That side effect is part of the exact implementation.

**Use one heap for free chairs and one for occupied chairs**

At most $N$ friends can be present, so chair numbers $0$ through $N-1$ are sufficient. `idle` initially contains that whole range and is heapified. Its smallest element is always the smallest currently unoccupied chair.

`busy` stores pairs `(leaving, chair)`. As a min-heap, it exposes the occupied chair whose friend leaves earliest.

Before assigning a chair to an arrival at time `arrival`, the loop repeatedly removes busy entries whose leaving time is at most the arrival. Each freed chair is pushed back into `idle`. The `<=` boundary is essential: a chair becomes available at the exact leaving moment and can be used by a friend arriving then.

After releasing all eligible chairs, `heappop(idle)` returns the smallest unoccupied chair `j`. If the arriving original index is the target, the method returns `j` immediately. Otherwise it records `(leaving, j)` in `busy` so that chair can be released later.

The target's busy entry is not inserted because the answer is already known and the function ends. This does not alter the returned assignment.

**Why the heaps model the party exactly**

Before each arrival, every chair in `busy` is occupied by a previously arrived friend who has not yet left, and every allocated chair not in `busy` is in `idle`. The release loop moves exactly the chairs whose owners have departed by the current time. Thus, after releases, `idle` contains all and only unoccupied chairs among the initialized range.

The minimum heap then implements the rule “take the unoccupied chair with the smallest number.” Recording the chosen chair with its leaving time preserves the invariant for the next arrival.

Induction over sorted arrivals proves every friend processed before the target receives the same chair as in the real event sequence. Therefore the chair returned at the target's arrival is correct.

**Why initializing only $N$ chairs is enough**

There are infinitely many chairs conceptually, but no more than $N$ friends can be seated simultaneously. Even if no chair is ever reused, the first $N$ assignments are chairs zero through $N-1$. A chair numbered $N$ or higher can never be the smallest available chair for one of only $N$ friends. Materializing `range(n)` is sufficient.

## Complexity detail

Let $N$ be the number of friends.

Appending indices takes $O(N)$ time. Sorting the augmented rows takes $O(N\log N)$. Each nontarget friend causes one pop from `idle` and one push into `busy`. Each departure before the target causes one pop from `busy` and one push into `idle`. Every heap operation costs $O(\log N)$, and each entry moves a constant number of times, so total time is $O(N\log N)$.

The two heaps together contain $O(N)$ entries. Sorting Python lists can also require $O(N)$ temporary storage. Auxiliary space is $O(N)$.

The input mutation does not allocate a separate event list, but the `idle` list and heaps still give linear space.

## Alternatives and edge cases

- **Linear chair scan:** For each arrival, scan chair states from zero upward. It is simple but can take $O(N^2)$ time.
- **Allocate chairs lazily:** Keep a next-new-chair counter plus a heap only for released chairs. This also gives $O(N\log N)$ time and can avoid preloading all chair numbers.
- **Separate event list:** Store arrival, leaving, and index tuples without changing `times`. It preserves the caller's data at the cost of another list.
- **Arrival at a departure time:** The release condition uses `<=`, so the newly freed chair is eligible immediately.
- **Several departures before one arrival:** The while loop releases all of them before selecting the minimum.
- **Departure order differs from arrival order:** The busy heap orders by leaving time independently, which is why one sorted arrival list alone is insufficient.
- **Distinct arrivals:** They guarantee one friend is processed at each arrival time and make lexicographic sorting unambiguous.
- **Target arrives first:** All chairs are idle and the method returns chair zero.
- **No chairs freed before target:** Earlier friends occupy chairs from zero upward, so the target receives the next smallest number.
- **Input mutation:** Rows gain original indices and the list is sorted in place; callers needing the original structure must pass a copy.
- **Imported heap functions:** The exact source assumes `heapify`, `heappop`, and `heappush` are available.
