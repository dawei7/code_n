## General

**Reconstruct the deck by undoing the reveal process**

The forward process repeatedly does two things:

1. reveal and remove the top card;
2. if cards remain, move the new top card to the bottom.

Simulating forward is easy once the initial deck is known, but the task asks us to construct that initial order. The solution works backward from the desired reveal order.

Because reveals must be increasing, the last card revealed is the largest. The algorithm processes card values from largest to smallest and maintains a deque representing the deck that would reveal the already-processed larger cards in increasing order.

**Undo the forward rotation**

In the forward direction, after revealing a card, the next top card moves to the bottom.

The inverse of moving top to bottom is moving bottom to top. For a nonempty deque, the code performs:

`q.appendleft(q.pop())`.

It removes the bottom element and places it at the top, exactly undoing the most recent forward rotation.

After undoing that rotation, the next smaller card is placed at the top with `q.appendleft(v)`. In forward play, this newly placed card will be the next one revealed.

**Why cards are processed in reverse sorted order**

Suppose desired reveal values are `a1 < a2 < ... < an`. Work backward:

- The state just before revealing `an` is simply `[an]`.
- To reconstruct the state before revealing `a(n-1)`, undo the rotation that would follow that reveal, then put `a(n-1)` on top.
- Repeat toward `a1`.

This is why `sorted(deck, reverse=True)` supplies values from largest down to smallest.

The input values are unique, so increasing order is strict and each card has one unambiguous position in the desired reveal sequence.

**A short reverse trace**

Use sorted values `[2, 3, 5, 7]`, processed as `7, 5, 3, 2`.

- Insert seven: deque is `[7]`.
- Before inserting five, move bottom seven to top, which changes nothing; then insert five: `[5, 7]`.
- Undo rotation by moving bottom seven to top: `[7, 5]`. Insert three: `[3, 7, 5]`.
- Move bottom five to top: `[5, 3, 7]`. Insert two: `[2, 5, 3, 7]`.

Now simulate forward:

- reveal two, move five to bottom;
- reveal three, move seven to bottom;
- reveal five;
- reveal seven.

The reveals are `2, 3, 5, 7`.

**The maintained invariant**

After processing some suffix of the values in descending construction order, deque `q` has this property:

> Applying the forward reveal process to `q` reveals exactly the values currently placed in increasing order.

The base case after inserting the largest value is obvious.

Assume the invariant holds for the larger values. Let `v` be the next smaller value. The reverse rotation prepares the old deque so that, after `v` is revealed and the forward top-to-bottom move occurs, the deque returns to the prior invariant state. Placing `v` at the front makes it reveal first. The remaining larger values then reveal in their already-correct increasing order.

Induction proves the final deque reveals the complete sorted deck.

**Why a deque is the right structure**

Construction repeatedly removes from the right end and inserts at the left end. A deque performs both in constant time.

Using a Python list and inserting at index zero would shift all existing elements on every step, turning the reconstruction phase into quadratic time.

At the end, `list(q)` converts the deque to the list format required by the interface. The first entry is the deck's top.

**Input handling**

The solution calls `sorted(deck, reverse=True)` rather than sorting `deck` in place. It leaves the caller's input list unchanged while producing the descending processing order.

## Complexity detail

Let `n` be the number of cards.

Sorting takes `O(n log n)` time. Each card then causes at most one deque pop, one rotation insertion, and one front insertion, all `O(1)`. Converting the final deque to a list costs `O(n)`. Total time is `O(n log n)`.

The sorted list, deque, and returned list each use linear storage at different stages, so auxiliary and output space are `O(n)`.

## Alternatives and edge cases

- **Simulate positions forward:** Keep a queue of indices, assign sorted card values to each next revealed index, and rotate the next index. This also takes `O(n log n)` time and `O(n)` space.
- **Use a list as a deque:** Removing from the end is cheap, but inserting at the front is `O(n)` and makes construction quadratic.
- **Forward trial and error:** Guessing deck orders explores permutations unnecessarily; reversing deterministic operations gives the answer directly.
- **One card:** The deque is empty before insertion, so no rotation occurs and the single card is returned.
- **Two cards:** Reverse construction returns them in increasing order, which reveals the smaller then the larger.
- **Unique values:** They guarantee one strictly increasing reveal order. With duplicates, non-decreasing reveals would require a slightly different statement but the construction still has a natural interpretation.
- **Top-of-deck convention:** `appendleft` and list index zero consistently represent the top.
- **Rotation only when nonempty:** Calling `pop` on an empty deque would fail, so the `if q` guard is essential.
- **Input preservation:** The original deck ordering remains unchanged because `sorted` returns a new list.
- **Large card values:** Only comparisons matter; magnitude does not affect the algorithm.
