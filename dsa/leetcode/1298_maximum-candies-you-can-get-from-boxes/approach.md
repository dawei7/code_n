## General

A box can be opened only when two independent conditions are both true:

1. we possess the physical box, and
2. the box is open already or we possess its key.

These facts can become true in either order. We might find a closed box first and obtain its key later, or obtain a key first and discover the matching box later. The Optimal solution treats every box whose two conditions have become true as ready work. A queue processes ready boxes, while separate sets remember possession and prevent collecting the same box twice.

**The three pieces of state**

`has` is initialized as `set(initialBoxes)`. Membership in `has` means that the box is physically available. Finding a key does not put a box in this set; a key can open a box only after that box has also been obtained.

`status` tells whether each box can currently be opened. Initially, its zeros and ones come from the input. When a key for box `k` is discovered, the exact code changes `status[k]` to one. Mutating the array turns it into the current “can open” state rather than merely the initial state.

`took` contains boxes that have already been scheduled for processing and whose candies have already been added. Its name is broader than “removed from the queue”: a box enters `took` at enqueue time. This choice guarantees that two different discoveries cannot enqueue and count the same box twice.

The key readiness condition is therefore:

`box in has`, `status[box] == 1`, and `box not in took`.

Whenever all three become true, the box is enqueued, marked in `took`, and its candy value is added to `ans`.

**Initializing boxes that are immediately usable**

The code examines every label in `initialBoxes`. An initially owned box whose `status` is one can be opened immediately, so it is placed in the queue, added to `took`, and its candies are counted.

An initially owned but closed box remains only in `has`. It is not lost. If a key is discovered later, the key-processing branch notices that the box is already owned and schedules it then.

Counting candies when a box is enqueued, instead of when it is dequeued, is safe because only owned, open, untaken boxes enter the queue. Once enqueued, nothing can revoke ownership or close the box. The queue will eventually remove it, so those candies are guaranteed to be obtainable.

**Processing keys found in an opened box**

When `box = q.popleft()`, the current box is being opened and its contents become available. The first inner loop visits `keys[box]`.

For a discovered key label `k`, the code checks `if not status[k]` before changing it to one. If the box was already open or an earlier key had already opened it, no state transition occurs and no duplicate scheduling is attempted through this branch.

When a newly useful key opens box `k`, the code next checks whether `k` is already in `has` and not in `took`. If so, both readiness requirements have just become true. The box is enqueued, marked, and counted. If we do not possess it yet, its open status remains recorded. Finding the physical box later will trigger the other branch.

The same key label may appear in key lists of different boxes. The first useful discovery sets `status[k]` to one. Later copies see that it is already one and do nothing, so repeated keys cannot duplicate candies.

**Processing newly contained boxes**

The next loop visits `containedBoxes[box]`. For each contained label `b`, `has.add(b)` records possession.

If `status[b]` is already one and `b` is not in `took`, obtaining the physical box completes its readiness condition. It is immediately enqueued, marked, and counted. If it is closed, it simply remains in `has` until a future key opens it.

This symmetry is the heart of the algorithm:

- key arrives second: the key loop sees an owned box and schedules it;
- box arrives second: the contained-box loop sees an open box and schedules it.

No special ordering of discoveries is required. Even within one opened parent, processing keys before contained boxes is safe. If it contains both a key and its matching box, the key first marks the target open and the box loop then schedules it. Reversing the loops would also work with the same two-state checks: possession would be recorded first and the key loop would schedule it afterward.

**Why a work queue reaches the maximum**

All candy values are positive. Opening a ready box can never reduce the answer or consume a key needed elsewhere. Keys are reusable facts that change openability, and obtaining a contained box does not force us to give up another box. Therefore, there is no strategic reason to skip any reachable ready box.

Every enqueued box is genuinely obtainable because it is both owned and open. Processing it reveals exactly the keys and contained boxes specified for it, so every state transition corresponds to a legal action.

Conversely, consider any box whose candies are obtainable through some legal sequence. The first boxes of that sequence that are initially owned and open are enqueued during initialization. Whenever processing an obtainable box reveals the next needed key or contained box, the appropriate loop records that fact. As soon as both facts for another box are present, it is enqueued. By following the legal sequence inductively, every obtainable box eventually reaches the queue.

`took` ensures each such box contributes once. When the queue empties, no processed box can reveal further information, and every currently owned and open box has already been scheduled. Thus, no additional box can become reachable. The accumulated sum contains all and only obtainable candies, which is the maximum possible amount.

## Complexity detail

Let $n$ be the number of boxes. Let

$$
S=\sum_{\text{processed box }b}
\left(\lvert\texttt{keys}[b]\rvert+
\lvert\texttt{containedBoxes}[b]\rvert\right)
$$

be the total number of key and contained-box entries scanned from boxes that actually become openable and owned.

Each box is added to `took` at most once and therefore processed from the queue at most once. Set membership, insertion, deque operations, status checks, and candy additions take expected $O(1)$ time. Each scanned entry causes constant expected work, so the exact running time is $O(n+S)$ including initialization. If $S$ is defined broadly to include the initial boxes and box-level processing, this is the manifest's $O(S)$.

The reference editorial notes that key labels can repeat across different key lists, and total list length can be $O(n^2)$. The same broad issue applies to the amount of adjacency data supplied by the input. Consequently, worst-case time expressed only with $n$ can be $O(n^2)$.

The `has` and `took` sets contain at most $n$ labels, and the queue contains at most one scheduled entry per box under the intended distinct-initial-box contract. Auxiliary space is $O(n)$. The input arrays and their lists are not counted as extra space. The method mutates `status` in place rather than allocating a separate openability array.

## Alternatives and edge cases

- **Repeated full scans:** One can repeatedly inspect all boxes until no new one becomes usable. This is easier to imagine but may rescan many unavailable boxes, while the queue reacts only to useful state changes.
- **Boolean arrays instead of sets:** Arrays such as `has_box` and `used` give worst-case constant-time access and avoid hash overhead because labels range from zero to $n-1$. They express the same state machine.
- **Recursive traversal:** Recursion can process newly ready boxes, but chains may be deep and Python's recursion limit is unnecessary risk. An explicit queue is safer.
- **Closed initial box:** It remains in `has` without entering the queue. A later key changes `status` and triggers scheduling.
- **Key found before its box:** The key sets `status` to one. When the box is later found inside another processed box, the contained-box branch schedules it.
- **Box found before its key:** The box enters `has` but stays unscheduled. A later key branch sees ownership and schedules it.
- **Key for an already open box:** The `if not status[k]` guard ignores it because it cannot create new reachability.
- **Same key found several times:** Only the first transition from closed to open is useful, so later duplicates cannot enqueue or count the target again.
- **A box reachable through several routes:** `took` is set at enqueue time, preventing duplicate queue entries and duplicate candy collection before either entry could be processed.
- **No initial boxes:** The queue is empty, no discovery can begin, and the correct answer is zero.
- **No initially open owned boxes:** The queue is likewise empty. Keys locked inside inaccessible boxes cannot help, so zero is correct.
- **All boxes become reachable:** Every one is scheduled once and the answer becomes the sum of all candy values.
- **Positive candy guarantee:** Since every box has at least one candy and opening a box has no cost, processing every reachable box is always optimal. With negative rewards or limited actions, the no-choice worklist argument would no longer be sufficient.
- **Duplicate labels in `initialBoxes` outside the intended contract:** The exact initialization loop does not check `box not in took` before enqueueing and counting. If duplicate initial labels were permitted, it could double count. A defensive version would apply the same untaken guard used elsewhere.
- **Input mutation:** Acquired keys change `status`. A caller that needs the original array afterward must pass a copy or use a separate `can_open` structure.
