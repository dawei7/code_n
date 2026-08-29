## General

A singly linked list does not provide direct indexing, so one way to find its middle is to count all nodes and traverse again. The fast-and-slow-pointer method obtains the same result in one traversal and constant extra space.

Both pointers begin at `head`:

- `slow` advances one node per loop iteration.
- `fast` advances two nodes per loop iteration.

The loop continues only while `fast` exists and `fast.next` exists. That condition ensures a two-step move is safe. After the loop, `slow` points to the required middle.

**The speed relationship locates halfway.** After $t$ completed iterations, `slow` has moved $t$ edges from the head, while `fast` has moved $2t$ edges. When the fast pointer reaches the end, the slow pointer has traveled half as far. The only subtlety is how this rounds for an even number of nodes.

Let the list contain $n$ nodes indexed from 0.

For odd $n=2q+1$, the loop runs $q$ times. The fast pointer reaches index $2q$, the last node, and cannot make another two-step move because `fast.next` is null. The slow pointer is at index $q$, the unique middle.

For even $n=2q$, the loop also runs $q$ times. On the final iteration, the fast pointer moves from index $2q-2$ beyond the list, while the slow pointer moves to index $q$. The two central indices are $q-1$ and $q$, and index $q$ is the second middle required by the problem.

Thus the loop condition and shared starting position are not arbitrary: together they implement the desired floor calculation,

$$
\text{middle index}=\left\lfloor\frac{n}{2}\right\rfloor.
$$

For odd lengths this is the single middle, and for even lengths it is the later of the two middle positions.

**Why tuple assignment is safe.** The update is written as

```text
slow, fast = slow.next, fast.next.next
```

Python evaluates both right-hand expressions using the old pointer values before assigning either new value. Advancing `slow` cannot affect the expression used to advance `fast`. The list nodes themselves are never changed.

**A five-node trace.** In `1 -> 2 -> 3 -> 4 -> 5`, both pointers start at node 1. After one iteration, slow is at 2 and fast at 3. After two iterations, slow is at 3 and fast at 5. Since node 5 has no next node, the loop stops and returns node 3.

**A six-node trace.** In `1 -> 2 -> 3 -> 4 -> 5 -> 6`, the states after successive iterations are:

```text
slow = 2, fast = 3
slow = 3, fast = 5
slow = 4, fast = None
```

The returned node is 4, the second of nodes 3 and 4.

The method returns the node object, not merely its value. In the list representation shown by examples, returning the middle node naturally exposes the suffix beginning there, such as `[3,4,5]`. No new list and no copy of the suffix is created.

**Why no node is skipped by the slow pointer.** The slow pointer advances exactly once per valid loop iteration, following `next` just as a normal traversal would. The fast pointer only determines when to stop. Since the contract guarantees at least one node and an acyclic singly linked list, the loop terminates and the returned pointer belongs to the original list.

## Complexity detail

Let $n$ be the number of nodes. The loop runs $\lfloor n/2\rfloor$ times. Each iteration performs a constant number of pointer reads and assignments.

- **Time complexity:** $O(n)$.
- **Space complexity:** $O(1)$. Only two node references are maintained, regardless of list length.

The original linked list is not modified, and the returned object is an existing node. Although the fast pointer visits positions two edges apart, asymptotic work is still linear.

## Alternatives and edge cases

- **Store nodes in an array:** Traverse once, append every node, then return element `n // 2`. This is simple but uses $O(n)$ extra space.
- **Count and traverse twice:** First determine $n$, then advance `n // 2` steps. This uses $O(1)$ space but makes two passes instead of one.
- **Start fast one node ahead:** That common variation stops slow at the first middle for even lengths, which does not satisfy this problem's second-middle rule.
- **Move fast only one step:** Both pointers would stay together and no halfway relationship would be created.
- **One node:** `fast.next` is null immediately, so the loop does not run and `head` is returned.
- **Two nodes:** One iteration moves slow to the second node and fast beyond the list, correctly selecting the second middle.
- **Odd length:** Fast stops on the last node, while slow stops at the unique center.
- **Even length:** Fast moves beyond the list, while slow stops at the later center.
- **Return type:** Return `slow` itself, not `slow.val`, because the contract asks for the middle node.
- **List preservation:** Neither `next` field is assigned, so the structure and the suffix beginning at the returned node remain intact.
- **Nonempty-list guarantee:** The exact code safely reads from `head` because the constraints provide at least one node.
- **Cycles:** A cyclic list would prevent termination, but the platform supplies an ordinary finite singly linked list, so cycle detection is outside this task.
