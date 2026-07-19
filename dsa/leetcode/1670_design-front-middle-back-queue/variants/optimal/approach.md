## General
**Represent two contiguous halves.** Store the queue's prefix in deque `left` and its suffix in deque `right`. Maintain

$$
\lvert\texttt{left}\rvert = \lvert\texttt{right}\rvert
\quad\text{or}\quad
\lvert\texttt{left}\rvert = \lvert\texttt{right}\rvert + 1.
$$

The queue order is all of `left` followed by all of `right`. Under this invariant, the frontmost middle element is always the back of `left`.

**Map each endpoint operation directly.** `pushFront` and `popFront` use the front of `left`. `pushBack` appends to `right`; `popBack` removes from `right` when it is nonempty and otherwise from the lone element in `left`. After an endpoint mutation, move at most one boundary value between the deques to restore their allowed size difference.

**Handle the middle convention explicitly.** Before `pushMiddle`, if `left` already has the extra element, move its back to the front of `right`. Appending the new value to `left` then places it at index $\lfloor n/2 \rfloor$. `popMiddle` removes the back of `left`, which is the unique middle for odd length and the frontmost of the two middles for even length; one rebalance restores the invariant.

**Why every operation selects the right position.** The concatenated deques always preserve the queue order, and rebalancing moves only the value crossing the boundary, never reordering either half. The invariant locates the front at `left`'s front, the back at the nonempty suffix's back, and the required middle at `left`'s back. Consequently each method changes exactly the requested position and leaves all other values ordered.

## Complexity detail
Every deque endpoint mutation is $O(1)$, and rebalancing performs at most one additional endpoint move. Each queue method therefore takes $O(1)$ time, so $q$ calls take $O(q)$ total time. The two deques jointly store every current queue element once, requiring $O(q)$ space in the worst case.

## Alternatives and edge cases
- **Single dynamic array:** Front and middle insertions or removals require shifting $O(n)$ values, producing $O(q^2)$ time for an adversarial operation sequence.
- **Custom doubly linked list plus middle pointer:** This also supports constant-time operations, but six mutations require careful pointer and parity updates and more implementation surface.
- **Order-statistics tree:** Rank-based insertion and deletion work in $O(\log n)$ time, which is unnecessary when two deques exploit the fixed front-middle-back positions.
- Every pop method returns `-1` on an empty queue.
- With one element, front, middle, and back all identify that same value.
- For even length, `popMiddle` removes the last value of the front half, not the first value of the back half.
- Repeated values are independent queue entries and must retain their positional order.
- Alternating pushes and pops may change parity after every operation; rebalancing must run after each applicable mutation.
