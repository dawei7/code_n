## General

Rider requests and driver availability each require FIFO order, so keep one deque for riders and another for drivers. Appending records arrival, and removing from the left selects the earliest entry.

Cancellation is harder because the requested rider may be anywhere inside the rider deque. Searching for and deleting that entry immediately would make a cancellation linear. Instead, maintain an `active_riders` set as the authoritative record of riders who are still eligible:

- `addRider` appends the ID to the rider deque and inserts it into the set.
- `cancelRider` discards the ID from the set. This also correctly does nothing for an unknown or already matched rider.
- `addDriver` appends the ID to the driver deque.
- Before matching, remove rider IDs from the front while they are absent from the active set. These are canceled requests whose queue entries have become stale.

After that cleanup, the rider at the front is the earliest still-waiting rider: every earlier arrival has either already been matched or has just been discarded as canceled. The driver at the front is likewise the earliest available driver because drivers are never canceled. If either deque has no valid entry, no pair exists and neither valid side is consumed. Otherwise, removing both fronts returns exactly the required FIFO pair, and deleting the rider from the active set records that the rider is now matched.

Each rider queue entry is appended once and removed at most once. Lazy cleanup can therefore perform many removals during one call without repeating that work later, which establishes the total linear bound.

## Complexity detail

Let $Q$ be the number of operations. `addRider`, `addDriver`, and `cancelRider` take expected $O(1)$ time. A single `matchDriverWithRider` call can take $O(Q)$ time when it clears a long canceled prefix, but across the complete trace all cleanup loops perform only $O(Q)$ deque removals. The full trace therefore takes expected $O(Q)$ time, or expected amortized $O(1)$ per operation.

The two deques and active-rider set retain at most $O(Q)$ IDs, so auxiliary space is $O(Q)$.

The benchmark defines size as the number of riders added and then canceled in reverse order before one match. The lazy set approach performs linear total work. A correct eager-list control searches the shrinking rider list for every reverse-order cancellation, requiring quadratic total time.

## Alternatives and edge cases

- **Eager list removal:** Deleting a canceled rider from a Python list keeps the queue physically clean, but locating an arbitrary ID is $O(Q)$ and many cancellations can make the trace quadratic.
- **Doubly linked list plus map:** A node map permits worst-case constant-time cancellation and a linked list preserves FIFO order, but it requires substantially more custom pointer bookkeeping.
- **Ordered dictionary for riders:** Insertion order plus key deletion supports the required operations in expected constant time and is a valid alternative, though separate queue-and-validity structures make the lazy-deletion argument explicit.
- **Cancellation before addition:** The rider does not yet exist, so `cancelRider` must have no effect; a later first addition of that ID is still active.
- **Cancellation after matching:** The rider is no longer active, so the call changes nothing.
- **Only one side available:** An unsuccessful match returns `[-1, -1]` without consuming the waiting riders or drivers.
- **Canceled rider behind a valid rider:** It remains physically queued until it reaches the front, but the active set prevents it from ever being matched.
- **Long canceled prefix:** Cleanup must continue past every stale rider until the earliest active rider is found or the queue becomes empty.
- **Equal rider and driver IDs:** The two ID namespaces are independent; `[x, x]` is a valid match.
