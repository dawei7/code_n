## General

**First find any meeting inside the cycle**

The solution begins with `fast` and `slow` at `head`. During each iteration, `slow` follows one `next` pointer and `fast` follows two.

The condition `while fast and fast.next` makes the two-step move safe. If either expression is null, the list has a reachable end and therefore no cycle.

If a cycle exists, both pointers eventually enter it. Once inside, `fast` gains one node on `slow` per iteration. On a finite circular sequence, that relative position must eventually become zero, so `slow == fast`.

This first meeting can occur anywhere in the cycle. Returning it immediately would detect a cycle but would not generally identify the cycle’s entrance.

**Derive why the second phase reaches the entrance**

Let:

- $\mu$ be the number of edges from `head` to the cycle entrance;
- $\lambda$ be the number of edges around the cycle;
- $b$ be the number of cycle edges from the entrance to the first meeting point.

At the meeting, slow has traveled:

$$
\mu+b
$$

edges, possibly with its cycle position understood modulo $\lambda$. Fast has traveled twice as far:

$$
2(\mu+b).
$$

Because both pointers are at the same cycle node, the extra distance traveled by fast is an integer number $k$ of complete cycles:

$$
2(\mu+b)-(\mu+b)=k\lambda.
$$

Therefore:

$$
\mu+b=k\lambda
$$

and:

$$
\mu=k\lambda-b.
$$

The quantity $k\lambda-b$ is exactly a whole number of cycles minus the distance already traveled from the entrance to the meeting point. In other words, it is the forward distance from the meeting point back to the entrance, possibly including extra complete laps.

**Move equal-speed pointers for the derived distance**

After the first meeting, the source creates `ans = head` and leaves `slow` at the meeting node. Both then move one edge per iteration.

After $\mu$ steps:

- `ans` has traveled from the head to the cycle entrance;
- `slow` has traveled from offset $b$ by another $\mu=k\lambda-b$ edges, reaching offset $k\lambda$, which is the entrance modulo the cycle length.

They therefore meet at the entrance. The loop returns `ans`, which is the native node reference required by the problem.

This also explains why equal speed is necessary in phase two. The useful relationship compares equal distances from two different starting positions. Continuing with speeds one and two would not apply the derived equation.

**Why this is the first phase-two meeting**

Before `ans` travels $\mu$ steps, it is still in the noncyclic prefix. `slow` remains inside the cycle. Those regions contain different node objects, so the pointers cannot meet earlier. At exactly $\mu$ steps, both reach the entrance.

If the cycle begins at `head`, then $\mu=0$. The first-meeting relation forces the meeting position to coincide with the entrance modulo $\lambda$, so `ans` and `slow` already match and the second loop performs zero iterations.

**What happens when there is no cycle**

In an acyclic list, the two-step pointer eventually becomes `None` or stands at a node whose `next` is `None`. The loop condition fails.

There is no explicit `return None` after the loop. Python functions return `None` implicitly when execution reaches the end, so this source still satisfies the native no-cycle result.

The list is never modified. All assignments change local pointer variables, not any node’s `next`.

The example variable `pos` is not passed to this function. It is only a harness description of how the input list was connected.

## Complexity detail

Let $n$ be the number of distinct nodes reachable from `head`.

In phase one, an acyclic fast pointer reaches the end in $O(n)$ time. With a cycle, slow traverses the noncyclic prefix and at most one additional cycle’s worth of relative positions before meeting, also $O(n)$.

Phase two takes exactly $\mu$ iterations to reach the entrance, at most $n$. The combined time is $O(n)+O(n)=O(n)$.

Only `fast`, `slow`, and `ans` node references are stored. Auxiliary space is $O(1)$, matching the manifest and follow-up. No values or links are modified.

## Alternatives and edge cases

- **Visited-node set:** Return the first object encountered twice. It is straightforward and directly identifies the entry, but requires $O(n)$ extra space.
- **Brent’s cycle algorithm:** It detects a cycle with constant space and can derive the cycle length, after which two pointers separated by that length can find the entry.
- **Compute the cycle length after meeting:** Walk once around the cycle to find $\lambda$, place one pointer $\lambda$ steps ahead of another, then advance together. They meet at the entrance.
- **Empty list:** The first loop never runs and the function implicitly returns `None`.
- **One acyclic node:** `fast.next` is null, so no movement occurs.
- **One-node self-cycle:** Both pointers return to the same node after one phase-one move; the head is returned immediately in phase two.
- **Cycle starts at head:** The head-to-entry distance is zero, and the second loop need not move.
- **Long prefix before a short cycle:** Phase one still meets, and phase two walks exactly the prefix length.
- **Repeated values:** Pointer equality under the platform’s default node identity is what matters; `val` is never inspected.
- **Implicit return:** Adding an explicit `return None` would improve readability but would not change Python behavior.
- **Runtime dependencies:** The selected source uses `Optional` without importing it. The platform provides `ListNode`; standalone Python needs the type definition and `from typing import Optional`.
