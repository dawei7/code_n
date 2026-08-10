## General

**Use two traversal speeds instead of remembered nodes**

The competitive solution applies Floyd’s cycle-detection algorithm. `slow` and `fast` both begin at `head`.

On every loop iteration:

- `slow` moves one `next` edge;
- `fast` moves two `next` edges;
- their identities are compared.

If the list has an end, the faster pointer reaches it. If the list contains a cycle, both pointers eventually occupy the cycle and the faster one catches the slower one.

No set of visited nodes is required.

**Why the loop condition protects two-step movement**

The loop runs only while both `fast` and `fast.next` are non-null. Under that condition, evaluating `fast.next.next` is safe.

If `fast` is `None`, it has moved past the tail. If `fast.next` is `None`, it is standing on the tail. Either situation proves that following `next` can terminate, so the reachable structure is acyclic and the function returns false after the loop.

The simultaneous assignment:

`fast, slow = fast.next.next, slow.next`

evaluates both right-hand expressions before changing either pointer. The moves therefore use the same iteration’s old positions.

**Why identity comparison is required**

`fast is slow` asks whether both variables refer to the exact same node object. Comparing `fast.val == slow.val` would be invalid because different list nodes are allowed to contain equal values.

A cycle is about revisiting an object through pointers, not about encountering a repeated integer.

The equality check occurs after movement. Starting both pointers at `head` would make a pre-movement check immediately true for every nonempty list, including acyclic ones. Moving first prevents that false positive.

**Why a cycle forces a meeting**

Let the noncyclic prefix before the cycle contain $\mu$ nodes, and let the cycle length be $\lambda$.

After enough iterations, `slow` enters the cycle. Since `fast` moves twice as quickly and cannot leave a cycle once inside, `fast` is also somewhere in that cycle.

Measure the clockwise distance from `slow` to `fast` modulo $\lambda$. In one iteration, slow advances one and fast advances two, so fast gains one position. The relative distance changes by one modulo $\lambda$ each time.

There are only $\lambda$ possible relative positions. Within at most $\lambda$ iterations, the relative distance becomes zero and both pointers reference the same node. The identity check returns true.

Another intuitive view is two runners on a circular track: the faster runner gains one node per round of movement and must eventually lap the slower runner.

**Why an acyclic list cannot produce a meeting**

In a simple forward chain, each pointer’s position is determined by how many steps it has taken from `head`. After a positive number of iterations, fast has taken twice as many steps as slow. They cannot reference the same non-null node in an acyclic chain because that would give one node two different forward distances from the head without any path looping back.

Instead, fast reaches `None` or a node whose `next` is `None`, causing the loop to end and false to be returned.

**Short-list traces**

For an empty list, `fast` is null and the loop never runs.

For one node with `next = None`, `fast.next` is null and the result is false.

For a one-node self-cycle, the loop is safe; both moves return to the same node, and the identity check returns true.

For two acyclic nodes, one iteration moves `fast` to `None` and `slow` to the second node. They are not identical, and the next condition ends the loop.

## Complexity detail

Let $n$ be the number of distinct reachable nodes.

In an acyclic list, fast traverses the chain and reaches the end after $O(n)$ pointer steps. In a cyclic list, slow needs at most the noncyclic-prefix length to enter the cycle, followed by fewer than or equal to one cycle length’s worth of relative movement before meeting. Total time is $O(n)$.

The function stores only two node references. It allocates no set and does not alter the list, so auxiliary space is $O(1)$, matching the manifest and the follow-up requirement.

The constant factor includes at most two pointer hops for `fast` per loop, but constant factors do not change the asymptotic bound.

## Alternatives and edge cases

- **Visited-node set:** Store each identity and report a cycle upon repetition. It is very direct and runs in expected $O(n)$ time but uses $O(n)$ space.
- **Brent’s algorithm:** Move one pointer with exponentially growing checkpoints. It also detects cycles in $O(n)$ time and $O(1)$ space, often with fewer pointer comparisons.
- **Pointer mutation:** Temporarily redirect or mark nodes. It risks corrupting caller data and is unnecessary here.
- **Empty list:** Fails the loop condition and returns false.
- **Self-loop:** Both pointers return to the same node after the first move.
- **Two-node cycle:** Slow advances one node while fast returns to the start, and a meeting follows within another iteration.
- **Repeated node values:** `is` ignores values and detects only shared identity.
- **Cycle after a long prefix:** Fast cannot terminate once it enters the cycle, and relative speed still guarantees a meeting.
- **Loop-condition order:** Testing `fast.next` before confirming `fast` is non-null would raise an exception at the tail.
- **Checking before movement:** Because both pointers initialize to `head`, a pre-movement equality check would incorrectly label every nonempty list cyclic.
- **Module-level `ListNode`:** The source defines the helper outside `Solution`, and the algorithm itself requires only its `next` field; the stored value is irrelevant.
